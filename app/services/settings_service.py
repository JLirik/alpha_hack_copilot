from flask import request

from db.scripts.operations_db import get_user_info, get_request_story, update_user_information
from ..models.requests import UpdateSettingsRequest
from ..models.responses import APIResponse


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
        # ПРОВЕРКА: если меняется пароль или логин, должен быть указан текущий пароль
        if (query.password or query.username) and not query.current_password:
            return APIResponse.error("Current password is required to change password or username", request.request_id,
                                     code=400)

        # ОБНОВЛЯЕМ ДАННЫЕ С ПРОВЕРКОЙ ПАРОЛЯ
        update_result = update_user_information(
            new_login=query.username,
            new_name=query.name,
            new_city=query.city,
            new_business=query.business,
            uuid=request.user["user_id"],
            current_password=query.current_password if (query.password or query.username) else None,
            new_password=query.password
        )

        if update_result == 401:
            return APIResponse.error("Current password is incorrect", request.request_id)
        elif update_result == 400:
            return APIResponse.error("Current password required for password or username change", request.request_id,
                                     code=400)
        elif update_result == 404:
            return APIResponse.error("User not found", request.request_id)
        elif update_result == 409:
            return APIResponse.error("Username already taken", request.request_id)
        elif update_result != 0:
            return APIResponse.error("Update failed", request.request_id)

        user_info = get_user_info(request.user["user_id"])
        if not user_info:
            return APIResponse.error("Failed to get updated user info", request.request_id)

        login, city, name, business = user_info

        from ..utils.jwt_utils import JWTUtils
        new_access_token = JWTUtils.create_access_token({
            "user_id": request.user["user_id"],
            "username": login,
            "business": business,
            "city": city,
            "name": name
        })

        return {
            "username": login,
            "business": business,
            "city": city,
            "name": name,
            "accessToken": new_access_token
        }


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