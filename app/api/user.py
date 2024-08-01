from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.crud import user as user_crud
from app.db.db import get_db
from app.core import auth
router = APIRouter()


@router.post("/register", response_model=user_schema.User)
def create_user(user: user_schema.CreateUser, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = auth.get_password_hash(user.password)
    return user_crud.create_user(db=db, user=user)

@router.post("/login", response_model=user_schema.Token)
def login_user(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email")
    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    access_token = auth.create_access_token(data={"id": db_user.id, "email": db_user.email})
    return user_schema.Token(access_token=access_token, token_type="bearer")

@router.get("/me", response_model=user_schema.User)
def get_current_user(current_user: user_schema.User = Depends(auth.get_current_user)):
    return current_user