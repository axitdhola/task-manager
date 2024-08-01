from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.db.db import get_db

def create_user(db: Session, user: user_schema.CreateUser):
    db_user = user_model.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()