from flask import request

from db.scripts.operations_db import get_user_info, insert_request
from ml.finance import finance_module
from ..models.requests import FinanceQuestionQuery


class FinanceService:
    """Сервис для работы с финансовым задачами"""

    @staticmethod
    def process_question(query: FinanceQuestionQuery) -> dict:
        city, business_info = get_user_info(request.user["user_id"])
        prompt_answer = finance_module.generate(query.query, city, business_info)

        insert_request(request.user["user_id"], query.query, prompt_answer, 'finance')

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "finance",
        }