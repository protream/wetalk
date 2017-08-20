<template>
  <div class="container app__container">
    <form class="post-form">
      <div class="form-group">
        <input type="text" placeholder="标题" class="post-title" v-model="form.title">
      </div>
      <div class="form-group post-topic">
        <select v-model="form.topic_name"><option v-for="topic in topics">{{ topic.name }}</option></select>
      </div>
      <div class="form-group">
        <textarea rows="25" placeholder="想说些什么..." v-model="form.content" v-if="!isPreview"></textarea>
        <div class="yue preview" v-html="markedContent" v-if="isPreview"></div> 
      </div>
      <div class="btn-group btn-group-justified" role="group">
       <div class="btn-group" role="group">
         <button type="submit" class="btn btn-default" @click.prevent="isPreview=!isPreview">{{ isPreview ? '继续编辑' : '预览'  }}</button>
       </div>
        <div class="btn-group" role="group">
          <button type="submit" class="btn btn-default" @click.prevent="submit">发布</button>
        </div>
      </div>
    </form> 
  </div> 
</template>

<script>
  import marked from 'marked'

  export default {
    data() {
      return {
        isPreview: false,
        form: new Form({
          title: '',
          content: '',
          topic_name: ''
        })
      }
    },
    methods: {
      submit() {
        this.form.post('/api/posts')
          .then(data => {
            this.$router.push('/')
          })
      }
    },
    computed: {
      topics() {
        return this.$store.state.topics
      },
      markedContent() {
        return marked(this.form.content, { sanitize: true })
      }
    }
  }
</script>

<style>
  .post-form {
  margin-bottom: 15px;
}
.post-form input, textarea, select{
  width: 100%;
  padding: 10px 0px;
  border: none;
  outline: none;
}
.post-form select {
  height: 30px;
}
.post-form textarea {
  font-size: 18px;
  color: #454545;
}
.post-form .post-title {
  font-size: 36px;
  font-weight: 600px;
}
.post-form .post-topic {
  font-size: 12px;
}
</style>