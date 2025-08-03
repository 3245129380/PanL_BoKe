<template>
  <div class="search-bar">
    <form @submit.prevent="performSearch">
      <input 
        type="text" 
        v-model="searchQuery" 
        placeholder="Search blogs..." 
        class="search-input"
      />
      <button type="submit" class="search-button">Search</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchQuery: ''
    }
  },
  methods: {
    performSearch() {
      if (this.searchQuery.trim()) {
        this.$router.push({ name: 'blogs', query: { search: this.searchQuery } })
      }
    }
  }
}
</script>

<style scoped>
.search-bar {
  margin: 1rem 0;
}

form {
  display: flex;
  gap: 0.5rem;
}

.search-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.search-button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #0056b3;
}
</style>