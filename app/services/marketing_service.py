from ..models.requests import MarketingGenerateQuery, MarketingRegenerateQuery


class MarketingService:
    """Сервис для работы с маркетинговыми задачами"""

    @staticmethod
    def generate_content(query: MarketingGenerateQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }

    @staticmethod
    def regenerate_content(query: MarketingRegenerateQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }
