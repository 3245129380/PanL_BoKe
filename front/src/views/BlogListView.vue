<template>
  <div class="blog-list">
    <h1>Blog Posts</h1>
    
    <div v-if="loading">Loading blogs...</div>
    
    <div v-else-if="error">{{ error }}</div>
    
    <div v-else>
      <div v-for="blog in blogs" :key="blog.id" class="blog-item">
        <h2 class="blog-title">
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
          <span class="stat-item">👁️ {{ blog.views }}</span>
          <span class="stat-item">❤️ {{ blog.likes }}</span>
          <span class="stat-item">🔗 {{ blog.shares }}</span>
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
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s ease;
}

.blog-item:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.blog-title {
  margin: 0 0 0.75rem 0;
  font-size: 1.4rem;
}

.blog-title a {
  text-decoration: none;
  color: #2c3e50;
  transition: color 0.3s ease;
}

.blog-title a:hover {
  color: #42b983;
}

.blog-meta {
  color: #7f8c8d;
  font-size: 0.9rem;
  margin: 0.75rem 0;
}

.blog-excerpt {
  margin: 0.75rem 0;
  font-size: 1rem;
  line-height: 1.6;
  color: #34495e;
}

.blog-tags {
  margin: 0.75rem 0;
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

.blog-stats {
  display: flex;
  gap: 1.5rem;
  font-size: 0.9rem;
  color: #7f8c8d;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #ecf0f1;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
</style>