from ..models.requests import MarketingGenerateQuery, MarketingRegenerateQuery
from db.scripts.operations_db import get_user_info, insert_request, get_request
from ml.marketing import marketing_module


class MarketingService:
    """Сервис для работы с маркетинговыми задачами"""

    @staticmethod
    def generate_content(query: MarketingGenerateQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        prompt_answer = marketing_module.generate(query.topic, city,
                                                business_info)

        req_id = insert_request(user_id, query.topic, prompt_answer, 'marketing')

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "marketing",
            "requestId": req_id[0]
        }

    @staticmethod
    def regenerate_content(query: MarketingRegenerateQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        last_query = get_request(query.contentId)[0]
        prompt_answer = marketing_module.generate(last_query[0], city,
                                                  business_info, last_query[1])

        req_id = insert_request(user_id, last_query[0], prompt_answer, 'marketing')

        return {
            "prompt": last_query[0],
            "answer": prompt_answer,
            "answerType": "marketing",
            "requestId": req_id
        }
