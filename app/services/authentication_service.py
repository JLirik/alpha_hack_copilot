from flask import make_response, request

from db.scripts.operations_db import login_user, register_user, get_user_info, get_user_info_by_login
from ..models.requests import AuthRequest, RegRequest
from ..models.responses import APIResponse
from ..utils.jwt_utils import JWTUtils


class AuthenticationService:
    """Сервис для работы задач аутентификации"""

    @staticmethod
    def auth(query: AuthRequest) -> tuple:
        succeed_login = login_user(query.username, query.password)
        if succeed_login == 0:
            user_data = get_user_info_by_login(query.username)
            access_token = JWTUtils.create_access_token({
                "user_id": user_data[0],
                "username": query.username,
                "business": user_data[3],
                "city": user_data[1],
                "name": user_data[2]})
            refresh_token = JWTUtils.create_refresh_token(user_data[0])

            response = make_response({"accessToken": access_token}, 200)
            response = JWTUtils.set_refresh_token_cookie(response, refresh_token)
            return response
        if succeed_login == 401:
            return APIResponse.error('Wrong password', request.request_id, code=401)
        if succeed_login == 404:
            return APIResponse.error("User doesn't exist", request.request_id, code=404)

    @staticmethod
    def refresh() -> tuple:
        refresh_token = request.cookies.get('refresh_token')
        if not refresh_token:
            return APIResponse.error("Refresh token missing", request.request_id, code=401)
        payload = JWTUtils.verify_token(refresh_token)
        if not payload or payload.get("token_type") != "refresh":
            return APIResponse.error("Invalid refresh token", request.request_id, code=401)

        user_id = payload.get("user_id")
        user_data = get_user_info(user_id)
        if not user_data:
            return APIResponse.error("User not found", request.request_id, code=404)

        access_token = JWTUtils.create_access_token({
            "user_id": user_id,
            "username": user_data[0],
            "business": user_data[3],
            "city": user_data[1],
            "name": user_data[2]
        })
        new_refresh_token = JWTUtils.create_refresh_token(user_id)

        response = make_response({"accessToken": access_token}, 200)
        response = JWTUtils.set_refresh_token_cookie(response, new_refresh_token)
        return response


    @staticmethod
    def reg(query: RegRequest) -> tuple:
        succeed_reg = register_user(query.username, query.password, query.name,
                                    query.city, query.business)
        if succeed_reg == 409:
            return APIResponse.error('User already exists', request.request_id,
                                     code=409)
        if succeed_reg == 400:
            return APIResponse.error('Wrong input data', request.request_id,
                                     code=400)
        if succeed_reg:
            access_token = JWTUtils.create_access_token({
                "user_id": succeed_reg,
                "username": query.username,
                "business": query.business,
                "city": query.city,
                "name": query.name
            })
            refresh_token = JWTUtils.create_refresh_token(succeed_reg)

            response = make_response({"accessToken": access_token}, 200)
            response = JWTUtils.set_refresh_token_cookie(response, refresh_token)
            return response

    @staticmethod
    def logout():
        response = JWTUtils.clear_refresh_token_cookie(make_response(200))
        return response
