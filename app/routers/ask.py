from fastapi import APIRouter
from pydantic import BaseModel

from ..agent import ask_dataframes

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    question: str
    answer: str


@router.post("", response_model=AskResponse)
def ask_question(req: AskRequest):
    answer = ask_dataframes(req.question)
    return AskResponse(question=req.question, answer=answer)
