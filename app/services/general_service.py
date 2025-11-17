from ..models.requests import GeneralQuestionQuery
from db.scripts.operations_db import get_user_info, insert_request
from ml.general import general_module


class GeneralService:
    """Сервис для работы с общими задачами"""

    @staticmethod
    def process_question(query: GeneralQuestionQuery, user_id) -> dict:
        city, business_info = get_user_info(user_id)
        prompt_answer = general_module.generate(query.query, city, business_info)

        insert_request(user_id, query.query, prompt_answer, 'other')

        return {
            "prompt": query.query,
            "answer": prompt_answer,
            "answerType": "other",
        }
