from pydantic import BaseModel, Field
from datetime import datetime


class QuestionSchema(BaseModel):
    text: str
    