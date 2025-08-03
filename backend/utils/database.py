import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "blog_database")

client = MongoClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Collections
blog_collection = db["blogs"]
comment_collection = db["comments"]
user_collection = db["users"]

# Create indexes for better performance
blog_collection.create_index("author")
blog_collection.create_index("tags")
blog_collection.create_index("created_at")
comment_collection.create_index("blog_id")
comment_collection.create_index("author")
# 为评论集合添加复合唯一索引，防止重复数据插入
comment_collection.create_index([("content", 1), ("author", 1), ("blog_id", 1), ("created_at", 1)], unique=True)
user_collection.create_index("email", unique=True)
user_collection.create_index("username", unique=True)