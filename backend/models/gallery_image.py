from pydantic import BaseModel, Field
from datetime import datetime

class GalleryImage(BaseModel):
    id: str = Field(default=None, alias='_id')
    url: str
    alt: str
    category: str = "general"
    order: int = 0
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True