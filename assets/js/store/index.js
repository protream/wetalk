import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  me: {},
  loginForm: false,
  topics: [],
  posts: [],
}

const getters = {

}

const mutations = {
  showLoginForm: state => state.loginForm = true,
  hideLoginForm: state => state.loginForm = false,
  recordMe: (state, { me }) => state.me = me,
  setTopics: (state, { topics }) => state.topics = topics,
  addPosts: (state, { posts }) => state.posts = state.posts.concat(posts),
  addPost: (state, { post }) => state.posts.unshift(post)
}

const actions = {

}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})