from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    raise RuntimeError("MONGODB_URI is not set")

client = MongoClient(MONGO_URI)

# database name from URI or explicit
db = client["sample_mflix"]

def get_db():
    return db
