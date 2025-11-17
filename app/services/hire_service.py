from ..models.requests import HireQuestionQuery
from db.scripts.operations_db import get_user_info, insert_request
from ml.hiring import hiring_module


class HireService:
    """Сервис для работы с задачами по найму"""

    @staticmethod
    def process_question(query: HireQuestionQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        prompt_answer = hiring_module.generate(query.query, city,
                                                business_info)

        insert_request(user_id, query.query, prompt_answer, 'hire')

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "hire",
        }
