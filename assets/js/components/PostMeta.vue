<template>
  <div class="post__meta">
    <span class="label post__topic" :style="{background: topicBackground}">{{ post.topic.name}}</span>
    {{ post.created_at | fromNow }} By {{ post.user.username }}
  </div>
</template>

<script>
  import wc from 'word-color'
  import moment from 'moment'

  export default {
    props: ['post'],
    computed: {
      topicBackground() {
        return wc(this.post.topic.name)
      }
    },
    filters: {
      fromNow(time) {
        return moment(time).fromNow()
      }
    } 
  }
</script>

<style>
  .post__meta {
    color: #999;
    font-size: 12px;
  }
  .post__topic {
    padding: 0 .2em;
    font-weight: normal;
    margin-right: .5em;
  }
</style>