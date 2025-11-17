import logging

from flask import current_app as app
from flask import request
from pydantic import ValidationError

from ..models.responses import APIResponse

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
