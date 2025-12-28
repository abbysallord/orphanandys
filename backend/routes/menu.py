from fastapi import APIRouter, HTTPException
from models.menu_item import MenuItem
from typing import List

router = APIRouter()

# Database will be injected via dependency
@router.get("/menu", response_model=List[MenuItem])
async def get_menu_items():
    \"""
    Get all menu items
    \"""
    from server import db
    
    try:
        menu_items = await db.menu_items.find().to_list(100)
        
        # Convert MongoDB _id to string
        for item in menu_items:
            item['_id'] = str(item['_id'])
        
        return menu_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))