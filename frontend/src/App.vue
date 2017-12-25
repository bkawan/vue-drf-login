<template>
  <div id="app" class="container py-3">
    <!--<signup></signup>-->
    <router-view></router-view>
  </div>
</template>

<script>
//  import Signup from './components/Signup.vue'

  export default {
    name: 'app',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }

    },
  }
</script>

<style lang="scss">
  @import '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
