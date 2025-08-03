from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []
    author: str
    
class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: str
    created_at: datetime
    updated_at: datetime
    likes: int = 0
    shares: int = 0
    views: int = 0
    html_content: Optional[str] = None
    
    class Config:
        orm_mode = True