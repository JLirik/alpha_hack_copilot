import logging
from typing import Callable, Any, Tuple

from flask import request
from ..models.responses import APIResponse

logger = logging.getLogger(__name__)


def handle_logic_request(service_method: Callable, data: Any, process_name: str) -> Tuple[dict, int]:
    """Общий обработчик для логики всех запросов"""

    try:
        result = service_method(data)
        return APIResponse.success(
            prompt=result["prompt"],
            answer=result["answer"],
            answer_type=result["answerType"],
            request_id=request.request_id
        )
    except Exception as e:
        logger.error(f"{process_name} failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during {process_name.lower()}", request.request_id)
