from pydantic import BaseModel

class AnswerSchema(BaseModel):
    text: str
    question_id: int
    user_id: int