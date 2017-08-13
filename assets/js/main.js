import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Form from './utils/form'

window.Form = Form
window.http = axios

new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store
})
