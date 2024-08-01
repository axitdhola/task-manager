from celery import Celery
from asgiref.sync import async_to_sync
from app.core.email import send_email
from app.core.config import settings
celery_app = Celery(
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL, 
    broker_connection_retry_on_startup=True
)

@celery_app.task()
def send_task_email(task_id: int):
    try:
        send_email()
    except Exception as e:
        print(e)


