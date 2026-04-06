from sqlalchemy import Column, Integer, String, Boolean
from app.models import Base


class UserProgress(Base):

    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer)

    subject = Column(String)

    chapter = Column(String)

    topic = Column(String)

    completed = Column(Boolean, default=False)