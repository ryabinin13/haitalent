from app.repositories.answer import AnswerRepository
from app.repositories.question import QuestionRepository
from app.services.answer import AnswerService
from app.services.question import QuestionService
from app.database import get_async_session

def get_answer_repository() -> AnswerRepository:
    async_session = get_async_session()
    return AnswerRepository(async_session)


def get_question_repository() -> QuestionRepository:
    async_session = get_async_session()
    return QuestionRepository(async_session)


def get_answer_service() -> AnswerService:
    answer_repository = get_answer_repository()
    question_repository = get_question_repository()
    return AnswerService(answer_repository, question_repository)


def get_question_service() -> QuestionService:
    answer_repository = get_answer_repository()
    question_repository = get_question_repository()
    return QuestionService(question_repository, answer_repository)