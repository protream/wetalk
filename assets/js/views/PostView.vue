<template>
  <div class="yue post-view">
    <div class="container app__container">
      <div class="post-title" v-text="post.title"></div>
      <post-meta :post="post"></post-meta>
      <div class="post-content" v-html="markedContent"></div>
    </div>
  </div>
</template>

<script>
  import PostMeta from '../components/PostMeta.vue'
  import marked from 'marked'

  export default {
    data() {
      return {

      }
    },
    computed: {
      post() {
       return this.$store.state.posts.find(post => post.id == this.$route.params.id)
      },
      markedContent() {
        return marked(this.post.content, { sanitize: true })
      }
    },
    components: {
      PostMeta
    }
  }
</script>

<style>
  .post-view .post-title {
    font-size: 36px;
    font-weight: 600px;
  }
</style>