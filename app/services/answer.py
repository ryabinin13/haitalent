from app.repositories.answer import AnswerRepository
from app.repositories.question import QuestionRepository
from exceptions import QuestionNotFound, AnswerNotFound

from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class AnswerService:
    def __init__(self, answer_repository: AnswerRepository, question_repository: QuestionRepository):
        self.answer_repository = answer_repository
        self.question_repository = question_repository

    async def add_answer(self, data, question_id):


        question = await self.question_repository.get_id(question_id)

        if not question:
            logger.error(f"Вопрос не существует")
            raise QuestionNotFound
        
        logger.info("Вопрос существует")

        data = data.model_dump()
        data["question_id"] = question_id
        data["created_at"] = datetime.now()

        return await self.answer_repository.create(data=data)

    async def get_answer(self, id):
        answer = await self.answer_repository.get_id(id=id)
        if not answer:
            logger.error(f"Ответ не существует")
            raise AnswerNotFound
        logger.info("Ответ существует")
        return answer
    
    async def delete_answer(self, id):
        answer = await self.answer_repository.get_id(id=id)
        if not answer:
            logger.error(f"Ответ не существует")
            raise AnswerNotFound
        logger.info("Ответ существует")
        return await self.answer_repository.delete(id=id)