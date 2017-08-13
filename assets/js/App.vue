<template>

  <div class="container-fluid app__container-fluid">
    <nav class="navbar navbar-default app__navbar">

      <div class="container app__container">
        <div class="navbar-header">
          <router-link to="/" class="navbar-brand">Wetalk</router-link>
        </div>
        <div class="collapse navbar-collapse app__navbar" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
             <li><router-link to="/about">关于</router-link></li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li v-if="!$store.state.me.username">
              <a @click="$store.commit('showLoginForm')">登录</a>
            </li>
            <li class="dropdown" v-if="$store.state.me.username">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                <avatar :alt="$store.state.me.username" :size="28"></avatar>
                <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
                <li><a href="#">我的主页</a></li>
                <li><a href="#">个人设置</a></li>
                 <li role="separator" class="divider"></li>
                <li><router-link to="/">退出登录</router-link></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>
    <div class="app__footer">
     <div class="container app__container">
     Copyright © 2017 By Protream
     </div>
    </div>
    <login-form v-if="$store.state.loginForm"></login-form>
    </div>
  </div>
</template>

<script>
  import Avatar from './components/Avatar.vue'
  import LoginForm from './components/LoginForm.vue'

  export default {
    components: {
      Avatar,
      LoginForm
    },
  }
</script>

<style>
body {
  margin-top: 15px;
}
.app__container-fluid {
  padding: 0;
}
.app__container {
  width: 940px;
  margin: 0 auto;
}
.app__navbar {
  background-color: #fff;
  border: none;
}
.app__footer {
  border-top: 1px solid #eee;
  padding: 16px 0 24px;
  color: #999;
  font-size: 14px;
}
</style>
