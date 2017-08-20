import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import CreatePost from '../views/CreatePost.vue'

Vue.use(Router)

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/about',
    component: About
  },
  {
    path: '/p/create',
    component: CreatePost 
  }
]

export default new Router({
  mode: 'history',
  routes: routes
})
