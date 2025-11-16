from ..models.requests import HireCreateOfferQuery, HirePostOfferQuery, HireQuestionQuery


class HireService:
    """Сервис для работы с задачами по найму"""

    @staticmethod
    def create_offer(query: HireCreateOfferQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }

    @staticmethod
    def post_offer(query: HirePostOfferQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }

    @staticmethod
    def process_question(query: HireQuestionQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }
