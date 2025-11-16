from ..models.requests import JurisdictionExplainQuery


class JurisdictionService:
    """Сервис для работы с юридическими задачами"""

    @staticmethod
    def parse_document(file) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }

    @staticmethod
    def explain_text(query: JurisdictionExplainQuery) -> dict:
        return {
            "prompt": "Сгенерируй пост для соцсетей про открытие новой кофейни",
            "answer": "Внимание! Уже завтра на главной улице мы откроем лучшую кофейню в городе. Приходите все!",
            "answerType": "law",
        }
