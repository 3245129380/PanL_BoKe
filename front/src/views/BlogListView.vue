<template>
  <div class="blog-list">
    <h1>Blog Posts</h1>
    
    <div v-if="loading">Loading blogs...</div>
    
    <div v-else-if="error">{{ error }}</div>
    
    <div v-else>
      <div v-for="blog in blogs" :key="blog.id" class="blog-item">
        <h2>
          <router-link :to="{ name: 'blog-detail', params: { id: blog.id } }">
            {{ blog.title }}
          </router-link>
        </h2>
        <p class="blog-meta">
          By {{ blog.author }} on {{ new Date(blog.created_at).toLocaleDateString() }}
        </p>
        <p class="blog-excerpt">{{ blog.content.substring(0, 150) }}...</p>
        <div class="blog-tags">
          <span v-for="tag in blog.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <div class="blog-stats">
          <span>👁️ {{ blog.views }}</span>
          <span>❤️ {{ blog.likes }}</span>
          <span>🔗 {{ blog.shares }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useBlogStore } from '../store/blog'

export default {
  name: 'BlogListView',
  setup() {
    const blogStore = useBlogStore()
    
    return {
      blogs: blogStore.blogs,
      loading: blogStore.loading,
      error: blogStore.error
    }
  },
  async created() {
    const blogStore = useBlogStore()
    await blogStore.fetchBlogs()
  }
}
</script>

<style scoped>
.blog-list {
  padding: 1rem;
}

.blog-item {
  border-bottom: 1px solid #eee;
  padding: 1rem 0;
}

.blog-item h2 {
  margin: 0 0 0.5rem 0;
}

.blog-item h2 a {
  text-decoration: none;
  color: #333;
}

.blog-meta {
  color: #666;
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.blog-excerpt {
  margin: 0.5rem 0;
}

.blog-tags {
  margin: 0.5rem 0;
}

.tag {
  display: inline-block;
  background-color: #f0f0f0;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  margin-right: 0.5rem;
  font-size: 0.8rem;
}

.blog-stats {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: #666;
}
</style>