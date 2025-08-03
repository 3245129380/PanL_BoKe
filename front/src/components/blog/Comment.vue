<template>
  <div class="comment">
    <div class="comment-header">
      <span class="comment-author">{{ comment.author }}</span>
      <span class="comment-date">{{ formatDate(comment.created_at) }}</span>
    </div>
    <div class="comment-content">
      {{ comment.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Comment',
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  methods: {
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString()
    }
  }
}
</script>

<style scoped>
.comment {
  border-bottom: 1px solid #ecf0f1;
  padding: 1.5rem 0;
}

.comment:last-child {
  border-bottom: none;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.comment-author {
  font-weight: bold;
  color: #2c3e50;
}

.comment-date {
  color: #7f8c8d;
  font-size: 0.9rem;
}

.comment-content {
  margin-left: 0;
  line-height: 1.6;
  color: #34495e;
}
</style>