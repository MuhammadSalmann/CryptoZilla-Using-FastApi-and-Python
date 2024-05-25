from motor.motor_asyncio import AsyncIOMotorClient

mongo_url = "mongodb+srv://210920:210920@cluster1.szirki2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = AsyncIOMotorClient(mongo_url)

db = client.test
collection = db.users
