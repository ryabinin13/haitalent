from fastapi import FastAPI
from app.routers.answer import answer_router
from app.routers.question import question_router
from app.lifespan import lifespan



app = FastAPI(lifespan=lifespan)

app.include_router(answer_router)
app.include_router(question_router)

