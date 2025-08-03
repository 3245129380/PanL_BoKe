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
  padding: 1rem;
  max-width: 800px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
}

.form-actions {
  margin-top: 2rem;
}

.form-actions button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 1rem;
}

.form-actions button:hover {
  background-color: #0056b3;
}

.form-actions button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.preview {
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.preview-content {
  margin-top: 1rem;
  line-height: 1.6;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>