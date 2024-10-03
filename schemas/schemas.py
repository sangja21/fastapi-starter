from typing import List, Union

from pydantic import BaseModel


# UserBase 생성
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    email: str

    class Config:
        from_attributes = True
