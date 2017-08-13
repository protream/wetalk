<template>
  <!-- 使用了 Bootstrap 中的 media 组件 -->
  <div class="media post">
    <div class="media-left">
      <a href="#">
        <avatar :alt="post.author.name" :size="45" class="v-avatar--squared"></avatar>
      </a>
    </div>
    <div class="media-body">
      <h4 class="media-heading" v-text="post.title"></h4>
      <div class="post__meta">1 minutes ago</div>
    </div>
  </div>
</template>

<script>
  import Avatar from './Avatar.vue'

  export default {
    props: ['post'],
    data() {
      return {
      }
    },
    components: {
      Avatar
    }
  }
</script>

<style>
  .post {
    margin-bottom: 15px;
    padding: 15px 10px;
    border: 1px solid #eee;
    border-radius: 3px;
  }
  .post__meta {
    color: #999;
  }
</style>