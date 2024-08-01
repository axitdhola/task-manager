from fastapi import FastAPI
from app.models import task as model
from app.db.db import engine
from app.api import task, user
from dotenv import load_dotenv

model.Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

app.include_router(task.router, prefix="/tasks", tags=["tasks"])
app.include_router(user.router, prefix="/user", tags=["user"])