from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class RatingBreakdown(BaseModel):
    stars: int
    count: int
    percentage: int

class PopularKeyword(BaseModel):
    word: str
    count: int

class ReviewStats(BaseModel):
    id: str = Field(default=None, alias='_id')
    average: float
    total: int
    breakdown: List[RatingBreakdown]
    popularKeywords: List[PopularKeyword]
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True