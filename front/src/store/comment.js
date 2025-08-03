import { defineStore } from 'pinia'
import { commentAPI } from '../api'

export const useCommentStore = defineStore('comment', {
  state: () => ({
    comments: [],
    loading: false,
    error: null
  }),
  
  actions: {
    async fetchComments(blogId) {
      this.loading = true
      this.error = null
      try {
        const response = await commentAPI.getComments(blogId)
        this.comments = response.data
      } catch (error) {
        this.error = error.message
      } finally {
        this.loading = false
      }
    },
    
    async addComment(commentData) {
      try {
        const response = await commentAPI.addComment(commentData)
        this.comments.unshift(response.data)
        return response.data
      } catch (error) {
        this.error = error.message
        throw error
      }
    },
    
    async deleteComment(id) {
      try {
        await commentAPI.deleteComment(id)
        this.comments = this.comments.filter(comment => comment.id !== id)
      } catch (error) {
        this.error = error.message
        throw error
      }
    }
  }
})