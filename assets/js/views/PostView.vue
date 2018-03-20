<template>
  <div class="post-view">
    <div class="yue container app__container">
      <div class="post-title" v-text="post.title"></div>
      <post-meta :post="post"></post-meta>
      <div class="post-content" v-html="markedContent"></div>
      <div class="post-actions">
        <button type="button" class="btn btn-success" aria-label="Left Align">
          <span class="glyphicon glyphicon-heart-empty" aria-hidden="true"></span>&nbsp;喜欢
        </button>
      </div>
    </div>
    <comment-box></comment-box>
  </div>
</template>

<script>
  import PostMeta from '../components/PostMeta.vue'
  import CommentBox from '../components/CommentBox.vue'
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
      PostMeta,
      CommentBox
    }
  }
</script>

<style>
  .post-view .post-title {
    font-size: 36px;
    font-weight: 600px;
  }
</style>