from app.tutor.tutor_engine import TutorEngine
from app.syllabus.syllabus_manager import SyllabusManager
from app.session.session_manager import SessionManager
from app.progress.progress_manager import ProgressManager


class FlowManager:

    def __init__(self):

        self.tutor = TutorEngine()
        self.syllabus = SyllabusManager()
        self.session = SessionManager()
        self.progress_manager = ProgressManager()

    def start_learning(self, user_id, subject, chapter):

        topics = self.syllabus.get_topics(subject, chapter)

        if not topics:
            return {"message": "No topics found"}

        topic = topics[0]

        self.session.start_session(
            user_id,
            subject,
            chapter,
            topic
        )

        explanation = self.tutor.explain_topic(
            subject,
            chapter,
            topic
        )

        return {
            "topic": topic,
            "explanation": explanation
        }

    def repeat(self, user_id):

        session = self.session.get_session(user_id)

        explanation = self.tutor.explain_topic(
            session["subject"],
            session["chapter"],
            session["topic"]
        )

        return {
            "topic": session["topic"],
            "explanation": explanation
        }

    def next_topic(self, db, user_id):

        session = self.session.get_session(user_id)

        if not session:
            return {"message": "Session not found"}

        topics = self.syllabus.get_topics(
            session["subject"],
            session["chapter"]
        )

        index = topics.index(session["topic"])

        # mark completed
        self.progress_manager.mark_completed(
            db,
            user_id,
            session["subject"],
            session["chapter"],
            session["topic"]
        )

        if index + 1 >= len(topics):
            return {"message": "Chapter completed 🎉"}

        next_topic = topics[index + 1]

        self.session.update_topic(
            user_id,
            next_topic
        )

        explanation = self.tutor.explain_topic(
            session["subject"],
            session["chapter"],
            next_topic
        )

        return {
            "topic": next_topic,
            "explanation": explanation
        }

    # Resume Learning
    def resume_learning(self, db, user_id):

        data = self.progress_manager.get_resume_topic(
            db,
            user_id
        )

        if not data:
            return {"message": "No previous learning found"}

        subject = data["subject"]
        chapter = data["chapter"]
        topic = data["topic"]

        self.session.start_session(
            user_id,
            subject,
            chapter,
            topic
        )

        explanation = self.tutor.explain_topic(
            subject,
            chapter,
            topic
        )

        return {
            "subject": subject,
            "chapter": chapter,
            "topic": topic,
            "explanation": explanation
        }