<template>
<li class="message-item">
  <span class="avatar">
    <avatar :alt="message.name"></avatar>
  </span>
  <div class="message-main">
    <div class="message-info">
      <span>{{ message.name }} </span>
      <div class="message-time">
        <div :datetime="message.created_at">{{ message.created_at | fromNow }}</div>
      </div>
    </div>
    <div class="message-text" v-html="message.text"></div>
  </div>
</li>
</template>

<script>
import Avatar from './Avatar.vue';
import moment from 'moment'

export default {
  props: ['message'],
  filters: {
    fromNow(time) {
      moment.locale('zh-cn');
      return moment(time).fromNow();
    }
  },
  components: {
    Avatar
  }
}
</script>

<style>
.message-item {
  color: #565655;
  padding-top: 14px;
  padding-bottom: 10px;
  list-style-type: none;
}

.message-item .message-info {
  position: relative;
  font-size: 13px;
  color: #999;
  margin-bottom: 10px;
  line-height: 1;
}

.message-item .message-main {
  overflow: hidden;
}

.message-item .message-time {
  position: absolute;
  right: 0;
  top: 0;
  font-size: 13px;
  transition: all .2s ease;
}

.message-item .message-text {
  line-height: 1.4;
  font-size: 16px;
  margin-bottom: 10px;
}

.avatar {
  float: left;
  margin-right: 12px;
}
</style>