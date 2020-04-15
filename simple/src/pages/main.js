import Vue from 'vue'
import Layout from './Layout.vue'
import VueRouter from "vue-router"
import IndexPage from "./pages/index.vue"

Vue.use(VueRouter)
let router = new VueRouter({
  mode:"history",
  routes:[
    {
      path:"/",
      component:IndexPage
    }
  ]
})

new Vue({
  el: '#app',
  router,
  components:{
    Layout
  },
  template:"<Layout/>"
})
