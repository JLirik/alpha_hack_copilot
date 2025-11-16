from ..models.requests import AuthRequest, RefreshRequest, RegRequest


class AuthenticationService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def auth(query: AuthRequest) -> tuple:
        return {
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }, 200  # 401 неверный пароль, 404 пользователь не существует

    @staticmethod
    def refresh(query: RefreshRequest) -> tuple:
        return {
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }, 200  # 401 неверный токен, 404 пользователь не существует

    @staticmethod
    def reg(query: RegRequest) -> tuple:
        return {
            "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
        }, 200  # 400 неверные данные, 409 пользователь уже существует
