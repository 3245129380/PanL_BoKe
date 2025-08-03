import { defineStore } from 'pinia'
import { blogAPI } from '../api'

export const useBlogStore = defineStore('blog', {
  state: () => ({
    blogs: [],
    currentBlog: null,
    loading: false,
    error: null
  }),
  
  actions: {
    async fetchBlogs() {
      this.loading = true
      try {
        const response = await blogAPI.getBlogs()
        this.blogs = response.data
        this.error = null
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },
    
    async fetchBlog(id) {
      this.loading = true
      try {
        const response = await blogAPI.getBlog(id)
        this.currentBlog = response.data
        this.error = null
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },
    
    async createBlog(blogData) {
      try {
        const response = await blogAPI.createBlog(blogData)
        this.blogs.push(response.data)
        return response.data
      } catch (error) {
        this.error = error.message
        throw error
      }
    },
    
    async updateBlog(id, blogData) {
      try {
        const response = await blogAPI.updateBlog(id, blogData)
        const index = this.blogs.findIndex(blog => blog.id === id)
        if (index !== -1) {
          this.blogs[index] = response.data
        }
        if (this.currentBlog && this.currentBlog.id === id) {
          this.currentBlog = response.data
        }
        return response.data
      } catch (error) {
        this.error = error.message
        throw error
      }
    },
    
    async deleteBlog(id) {
      try {
        await blogAPI.deleteBlog(id)
        this.blogs = this.blogs.filter(blog => blog.id !== id)
        if (this.currentBlog && this.currentBlog.id === id) {
          this.currentBlog = null
        }
      } catch (error) {
        this.error = error.message
        throw error
      }
    },
    
    async likeBlog(id) {
      try {
        await blogAPI.likeBlog(id)
        // Update the like count in the local state
        const blog = this.blogs.find(blog => blog.id === id)
        if (blog) {
          blog.likes += 1
        }
        if (this.currentBlog && this.currentBlog.id === id) {
          this.currentBlog.likes += 1
        }
      } catch (error) {
        this.error = error.message
        throw error
      }
    }
  }
})