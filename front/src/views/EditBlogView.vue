<template>
  <div class="edit-blog">
    <h1>Edit Blog</h1>
    
    <div v-if="loading">Loading blog...</div>
    
    <div v-else-if="error">{{ error }}</div>
    
    <div v-else-if="currentBlog">
      <BlogEditor 
        :initial-data="blogForm" 
        :submitting="isSubmitting" 
        submit-text="Update Blog"
        @submit="submitForm"
        @cancel="cancelEdit"
      />
    </div>
    
    <div v-if="updateError" class="error">{{ updateError }}</div>
  </div>
</template>

<script>
import { useBlogStore } from '../store/blog'
import BlogEditor from '../components/blog/BlogEditor.vue'

export default {
  name: 'EditBlogView',
  components: {
    BlogEditor
  },
  props: {
    id: {
      type: String,
      required: true
    }
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
      loading: true,
      error: null,
      updateError: null
    }
  },
  computed: {
    currentBlog() {
      const blogStore = useBlogStore()
      return blogStore.currentBlog
    }
  },
  async created() {
    try {
      const blogStore = useBlogStore()
      await blogStore.fetchBlog(this.id)
      
      // Populate form with existing blog data
      if (blogStore.currentBlog) {
        this.blogForm.title = blogStore.currentBlog.title
        this.blogForm.author = blogStore.currentBlog.author
        this.blogForm.tags = blogStore.currentBlog.tags
        this.blogForm.content = blogStore.currentBlog.content
      }
    } catch (err) {
      this.error = err.message || 'Failed to load blog'
    } finally {
      this.loading = false
    }
  },
  methods: {
    async submitForm(blogData) {
      this.isSubmitting = true
      this.updateError = null
      
      try {
        const blogStore = useBlogStore()
        await blogStore.updateBlog(this.id, blogData)
        
        // Navigate to blog detail page
        this.$router.push({ name: 'blog-detail', params: { id: this.id } })
      } catch (err) {
        this.updateError = err.message || 'Failed to update blog'
      } finally {
        this.isSubmitting = false
      }
    },
    cancelEdit() {
      this.$router.push({ name: 'blog-detail', params: { id: this.id } })
    }
  }
}
</script>

<style scoped>
.edit-blog {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.edit-blog h1 {
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