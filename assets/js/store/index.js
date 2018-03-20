import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  me: {},
  loginForm: false,
  topics: [],
  posts: [],
  offset: 0,
  currentTopic: '全部话题'
}

const getters = {

}

const mutations = {
  showLoginForm: state => state.loginForm = true,
  hideLoginForm: state => state.loginForm = false,
  recordMe: (state, { me }) => state.me = me,
  setTopics: (state, { topics }) => state.topics = topics,
  addPosts: (state, { posts }) => state.posts = state.posts.concat(posts),
  addPost: (state, { post }) => state.posts.unshift(post),
  setOffset: (state, { offset }) => state.offset = offset,
  setCurrentTopic: (state, { topic }) => state.currentTopic = topic,
  clearPosts: state => state.posts = [],
}

const actions = {
  loadPosts: ({ state, commit }) => {
    http.get('/api/posts', { params: { offset: state.offset, topic: state.currentTopic } })
      .then(({ data }) => {
        commit('addPosts', { posts: data.data })
        commit('setOffset', { offset: data.offset })
      })
  },
  selectTopic: ({ state, commit, dispatch }, { topicName }) => {
    commit('setOffset', { offset: 0 })
    commit('setCurrentTopic', { topic: topicName })
    commit('clearPosts')
    dispatch('loadPosts')
  }
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})