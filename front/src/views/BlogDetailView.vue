<template>
  <div class="blog-detail" v-if="currentBlog">
    <h1>{{ currentBlog.title }}</h1>
    
    <div class="blog-meta">
      <p>By {{ currentBlog.author }} on {{ new Date(currentBlog.created_at).toLocaleDateString() }}</p>
      <div class="blog-stats">
        <span>👁️ {{ currentBlog.views }}</span>
        <span>❤️ {{ currentBlog.likes }}</span>
        <span>🔗 {{ currentBlog.shares }}</span>
      </div>
    </div>
    
    <div class="blog-tags">
      <span v-for="tag in currentBlog.tags" :key="tag" class="tag">{{ tag }}</span>
    </div>
    
    <div class="blog-content" v-html="renderedContent"></div>
    
    <div class="blog-actions">
      <button @click="likeBlog(currentBlog.id)">Like</button>
      <button @click="shareBlog(currentBlog.id)">Share</button>
    </div>
    
    <CommentSection :blog-id="id" />
    
    <div class="navigation">
      <router-link v-if="prevBlog" :to="{ name: 'blog-detail', params: { id: prevBlog.id } }">
        ← Previous: {{ prevBlog.title }}
      </router-link>
      <router-link v-if="nextBlog" :to="{ name: 'blog-detail', params: { id: nextBlog.id } }">
        Next: {{ nextBlog.title }} →
      </router-link>
    </div>
  </div>
  
  <div v-else-if="loading">Loading blog...</div>
  
  <div v-else-if="error">{{ error }}</div>
  
  <div v-else>Blog not found</div>
</template>

<script>
import { useBlogStore } from '../store/blog'
import { renderMarkdown } from '../utils/markdown'
import CommentSection from '../components/blog/CommentSection.vue'

export default {
    name: 'BlogDetailView',
    components: {
      CommentSection
    },
    props: {
      id: {
        type: String,
        required: true
      }
    },
  setup() {
    const blogStore = useBlogStore()
    
    return {
      currentBlog: blogStore.currentBlog,
      loading: blogStore.loading,
      error: blogStore.error
    }
  },
  data() {
    return {
      prevBlog: null,
      nextBlog: null
    }
  },
  computed: {
    renderedContent() {
      if (this.currentBlog && this.currentBlog.html_content) {
        return this.currentBlog.html_content
      } else if (this.currentBlog && this.currentBlog.content) {
        return renderMarkdown(this.currentBlog.content)
      }
      return ''
    }
  },
  async created() {
    const blogStore = useBlogStore()
    await blogStore.fetchBlog(this.id)
    
    // Set up navigation
    if (blogStore.blogs.length > 0) {
      const currentIndex = blogStore.blogs.findIndex(blog => blog.id === this.id)
      if (currentIndex > 0) {
        this.prevBlog = blogStore.blogs[currentIndex - 1]
      }
      if (currentIndex < blogStore.blogs.length - 1) {
        this.nextBlog = blogStore.blogs[currentIndex + 1]
      }
    }
  },
  methods: {
    async likeBlog(id) {
      const blogStore = useBlogStore()
      await blogStore.likeBlog(id)
    },
    async shareBlog(id) {
      // Implementation for sharing
      alert('Blog shared!')
    }
  }
}
</script>

<style scoped>
.blog-detail {
  padding: 1rem;
}

.blog-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.blog-stats {
  display: flex;
  gap: 1rem;
}

.blog-tags {
  margin: 1rem 0;
}

.tag {
  display: inline-block;
  background-color: #f0f0f0;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  margin-right: 0.5rem;
  font-size: 0.8rem;
}

.blog-content {
  margin: 1rem 0;
  line-height: 1.6;
}

.blog-actions {
  margin: 1rem 0;
}

.blog-actions button {
  margin-right: 1rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.blog-actions button:hover {
  background-color: #0056b3;
}

.comments-section {
  margin: 2rem 0;
  padding: 1rem;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.navigation a {
  text-decoration: none;
  color: #007bff;
}

.navigation a:hover {
  text-decoration: underline;
}
</style>