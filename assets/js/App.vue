<template>
<div class="container-fluid app">
  <nav class="navbar navbar-default app__navbar">
    <div class="container-fluid ">
      <div class="navbar-header">
        <router-link to="/" class="navbar-brand">Wetalk</router-link>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li>
            <router-link to="/about">关于</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#" class="navbar-btn">注册</a></li>
          <li><a href="#" class="navbar-btn">登陆</a></li>
        </ul>
      </div>
    </div>
  </nav>
  <router-view></router-view>
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
body {
  margin-top: 15px;
}
.jumbotron h1, h2 {
  color: #FF5A5F;
}
.app,
.app__body {
  padding-right: 0;
  padding-left: 0;
}
.app {
  width: 940px;
}
.app .app__navbar {
  background: #fff;
  border: 0;
}
</style>
