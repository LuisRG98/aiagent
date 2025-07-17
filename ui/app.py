import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.transcriber import transcribe_audio
from services.gemini_client import summarize_transcript, extract_tasks
from services.jira_client import create_jira_task
import tempfile

st.title("🤖 Asistente Inteligente de Reuniones")

uploaded_file = st.file_uploader("📤 Sube un archivo de audio", type=["mp3", "wav", "m4a"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        audio_path = tmp_file.name

    st.info("🔍 Transcribiendo audio...")
    transcript = transcribe_audio(audio_path)

    st.subheader("📝 Transcripción")
    st.write(transcript)

    st.info("✍️ Generando resumen...")
    summary = summarize_transcript(transcript)
    st.subheader("📌 Resumen y Tareas")
    st.markdown(summary)

    st.info("📋 Extrayendo tareas para Jira...")
    tasks = extract_tasks(transcript)
    print(tasks)
    if tasks:
        for task in tasks:
           
            issue_key = create_jira_task(task)
            st.success(f"Tarea creada en Jira: `{issue_key}` - {task['descripcion']}")
    else:
        st.warning("No se encontraron tareas claras en la transcripción.")
