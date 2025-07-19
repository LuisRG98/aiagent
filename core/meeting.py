# core/meeting.py
from services.transcriber import transcribe_audio
from agent.agent import MeetingAgent

def run_meeting_assistant(audio_path: str):
    print("🎙 Transcribiendo reunión...")
    transcript = transcribe_audio(audio_path)

    agent = MeetingAgent(transcript)
    agent.deliberate()
    agent.execute()
