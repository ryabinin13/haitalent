from sqlalchemy import select
from sqlalchemy.orm import selectinload, Session
from app.models.question import Question


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
            return db.query(Question).all()
