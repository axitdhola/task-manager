from sqlalchemy.orm import Session
from app.models import task as task_model
from app.schemas import task as task_schema

def create_task(db: Session, task: task_schema.TaskCreate) -> task_model.Task:
    db_task = task_model.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10) -> list[task_model.Task]:
    return db.query(task_model.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int) -> task_model.Task:
    return db.query(task_model.Task).filter(task_model.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task: task_schema.TaskUpdate) -> task_model.Task:
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if db_task: 
        setattr(db_task, 'title', task.title)
        setattr(db_task, 'description', task.description)
        db.commit()
        db.refresh(db_task)
    return db_task
