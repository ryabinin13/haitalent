from fastapi import APIRouter


question_router = APIRouter()


@question_router.get("/questions/")
async def get_questions():
    pass

@question_router.post("/questions/")
async def create_questions():
    pass

@question_router.get("/questions/{id}")
async def get_question(id: int):
    pass


@question_router.delete("/questions/{id}")
async def delete_questions(id: int):
    pass