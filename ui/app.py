import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.transcriber import transcribe_audio
from services.gemini_client import summarize_transcript, extract_tasks
from services.jira_client import create_jira_task
import tempfile
from services.mailer import send_email


st.title("🤖 ConverSync")

uploaded_file = st.file_uploader("📤 Upload your audio file", type=["mp3", "wav", "m4a"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_file.write(uploaded_file.read())
        audio_path = tmp_file.name

    st.info("🔍 Transcribing audio...")
    transcript = transcribe_audio(audio_path)

    st.subheader("📝 Transcription")
    st.write(transcript)

    st.info("✍️ Generating summary...")
    summary = summarize_transcript(transcript)
    st.subheader("📌 Summary and Tasks")
    st.markdown(summary)

    st.info("📋 Extracting tasks for Jira...")
    tasks = extract_tasks(transcript)
    if tasks:
        for task in tasks:
           
            issue_key = create_jira_task(task)
            st.success(f"Task created in Jira: `{issue_key}` - {task['descripcion']}")
    else:
        st.warning("No clear tasks found in the transcript.")

    email_to = st.text_input("✉️ Email to send summary")

if st.button("Send summary via email"):
    from services.mailer import send_email, SMTP_CONFIG

    try:
        send_email(
            "Meeting Summary",
            summary,
            email_to,
        )
        st.success(f"📨 Summary sent to {email_to}")
    except Exception as e:
        st.error(f"❌ Could not send email: {e}")

