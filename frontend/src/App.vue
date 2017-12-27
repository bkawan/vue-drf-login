<template>
  <div id="app" class="bg-inverse text-white">
    <div class="container py-3" id="main-container">
      <router-view></router-view>
    </div>
    <div id="footer" class="bg-black py-2">
      <div class="container text-info text-center">
        <p>{{footer}}</p>
      </div>
    </div>
  </div>
</template>

<script>
  //  import Signup from './components/Signup.vue'
  export default {
    name: 'app',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        footer: 'copyright @ bkawan ' + new Date().getFullYear() + ' | Powered by Vue js and Django Rest Framework'
      }

    },
  }
</script>

<style lang="scss">
  @import '../node_modules/bootstrap/scss/bootstrap.scss';

  .bg-black {
    background-color: black;
  }
</style>
