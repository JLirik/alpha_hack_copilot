from flask import request

from db.scripts.operations_db import get_user_info, get_request_story, update_user_information
from ..models.requests import UpdateSettingsRequest


class SettingsService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def get_settings() -> dict:
        login, city, name, business = get_user_info(request.user["user_id"])
        return {
            "username": login,
            "business": business,
            "city": city,
            "name": name
        }

    @staticmethod
    def update_settings(query: UpdateSettingsRequest) -> dict:
        update_user_information(query.name, query.city, query.business, request.user["user_id"])
        login, city, name, business = get_user_info(request.user["user_id"])
        return {
            "username": login,
            "business": business,
            "city": city,
            "name": name
        }

        # new_access_token = JWTUtils.create_access_token(updated_user)   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # response_data = {
        #     "username": updated_user["username"],
        #     "business": updated_user["business"],
        #     "city": updated_user["city"],
        #     "accessToken": new_access_token  # Возвращаем новый токен
        # }
        # return response_data

    @staticmethod
    def get_history(amount: int) -> list:
        requests = get_request_story(request.user["user_id"], amount)
        lst = []
        for r in requests:
            lst.append(
                {
                    "prompt": r[1],
                    "answer": r[2],
                    "answerType": r[3],
                    "requestId": r[0],
                    "createdAt": r[4]
                }
            )

        return lst