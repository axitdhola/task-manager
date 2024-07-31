from sqlalchemy.orm import Session
from app.models import task as task_model
from app.schemas import task as task_schema

def create_task(db: Session, task: task_schema.TaskCreate) -> task_model.Task:
    db_task = task_model.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

