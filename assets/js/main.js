import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Form from './utils/form'
import * as filters from './utils/filters'

window.Form = Form
window.http = axios

Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

new Vue({
  el: '#app',
  render: h => h(App),
  router,
  store
})
