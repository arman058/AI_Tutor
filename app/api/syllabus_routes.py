from fastapi import APIRouter, Depends
from app.auth.auth_dependency import get_current_user
from app.syllabus.syllabus_manager import SyllabusManager

router = APIRouter(
    prefix="/syllabus",
    tags=["Syllabus"]
)

syllabus = SyllabusManager()


@router.get("/subjects")
def get_subjects(user=Depends(get_current_user)):
    return {"subjects": syllabus.get_subjects()}


@router.get("/{subject}/chapters")
def get_chapters(subject: str, user=Depends(get_current_user)):
    return {
        "subject": subject,
        "chapters": syllabus.get_chapters(subject)
    }


@router.get("/{subject}/{chapter}/topics")
def get_topics(subject: str, chapter: str, user=Depends(get_current_user)):
    return {
        "subject": subject,
        "chapter": chapter,
        "topics": syllabus.get_topics(subject, chapter)
    }