<template>
  <div class="home">
    <h1>Welcome to My Personal Blog</h1>
    <p>This is a simple blog application built with Vue 3, FastAPI, and MongoDB.</p>
    
    <div class="features">
      <div class="feature">
        <h2>Latest Blogs</h2>
        <p>Check out the latest blog posts.</p>
        <router-link to="/blogs">View Blogs</router-link>
      </div>
      
      <div class="feature">
        <h2>Create Blog</h2>
        <p>Share your thoughts with the world.</p>
        <router-link to="/create">Create Blog</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}

.features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.feature {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1rem;
  width: 300px;
}

.feature h2 {
  margin-top: 0;
}

.feature a {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}

.feature a:hover {
  background-color: #0056b3;
}
</style>