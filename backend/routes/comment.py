from fastapi import APIRouter, HTTPException
from typing import List
from models.comment import Comment, CommentCreate
from utils.database import comment_collection, blog_collection
import uuid
from datetime import datetime

router = APIRouter(prefix="/api/comments", tags=["comments"])

@router.get("/", response_model=List[Comment])
def get_comments():
    comments = list(comment_collection.find({}))
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

@router.post("/", response_model=Comment)
def create_comment(comment: CommentCreate):
    # Verify blog exists
    blog = blog_collection.find_one({"_id": comment.blog_id})
    if blog is None:
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