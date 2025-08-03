from fastapi import APIRouter, HTTPException
from typing import List
from models.blog import Blog, BlogCreate
from models.comment import CommentCreate
from utils.database import blog_collection, comment_collection
from utils.markdown import convert_markdown_to_html
import uuid
from datetime import datetime

router = APIRouter(prefix="/api/blogs", tags=["blogs"])

@router.options("/")
def options_blogs():
    return {"message": "OPTIONS request allowed"}

@router.options("/{blog_id}")
def options_blog(blog_id: str):
    return {"message": "OPTIONS request allowed"}

@router.get("/", response_model=List[Blog])
def get_blogs():
    blogs = list(blog_collection.find({}))
    # Convert ObjectId to string for JSON serialization
    for blog in blogs:
        blog["id"] = str(blog["_id"])
        del blog["_id"]
    return blogs

@router.get("/{blog_id}", response_model=Blog)
def get_blog(blog_id: str):
    blog = blog_collection.find_one({"_id": blog_id})
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    # Increment view count
    blog_collection.update_one({"_id": blog_id}, {"$inc": {"views": 1}})
    
    # Refresh blog data to get updated view count
    blog = blog_collection.find_one({"_id": blog_id})
    blog["id"] = str(blog["_id"])
    del blog["_id"]
    return blog

@router.post("/", response_model=Blog)
def create_blog(blog: BlogCreate):
    blog_dict = blog.dict()
    blog_dict["_id"] = str(uuid.uuid4())
    blog_dict["created_at"] = datetime.now()
    blog_dict["updated_at"] = datetime.now()
    blog_dict["likes"] = 0
    blog_dict["shares"] = 0
    blog_dict["views"] = 0
    
    # Convert markdown to HTML
    blog_dict["html_content"] = convert_markdown_to_html(blog_dict["content"])
    
    result = blog_collection.insert_one(blog_dict)
    
    if result.inserted_id:
        blog_dict["id"] = blog_dict["_id"]
        del blog_dict["_id"]
        return blog_dict
    else:
        raise HTTPException(status_code=500, detail="Failed to create blog")

@router.put("/{blog_id}", response_model=Blog)
def update_blog(blog_id: str, blog: BlogCreate):
    blog_dict = blog.dict()
    blog_dict["updated_at"] = datetime.now()
    
    # Convert markdown to HTML
    blog_dict["html_content"] = convert_markdown_to_html(blog_dict["content"])
    
    result = blog_collection.update_one({"_id": blog_id}, {"$set": blog_dict})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    updated_blog = blog_collection.find_one({"_id": blog_id})
    updated_blog["id"] = str(updated_blog["_id"])
    del updated_blog["_id"]
    return updated_blog

@router.delete("/{blog_id}")
def delete_blog(blog_id: str):
    result = blog_collection.delete_one({"_id": blog_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return {"message": "Blog deleted successfully"}

@router.post("/{blog_id}/like")
def like_blog(blog_id: str):
    result = blog_collection.update_one({"_id": blog_id}, {"$inc": {"likes": 1}})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return {"message": "Blog liked successfully"}

@router.post("/{blog_id}/share")
def share_blog(blog_id: str):
    result = blog_collection.update_one({"_id": blog_id}, {"$inc": {"shares": 1}})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return {"message": "Blog shared successfully"}

@router.post("/{blog_id}/view")
def view_blog(blog_id: str):
    result = blog_collection.update_one({"_id": blog_id}, {"$inc": {"views": 1}})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    return {"message": "Blog view counted successfully"}

@router.post("/{blog_id}/comments", response_model=CommentCreate)
def add_comment(blog_id: str, comment: CommentCreate):
    # Verify blog exists
    blog = blog_collection.find_one({"_id": blog_id})
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    comment_dict = comment.dict()
    comment_dict["_id"] = str(uuid.uuid4())
    comment_dict["created_at"] = datetime.now()
    comment_dict["blog_id"] = blog_id
    
    result = comment_collection.insert_one(comment_dict)
    
    if result.inserted_id:
        return comment
    else:
        raise HTTPException(status_code=500, detail="Failed to add comment")