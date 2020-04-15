import Vue from 'vue/dist/vue.js'
import vueplugin from './vueplugin.js'
import Vuex from 'vuex'

Vue.use(vueplugin)
// 调用vuex插件
Vue.use(Vuex)

// vuex 使用
var store = new Vuex.Store({
    state:{message:'hello'},
    mutations:{

    },
    actions:{},
    getters:{}

});
new Vue({
    el:'#app',
    data:{
        item:20
    },
    store:store // 初始化vuex
})