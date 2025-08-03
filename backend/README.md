# Personal Blog API

This is the backend API for a personal blog application built with FastAPI and MongoDB.

## Features

- Create, read, update, and delete blog posts
- Add comments to blog posts
- Like and share blog posts
- Search functionality
- Tag-based organization
- File upload for images
- Markdown support with HTML conversion

## API Endpoints

### Blog Endpoints

- `GET /api/blogs` - Get all blogs
- `GET /api/blogs/{blog_id}` - Get a specific blog
- `POST /api/blogs` - Create a new blog
- `PUT /api/blogs/{blog_id}` - Update a blog
- `DELETE /api/blogs/{blog_id}` - Delete a blog
- `POST /api/blogs/{blog_id}/like` - Like a blog
- `POST /api/blogs/{blog_id}/share` - Share a blog
- `POST /api/blogs/{blog_id}/view` - Increment view count
- `POST /api/blogs/{blog_id}/comments` - Add a comment to a blog

### User Endpoints

- `GET /api/users` - Get all users
- `GET /api/users/{user_id}` - Get a specific user
- `POST /api/users` - Create a new user
- `PUT /api/users/{user_id}` - Update a user
- `DELETE /api/users/{user_id}` - Delete a user

### Comment Endpoints

- `GET /api/comments` - Get all comments
- `GET /api/comments/{comment_id}` - Get a specific comment
- `POST /api/comments` - Create a new comment
- `DELETE /api/comments/{comment_id}` - Delete a comment

### Search Endpoints

- `GET /api/search/blogs?q={query}` - Search blogs by query
- `GET /api/search/tags` - Get all tags
- `GET /api/search/blogs/by-tag/{tag}` - Get blogs by tag
- `GET /api/search/blogs/latest` - Get latest blogs

### Upload Endpoints

- `POST /api/upload/image` - Upload an image
- `GET /api/upload/files` - List uploaded files

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Make sure MongoDB is running on your system

3. Run the application:
   ```
   python main.py
   ```

The API will be available at `http://localhost:8000`