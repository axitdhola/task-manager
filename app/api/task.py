from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import task as task_schema
from app.crud import task as task_crud
from app.db.db import get_db

router = APIRouter()

@router.post("/", response_model=task_schema.Task)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_crud.create_task(db, task)
    return db_task