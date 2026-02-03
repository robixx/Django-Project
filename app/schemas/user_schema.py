
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
    IsActive: int = 1

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    createDate: datetime
    IsActive: int

    class Config:
        orm_mode = True