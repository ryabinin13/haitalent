from app.repositories.answer import AnswerRepository
from app.repositories.question import QuestionRepository
from app.database import get_async_session

def get_answer_repository() -> AnswerRepository:
    async_session = get_async_session()
    return AnswerRepository(async_session)


def get_question_repository() -> QuestionRepository:
    async_session = get_async_session()
    return QuestionRepository(async_session)