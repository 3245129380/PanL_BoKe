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
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useBlogStore } from '../store/blog'
import { renderMarkdown } from '../utils/markdown'
import CommentSection from '../components/blog/CommentSection.vue'

export default {
  name: 'BlogDetailView',
  components: {
    CommentSection
  },
  setup() {
    const route = useRoute()
    const blogStore = useBlogStore()
    const prevBlog = ref(null)
    const nextBlog = ref(null)
    
    // 计算渲染内容
    const renderedContent = computed(() => {
      if (blogStore.currentBlog && blogStore.currentBlog.html_content) {
        return blogStore.currentBlog.html_content
      } else if (blogStore.currentBlog && blogStore.currentBlog.content) {
        return renderMarkdown(blogStore.currentBlog.content)
      }
      return ''
    })
    
    // 获取博客详情
    const fetchBlogDetail = async () => {
      // Increment view count when blog is accessed
      try {
        await blogAPI.viewBlog(route.params.id)
      } catch (error) {
        console.error('Failed to increment view count:', error)
      }
      
      await blogStore.fetchBlog(route.params.id)
      
      // Set up navigation
      if (blogStore.blogs.length > 0) {
        const currentIndex = blogStore.blogs.findIndex(blog => blog.id === route.params.id)
        if (currentIndex > 0) {
          prevBlog.value = blogStore.blogs[currentIndex - 1]
        }
        if (currentIndex < blogStore.blogs.length - 1) {
          nextBlog.value = blogStore.blogs[currentIndex + 1]
        }
      }
    }
    
    // 点赞博客
    const likeBlog = async (id) => {
      await blogStore.likeBlog(id)
    }
    
    // 分享博客
    const shareBlog = async (id) => {
      // Implementation for sharing
      alert('Blog shared!')
    }
    
    // 组件挂载时获取博客详情
    onMounted(() => {
      fetchBlogDetail()
    })
    
    return {
      id: route.params.id,  // 确保id在模板中可用
      currentBlog: blogStore.currentBlog,
      loading: blogStore.loading,
      error: blogStore.error,
      prevBlog,
      nextBlog,
      renderedContent,
      likeBlog,
      shareBlog
    }
  }
}
</script>

<style scoped>
.blog-detail {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.blog-detail h1 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.blog-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ecf0f1;
  padding-bottom: 1rem;
  margin-bottom: 1rem;
}

.blog-meta p {
  color: #7f8c8d;
  font-size: 1rem;
  margin: 0;
}

.blog-stats {
  display: flex;
  gap: 1.5rem;
  font-size: 0.9rem;
  color: #7f8c8d;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.blog-tags {
  margin: 1.5rem 0;
}

.tag {
  display: inline-block;
  background-color: #ecf0f1;
  padding: 0.25rem 0.6rem;
  border-radius: 12px;
  margin-right: 0.5rem;
  font-size: 0.8rem;
  color: #7f8c8d;
}

.blog-content {
  margin: 1.5rem 0;
  line-height: 1.8;
  font-size: 1.1rem;
  color: #34495e;
}

.blog-actions {
  margin: 1.5rem 0;
  padding: 1.5rem 0;
  border-top: 1px solid #ecf0f1;
  border-bottom: 1px solid #ecf0f1;
}

.blog-actions button {
  margin-right: 1rem;
  padding: 0.6rem 1.2rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.blog-actions button:hover {
  background-color: #359c6d;
}

.comments-section {
  margin: 2rem 0;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.navigation {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #ecf0f1;
}

.navigation a {
  text-decoration: none;
  color: #42b983;
  font-size: 1rem;
  transition: color 0.3s ease;
}

.navigation a:hover {
  color: #359c6d;
  text-decoration: underline;
}
</style>