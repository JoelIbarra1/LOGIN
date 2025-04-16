from pydantic import BaseModel,EmailStr
from typing import Optional

# ITEMS
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# USERS
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
