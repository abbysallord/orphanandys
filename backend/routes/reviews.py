from fastapi import APIRouter, HTTPException
from models.review_stats import ReviewStats

router = APIRouter()

@router.get("/reviews/stats", response_model=ReviewStats)
async def get_review_stats():
    \"""
    Get review statistics
    \"""
    from server import db
    
    try:
        stats = await db.review_stats.find_one()
        
        if not stats:
            raise HTTPException(status_code=404, detail="Review stats not found")
        
        stats['_id'] = str(stats['_id'])
        return stats
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))