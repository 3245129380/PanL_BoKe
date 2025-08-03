<template>
  <div class="comment-section">
    <h3>评论</h3>
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <Comment
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
      <div v-if="comments.length === 0" class="no-comments">
        暂无评论，快来抢沙发吧！
      </div>
    </div>
    
    <CommentForm @submit="handleCommentSubmit" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import Comment from './Comment.vue'
import CommentForm from './CommentForm.vue'

export default {
  name: 'CommentSection',
  components: {
    Comment,
    CommentForm
  },
  props: {
    blogId: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const comments = ref([])
    const loading = ref(false)
    const error = ref('')
    
    // 模拟获取评论数据
    const fetchComments = async () => {
      loading.value = true
      error.value = ''
      
      try {
        // 这里应该调用实际的API获取评论数据
        // 暂时使用模拟数据
        await new Promise(resolve => setTimeout(resolve, 1000))
        comments.value = [
          {
            id: '1',
            author: '张三',
            content: '这篇文章写得真好！',
            createdAt: '2023-05-01T12:00:00Z'
          },
          {
            id: '2',
            author: '李四',
            content: '感谢分享，学到了很多。',
            createdAt: '2023-05-02T14:30:00Z'
          }
        ]
      } catch (err) {
        error.value = '获取评论失败'
      } finally {
        loading.value = false
      }
    }
    
    // 处理提交评论
    const handleCommentSubmit = async (commentData) => {
      try {
        // 这里应该调用实际的API提交评论
        // 暂时使用模拟数据
        const newComment = {
          id: Date.now().toString(),
          author: commentData.author,
          content: commentData.content,
          createdAt: new Date().toISOString()
        }
        
        comments.value.unshift(newComment)
      } catch (err) {
        console.error('提交评论失败:', err)
      }
    }
    
    onMounted(() => {
      fetchComments()
    })
    
    return {
      comments,
      loading,
      error,
      handleCommentSubmit
    }
  }
}
</script>

<style scoped>
.comment-section {
  margin-top: 2rem;
}

.comment-section h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.loading, .error, .no-comments {
  padding: 1rem;
  text-align: center;
}

.error {
  color: #f56565;
}
</style>