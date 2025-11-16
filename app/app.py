import logging
import time
import uuid

from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.config["API_PREFIX"] = "/api/v1"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB

from .utils.validation import validate_json_request, validate_file_request
from .utils.handlers import handle_logic_request
from .models.requests import *
from .models.responses import APIResponse
from .services.finance_service import FinanceService
from .services.general_service import GeneralService
from .services.hire_service import HireService
from .services.jurisdiction_service import JurisdictionService
from .services.marketing_service import MarketingService


@app.before_request
def before_request():
    """Инициализация контекста запроса"""

    request.start_time = time.time()
    request.request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))
    logger.info(f"Request started", extra={
        "request_id": request.request_id,
        "method": request.method,
        "path": request.path,
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
def generate_marketing_content():
    """Генерация маркетингового контента"""

    validation_error, query = validate_json_request(MarketingGenerateQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(MarketingService.generate_content, query, "Content generation")


@app.route(f'{app.config["API_PREFIX"]}/query/marketing/regenerate', methods=['POST'])
def regenerate_marketing_content():
    """Перегенерация маркетингового контента"""

    validation_error, query = validate_json_request(MarketingRegenerateQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(MarketingService.regenerate_content, query, "Content regeneration")


@app.route(f'{app.config["API_PREFIX"]}/query/law/parse', methods=['POST'])
def parse_legal_document():
    """Разбор юридического документа"""

    validation_error, file = validate_file_request()
    if validation_error:
        return validation_error
    return handle_logic_request(JurisdictionService.parse_document, file, "Parsing legal document")


@app.route(f'{app.config["API_PREFIX"]}/query/law/explain', methods=['POST'])
def explain_legal_text():
    """Объяснение юридического пункта или текста"""

    validation_error, query = validate_json_request(JurisdictionExplainQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(JurisdictionService.explain_text, query, "Explaining legal text")


@app.route(f'{app.config["API_PREFIX"]}/query/hire/createOffer', methods=['POST'])
def create_offer():
    """Генерация предложения о работе"""

    validation_error, query = validate_json_request(HireCreateOfferQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(HireService.create_offer, query, "Creating offer")


@app.route(f'{app.config["API_PREFIX"]}/query/hire/postOffer', methods=['POST'])
def post_offer():
    """Публикация вакансии"""

    validation_error, query = validate_json_request(HirePostOfferQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(HireService.post_offer, query, "Posting offer")


@app.route(f'{app.config["API_PREFIX"]}/query/hire', methods=['POST'])
def process_hire_question():
    """Обработка вопроса по найму"""

    validation_error, query = validate_json_request(HireQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(HireService.process_question, query, "Processing hire question")


@app.route(f'{app.config["API_PREFIX"]}/query/finance', methods=['POST'])
def process_finance_question():
    """Обработка финансового вопроса"""

    validation_error, query = validate_json_request(FinanceQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(FinanceService.process_question, query, "Processing finance question")


@app.route(f'{app.config["API_PREFIX"]}/query/general', methods=['POST'])
def process_general_question():
    """Обработка общего вопроса"""

    validation_error, query = validate_json_request(GeneralQuestionQuery)
    if validation_error:
        return validation_error
    return handle_logic_request(GeneralService.process_question, query, "Processing general question")


@app.route(f'{app.config["API_PREFIX"]}/query/marketing/generate', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/marketing/regenerate', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/law/parse', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/law/explain', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/hire/createOffer', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/hire/postOffer', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/hire', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/finance', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@app.route(f'{app.config["API_PREFIX"]}/query/general', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def method_not_allowed():
    """Обработчик неподдерживаемых методов"""

    return APIResponse.error(f"Method {request.method} not allowed for this endpoint", request.request_id)
