from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import task as task_schema
from app.crud import task as task_crud
from app.db.db import get_db
from app.worker import send_task_email
from app.core import auth

router = APIRouter(
    dependencies=[Depends(auth.get_current_user)],
)

@router.post("/", response_model=task_schema.Task)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    db_task = task_crud.create_task(db, task)
    send_task_email.delay(db_task.id)
    return db_task

@router.get("/", response_model=list[task_schema.Task])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    tasks = task_crud.get_tasks(db, skip, limit)
    return tasks

@router.get("/task_id", response_model=task_schema.Task)
def get_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    tasks = task_crud.get_task(db, task_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks

@router.put("/task_id", response_model=task_schema.Task)
def update_task(task_id: int, task: task_schema.TaskUpdate, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    db_task = task_crud.update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/task_id")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(auth.get_current_user)):
    db_task = task_crud.delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task" + str(task_id) + " deleted successfully"}