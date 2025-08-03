from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes import blog, user, comment, search, upload
import os
from fastapi import Request

app = FastAPI(title="Personal Blog API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add middleware to log all requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    print(f"Headers: {request.headers}")
    if request.method in ["POST", "PUT", "PATCH"]:
        body = await request.body()
        print(f"Body: {body}")
    response = await call_next(request)
    return response

# Create uploads directory if it doesn't exist
os.makedirs("uploads", exist_ok=True)

# Serve static files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Include routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(comment.router)
app.include_router(search.router)
app.include_router(upload.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Personal Blog API"}

# Create a test blog post for comment testing
@app.on_event("startup")
async def create_test_blog():
    from models.blog import BlogCreate
    from utils.database import blog_collection
    import uuid
    
    # Check if test blog already exists
    test_blog = blog_collection.find_one({"title": "测试博客文章"})
    if not test_blog:
        blog_data = {
            "_id": "test-blog-1",
            "title": "测试博客文章",
            "content": "这是一个用于测试评论功能的博客文章。",
            "author": "测试用户",
            "tags": ["测试", "评论"],
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-01T00:00:00",
            "views": 0,
            "likes": 0,
            "shares": 0
        }
        blog_collection.insert_one(blog_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)