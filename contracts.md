# Orphan Andy's Restaurant - Backend Integration Contracts

## Current State (Mocked Data)
All data is currently stored in `/app/frontend/src/data/mockData.js`:
- MENU_ITEMS (9 items with name, description, price, image)
- REVIEWS_STATS (rating breakdown, total reviews, popular keywords)
- BUSY_TIMES (hourly traffic data)
- GALLERY_IMAGES (8 images with URLs and alt text)

## Backend Implementation Plan

### 1. Database Models

#### MenuItemModel
```python
{
  "_id": ObjectId,
  "name": String,
  "description": String,
  "price": Float,
  "image": String (URL),
  "category": String (breakfast/burgers/drinks/sides),
  "createdAt": DateTime
}
```

#### ReviewStatsModel
```python
{
  "_id": ObjectId,
  "average": Float,
  "total": Integer,
  "breakdown": [
    {
      "stars": Integer,
      "count": Integer,
      "percentage": Integer
    }
  ],
  "popularKeywords": [
    {
      "word": String,
      "count": Integer
    }
  ],
  "updatedAt": DateTime
}
```

#### BusyTimeModel
```python
{
  "_id": ObjectId,
  "hour": String (e.g., "12 PM"),
  "value": Integer (percentage),
  "dayOfWeek": String (optional),
  "updatedAt": DateTime
}
```

#### GalleryImageModel
```python
{
  "_id": ObjectId,
  "url": String,
  "alt": String,
  "category": String (diner/food/interior),
  "order": Integer,
  "createdAt": DateTime
}
```

### 2. API Endpoints

#### GET /api/menu
- **Response**: List of menu items
- **Status**: 200 OK
```json
[
  {
    "id": "string",
    "name": "string",
    "description": "string",
    "price": "string",
    "image": "string",
    "category": "string"
  }
]
```

#### GET /api/reviews/stats
- **Response**: Review statistics
- **Status**: 200 OK
```json
{
  "average": 4.5,
  "total": 2387,
  "breakdown": [...],
  "popularKeywords": [...]
}
```

#### GET /api/busy-times
- **Response**: Busy times data
- **Status**: 200 OK
```json
[
  {
    "hour": "12 PM",
    "value": 95
  }
]
```

#### GET /api/gallery
- **Response**: Gallery images
- **Status**: 200 OK
```json
[
  {
    "url": "string",
    "alt": "string"
  }
]
```

### 3. Frontend Integration Changes

#### Files to Update:
1. **MenuHighlights.js**
   - Remove: `import { MENU_ITEMS } from '../data/mockData'`
   - Add: API call to fetch menu items
   - Add: Loading state and error handling

2. **Reviews.js**
   - Remove: `import { REVIEWS_STATS, POPULAR_KEYWORDS } from '../data/mockData'`
   - Add: API call to fetch review stats
   - Add: Loading state

3. **BusyTimes.js**
   - Remove: `import { BUSY_TIMES } from '../data/mockData'`
   - Add: API call to fetch busy times
   - Add: Loading state

4. **Gallery.js**
   - Remove: `import { GALLERY_IMAGES } from '../data/mockData'`
   - Add: API call to fetch gallery images
   - Add: Loading state

### 4. Data Seeding
- Create a seed script to populate MongoDB with initial data from mockData.js
- Script location: `/app/backend/seed_data.py`

### 5. Integration Steps
1. Create MongoDB models in `/app/backend/models/`
2. Create API routes in `/app/backend/routes/`
3. Update server.py to include new routes
4. Create and run seed script to populate database
5. Update frontend components to use API calls
6. Test all endpoints with curl
7. Verify frontend displays data correctly

## Notes
- All static content (About, Services sections) remains hardcoded in frontend
- Restaurant contact info remains in frontend (no backend needed)
- Focus on dynamic data that could change or be managed via admin panel later
