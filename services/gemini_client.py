import os
import re
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_transcript(transcript: str) -> str:
    prompt = f"""
Actúa como un asistente de reuniones.
Basado en la siguiente transcripción:

1. Extrae los nombres de los participantes mencionados o que hablaron.
2. Resume brevemente los puntos clave discutidos.
3. Extrae una lista de tareas, acciones o acuerdos.

Transcripción:
{transcript}
"""
    response = model.generate_content(prompt)
    return response.text

def extract_tasks(transcript: str) -> list[dict]:
    prompt = f"""
Extrae todas las tareas de esta transcripción.

Por cada tarea incluye:
- "descripcion"
- "responsable"
- "fecha_limite" (si no se menciona, usa "No especificada")

Devuelve SOLO el JSON. No agregues ningún comentario, texto adicional ni bloque Markdown.

Ejemplo de salida:
[
  {{
    "descripcion": "Enviar el reporte financiero",
    "responsable": "Luis",
    "fecha_limite": "mañana"
  }}
]

Transcripción:
{transcript}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()

        # Elimina posibles bloques Markdown
        text = re.sub(r"^```json|```$", "", text).strip()

        return json.loads(text)

    except json.JSONDecodeError as e:
        print("❌ Error al parsear JSON:", e)
        print("Contenido recibido:\n", response.text)
        return []
    except Exception as e:
        print("❌ Error inesperado:", e)
        return [] 