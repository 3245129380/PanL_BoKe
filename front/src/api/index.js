import axios from 'axios'

const API_BASE_URL = 'http://localhost:8001/api'

// Create an axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000
})

// Blog API
export const blogAPI = {
  // Get all blogs
  getBlogs: () => apiClient.get('/blogs'),
  
  // Get a single blog by ID
  getBlog: (id) => apiClient.get(`/blogs/${id}`),
  
  // Create a new blog
  createBlog: (blog) => apiClient.post('/blogs', blog),
  
  // Update a blog
  updateBlog: (id, blog) => apiClient.put(`/blogs/${id}`, blog),
  
  // Delete a blog
  deleteBlog: (id) => apiClient.delete(`/blogs/${id}`),
  
  // Like a blog
  likeBlog: (id) => apiClient.post(`/blogs/${id}/like`),
  
  // Share a blog
  shareBlog: (id) => apiClient.post(`/blogs/${id}/share`),
  
  // View a blog
  viewBlog: (id) => apiClient.post(`/blogs/${id}/view`)
}

// Comment API
// 用于防重复提交的时间戳
let lastCommentTimestamp = 0;

export const commentAPI = {
  // Get comments for a blog
  getComments: (blogId) => apiClient.get(`/comments/${blogId}`),
  
  // Add a comment
  addComment: (comment) => {
    // 防重复提交机制
    const now = Date.now();
    if (now - lastCommentTimestamp < 1000) { // 1秒内不允许重复提交
      return Promise.reject(new Error('提交过于频繁，请稍后再试'));
    }
    lastCommentTimestamp = now;
    
    return apiClient.post('/comments', comment);
  },
  
  // Delete a comment
  deleteComment: (id) => apiClient.delete(`/comments/${id}`)
}

// User API
export const userAPI = {
  // Get all users
  getUsers: () => apiClient.get('/users'),
  
  // Get a single user
  getUser: (id) => apiClient.get(`/users/${id}`),
  
  // Create a new user
  createUser: (user) => apiClient.post('/users', user),
  
  // Update a user
  updateUser: (id, user) => apiClient.put(`/users/${id}`, user),
  
  // Delete a user
  deleteUser: (id) => apiClient.delete(`/users/${id}`)
}

// Search API
export const searchAPI = {
  // Search blogs by keyword
  searchBlogs: (keyword) => apiClient.get(`/search?q=${keyword}`),
  
  // Get all tags
  getTags: () => apiClient.get('/search/tags'),
  
  // Get blogs by tag
  getBlogsByTag: (tag) => apiClient.get(`/search/tag/${tag}`),
  
  // Get latest blogs
  getLatestBlogs: () => apiClient.get('/search/latest')
}

// Upload API
export const uploadAPI = {
  // Upload an image
  uploadImage: (formData) => apiClient.post('/upload/image', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }),
  
  // Get uploaded files
  getFiles: () => apiClient.get('/upload/files')
}

export default {
  blogAPI,
  commentAPI,
  userAPI,
  searchAPI,
  uploadAPI
}