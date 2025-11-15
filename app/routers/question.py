from fastapi import APIRouter, Depends
from typing import Annotated
from app.repositories.question import QuestionRepository
from app.dependencies import get_question_repository
from app.schemas.question import QuestionSchema


question_router = APIRouter()


@question_router.get("/questions/")
async def get_questions(
    answer_repository: QuestionRepository = Depends(get_question_repository),
):
    return await answer_repository.getall()

@question_router.post("/questions/")
async def create_questions(
    question_schema: QuestionSchema,
    answer_repository: QuestionRepository = Depends(get_question_repository),
):
    return await answer_repository.create(data=question_schema)

@question_router.get("/questions/{id}")
async def get_question(id: int):
    pass


@question_router.delete("/questions/{id}")
async def delete_questions(id: int):
    pass