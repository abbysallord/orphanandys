from fastapi import APIRouter, HTTPException
from models.gallery_image import GalleryImage
from typing import List

router = APIRouter()

@router.get("/gallery", response_model=List[GalleryImage])
async def get_gallery_images():
    \"""
    Get all gallery images
    \"""
    from server import db
    
    try:
        images = await db.gallery_images.find().sort("order", 1).to_list(100)
        
        # Convert MongoDB _id to string
        for item in images:
            item['_id'] = str(item['_id'])
        
        return images
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))