<template>
  <li class="comment-item">
    <span class="avatar">
      <avatar :alt="comment.user.username"></avatar>
    </span>
    <div class="comment-main">
      <div class="comment-info">
        <span>{{ comment.user.username }}</span>
        <div class="comment-time">
          <div :datetime="comment.created_at">{{ comment.created_at | fromNow }}</div>
        </div>
      </div>
      <div class="comment-text" v-html="comment.content"></div>
    </div>
  </li>
</template>

<script>
import Avatar from './Avatar.vue'

export default {
  props: ['comment'],
  components: {
    Avatar
  }
}
</script>

<style>
.comment-item {
  color: #565655;
  padding-top: 14px;
  padding-bottom: 10px;
  list-style-type: none;
}

.comment-item .comment-info {
  position: relative;
  font-size: 13px;
  color: #999;
  margin-bottom: 10px;
  line-height: 1;
}

.comment-item .comment-main {
  overflow: hidden;
}

.comment-item .comment-time {
  position: absolute;
  right: 0;
  top: 0;
  font-size: 13px;
  transition: all .2s ease;
}

.comment-item .comment-text {
  line-height: 1.4;
  font-size: 16px;
  margin-bottom: 10px;
}

.avatar {
  float: left;
  margin-right: 12px;
}
</style>
