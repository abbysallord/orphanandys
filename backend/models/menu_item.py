from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MenuItem(BaseModel):
    id: str = Field(default=None, alias='_id')
    name: str
    description: str
    price: str
    image: str
    category: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "Fluffy Pancakes",
                "description": "Stack of golden pancakes",
                "price": "12.99",
                "image": "https://example.com/image.jpg",
                "category": "breakfast"
            }
        }

class MenuItemCreate(BaseModel):
    name: str
    description: str
    price: str
    image: str
    category: str