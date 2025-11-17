import datetime
import secrets
from typing import Optional, Dict, Any

import jwt
from flask import current_app as app


class JWTUtils:
    """Утилиты для работы с JWT токенами"""

    @staticmethod
    def create_access_token(user_data: Dict[str, Any]) -> str:
        """Создание access токена"""
        payload = {
            **user_data,
            "token_type": "access",
            "exp": datetime.datetime.now() + app.config["JWT_ACCESS_TOKEN_EXPIRES"],
            "iat": datetime.datetime.now(),
            "jti": secrets.token_urlsafe(16)
        }
        return jwt.encode(payload, app.config["JWT_SECRET_KEY"], algorithm="HS256")

    @staticmethod
    def create_refresh_token(user_id: str) -> str:
        """Создание refresh токена"""
        payload = {
            "user_id": user_id,
            "token_type": "refresh",
            "exp": datetime.datetime.now() + app.config["JWT_REFRESH_TOKEN_EXPIRES"],
            "iat": datetime.datetime.now(),
            "jti": secrets.token_urlsafe(16)
        }
        return jwt.encode(payload, app.config["JWT_SECRET_KEY"], algorithm="HS256")

    @staticmethod
    def set_refresh_token_cookie(response, refresh_token: str):
        """Установка refresh token в httpOnly cookie"""
        response.set_cookie(
            app.config["JWT_REFRESH_COOKIE_NAME"],
            refresh_token,
            httponly=app.config["JWT_REFRESH_COOKIE_HTTPONLY"],
            secure=app.config["JWT_REFRESH_COOKIE_SECURE"],
            samesite=app.config["JWT_REFRESH_COOKIE_SAMESITE"],
            path=app.config["JWT_REFRESH_COOKIE_PATH"],
            max_age=int(app.config["JWT_REFRESH_TOKEN_EXPIRES"].total_seconds())
        )
        return response

    @staticmethod
    def clear_refresh_token_cookie(response):
        """Очистка refresh token cookie"""
        response.set_cookie(
            app.config["JWT_REFRESH_COOKIE_NAME"],
            '',
            httponly=app.config["JWT_REFRESH_COOKIE_HTTPONLY"],
            secure=app.config["JWT_REFRESH_COOKIE_SECURE"],
            samesite=app.config["JWT_REFRESH_COOKIE_SAMESITE"],
            path=app.config["JWT_REFRESH_COOKIE_PATH"],
            max_age=0
        )
        return response

    @staticmethod
    def verify_token(token: str) -> Optional[Dict[str, Any]]:
        """Верификация токена"""
        try:
            payload = jwt.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def get_user_from_token(token: str) -> Optional[Dict[str, Any]]:
        """Получение пользователя из токена"""
        payload = JWTUtils.verify_token(token)
        if payload and payload.get("token_type") == "access":
            return {
                "user_id": payload.get("user_id"),
                "username": payload.get("username"),
                "business": payload.get("business"),
                "city": payload.get("city"),
                "name": payload.get("name")
            }
        return None
