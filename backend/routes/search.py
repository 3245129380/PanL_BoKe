from fastapi import APIRouter, Query
from typing import List
from models.blog import Blog
from utils.database import blog_collection

router = APIRouter(prefix="/api/search", tags=["search"])

@router.get("/blogs", response_model=List[Blog])
def search_blogs(q: str = Query(..., min_length=1)):
    # Search in title, content, and tags
    query = {
        "$or": [
            {"title": {"$regex": q, "$options": "i"}},
            {"content": {"$regex": q, "$options": "i"}},
            {"tags": {"$in": [q]}}
        ]
    }
    
    blogs = list(blog_collection.find(query))
    # Convert ObjectId to string for JSON serialization
    for blog in blogs:
        blog["id"] = str(blog["_id"])
        del blog["_id"]
    return blogs

@router.get("/tags", response_model=List[str])
def get_tags():
    # Get all unique tags
    tags = blog_collection.distinct("tags")
    return tags

@router.get("/blogs/by-tag/{tag}", response_model=List[Blog])
def get_blogs_by_tag(tag: str):
    blogs = list(blog_collection.find({"tags": tag}))
    # Convert ObjectId to string for JSON serialization
    for blog in blogs:
        blog["id"] = str(blog["_id"])
        del blog["_id"]
    return blogs

@router.get("/blogs/latest", response_model=List[Blog])
def get_latest_blogs(limit: int = 10):
    blogs = list(blog_collection.find().sort("created_at", -1).limit(limit))
    # Convert ObjectId to string for JSON serialization
    for blog in blogs:
        blog["id"] = str(blog["_id"])
        del blog["_id"]
    return blogs