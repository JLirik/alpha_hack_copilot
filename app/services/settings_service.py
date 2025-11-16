from datetime import datetime

from ..models.requests import UpdateSettingsRequest


class SettingsService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def get_settings() -> dict:
        return {
            "username": "new_user",
            "password": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "business": "Маленькая франшиза спешалти-кофеен",
            "city": "Москва"
        }

    @staticmethod
    def update_settings(query: UpdateSettingsRequest) -> dict:
        return {
            "username": "new_user",
            "password": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "business": "Маленькая франшиза спешалти-кофеен",
            "city": "Москва"
        }

    @staticmethod
    def get_history(amount: int, request_id) -> list:
        return [
            {
                "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
                "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
                "answerType": "law",
                "requestId": request_id,
                "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            }
        ]
