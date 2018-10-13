import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
 // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/hot-company',
      name: 'hot',
      component: () => import(/* webpackChunkName: "about" */ './views/HotCompany.vue')
    },
    {
      path: '/workyear',
      name: 'workyear',
      component: () => import(/* webpackChunkName: "about" */ './views/Workyear.vue')
    },
    {
      path: '/weekline',
      name: 'weekline',
      component: () => import(/* webpackChunkName: "about" */ './views/Weekline.vue')
    },
    {
      path: '/education',
      name: 'education',
      component: () => import(/* webpackChunkName: "about" */ './views/Education.vue')
    },
    {
      path: '/wordcloud',
      name: 'wordcloud',
      component: () => import(/* webpackChunkName: "about" */ './views/Word.vue')
    },

  ]
})
