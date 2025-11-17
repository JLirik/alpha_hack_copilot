from functools import wraps

from flask import request

from .jwt_utils import JWTUtils
from ..models.responses import APIResponse


def token_required(f):
    """Декоратор для проверки JWT токена"""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        if not token:
            return APIResponse.error("Token is missing", request.request_id)

        user_data = JWTUtils.get_user_from_token(token)
        if not user_data:
            return APIResponse.error("Invalid or expired token", request.request_id)

        request.user = user_data
        return f(*args, **kwargs)

    return decorated
