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
    
    <CommentForm :blog-id="blogId" @submit="handleCommentSubmit" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import Comment from './Comment.vue'
import CommentForm from './CommentForm.vue'
import { useCommentStore } from '../../store'

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
    const commentStore = useCommentStore()
    
    // 获取评论数据
    const fetchComments = async () => {
      await commentStore.fetchComments(props.blogId)
    }
    
    // 处理提交评论
    const handleCommentSubmit = async (commentData) => {
      console.log('CommentSection received commentData:', commentData);
      try {
        await commentStore.addComment(commentData)
      } catch (err) {
        console.error('提交评论失败:', err)
      }
    }
    
    onMounted(() => {
      fetchComments()
    })
    
    return {
      comments: commentStore.comments,
      loading: commentStore.loading,
      error: commentStore.error,
      handleCommentSubmit
    }
  }
}
</script>

<style scoped>
.comment-section {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #f8f9fa;
  border-radius: 8px;
}

.comment-section h3 {
  margin-bottom: 1rem;
  font-size: 1.5rem;
  color: #2c3e50;
  text-align: center;
}

.loading, .error, .no-comments {
  padding: 1.5rem;
  text-align: center;
  font-size: 1rem;
}

.loading {
  color: #7f8c8d;
}

.error {
  color: #e74c3c;
  font-weight: bold;
}

.no-comments {
  color: #7f8c8d;
  font-style: italic;
}
</style>