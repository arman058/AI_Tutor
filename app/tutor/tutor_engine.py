from openai import OpenAI
from app.config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL


class TutorEngine:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )

        self.model = "meta-llama/llama-3.1-8b-instruct"

    def explain_topic(self, subject, chapter, topic):

        prompt = f"""
You are an expert programming tutor.

Subject: {subject}
Chapter: {chapter}
Topic: {topic}

Explain the topic clearly like a teacher teaching a beginner.

Rules:
- Use simple language
- Give examples
- Use structured explanation
- At the end ask: Did you understand?
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful programming tutor."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content