from fastapi import APIRouter, Depends, HTTPException
from app.schemas.answer import AnswerSchema
# from app.repositories.answer import AnswerRepository
from app.services.answer import AnswerService
from app.dependencies import get_answer_service
from exceptions import QuestionNotFound, AnswerNotFound


answer_router = APIRouter()


@answer_router.post("/questions/{id}/answers/")
async def create_answer(
    question_id: int,
    answer_schema: AnswerSchema,
    answer_service: AnswerService = Depends(get_answer_service),
):
    try:
        return await answer_service.add_answer(data=answer_schema, question_id=question_id)
    except QuestionNotFound as e:
        raise HTTPException(status_code=404, detail="Вопрос не найден")

@answer_router.get("/answers/{id}")
async def get_answer(
    id: int,
    answer_service: AnswerService = Depends(get_answer_service),
):
    try:
        return await answer_service.get_answer(id=id)
    except AnswerNotFound as e:
        raise HTTPException(status_code=404, detail="Ответ не найден")

@answer_router.delete("/answers/{id}")
async def delete_answer(
    id: int,
     answer_service: AnswerService = Depends(get_answer_service),
):
    try:
        return await answer_service.delete_answer(id=id)
    except AnswerNotFound as e:
        raise HTTPException(status_code=404, detail="Ответ не найден")