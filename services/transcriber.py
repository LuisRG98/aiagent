from faster_whisper import WhisperModel

def transcribe_audio(audio_path: str) -> str:
    model = WhisperModel("base", compute_type="float32")
    segments, _ = model.transcribe(audio_path)
    transcript = " ".join([segment.text for segment in segments])
    return transcript
