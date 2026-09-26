from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from app.core.enums import UserRole

class Message(BaseModel):
    message: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    username : str
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    full_name: str
    phone : str = Field(min_length=10, max_length=15)   

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)

class UserUpdate(BaseModel):
    full_name: str
    email: EmailStr
    phone : str = Field(min_length=10, max_length=15)

class ChangePassword(BaseModel):
    old_password: str = Field(min_length=6, max_length=72)

    new_password: str = Field(min_length=6, max_length=72)
class UserResponse(BaseModel):
    id : int
    username: str
    email: EmailStr
    full_name: str
    phone: str
    role: UserRole
    avatar_url: str | None = None
    avatar_public_id: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
