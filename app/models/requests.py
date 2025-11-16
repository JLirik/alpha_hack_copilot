from pydantic import BaseModel


class MarketingGenerateQuery(BaseModel):
    """Модель запроса для генерации маркетингового контента"""

    topic: str
    amount: int
    style: str
    contentType: str


class MarketingRegenerateQuery(BaseModel):
    """Модель запроса для перегенерации маркетингового контента"""

    contentId: str


class JurisdictionExplainQuery(BaseModel):
    """Модель запроса для объяснения юридического пункта или текста"""

    clause: str
    documentId: str


class HireCreateOfferQuery(BaseModel):
    """Модель запроса для генерации предложения о работе"""

    vacancy: str
    maxSalary: int
    minSalary: int
    responsibilities: str


class HirePostOfferQuery(BaseModel):
    """Модель запроса для публикации вакансии"""

    vacancy: str
    maxSalary: int
    minSalary: int
    description: str
    area: str


class HireQuestionQuery(BaseModel):
    """Модель запроса для обработки вопроса по найму"""

    query: str


class FinanceQuestionQuery(BaseModel):
    """Модель запроса для обработки финансового вопроса"""
    query: str


class GeneralQuestionQuery(BaseModel):
    """Модель запроса для обработки общего вопроса"""
    query: str
