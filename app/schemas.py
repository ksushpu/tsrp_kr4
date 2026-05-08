from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    username: str
    age: int = Field(gt=18)
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'

class UserResponse(BaseModel):
    id: int
    username: str
    age: int
    email: str
    phone: Optional[str] = 'Unknown'

class ProductCreate(BaseModel):
    title: str
    price: float
    count: int
    description: str

class ProductResponse(BaseModel):
    id: int
    title: str
    price: float
    count: int
    description: str
    model_config = ConfigDict(from_attributes=True)

class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: Optional[str] = None