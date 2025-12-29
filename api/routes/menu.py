from fastapi import APIRouter, HTTPException
from models.menu_item import MenuItem
from typing import List

router = APIRouter()

@router.get("/menu", response_model=List[MenuItem])
async def get_menu_items():
    """
    Get all menu items
    Returns list of menu items with proper error handling
    """
    from server import db
    
    try:
        menu_items = await db.menu_items.find().to_list(100)
        
        if not menu_items:
            return []
        
        # Convert MongoDB _id to string and validate data
        for item in menu_items:
            item['_id'] = str(item['_id'])
        
        return menu_items
    except Exception as e:
        # Log error but don't expose internal details
        print(f"Error fetching menu items: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail="Unable to fetch menu items. Please try again later."
        )