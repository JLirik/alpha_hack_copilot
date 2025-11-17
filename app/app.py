import logging
import os
import time
import uuid
from datetime import timedelta

from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config["API_PREFIX"] = "/api/v1"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

app.config["JWT_REFRESH_COOKIE_NAME"] = "refresh_token"
app.config["JWT_REFRESH_COOKIE_HTTPONLY"] = True
app.config["JWT_REFRESH_COOKIE_SECURE"] = True
app.config["JWT_REFRESH_COOKIE_SAMESITE"] = "Strict"
app.config["JWT_REFRESH_COOKIE_PATH"] = "/api/v1/refresh"

from .utils.validation import validate_json_request
from .utils.handlers import handle_logic_request
from .utils.auth_middleware import token_required
from .models.requests import *
from .models.responses import APIResponse
from .services.authentication_service import AuthenticationService
from .services.finance_service import FinanceService
from .services.general_service import GeneralService
from .services.hire_service import HireService
from .services.jurisdiction_service import JurisdictionService
from .services.marketing_service import MarketingService
from .services.settings_service import SettingsService


@app.before_request
def before_request():
    """Инициализация контекста запроса"""

    request.start_time = time.time()
    request.request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))
    logger.info(f"Request started", extra={
        "request_id": request.request_id,
        "method": request.method,
        "path": request.path,
        "endpoint": request.endpoint,
        "user_agent": request.headers.get('User-Agent'),
        "ip": request.remote_addr
    })


@app.after_request
def after_request(response):
    """Логирование завершения запроса"""

    if hasattr(request, 'start_time') and hasattr(request, 'request_id'):
        processing_time = time.time() - request.start_time
        logger.info(f"Request completed", extra={
            "request_id": request.request_id,
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "processing_time_ms": round(processing_time * 1000, 2)
        })
        response.headers['X-Request-ID'] = request.request_id
    return response


@app.route(f'{app.config["API_PREFIX"]}/query/marketing/generate', methods=['POST'])
@token_required
def generate_marketing_content():
    """Генерация маркетингового контента"""

    validation_error, query = validate_json_request(MarketingGenerateQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(MarketingService.generate_content, query, "Content generation")


@app.route(f'{app.config["API_PREFIX"]}/query/marketing/regenerate', methods=['POST'])
@token_required
def regenerate_marketing_content():
    """Перегенерация маркетингового контента"""

    validation_error, query = validate_json_request(MarketingRegenerateQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(MarketingService.regenerate_content, query, "Content regeneration")


@app.route(f'{app.config["API_PREFIX"]}/query/law/explain', methods=['POST'])
@token_required
def explain_legal_text():
    """Объяснение юридического пункта или текста"""

    validation_error, query = validate_json_request(JurisdictionExplainQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(JurisdictionService.explain_text, query, "Explaining legal text")


@app.route(f'{app.config["API_PREFIX"]}/query/hire', methods=['POST'])
@token_required
def process_hire_question():
    """Обработка вопроса по найму"""

    validation_error, query = validate_json_request(HireQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(HireService.process_question, query, "Processing hire question")


@app.route(f'{app.config["API_PREFIX"]}/query/finance', methods=['POST'])
@token_required
def process_finance_question():
    """Обработка финансового вопроса"""

    validation_error, query = validate_json_request(FinanceQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(FinanceService.process_question, query, "Processing finance question")


@app.route(f'{app.config["API_PREFIX"]}/query/general', methods=['POST'])
@token_required
def process_general_question():
    """Обработка общего вопроса"""

    validation_error, query = validate_json_request(GeneralQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(GeneralService.process_question, query, "Processing general question")


@app.route(f'{app.config["API_PREFIX"]}/auth', methods=['POST'])
def auth():
    """Аутентификация пользователя"""

    validation_error, query = validate_json_request(AuthRequest)
    if validation_error:
        return validation_error
    try:
        return AuthenticationService.auth(query)
    except Exception as e:
        logger.error(f"Authentication failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during authentication", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/refresh', methods=['GET'])
def refresh():
    """Обновление JWT-токена"""

    try:
        return AuthenticationService.refresh()
    except Exception as e:
        logger.error(f"Refresh failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during refresh", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/reg', methods=['POST'])
def reg():
    """Регистрация нового пользователя"""

    validation_error, query = validate_json_request(RegRequest)
    if validation_error:
        return validation_error
    try:
        return AuthenticationService.reg(query)
    except Exception as e:
        logger.error(f"Reg failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during reg", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/logout', methods=['GET'])
@token_required
def logout():
    """Выход пользователя"""

    try:
        return AuthenticationService.logout()
    except Exception as e:
        logger.error(f"Logout failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during logout", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/settings', methods=['GET'])
@token_required
def get_settings():
    """Получение настроек пользователя"""

    try:
        return SettingsService.get_settings(), 200
    except Exception as e:
        logger.error(f"Getting settings failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during getting settings", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/settings', methods=['PATCH'])
@token_required
def update_settings():
    """Обновление настроек пользователя"""

    validation_error, query = validate_json_request(UpdateSettingsRequest)
    if validation_error:
        return validation_error
    try:
        return SettingsService.update_settings(query), 200
    except Exception as e:
        logger.error(f"Update settings failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during update settings", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/history/<int:amount>', methods=['GET'])
@token_required
def history(amount):
    """Получение истории запросов пользователя"""

    if amount < 1 or amount > 50:
        return APIResponse.error("Amount must be >= 1 and <= 50", request.request_id)
    try:
        return jsonify(SettingsService.get_history(amount)), 200
    except Exception as e:
        logger.error(f"Getting history failed for request {request.request_id}: {str(e)}", exc_info=True)
        return APIResponse.error(f"Internal server error during getting history", request.request_id)


@app.route(f'{app.config["API_PREFIX"]}/query/marketing/generate', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/marketing/regenerate', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/law/explain', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/hire', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/finance', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/general', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/auth', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/refresh', methods=['POST', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/reg', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/logout', methods=['POST', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/settings', methods=['POST', 'PUT', 'DELETE'])
@app.route(f'{app.config["API_PREFIX"]}/history/<int:amount>', methods=['POST', 'PUT', 'DELETE', 'PATCH'])
@token_required
def method_not_allowed():
    """Обработчик неподдерживаемых методов"""

    return APIResponse.error(f"Method {request.method} not allowed for this endpoint", request.request_id)
