from datetime import datetime
from db.scripts.operations_db import get_user_info, get_uuid_by_login, get_request_story, update_user_information
from ..models.requests import UpdateSettingsRequest


class SettingsService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def get_settings(user_id) -> dict:
        login, city, name, business = get_user_info(user_id)
        return {
            "username": login,
            "business": business,
            "city": city,
            "name": name
        }

    @staticmethod
    def update_settings(query: UpdateSettingsRequest) -> dict:
        user_id = get_uuid_by_login(query.username)
        update_user_information(query.name, query.city, query.business, user_id)
        login, city, name, business = get_user_info(user_id)
        return {
            "username": login,
            "business": business,
            "city": city,
            "name": name
        }

    @staticmethod
    def get_history(amount: int, user_id) -> list:
        requests = get_request_story(user_id, amount)
        lst = []
        for request in requests:
            lst.append(
                {
                    "prompt": request[1],
                    "answer": request[2],
                    "answerType": request[3],
                    "requestId": request[0],
                    "createdAt": request[4]
                }
            )

        return lst