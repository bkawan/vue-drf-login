import Vue from 'vue'
import Router from 'vue-router'
import Signup from '../components/Signup.vue'
import Login from '../components/Login.vue'

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
    {
      path: '/login',
      name: 'login',
      component: Login
   }
  ]
})

