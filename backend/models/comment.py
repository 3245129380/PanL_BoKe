from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    content: str
    author: str
    blog_id: str
    
class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: str
    created_at: datetime
    
    class Config:
        orm_mode = True