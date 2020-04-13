import Vue from 'vue/dist/vue.js'
import vueplugin from './vueplugin.js'

Vue.use(vueplugin)

new Vue({
    el:'#app',
    data:{
        item:20
    }
})