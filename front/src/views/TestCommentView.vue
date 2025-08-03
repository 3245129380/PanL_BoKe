<template>
  <div class="test-comment">
    <h1>评论功能测试</h1>
    <CommentSection :blog-id="'test-blog-1'" />
  </div>
</template>

<script>
import CommentSection from '../components/blog/CommentSection.vue'

export default {
  name: 'TestCommentView',
  components: {
    CommentSection
  }
}
</script>

<style scoped>
.test-comment {
  padding: 2rem;
}
</style>