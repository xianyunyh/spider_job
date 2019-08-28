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
      component: () => import(/* webpackChunkName: "index" */ './views/HotCompany.vue')
    },
    {
      path: '/map',
      name: 'company-map',
      component: () => import(/* webpackChunkName: "index" */ './views/CompanyMap.vue')
    },
    {
      path: '/workyear',
      name: 'workyear',
      component: () => import(/* webpackChunkName: "index" */ './views/Workyear.vue')
    },
    {
      path: '/weekline',
      name: 'weekline',
      component: () => import(/* webpackChunkName: "index" */ './views/Weekline.vue')
    },
    {
      path: '/education',
      name: 'education',
      component: () => import(/* webpackChunkName: "index" */ './views/Education.vue')
    },
    {
      path: '/wordcloud',
      name: 'wordcloud',
      component: () => import(/* webpackChunkName: "about" */ './views/Word.vue')
    },
    

  ]
})
