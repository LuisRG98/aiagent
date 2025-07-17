from services.transcriber import transcribe_audio
from agent.agent import MeetingAgent

if __name__ == "__main__":
    print("🎙 Transcribiendo reunión...")
    transcript = transcribe_audio("data/meeting.mp3")

    agent = MeetingAgent(transcript)
    agent.deliberate()
    agent.execute()
