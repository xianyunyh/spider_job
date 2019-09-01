import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@/static/css/bootstrap.min.css'

Vue.config.productionTip = true

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
