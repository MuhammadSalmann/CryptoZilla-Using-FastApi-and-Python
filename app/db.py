from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = "Your Url"

client = AsyncIOMotorClient(mongo_url)

db = client.test
collection = db.users
