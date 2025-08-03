<template>
  <div class="comment-form">
    <h3>Add a Comment</h3>
    <div v-if="success" class="success">{{ success }}</div>
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
      error: null,
      success: null
    }
  },
  methods: {
    async submitComment(event) {
      // 阻止表单的默认提交行为，防止重复提交
      event.preventDefault();
      
      // 如果正在提交中，则直接返回，防止重复点击
      if (this.isSubmitting) return;
      
      // 验证数据格式
      if (!this.commentForm.author.trim() || !this.commentForm.content.trim()) {
        this.error = '请填写完整的评论信息';
        return;
      }
      
      // 检查数据是否包含异常字段
      if (typeof this.commentForm.author !== 'string' || typeof this.commentForm.content !== 'string') {
        this.error = '评论数据格式不正确';
        return;
      }
      
      // Debugging: log the blogId
      console.log('CommentForm blogId:', this.blogId);
      
      this.isSubmitting = true
      this.error = null
      
      try {
        // Debugging: log the data being sent
        const commentData = {
          ...this.commentForm,
          blog_id: this.blogId
        }
        console.log('Sending comment data:', commentData)
        
        // Submit the comment
        this.$emit('submit', commentData)
        
        // Reset form
        this.commentForm = {
          author: '',
          content: ''
        }
        
        // Show success message
        this.success = '评论提交成功!'
        
        // Clear success message after 3 seconds
        setTimeout(() => {
          this.success = null
        }, 3000)
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
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.comment-form h3 {
  margin-top: 0;
  color: #2c3e50;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

.submit-button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
  display: block;
  margin: 0 auto;
}

.submit-button:hover {
  background-color: #359c6d;
}

.submit-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  color: #e74c3c;
  margin-top: 1rem;
  text-align: center;
  font-weight: bold;
}

.success {
  color: #42b983;
  margin-bottom: 1rem;
  text-align: center;
  font-weight: bold;
}
</style>