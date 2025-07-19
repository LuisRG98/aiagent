# 🎙️ CodeSync — Intelligent Meeting Assistant

> Transcribe, summarize, and automate task creation from your meetings using AI.

Vocalin is a smart meeting assistant that extracts valuable insights from your meeting recordings. It leverages state-of-the-art transcription (`faster-whisper`) and summarization (`Gemini 2.5 Flash`) models to turn hours of meeting audio into actionable content like summaries, tasks, and Jira tickets.

---

## 🚀 Features

- ✅ **Automatic Audio Transcription** with `faster-whisper`
- ✅ **Meeting Summarization** using Gemini 2.5 Flash (Google AI)
- ✅ **Task Extraction** from meeting content
- ✅ **Jira Integration**: auto-create issues from tasks
- ✅ **Email Summaries** to participants
- ✅ **Streamlit UI**: user-friendly interface for non-devs
- ✅ **Multi-format audio support** (`.mp3`, `.wav`, `.m4a`)
- 🚧 **(Coming Soon)**: multi-language support, versioning, Slack/MS Teams integration

---

## 🎯 Pain Points Solved

- 🧠 No more manual note-taking during meetings  
- 🕑 Save time reviewing entire recordings  
- 🤝 Align teams quickly with shared summaries  
- 📝 Avoid missed tasks or forgotten decisions  
- 🔁 Automate repetitive meeting documentation  
- 🌍 Help global teams with multilingual transcription (planned)

---

## 📦 Tech Stack

- `Python`
- [`faster-whisper`](https://github.com/guillaumekln/faster-whisper) for transcription
- `Gemini 2.5 Flash` (via Google AI) for summarization and task generation
- `Streamlit` for the front-end
- `Jira API` for task creation
- `SMTP` or external service for email delivery

---

## 🖥️ Usage

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/vocalin.git
cd vocalin
