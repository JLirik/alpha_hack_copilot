from ..models.requests import FinanceQuestionQuery


class FinanceService:
    """Сервис для работы с финансовым задачами"""

    @staticmethod
    def process_question(query: FinanceQuestionQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }
