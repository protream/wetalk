<template>
  <div class="overlay">
    <div class="overlay-content">
      <div class="login-form">
        <div class="btn-group btn-group-justified login-tab" role="group" aria-label="login">
          <div class="btn-group" role="group">
            <button type="button" class="btn btn-default" @click="login=true">登录</button>
          </div>
          <div class="btn-group" role="group">
            <button type="button" class="btn btn-default" @click="login=false">注册</button>
          </div>
        </div>

        <form v-show="login" @submit.prevent="loginSubmit">
          <div class="form-group">
            <input type="email" class="form-control" placeholder="邮箱" v-model="loginForm.email">
            <span class="help-block" v-if="loginForm.errors.has('email')" v-text="loginForm.errors.get('email')"></span>
          </div>
          <div class="form-group">
            <input type="password" class="form-control"  placeholder="密码" v-model="loginForm.password">
          </div>
          <div class="checkbox">
            <label>
              <input type="checkbox"> 记住我
            </label>
          </div>
          <button type="submit" class="btn btn-default login-submit">登录</button>
        </form>

        <form v-show="!login" @submit.prevent="registerSubmit">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="用户名" v-model="registerForm.username">
          </div>
          <div class="form-group">
            <input type="email" class="form-control" placeholder="邮箱" v-model="registerForm.email">
          </div>
          <div class="form-group">
            <input type="password" class="form-control" placeholder="密码" v-model="registerForm.password">
          </div>
          <button type="submit" class="btn btn-default login-submit">注册</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        login: true,
        registerForm: new Form({
          username: '',
          email: '',
          password: ''
        }),
        loginForm: new Form({
          email: '',
          password: ''
        })
      }
    },

    methods: {
      registerSubmit() {
        this.registerForm.post('/api/user')
          .then(data => {
            this.$store.commit('recordMe', { me: data })
            this.$store.commit('hideLoginForm')
          })
      },

      loginSubmit() {
        this.loginForm.post('/api/user/session')
          .then(data => {
            this.$store.commit('recordMe', { me: data })
            this.$store.commit('hideLoginForm')
          })
      }
    }
  }
</script>

<style>
  .overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    justify-content: center;
    top: 0; 
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(255, 255, 255, 0.98);
    z-index: 2;
    cursor: pointer; 
  }
  .overlay-content {
    position: relative;
    max-width: 800px;
    box-sizing: border-box;
    top: 180px;
    margin: 0 auto;
    padding: 0 10px;
  }
  .login-form {
    width: 400px;
    margin: 0 auto;
  }
  .login-tab {
    margin-bottom: 20px;
  }
  .login-submit {
    color: #fff;
    width: 100%;
    background-color: #8766B3;
    border: none;
  }
</style>