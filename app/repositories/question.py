from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload, Session
from app.models import Question, Answer


class QuestionRepository:
    def __init__(self, async_session: Session):
        self.async_session = async_session

    async def create(self, data: dict) -> int:
        async with self.async_session as db:
            question = Question(**data)
            db.add(question)
            await db.commit()
            return question.id

    async def get_id(self, id: int) -> Question:
        async with self.async_session as db:
            query = select(Question).where(Question.id == int(id))
            question = await db.execute(query)
            return question.scalars().first()
        

    async def getall(self) -> list[Question]:
        async with self.async_session as db:
            query = select(Question)
            question = await db.execute(query)
            return question.scalars().all()
        
    async def delete(self, id: int) -> None:
        async with self.async_session as db:
            # Находим вопрос
            query = select(Question).where(Question.id == id)
            result = await db.execute(query)
            question = result.scalar_one_or_none()
            
            if question:
                # Удаляем через ORM - сработает каскадное удаление ответов
                await db.delete(question)
                await db.commit()
            return None
