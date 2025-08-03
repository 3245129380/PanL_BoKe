<template>
  <div class="tag-cloud">
    <h3>Popular Tags</h3>
    <div class="tags">
      <span 
        v-for="tag in tags" 
        :key="tag" 
        class="tag" 
        :style="{ fontSize: calculateFontSize(tag.count) }"
        @click="filterByTag(tag.name)"
      >
        {{ tag.name }}
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TagCloud',
  props: {
    tags: {
      type: Array,
      required: true
    }
  },
  methods: {
    calculateFontSize(count) {
      // Calculate font size based on tag count
      const baseSize = 12
      const maxSize = 24
      const minCount = Math.min(...this.tags.map(t => t.count))
      const maxCount = Math.max(...this.tags.map(t => t.count))
      
      if (maxCount === minCount) {
        return `${baseSize}px`
      }
      
      const size = baseSize + ((count - minCount) / (maxCount - minCount)) * (maxSize - baseSize)
      return `${size}px`
    },
    filterByTag(tag) {
      this.$router.push({ name: 'blogs', query: { tag: tag } })
    }
  }
}
</script>

<style scoped>
.tag-cloud {
  margin: 1rem 0;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.tag-cloud h3 {
  margin-top: 0;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  cursor: pointer;
  padding: 0.2rem 0.5rem;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.tag:hover {
  background-color: #0056b3;
}
</style>