import Vue from 'vue'
import Router from 'vue-router'
import Signup from '../components/Signup.vue'

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: '/signup',
      name: 'signup',
      component:Signup
    }
  ]
})

