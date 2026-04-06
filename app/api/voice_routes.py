from fastapi import APIRouter, WebSocket
from app.tutor.tutor_engine import TutorEngine
from app.voice.voice_engine import VoiceEngine

router = APIRouter()

tutor = TutorEngine()
voice = VoiceEngine()


@router.websocket("/voice-tutor")
async def voice_tutor(websocket: WebSocket):

    await websocket.accept()

    while True:

        data = await websocket.receive_json()

        subject = data["subject"]
        chapter = data["chapter"]
        topic = data["topic"]

        explanation = tutor.explain_topic(
            subject,
            chapter,
            topic
        )

        async for audio_chunk in voice.stream_voice(explanation):

            await websocket.send_bytes(audio_chunk)

        await websocket.send_text("END")