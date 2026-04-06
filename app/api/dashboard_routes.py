from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config import get_db
from app.auth.auth_dependency import get_current_user
from app.dashboard.dashboard_manager import DashboardManager

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

dashboard = DashboardManager()


@router.get("/")
def get_dashboard(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return dashboard.get_dashboard(
        db,
        user["user_id"]
    )