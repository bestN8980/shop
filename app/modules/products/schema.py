from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class Message(BaseModel):
    message: str

class ProductCreate(BaseModel):
    name : str
    description: str | None = None
    price: int
    stock: int
    category_id : int

class ProductUpdate(BaseModel):
    name: str | None = None
    description: str| None = None
    price: int| None = None
    stock: int| None = None
    category_id : int| None = None

class ProductResponse(BaseModel):
    id: int
    name : str
    description: str|None
    price: int
    stock: int
    category_id: int
    image_url: str | None = None
    image_public_id: str | None = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)