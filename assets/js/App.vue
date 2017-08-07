<template>
<div class="container-fluid app">
  <nav class="navbar navbar-default app__navbar">
    <div class="container-fluid ">
      <!-- Brand and toggle get grouped for better mobile display -->
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">
         Wetalk
        </a>
      </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li>
            <router-link to="/">Home</router-link>
          </li>
          <li>
            <router-link to="/about">About</router-link>
          </li>
          <li>
            <router-link to="/contact">Contact</router-link>
          </li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#" class="navbar-btn">注册</a></li>
          <li><a href="#" class="navbar-btn">登陆</a></li>
        </ul>
      </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
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
