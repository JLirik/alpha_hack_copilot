from datetime import datetime


class APIResponse:
    """Стандартизированная модель ответа API"""

    @staticmethod
    def success(prompt: str, answer: str, answer_type: str, request_id: str, addition: dict = {}):
        return {
            "prompt": prompt,
            "answer": answer,
            "answerType": answer_type,
            "request_id": request_id,
            "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        } | addition, 200

    @staticmethod
    def error(error: str, request_id: str = "", code: int = 400):
        return {
            "error": error,
            "code": code,
            "request_id": request_id
        }, code
