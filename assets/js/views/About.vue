<template>
  <div class="container-fluid">
    <div class="jumbotron">
      <h2>About</h2>
    </div>
      Count: <span style="font-size: 50px">{{ $store.state.count }}</span>
      <div class="btn-group btn-group-justified" role="group">
        <div class="btn-group" role="group">
          <!-- 鼠标点击时，触发 increment mutation -->
          <button type="button" class="btn btn-default" @click="$store.commit('increment')">+</button>
        </div>
        <div class="btn-group" role="group">
          <!-- 鼠标点击时，触发 decrement mutation -->
          <button type="button" class="btn btn-default" @click="$store.commit('decrement')">-</button>
        </div>
      </div>
    </div>
  </div>
</template>