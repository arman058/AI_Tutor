import json
import os


class SyllabusManager:

    def __init__(self):

        file_path = os.path.join(
            os.path.dirname(__file__),
            "syllabus.json"
        )

        with open(file_path, "r") as f:
            self.syllabus = json.load(f)

    def get_subjects(self):

        return list(self.syllabus.keys())

    def get_chapters(self, subject):

        if subject not in self.syllabus:
            return []

        return list(self.syllabus[subject].keys())

    def get_topics(self, subject, chapter):

        if subject not in self.syllabus:
            return []

        if chapter not in self.syllabus[subject]:
            return []

        return self.syllabus[subject][chapter]