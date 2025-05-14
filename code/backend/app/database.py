from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
from urllib.parse import quote_plus

# # Your MongoDB credentials
# username = "abel12"  # Replace with your actual username
# password = "Appillil@2024"  # Replace with your actual password

# # URL encode the username and password
# encoded_username = quote_plus(username)
# encoded_password = quote_plus(password)

MONGO_URI = f"mongodb+srv://abel:210404@cluster1.6ysag.mongodb.net/"

client = AsyncIOMotorClient(MONGO_URI)  # Replace with MongoDB URI
db = client["User"]
users_collection = db["users"]
