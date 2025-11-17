from flask import request

from db.scripts.operations_db import get_user_info, insert_request, get_request
from ml.marketing import marketing_module
from ..models.requests import MarketingGenerateQuery, MarketingRegenerateQuery


class MarketingService:
    """Сервис для работы с маркетинговыми задачами"""

    @staticmethod
    def generate_content(query: MarketingGenerateQuery) -> dict:
        city, business_info = get_user_info(request.user["user_id"])
        prompt_answer = marketing_module.generate(query.topic, city,
                                                business_info)

        req_id = insert_request(request.user["user_id"], query.topic, prompt_answer, 'marketing')

        return {
            "prompt": query.topic,
            "answer": prompt_answer,
            "answerType": "marketing",
            "requestId": req_id[0]
        }

    @staticmethod
    def regenerate_content(query: MarketingRegenerateQuery) -> dict:
        city, business_info = get_user_info(request.user["user_id"])
        last_query = get_request(query.contentId)
        prompt_answer = marketing_module.generate(last_query[0], city,
                                                  business_info, last_query[1])

        req_id = insert_request(request.user["user_id"], last_query[0], prompt_answer, 'marketing')

        return {
            "prompt": last_query[0],
            "answer": prompt_answer,
            "answerType": "marketing",
            "requestId": req_id[0]
        }
