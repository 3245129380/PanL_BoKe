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