from celery import Celery
from asgiref.sync import async_to_sync
from app.core.email import send_email
from app.core.config import settings
from sqlalchemy.orm import Session
from app.schemas import task
from app.schemas import user as user_schema
from app.crud import user as user_crud, task as task_crud
from app.db.db import get_db

celery_app = Celery(
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL, 
    broker_connection_retry_on_startup=True
)

@celery_app.task()
def send_task_email(user_id : int, task_id : int):
    try:
        db = next(get_db())
        user = user_crud.get_user_by_id(db, user_id = user_id)
        task = task_crud.get_task(db, task_id = task_id, user_id = user_id)
        send_email(user , task)
    except Exception as e:
        print(e)


