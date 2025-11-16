from app.repositories.question import QuestionRepository
from app.repositories.answer import AnswerRepository
from exceptions import QuestionNotFound

from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class QuestionService:
    def __init__(self, question_repositore: QuestionRepository, answer_repository = AnswerRepository):
        self.question_repository = question_repositore
        self.answer_repository = answer_repository


    async def get_all_questions(self):
        return await self.question_repository.getall()
    

    async def add_question(self, data):
        data = data.model_dump()
        data['created_at'] = datetime.now()
        return await self.question_repository.create(data=data)
    

    async def get_question(self, id):
        question = await self.question_repository.get_id(id=id)
        if not question:
            logger.error(f"Вопрос не существует")
            raise QuestionNotFound
        
        logger.info("Вопрос существует")
        return question
    

    async def delete_question(self, id):
        question = await self.question_repository.get_id(id=id)
        if not question:
            logger.error(f"Вопрос не существует")
            raise QuestionNotFound
        logger.info("Вопрос существует")
        return await self.question_repository.delete(id=id)
    
