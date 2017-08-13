import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  count: 0
}

const getters = {
  evenOrOdd: state => state.count % 2 === 0 ? 'even' : 'odd'
}

const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,
  incrByAmount: (state, { amount }) => state.count += amount
}

const actions = {
  asyncIncrByAmount: ({ commit}, { amount }) => {
    setTimeout(() => {
      console.log(amount)
      commit('incrByAmount', { amount })
    }, 2000)
  }
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})