from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import task as task_model
from app.schemas import task as task_schema

def create_task(db: Session, task: task_schema.TaskCreate, user_id: int) -> task_model.Task:
    db_task = task_model.Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> list[task_model.Task]:
    return db.query(task_model.Task).filter(task_model.Task.user_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int, user_id: int) -> task_model.Task:
    return db.query(task_model.Task).filter(
        and_(
            task_model.Task.id == task_id,
            task_model.Task.user_id == user_id
        )
    ).first()

def update_task(db: Session, task_id: int, task: task_schema.TaskUpdate, user_id: int) -> task_model.Task:
    db_task = db.query(task_model.Task).filter(
        and_(
            task_model.Task.id == task_id,
            task_model.Task.user_id == user_id
        )
    ).first()

    if db_task: 
        setattr(db_task, 'title', task.title)
        setattr(db_task, 'description', task.description)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = db.query(task_model.Task).filter(
        and_(
            task_model.Task.id == task_id,
            task_model.Task.user_id == user_id
        )
    ).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
    