import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  me: {},
  loginForm: false,
  topics: [],
}

const getters = {

}

const mutations = {
  showLoginForm: state => state.loginForm = true,
  hideLoginForm: state => state.loginForm = false,
  recordMe: (state, { me }) => state.me = me,
  setTopics: (state, { topics }) => state.topics = topics
}

const actions = {

}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})