<template>
  <div id="app">
  	<h1>{{ msg }}</h1>
  </div>
</template>

<script>
	export default {
		data() {
      return {
        msg: 'Hello Vue!'
      }
		}
	}
</script>

<style>
  h1 {
    color: blue;
  }
</style>