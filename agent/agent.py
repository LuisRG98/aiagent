import re
from services.gemini_client import summarize_transcript

class MeetingAgent:
    def __init__(self, transcript):
        self.transcript = transcript
        self.summary = ""
        self.tasks = []
        self.participants = []

    def deliberate(self):
        raw_response = summarize_transcript(self.transcript)

        # Puedes imprimir esto para debug: print(raw_response)

        # Extraer partes usando regex si no lo separas en JSON
        self.participants = re.findall(r"(?i)Participantes?:\s*(.+)", raw_response)
        self.summary = self._extract_section(raw_response, "Resumen")
        self.tasks = self._extract_tasks(raw_response)

    def _extract_section(self, text, section_title):
        pattern = rf"{section_title}:\s*(.+?)(?:\n\n|$)"
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else "No disponible."

    def _extract_tasks(self, text):
        tasks = []
        for line in text.splitlines():
            if re.match(r"[-*•]\s", line):
                tasks.append(line.strip("-*• ").strip())
        return tasks

    def execute(self):
        return self.summary, self.tasks, self.participants
