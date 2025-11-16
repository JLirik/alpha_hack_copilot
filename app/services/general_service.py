from ..models.requests import GeneralQuestionQuery


class GeneralService:
    """Сервис для работы с общими задачами"""

    @staticmethod
    def process_question(query: GeneralQuestionQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }
