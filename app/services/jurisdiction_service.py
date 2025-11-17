from ..models.requests import JurisdictionExplainQuery
from db.scripts.operations_db import get_user_info, insert_request
from ml.law import law_module


class JurisdictionService:
    """Сервис для работы с юридическими задачами"""

    @staticmethod
    def explain_text(query: JurisdictionExplainQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        prompt_answer = law_module.generate(query.query, city,
                                                business_info)

        insert_request(user_id, query.query, prompt_answer)

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "finance",
        }
