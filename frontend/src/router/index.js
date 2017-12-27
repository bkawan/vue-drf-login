import Vue from 'vue'
import Router from 'vue-router'
import Signup from '../components/Signup.vue'
import Login from '../components/Login.vue'
import Index from '../components/Index.vue'

import Dashboard from '../components/Dashboard.vue'

Vue.use(Router);
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    }
    ,
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
    }
  ]
})

