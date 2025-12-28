from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.busy_time import BusyTime
from typing import List
import os

router = APIRouter()

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

@router.get("/busy-times", response_model=List[BusyTime])
async def get_busy_times():
    """
    Get busy times data
    """
    try:
        busy_times = await db.busy_times.find().sort("order", 1).to_list(100)
        
        # Convert MongoDB _id to string
        for item in busy_times:
            item['_id'] = str(item['_id'])
        
        return busy_times
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))