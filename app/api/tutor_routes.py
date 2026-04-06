from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth.auth_dependency import get_current_user
from app.config import get_db
from app.tutor.tutor_engine import TutorEngine
from app.teaching.flow_manager import FlowManager

router = APIRouter(
    prefix="/tutor",
    tags=["Tutor"]
)

tutor = TutorEngine()
flow = FlowManager()


class TopicRequest(BaseModel):
    subject: str
    chapter: str
    topic: str


class StartRequest(BaseModel):
    subject: str
    chapter: str


@router.post("/start-learning")
def start_learning(
    data: StartRequest,
    user=Depends(get_current_user)
):

    result = flow.start_learning(
        user["user_id"],
        data.subject,
        data.chapter
    )

    return result


@router.post("/repeat")
def repeat(user=Depends(get_current_user)):

    return flow.repeat(user["user_id"])


@router.post("/example")
def example_topic(
    data: TopicRequest,
    user=Depends(get_current_user)
):

    result = flow.example_topic(
        data.subject,
        data.chapter,
        data.topic
    )

    return result


@router.post("/next")
def next_topic(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return flow.next_topic(
        db,
        user["user_id"]
    )

@router.post("/resume-learning")
def resume_learning(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return flow.resume_learning(
        db,
        user["user_id"]
    )