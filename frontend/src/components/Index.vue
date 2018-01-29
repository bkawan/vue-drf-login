<template>
  <div id="index" class="text-white">
    <div class="container pt-3">
      <h3>Welcome to Vue Js and and Django Rest Framework Authentication System</h3>
      <div class="py-lg-5 my-lg-5 offset-4">
        <router-link class="btn btn-outline-primary" :to="{'name':'signup'}">Sign Up</router-link>
        <router-link class="btn btn-outline-success" :to="{'name':'login'}">Login</router-link>
      </div>

    </div>
  </div>
</template>


<script>
  export default {
    data () {
    }
  }
</script>




