<template>
  <div class="container app__container comment-box">
    <form @submit.prevent="submit">
      <div class="form-group">
        <textarea name="content" rows="5" placeholder="评论..." @focus="checkLogin"></textarea>
      </div>
      <button v-if="isLogin" type="submit" class="btn btn-default">Submit</button>
    </form>
    <div class="comment-box__header">{{ comments.length }} comments</div>
    <div class="comment-box__comments">
      <ul tansition="fade">
        <template v-for="comment in comments">
          <comment-item :comment="comment"></comment-item>
        </template>
      </ul>
    </div>
  </div>
</template>

<script>
  import CommentItem from './CommentItem.vue'

  export default {
    props: ['post'],
    data() {
      return {
        comments: [
          {
            content: "Good job!",
            user: {
              username: "protream"
            },
            created_at: "2017-08-22T14:00:00Z"
          },
          {
            content: "Good job!",
            user: {
              username: "Tony"
            },
            created_at: "2017-08-22T14:00:00Z"
          },
          {
            content: "Good job!",
            user: {
              username: "Jack"
            },
            created_at: "2017-08-22T14:00:00Z"
          }
        ]
      }
    },
    methods: {
      submit() {

      },
      checkLogin() {
        if (!this.isLogin) {
          this.$store.commit('showLoginForm')
        }
      }
    },
    computed: {
      isLogin() {
        return this.$store.state.me.username
      }
    },
    components: {
      CommentItem
    }
  }
</script>

<style>
  .comment-box {
    margin: 15px auto;
  }
  .comment-box__header {
    line-height: 1;
    color: #666;
    padding: 20px 0 6px;
    border-bottom: 1px solid #eee;
    text-transform: uppercase;
    font-size: 13px;
  }
  .comment-box__comments ul {
    margin: 0;
    padding: 0;
  }
</style>