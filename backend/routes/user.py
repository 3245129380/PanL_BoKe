from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User, UserCreate
from utils.database import user_collection
import uuid
from datetime import datetime

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[User])
def get_users():
    users = list(user_collection.find({}))
    # Convert ObjectId to string for JSON serialization
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    return users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    user = user_collection.find_one({"_id": user_id})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user["_id"])
    del user["_id"]
    return user

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    # Check if user already exists
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    user_dict = user.dict()
    user_dict["_id"] = str(uuid.uuid4())
    user_dict["created_at"] = datetime.now()
    user_dict["is_active"] = True
    
    result = user_collection.insert_one(user_dict)
    
    if result.inserted_id:
        user_dict["id"] = user_dict["_id"]
        del user_dict["_id"]
        del user_dict["password"]  # Don't return password
        return user_dict
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")

@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: UserCreate):
    user_dict = user.dict()
    
    result = user_collection.update_one({"_id": user_id}, {"$set": user_dict})
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = user_collection.find_one({"_id": user_id})
    updated_user["id"] = str(updated_user["_id"])
    del updated_user["_id"]
    del updated_user["password"]  # Don't return password
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id: str):
    result = user_collection.delete_one({"_id": user_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}