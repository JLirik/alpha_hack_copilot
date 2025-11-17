from pydantic import BaseModel


class MarketingGenerateQuery(BaseModel):
    """Модель запроса для генерации маркетингового контента"""
    topic: str


class MarketingRegenerateQuery(BaseModel):
    """Модель запроса для перегенерации маркетингового контента"""
    contentId: str


class JurisdictionExplainQuery(BaseModel):
    """Модель запроса для объяснения юридического пункта или текста"""
    clause: str
    documentId: str


class HireQuestionQuery(BaseModel):
    """Модель запроса для обработки вопроса по найму"""
    query: str


class FinanceQuestionQuery(BaseModel):
    """Модель запроса для обработки финансового вопроса"""
    query: str


class GeneralQuestionQuery(BaseModel):
    """Модель запроса для обработки общего вопроса"""
    query: str


class AuthRequest(BaseModel):
    """Модель запроса для аутентификации пользователя"""
    username: str
    password: str


class RefreshRequest(BaseModel):
    """Модель запроса для обновления JWT-токена"""
    username: str
    refreshToken: str


class RegRequest(BaseModel):
    """Модель запроса для регистрации нового пользователя"""
    username: str
    password: str
    business: str
    city: str
    name: str


class UpdateSettingsRequest(BaseModel):
    """Модель запроса для обновления настроек пользователя"""
    username: Optional[str] = None
    password: Optional[str] = None
    current_password: Optional[str] = None
    business: Optional[str] = None
    city: Optional[str] = None
    name: Optional[str] = None
