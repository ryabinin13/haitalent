from fastapi import FastAPI
from app.routers.answer import answer_router
from app.routers.question import question_router

app = FastAPI()

app.include_router(answer_router)
app.include_router(question_router)

