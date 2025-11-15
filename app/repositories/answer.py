from sqlalchemy.orm import selectinload, Session


class AnswerRepository:
    def __init__(self, async_session: Session):
        self.async_session = async_session