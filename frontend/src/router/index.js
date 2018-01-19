import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: function (resolve) {
        require(['../components/Index'], resolve)
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: function (resolve) {
        require(['../components/login/Login'], resolve)
      }
    },
    {
      path: '/signup',
      name: 'Signup',
      component: function (resolve) {
        require(['../components/signup/Signup'], resolve)
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: function (resolve) {
        require(['../components/dashboard/Dashboard'], resolve)
      },
      beforeEnter: guardRoute
    },
    {
      path: '/dashboard/profile',
      name: 'profile',
      component: function (resolve) {
        require(['../components/dashboard/Profile'], resolve)
      },
      beforeEnter: guardRoute
    },
    {
      path: '/dashboard/profile/edit',
      name: 'profileEdit',
      component: function (resolve) {
        require(['../components/dashboard/ProfileEdit'], resolve)
      },
      beforeEnter: guardRoute
    },
    {
      path: '/404',
      name: '404',
      component: function (resolve) {
        require(['../components/404'], resolve)
      },
    },
    { path: '*', redirect: '/404', hidden: true }
  ]
})
function guardRoute (to, from, next) {

  const auth = router.app.$options.store.state.auth

  if (!auth.isLoggedIn) {
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}
