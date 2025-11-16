from typing import List
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from datetime import datetime, date
import enum

class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime]

    answers: Mapped[List["Answer"]] = relationship(
        back_populates="question",
        cascade="all, delete-orphan")


class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("question.id"))
    user_id: Mapped[int]
    text: Mapped[str]
    created_at: Mapped[datetime]

    question: Mapped["Question"] = relationship(
        back_populates="answers"
    )