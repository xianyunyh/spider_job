import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

const router =  new Router({
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
      meta:{title:"热门公司排行"},
      component: () => import(/* webpackChunkName: "index" */ './views/HotCompany.vue')
    },
    {
      path: '/map',
      name: 'company-map',
      meta:{title:"公司所在位置展示"},
      component: () => import(/* webpackChunkName: "index" */ './views/CompanyMap.vue')
    },
    {
      path: '/workyear',
      name: 'workyear',
      meta:{title:"工作年限分析"},
      component: () => import(/* webpackChunkName: "index" */ './views/Workyear.vue')
    },
    {
      path: '/weekline',
      name: 'weekline',
      meta:{title:"一周内职位发布情况"},
      component: () => import(/* webpackChunkName: "index" */ './views/Weekline.vue')
    },
    {
      path: '/education',
      name: 'education',
      meta:{title:"教育情况"},

      component: () => import(/* webpackChunkName: "index" */ './views/Education.vue')
    },
    {
      path: '/wordcloud',
      name: 'wordcloud',
      component: () => import(/* webpackChunkName: "index" */ './views/Word.vue')
    },
    {
      path: '/company',
      name: 'company',
      component: () => import(/* webpackChunkName: "index" */ './views/Company.vue')
    },

  ]
})
router.beforeEach((to, from, next) => {
  /*路由发生改变修改页面的title */
  if(to.meta.title) {
    document.title = to.meta.title
  }
  next();
})
export default router