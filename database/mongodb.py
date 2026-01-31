from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["couple_bot"]

users = db["users"]
waiting = db["waiting"]
chats = db["chats"]
