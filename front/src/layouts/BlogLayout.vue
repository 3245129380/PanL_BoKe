<template>
  <div class="blog-layout">
    <header class="blog-header">
      <div class="container">
        <h1 class="blog-title">
          <router-link to="/">My Blog</router-link>
        </h1>
        <nav class="blog-nav">
          <router-link to="/" exact>首页</router-link>
          <router-link to="/blogs">博客列表</router-link>
          <router-link to="/create">创建博客</router-link>
        </nav>
      </div>
    </header>
    
    <main class="blog-main">
      <div class="container">
        <router-view />
      </div>
    </main>
    
    <footer class="blog-footer">
      <div class="container">
        <p>&copy; 2023 My Blog. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'BlogLayout'
}
</script>

<style scoped>
.blog-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.blog-header {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  padding: 1rem 0;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.blog-title {
  margin: 0;
  font-size: 1.5rem;
}

.blog-title a {
  text-decoration: none;
  color: #333;
}

.blog-nav {
  display: flex;
  gap: 1rem;
}

.blog-nav a {
  text-decoration: none;
  color: #333;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.blog-nav a:hover,
.blog-nav a.router-link-active {
  background-color: #007bff;
  color: #fff;
}

.blog-main {
  flex: 1;
  padding: 2rem 0;
}

.blog-footer {
  background-color: #f8f9fa;
  padding: 1rem 0;
  text-align: center;
  border-top: 1px solid #eee;
}
</style>