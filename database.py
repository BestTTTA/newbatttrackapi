from pymongo import MongoClient
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = AsyncIOMotorClient(MONGO_URL)
db = client.testapibatttrack
collection = db["products"] 
