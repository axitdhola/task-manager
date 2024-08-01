from email.mime.text import MIMEText
import smtplib
from app.core.config import settings
from app.schemas import task as task_schema
from app.schemas import user as user_schema

def send_email(user: user_schema.User, task: task_schema.Task):
    text = f"""\
    Hi {user.name},
    You have created a new task
    Task title : {task.title}
    Task description : {task.description}
    Thank you.
    """

    message = MIMEText(text, "plain")
    message["Subject"] = "Celery text email"
    message["From"] = settings.EMAIL_FROM
    message["To"] = user.email

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()  
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(settings.EMAIL_FROM, 'axitmw@gmail.com', message.as_string())