<template>
  <div class="blog-card">
    <h3>
      <router-link :to="{ name: 'blog-detail', params: { id: blog.id } }">
        {{ blog.title }}
      </router-link>
    </h3>
    <p class="blog-meta">
      By {{ blog.author }} on {{ new Date(blog.created_at).toLocaleDateString() }}
    </p>
    <p class="blog-excerpt">{{ blog.content.substring(0, 100) }}...</p>
    <div class="blog-tags">
      <span v-for="tag in blog.tags" :key="tag" class="tag">{{ tag }}</span>
    </div>
    <div class="blog-stats">
      <span>👁️ {{ blog.views }}</span>
      <span>❤️ {{ blog.likes }}</span>
      <span>🔗 {{ blog.shares }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogCard',
  props: {
    blog: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.blog-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.blog-card h3 {
  margin: 0 0 0.5rem 0;
}

.blog-card h3 a {
  text-decoration: none;
  color: #333;
}

.blog-meta {
  color: #666;
  font-size: 0.8rem;
  margin: 0.5rem 0;
}

.blog-excerpt {
  margin: 0.5rem 0;
  font-size: 0.9rem;
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
  font-size: 0.7rem;
}

.blog-stats {
  display: flex;
  gap: 1rem;
  font-size: 0.8rem;
  color: #666;
}
</style>