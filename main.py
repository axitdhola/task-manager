from fastapi import FastAPI
from app.models import task as model
from app.db.db import engine
from app.api import task
model.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(task.router, prefix="/tasks", tags=["tasks"])