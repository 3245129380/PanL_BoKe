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

.home h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.home p {
  font-size: 1.2rem;
  color: #7f8c8d;
  max-width: 600px;
  margin: 0 auto 2rem auto;
  line-height: 1.6;
}

.features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
  flex-wrap: wrap;
}

.feature {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  width: 300px;
  background-color: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: box-shadow 0.3s ease;
}

.feature:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.feature h2 {
  margin-top: 0;
  color: #2c3e50;
}

.feature p {
  color: #7f8c8d;
  font-size: 1rem;
  margin: 0.5rem 0;
}

.feature a {
  display: inline-block;
  margin-top: 1rem;
  padding: 0.6rem 1.2rem;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.feature a:hover {
  background-color: #359c6d;
  transform: translateY(-2px);
}
</style>