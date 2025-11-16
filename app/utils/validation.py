import logging
import os

from flask import current_app as app
from flask import request
from ..models.responses import APIResponse
from pydantic import ValidationError

logger = logging.getLogger(__name__)


def validate_json_request(model_class=None) -> tuple:
    """
    Валидация параметров запроса
    Возвращает tuple (error_response, validated_data)
    """

    if not request.is_json:
        return APIResponse.error("Content-Type must be application/json"), None
    if request.content_length > app.config['MAX_CONTENT_LENGTH']:
        return APIResponse.error("Request payload too large"), None
    json_data = request.get_json()
    if not json_data:
        return APIResponse.error("Empty request body", request_id=request.request_id), None
    if model_class:
        try:
            validated_data = model_class(**json_data)
            return None, validated_data
        except ValidationError as e:
            logger.warning(f"Request validation failed: {str(e)}", extra={
                "request_id": request.request_id
            })
            return APIResponse.error("Invalid request parameters", request_id=request.request_id), None
    return None, json_data


def validate_file_request() -> tuple:
    """
    Валидация параметров запроса
    Возвращает tuple (error_response, file)
    """

    if request.content_length > app.config['MAX_CONTENT_LENGTH']:
        return APIResponse.error("Request payload too large"), None
    if not request.files:
        return APIResponse.error("No files in request"), None

    file = None
    for field_name in request.files:
        potential_file = request.files[field_name]
        if potential_file.filename != '' and potential_file.filename:
            file = potential_file
            break
    if not file:
        return APIResponse.error("No valid file found"), None

    if file.mimetype not in {'application/pdf', 'application/msword',
                             'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}:
        return APIResponse.error("Invalid file type"), None
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in {".pdf", ".doc", ".docx"}:
        return APIResponse.error("File type not allowed"), None

    return None, file
