from ..models.requests import FinanceQuestionQuery
from ml.finance import finance_module
from db.scripts.operations_db import get_user_info, insert_request


class FinanceService:
    """Сервис для работы с финансовым задачами"""

    @staticmethod
    def process_question(query: FinanceQuestionQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        prompt_answer = finance_module.generate(query.query, city, business_info)

        insert_request(user_id, query.query, prompt_answer, 'finance')

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "finance",
        }