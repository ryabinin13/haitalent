from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import Base, async_engine

@asynccontextmanager
async def lifespan(app: FastAPI):

    async with async_engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)