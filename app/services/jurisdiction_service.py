from flask import request

from db.scripts.operations_db import get_user_info, insert_request
from ml.law import law_module
from ..models.requests import JurisdictionExplainQuery


class JurisdictionService:
    """Сервис для работы с юридическими задачами"""

    @staticmethod
    def explain_text(query: JurisdictionExplainQuery) -> dict:
        city, business_info = get_user_info(request.user["user_id"])
        prompt_answer = law_module.generate(query.clause, city,
                                                business_info)

        insert_request(request.user["user_id"], query.clause, prompt_answer, 'law')

        return {
            "prompt": query.clause,
            "answer": prompt_answer,
            "answerType": "law",
        }
