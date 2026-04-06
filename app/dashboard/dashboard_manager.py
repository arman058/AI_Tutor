from app.models_progress import UserProgress
from app.syllabus.syllabus_manager import SyllabusManager


class DashboardManager:

    def get_dashboard(self, db, user_id):

        completed = db.query(UserProgress).filter(
            UserProgress.user_id == user_id
        ).count()

        syllabus = SyllabusManager()

        total_topics = 0

        for subject in syllabus.get_subjects():

            chapters = syllabus.get_chapters(subject)

            for chapter in chapters:

                topics = syllabus.get_topics(subject, chapter)

                total_topics += len(topics)

        percentage = 0

        if total_topics > 0:
            percentage = round((completed / total_topics) * 100)

        last_topic = db.query(UserProgress)\
            .filter(UserProgress.user_id == user_id)\
            .order_by(UserProgress.id.desc())\
            .first()

        return {
            "completed_topics": completed,
            "total_topics": total_topics,
            "completion_percentage": percentage,
            "recent_topic": last_topic.topic if last_topic else None
        }