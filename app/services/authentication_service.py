from ..models.requests import AuthRequest, RefreshRequest, RegRequest
from db.scripts.operations_db import login_user, register_user
from ..models.responses import APIResponse


class AuthenticationService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def auth(query: AuthRequest, request_id) -> tuple:
        succeed_login = login_user(query.username, query.password)
        if succeed_login == 0:
            return {
                "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }, 200
        if succeed_login == 401:
            return APIResponse.error('Wrong password', request_id, code=401)
        if succeed_login == 404:
            return APIResponse.error("User doesn't exist", request_id,
                                     code=404)

    @staticmethod
    def refresh(query: RefreshRequest, request_id) -> tuple:
        return {
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }, 200  # 401 неверный токен, 404 пользователь не существует

    @staticmethod
    def reg(query: RegRequest, request_id) -> tuple:
        succeed_reg = register_user(query.username, query.password, query.name,
                                    query.city, query.business)
        if succeed_reg == 0:
            return {
                "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            }, 200  # 400 неверные данные, 409 пользователь уже существует
        if succeed_reg == 409:
            return APIResponse.error('User already exists', request_id,
                                     code=409)
        if succeed_reg == 400:
            return APIResponse.error('Wrong input data', request_id,
                                     code=400)
