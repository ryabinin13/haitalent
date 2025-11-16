from pydantic import BaseModel, Field
from datetime import datetime

class AnswerSchema(BaseModel):
    text: str
    user_id: int
    