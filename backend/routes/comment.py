from fastapi import APIRouter, HTTPException
from typing import List
from models.comment import Comment, CommentCreate
from utils.database import comment_collection, blog_collection
import uuid
from datetime import datetime

router = APIRouter(prefix="/api/comments", tags=["comments"])

@router.get("/{blog_id}", response_model=List[Comment])
def get_comments(blog_id: str):
    comments = list(comment_collection.find({"blog_id": blog_id}))
    # Convert ObjectId to string for JSON serialization
    for comment in comments:
        comment["id"] = str(comment["_id"])
        del comment["_id"]
    return comments

@router.get("/{comment_id}", response_model=Comment)
def get_comment(comment_id: str):
    comment = comment_collection.find_one({"_id": comment_id})
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment["id"] = str(comment["_id"])
    del comment["_id"]
    return comment

from fastapi import APIRouter, HTTPException, Request
from fastapi.exceptions import RequestValidationError

@router.post("/", response_model=Comment)
async def create_comment(request: Request, comment: CommentCreate):
    # Print request body for debugging
    try:
        request_body = await request.body()
        print("Request body:", request_body)
        print("Comment data:", comment)
        print("Comment data dict:", comment.dict())
        print("Comment data fields:", comment.content, comment.author, comment.blog_id)
    except Exception as e:
        print("Error reading request body:", str(e))
    
    # 验证数据格式，防止浏览器自动填充等异常数据
    if not comment.content or not comment.author or not comment.blog_id:
        print("Validation failed: content=", comment.content, "author=", comment.author, "blog_id=", comment.blog_id)
        raise HTTPException(status_code=422, detail="Invalid comment data")
    
    # 检查是否为异常数据格式
    if hasattr(comment.content, '_vts') or hasattr(comment.author, '_vts') or hasattr(comment.blog_id, '_vts'):
        raise HTTPException(status_code=422, detail="Invalid comment data format")
    
    # Verify blog exists
    blog = blog_collection.find_one({"_id": comment.blog_id})
    if blog is None:
        print("Blog not found for ID:", comment.blog_id)
        raise HTTPException(status_code=404, detail="Blog not found")
    
    comment_dict = comment.dict()
    comment_dict["_id"] = str(uuid.uuid4())
    comment_dict["created_at"] = datetime.now()
    
    result = comment_collection.insert_one(comment_dict)
    
    if result.inserted_id:
        comment_dict["id"] = comment_dict["_id"]
        del comment_dict["_id"]
        return comment_dict
    else:
        raise HTTPException(status_code=500, detail="Failed to create comment")

@router.delete("/{comment_id}")
def delete_comment(comment_id: str):
    result = comment_collection.delete_one({"_id": comment_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    return {"message": "Comment deleted successfully"}