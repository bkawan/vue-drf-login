import Vue from 'vue'
import Router from 'vue-router'
import Signup from '../components/Signup.vue'
<<<<<<< HEAD
import Login from '../components/Login.vue'
=======
>>>>>>> 7004c2ed515b694516750bc93922cdc1ef707d4c

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

