<template>
  <div class="container-fluid app__container-fluid">
    <div class="jumbotron home__jumbotron">
      <div class="container app__container">
        <p>忙里偷闲，扯下蛋去；苦中作乐，灌个水来</p>
      </div>
    </div>

    <div class="container app__container">
      <div class="home__toolbar">
        <div class="dropdown">
          <button class="btn btn-default btn-sm dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
            <span class="glyphicon glyphicon-th" aria-hidden="true"></span>
            <span>{{ $store.state.currentTopic }}</span>
            <span class="caret"></span>
          </button>
          <router-link to="/p/create" class="btn btn-default btn-sm" type="button">
            <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>发布帖子
          </router-link>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
            <li v-for="topic in topics"><a @click="selectTopic(topic)">{{ topic.name }}</a></li>
          </ul>
        </div>
      </div>

      <div class="home__post-list">
        <post-item v-for="post in posts" :post="post"></post-item>
        <div class="home__loading" v-if="loading">加载中...</div>
        <div class="home__loadmore" v-if="!loading && offset" @click="loadPosts">Load More</div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
  import PostItem from '../components/PostItem.vue'

  export default {
    data() {
      return {
        loading: false
      }
    }, 
    methods: {
      loadPosts() {
        this.loading = true
        this.$store.dispatch('loadPosts')
        this.loading = false
      },
      selectTopic(topic) {
        this.loading = true
        this.$store.dispatch('selectTopic', { topicName: topic.name })
        this.loading = false
      }
    },
    computed: {
      topics() {
        return this.$store.state.topics
      },
      posts() {
        return this.$store.state.posts
      },
      offset() {
        return this.$store.state.offset
      }
    },
    components: {
      PostItem
    }
  }
</script>

<style>
  .home__jumbotron {
    height: 240px;
    border-radius: none;
    background-image: url("../../images/jumbotron.jpg");
    background-size: 100% 100%;
  }
  .home__jumbotron p {
    color: #fff;
    margin-top: 140px;
  }
  .home__toolbar {
    margin-bottom: 15px;
  }
  .home__loadmore {
  width: 100%;
  height: 38px;
  line-height: 38px;
  background-color: #f0f0f0;
  text-align: center;
  margin-bottom: 30px;
  color: #999;
  cursor: pointer;
}
.home__loadmore:hover{
  background-color: #dadada;
}
</style>