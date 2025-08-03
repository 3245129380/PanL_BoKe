<template>
  <div class="comment-form">
    <h3>Add a Comment</h3>
    <form @submit.prevent="submitComment">
      <div class="form-group">
        <input 
          type="text" 
          v-model="commentForm.author" 
          placeholder="Your name" 
          required 
          class="form-input"
        />
      </div>
      <div class="form-group">
        <textarea 
          v-model="commentForm.content" 
          placeholder="Your comment" 
          rows="4" 
          required 
          class="form-textarea"
        ></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" :disabled="isSubmitting" class="submit-button">
          {{ isSubmitting ? 'Posting...' : 'Post Comment' }}
        </button>
      </div>
    </form>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
export default {
  name: 'CommentForm',
  props: {
    blogId: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      commentForm: {
        author: '',
        content: ''
      },
      isSubmitting: false,
      error: null
    }
  },
  methods: {
    async submitComment() {
      this.isSubmitting = true
      this.error = null
      
      try {
        // This would typically call an API to submit the comment
        // For now, we'll just emit an event
        this.$emit('comment-submitted', {
          ...this.commentForm,
          blogId: this.blogId,
          created_at: new Date().toISOString()
        })
        
        // Reset form
        this.commentForm = {
          author: '',
          content: ''
        }
      } catch (err) {
        this.error = err.message || 'Failed to post comment'
      } finally {
        this.isSubmitting = false
      }
    }
  }
}
</script>

<style scoped>
.comment-form {
  margin: 2rem 0;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.comment-form h3 {
  margin-top: 0;
}

.form-group {
  margin-bottom: 1rem;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
}

.submit-button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.submit-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>