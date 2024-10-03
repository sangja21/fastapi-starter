from sqlalchemy.orm import Session
from fastapi import HTTPException

from schemas import schemas
from service import user_service

def create_user(user: schemas.UserBase , db: Session):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user, db)

def read_users(skip: int, limit: int, db: Session):
    return user_service.get_users(db, skip, limit)

def read_user(user_id: int, db: Session):
    user = user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
