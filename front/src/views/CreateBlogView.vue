<template>
  <div class="create-blog">
    <h1>Create New Blog</h1>
    
    <BlogEditor 
      :initial-data="blogForm" 
      :submitting="isSubmitting" 
      submit-text="Create Blog"
      @submit="submitForm"
      @cancel="cancel"
    />
    
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import { useBlogStore } from '../store/blog'
import BlogEditor from '../components/blog/BlogEditor.vue'

export default {
  name: 'CreateBlogView',
  components: {
    BlogEditor
  },
  data() {
    return {
      blogForm: {
        title: '',
        author: '',
        tags: [],
        content: ''
      },
      isSubmitting: false,
      error: null
    }
  },
  methods: {
    async submitForm(blogData) {
      this.isSubmitting = true
      this.error = null
      
      try {
        const blogStore = useBlogStore()
        await blogStore.createBlog(blogData)
        
        // Navigate to blogs list
        this.$router.push({ name: 'blogs' })
      } catch (err) {
        this.error = err.message || 'Failed to create blog'
      } finally {
        this.isSubmitting = false
      }
    },
    cancel() {
      // Navigate back to blogs list
      this.$router.push({ name: 'blogs' })
    }
  }
}
</script>

<style scoped>
.create-blog {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.create-blog h1 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #2c3e50;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

.form-actions {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.form-actions button {
  padding: 0.75rem 1.5rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.form-actions button:hover {
  background-color: #359c6d;
}

.form-actions button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.preview {
  margin-top: 2rem;
  padding: 1.5rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f8f9fa;
}

.preview h2 {
  margin-top: 0;
  color: #2c3e50;
}

.preview-content {
  margin-top: 1rem;
  line-height: 1.8;
  color: #34495e;
}

.error {
  color: #e74c3c;
  margin-top: 1rem;
  text-align: center;
  font-weight: bold;
}
</style>