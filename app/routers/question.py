from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
# from app.repositories.question import QuestionRepository
from app.services.question import QuestionService
from app.dependencies import get_question_service
from app.schemas.question import QuestionSchema
from exceptions import QuestionNotFound


question_router = APIRouter()


@question_router.get("/questions/")
async def get_questions(
    question_service: QuestionService = Depends(get_question_service),
):
    return await question_service.get_all_questions()

@question_router.post("/questions/")
async def create_question(
    question_schema: QuestionSchema,
    question_service: QuestionService = Depends(get_question_service),
):
    return await question_service.add_question(data=question_schema)

@question_router.get("/questions/{id}")
async def get_question(
    id: int,
    question_service: QuestionService = Depends(get_question_service),
):
    try:
        return await question_service.get_question(id=id)
    except QuestionNotFound as e:
        raise HTTPException(status_code=404, detail="Вопрос не найден")


@question_router.delete("/questions/{id}")
async def delete_questions(
    id: int,
    question_service: QuestionService = Depends(get_question_service),
):
    try:
        return await question_service.delete_question(id=id)
    except QuestionNotFound as e:
        raise HTTPException(status_code=404, detail="Вопрос не найден")