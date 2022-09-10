from typing import List, Union
from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_active = False


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


