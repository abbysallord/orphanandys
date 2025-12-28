from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from models.menu_item import MenuItem
from typing import List
import os

router = APIRouter()

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

@router.get("/menu", response_model=List[MenuItem])
async def get_menu_items():
    """
    Get all menu items
    """
    try:
        menu_items = await db.menu_items.find().to_list(100)
        
        # Convert MongoDB _id to string
        for item in menu_items:
            item['_id'] = str(item['_id'])
        
        return menu_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))