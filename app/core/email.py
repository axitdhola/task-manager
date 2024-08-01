from email.mime.text import MIMEText
import smtplib
from app.core.config import settings

def send_email():
    text = """\
    Hi From Celery,
    Check out the new post on the Mailtrap blog:
    SMTP Server for Testing: Cloud-based or Local?
    https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
    Feel free to let us know what content would be useful for you!
    """

    message = MIMEText(text, "plain")
    message["Subject"] = "Celery text email"
    message["From"] = settings.EMAIL_FROM
    message["To"] = 'axitmw@gmail.com'

    with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
        server.starttls()  
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(settings.EMAIL_FROM, 'axitmw@gmail.com', message.as_string())