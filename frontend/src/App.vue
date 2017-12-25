<template>
  <div id="app" class="container py-3">
    <h1 class="py-3">Signup / Login</h1>
    <signup></signup>
  </div>
</template>

<script>
  import Signup from './components/Signup.vue'

  export default {
    name: 'app',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }

    },
    components: {
      'signup': Signup
    }
  }
</script>

<style lang="scss">
  @import '../node_modules/bootstrap/scss/bootstrap.scss';
</style>
