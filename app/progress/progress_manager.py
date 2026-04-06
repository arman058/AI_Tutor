from sqlalchemy.orm import Session
from app.models_progress import UserProgress
from app.syllabus.syllabus_manager import SyllabusManager


class ProgressManager:

    def mark_completed(
        self,
        db: Session,
        user_id,
        subject,
        chapter,
        topic
    ):

        progress = UserProgress(
            user_id=user_id,
            subject=subject,
            chapter=chapter,
            topic=topic,
            completed=True
        )

        db.add(progress)
        db.commit()

        return progress

    def get_user_progress(self, db: Session, user_id):

        return db.query(UserProgress).filter(
            UserProgress.user_id == user_id
        ).all()

    # Topic Resume
    def get_resume_topic(self, db: Session, user_id):

        last = db.query(UserProgress)\
            .filter(UserProgress.user_id == user_id)\
            .order_by(UserProgress.id.desc())\
            .first()

        if not last:
            return None

        syllabus = SyllabusManager()

        topics = syllabus.get_topics(
            last.subject,
            last.chapter
        )

        if last.topic not in topics:
            return None

        index = topics.index(last.topic)

        if index + 1 >= len(topics):
            return None

        next_topic = topics[index + 1]

        return {
            "subject": last.subject,
            "chapter": last.chapter,
            "topic": next_topic
        }