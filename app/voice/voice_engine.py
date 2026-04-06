import edge_tts

class VoiceEngine:

    async def stream_voice(self, text):

        communicate = edge_tts.Communicate(
            text,
            voice="en-US-GuyNeural"
        )

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]