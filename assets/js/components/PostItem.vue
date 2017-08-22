<template>
  <!-- 使用了 Bootstrap 中的 media 组件 -->
  <div class="media post">
    <div class="media-left">
      <a href="#">
        <avatar :alt="post.user.username" :size="45" class="v-avatar--squared"></avatar>
      </a>
    </div>
    <div class="media-body">
      <router-link class="media-heading" :to="'/p/' + post.id">{{ post.title }}</router-link>
      <post-meta :post="post"></post-meta>
    </div>
  </div>
</template>

<script>
  import Avatar from './Avatar.vue'
  import PostMeta from './PostMeta.vue'
  import wc from 'word-color'
  

  export default {
    props: ['post'],
    data() {
      return {
      }
    },
    computed: {
      topicBackground() {
        return wc(this.post.topic.name)
      }
    },
    components: {
      Avatar,
      PostMeta
    },
    filters: {
      fromNow(created_at) {
        return moment(created_at).fromNow()
      }
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
  .media-body > a {
    color: #333;
    font-size: 18px;
    text-decoration: none;
  }
</style>