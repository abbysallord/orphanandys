"""
Seed script to populate MongoDB with initial restaurant data
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Menu Items Data
MENU_ITEMS = [
    {
        "name": "Fluffy Pancakes",
        "description": "Stack of golden pancakes served with butter and maple syrup",
        "price": "12.99",
        "image": "https://images.unsplash.com/photo-1667489012841-c6f8458da3e6",
        "category": "breakfast"
    },
    {
        "name": "Classic Cheeseburger",
        "description": "Juicy beef patty with melted cheese, lettuce, tomato, and special sauce",
        "price": "14.99",
        "image": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9",
        "category": "burgers"
    },
    {
        "name": "Biscuits & Gravy",
        "description": "Fresh baked biscuits smothered in creamy sausage gravy",
        "price": "10.99",
        "image": "https://images.unsplash.com/photo-1700659392748-68904081f748",
        "category": "breakfast"
    },
    {
        "name": "French Toast",
        "description": "Thick-cut brioche dipped in cinnamon batter, grilled to perfection",
        "price": "11.99",
        "image": "https://images.pexels.com/photos/35346351/pexels-photo-35346351.jpeg",
        "category": "breakfast"
    },
    {
        "name": "Mushroom Burger",
        "description": "Beef patty topped with sautéed mushrooms and Swiss cheese",
        "price": "15.99",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
        "category": "burgers"
    },
    {
        "name": "Signature Milkshake",
        "description": "Creamy hand-spun milkshake in vanilla, chocolate, or strawberry",
        "price": "6.99",
        "image": "https://images.pexels.com/photos/103566/pexels-photo-103566.jpeg",
        "category": "drinks"
    },
    {
        "name": "Chicken Apple Sausage & Eggs",
        "description": "Scrambled eggs with savory chicken apple sausage links",
        "price": "13.99",
        "image": "https://images.unsplash.com/photo-1639537255146-0532ecc4a78d",
        "category": "breakfast"
    },
    {
        "name": "French Fries",
        "description": "Crispy golden fries served with ketchup",
        "price": "5.99",
        "image": "https://images.unsplash.com/photo-1518013431117-eb1465fa5752?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3MjQyMTd8MHwxfHNlYXJjaHwyfHxmcmllc3xlbnwwfHx8fDE3NjY4MjEyOTJ8MA&ixlib=rb-4.1.0&q=85",
        "category": "sides"
    },
    {
        "name": "Deluxe Burger",
        "description": "Double patty burger with all the fixings",
        "price": "16.99",
        "image": "https://images.unsplash.com/photo-1550547660-d9450f859349",
        "category": "burgers"
    }
]

# Review Stats Data
REVIEW_STATS = {
    "average": 4.5,
    "total": 2387,
    "breakdown": [
        {"stars": 5, "count": 1789, "percentage": 75},
        {"stars": 4, "count": 430, "percentage": 18},
        {"stars": 3, "count": 119, "percentage": 5},
        {"stars": 2, "count": 31, "percentage": 1},
        {"stars": 1, "count": 18, "percentage": 1}
    ],
    "popularKeywords": [
        {"word": "pancakes", "count": 456},
        {"word": "milkshakes", "count": 389},
        {"word": "biscuits and gravy", "count": 312},
        {"word": "burgers", "count": 298},
        {"word": "friendly staff", "count": 276},
        {"word": "24/7", "count": 245}
    ]
}

# Busy Times Data
BUSY_TIMES = [
    {"hour": "12 AM", "value": 15, "order": 0},
    {"hour": "3 AM", "value": 8, "order": 1},
    {"hour": "6 AM", "value": 45, "order": 2},
    {"hour": "9 AM", "value": 65, "order": 3},
    {"hour": "12 PM", "value": 95, "order": 4},
    {"hour": "3 PM", "value": 52, "order": 5},
    {"hour": "6 PM", "value": 78, "order": 6},
    {"hour": "9 PM", "value": 68, "order": 7}
]

# Gallery Images Data
GALLERY_IMAGES = [
    {
        "url": "https://images.unsplash.com/photo-1761245193924-53a5a4bed9ef?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1Nzl8MHwxfHNlYXJjaHwxfHxjbGFzc2ljJTIwYW1lcmljYW4lMjBkaW5lcnxlbnwwfHx8fDE3NjY5MTU0ODB8MA&ixlib=rb-4.1.0&q=85",
        "alt": "Orphan Andy's exterior at night",
        "category": "diner",
        "order": 0
    },
    {
        "url": "https://images.unsplash.com/photo-1763949391256-aa46ed9105fe?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1Nzl8MHwxfHNlYXJjaHwzfHxjbGFzc2ljJTIwYW1lcmljYW4lMjBkaW5lcnxlbnwwfHx8fDE3NjY5MTU0ODB8MA&ixlib=rb-4.1.0&q=85",
        "alt": "Classic diner neon sign",
        "category": "diner",
        "order": 1
    },
    {
        "url": "https://images.unsplash.com/photo-1538333581680-29dd4752ddf2?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHw0fHxyZXN0YXVyYW50JTIwaW50ZXJpb3J8ZW58MHx8fHwxNzY2ODk0MTEwfDA&ixlib=rb-4.1.0&q=85",
        "alt": "Restaurant interior",
        "category": "interior",
        "order": 2
    },
    {
        "url": "https://images.pexels.com/photos/35133248/pexels-photo-35133248.jpeg",
        "alt": "Cozy dining atmosphere",
        "category": "interior",
        "order": 3
    },
    {
        "url": "https://images.unsplash.com/photo-1667489012841-c6f8458da3e6",
        "alt": "Delicious pancakes",
        "category": "food",
        "order": 4
    },
    {
        "url": "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9",
        "alt": "Classic cheeseburger",
        "category": "food",
        "order": 5
    },
    {
        "url": "https://images.pexels.com/photos/103566/pexels-photo-103566.jpeg",
        "alt": "Signature milkshake",
        "category": "food",
        "order": 6
    },
    {
        "url": "https://images.pexels.com/photos/2638026/pexels-photo-2638026.jpeg",
        "alt": "Indulgent milkshake",
        "category": "food",
        "order": 7
    }
]

async def seed_database():
    """Seed the database with initial data"""
    print("Starting database seeding...")
    
    try:
        # Clear existing data
        await db.menu_items.delete_many({})
        await db.review_stats.delete_many({})
        await db.busy_times.delete_many({})
        await db.gallery_images.delete_many({})
        print("✓ Cleared existing data")
        
        # Insert menu items
        result = await db.menu_items.insert_many(MENU_ITEMS)
        print(f"✓ Inserted {len(result.inserted_ids)} menu items")
        
        # Insert review stats
        result = await db.review_stats.insert_one(REVIEW_STATS)
        print(f"✓ Inserted review stats")
        
        # Insert busy times
        result = await db.busy_times.insert_many(BUSY_TIMES)
        print(f"✓ Inserted {len(result.inserted_ids)} busy times")
        
        # Insert gallery images
        result = await db.gallery_images.insert_many(GALLERY_IMAGES)
        print(f"✓ Inserted {len(result.inserted_ids)} gallery images")
        
        print("\n✅ Database seeding completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error seeding database: {str(e)}")
        raise
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())
