<template>
  <div class="container-fluid">
    <div class="jumbotron">
      <h2>Home</h2>
    </div>
    <!-- 绑定数值为 state 中的 count -->
    Count: <span style="font-size: 50px">{{ $store.state.count }}</span>，count is <span style="font-size: 50px">{{ $store.getters.evenOrOdd }}</span>
    <div class="btn-group btn-group-justified" role="group">
      <div class="btn-group" role="group">
        <!-- 鼠标点击时，触发 increment mutation -->
        <button type="button" class="btn btn-default" @click="$store.dispatch('asyncIncrByAmount', { amount: 10 })">+</button>
      </div>
      <div class="btn-group" role="group">
        <!-- 鼠标点击时，触发 decrement mutation -->
        <button type="button" class="btn btn-default" @click="$store.commit('decrement')">-</button>
      </div>
    </div>
  </div>
</template>