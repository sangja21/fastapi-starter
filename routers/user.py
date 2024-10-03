from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from controller import user_controller
from model import user_model # SQLAlchemy 모델
from schemas import schemas  # Pydantic 모델
from config.database import get_db  # db 세션 가져오기

router = APIRouter()

# 사용자 생성
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return user_controller.create_user(user, db)

# 사용자 목록 조회
@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_controller.read_users(skip, limit, db)

# 특정 사용자 조회
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.read_user(user_id, db)
