from pymongo import MongoClient
from config import client


db=client.user1

collection_name=db["user1_collection"]
