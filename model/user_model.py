from sqlalchemy import Column, Integer, String

# database.py에서 생성한 Base import
from config.database import Base

# User 테이블 정의
class User(Base):
        # 해당 모델이 사용할 table 이름 지정
    __tablename__ = "users"

    # Model의 attribute(column) 생성 -> "="를 사용하여 속성을 정의
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
