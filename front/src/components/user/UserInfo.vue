<template>
  <div class="user-info">
    <div class="user-avatar">
      <img :src="user.avatar || defaultAvatar" :alt="user.name" />
    </div>
    <div class="user-details">
      <h3>{{ user.name }}</h3>
      <p v-if="user.bio" class="user-bio">{{ user.bio }}</p>
      <div class="user-stats">
        <span>文章: {{ user.postCount || 0 }}</span>
        <span>关注: {{ user.followingCount || 0 }}</span>
        <span>粉丝: {{ user.followerCount || 0 }}</span>
      </div>
      <div class="user-actions" v-if="!isCurrentUser">
        <el-button 
          :type="isFollowing ? 'default' : 'primary'" 
          @click="toggleFollow"
          size="small"
        >
          {{ isFollowing ? '已关注' : '关注' }}
        </el-button>
        <el-button type="default" size="small" @click="sendMessage">私信</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  props: {
    user: {
      type: Object,
      required: true,
      default: () => ({
        id: '',
        name: '',
        avatar: '',
        bio: '',
        postCount: 0,
        followingCount: 0,
        followerCount: 0
      })
    },
    isCurrentUser: {
      type: Boolean,
      default: false
    },
    isFollowing: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      defaultAvatar: 'https://via.placeholder.com/100x100?text=Avatar'
    }
  },
  methods: {
    toggleFollow() {
      this.$emit('toggle-follow', this.user.id)
    },
    sendMessage() {
      this.$emit('send-message', this.user.id)
    }
  }
}
</script>

<style scoped>
.user-info {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #fff;
}

.user-avatar img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
}

.user-details {
  flex: 1;
}

.user-details h3 {
  margin: 0 0 0.5rem 0;
}

.user-bio {
  margin: 0 0 1rem 0;
  color: #666;
}

.user-stats {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.user-stats span {
  font-size: 0.9rem;
}

.user-actions {
  display: flex;
  gap: 0.5rem;
}
</style>