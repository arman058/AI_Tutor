from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import get_db
from app.auth.auth_dependency import get_current_user
from app.progress.progress_manager import ProgressManager

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)

progress_manager = ProgressManager()


@router.get("/my-progress")
def my_progress(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    data = progress_manager.get_user_progress(
        db,
        user["user_id"]
    )

    return data


@router.get("/resume")
def resume_learning(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    data = progress_manager.get_resume_topic(
        db,
        user["user_id"]
    )

    if not data:
        return {"message": "No previous learning found"}

    return data