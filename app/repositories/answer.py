from sqlalchemy.orm import selectinload, Session
from app.models import Answer
from sqlalchemy import select, delete


class AnswerRepository:
    def __init__(self, async_session: Session):
        self.async_session = async_session

    async def create(self, data: dict) -> int:
        async with self.async_session as db:
            answer = Answer(**data)
            db.add(answer)
            await db.commit()
            return answer.id
        
    async def get_id(self, id: int) -> Answer:
        async with self.async_session as db:
            query = select(Answer).where(Answer.id == int(id))
            answer = await db.execute(query)
            return answer.scalars().first()
        
    async def delete(self, id: int) -> None:
        async with self.async_session as db:
            query = delete(Answer).where(Answer.id == id)
            await db.execute(query)
            await db.commit()
            return None
        

    async def get_answers_with_question(self, question_id):
        async with self.async_session as db:
            pass