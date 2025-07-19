import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración SMTP desde el entorno
SMTP_CONFIG = {
    "server": os.getenv("SMTP_SERVER"),
    "port": int(os.getenv("SMTP_PORT")),
    "user": os.getenv("SMTP_USER"),
    "password": os.getenv("SMTP_PASSWORD"),
    "sender": os.getenv("SMTP_SENDER")
}

def send_email(subject: str, body: str, to: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_CONFIG["sender"]
    msg["To"] = to
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_CONFIG["server"], SMTP_CONFIG["port"]) as smtp:
            smtp.starttls()
            smtp.login(SMTP_CONFIG["user"], SMTP_CONFIG["password"])
            smtp.send_message(msg)
            print(f"✅ Correo enviado a {to}")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
