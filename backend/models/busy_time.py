from pydantic import BaseModel, Field
from datetime import datetime

class BusyTime(BaseModel):
    id: str = Field(default=None, alias='_id')
    hour: str
    value: int
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True