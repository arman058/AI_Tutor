class SessionManager:

    def __init__(self):

        self.sessions = {}

    def start_session(self, user_id, subject, chapter, topic):

        self.sessions[user_id] = {
            "subject": subject,
            "chapter": chapter,
            "topic": topic
        }

    def get_session(self, user_id):

        return self.sessions.get(user_id)

    def update_topic(self, user_id, topic):

        if user_id in self.sessions:
            self.sessions[user_id]["topic"] = topic

    def clear_session(self, user_id):

        if user_id in self.sessions:
            del self.sessions[user_id]