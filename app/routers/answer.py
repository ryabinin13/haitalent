from fastapi import APIRouter, Depends


answer_router = APIRouter()


@answer_router.post("/questions/{id}/answers/")
async def create_answer():
    pass

@answer_router.get("/answers/{id}")
async def get_answer():
    pass

@answer_router.delete("/answers/{id}")
async def delete_answer():
    pass