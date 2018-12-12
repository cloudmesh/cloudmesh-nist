import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Vm from './views/Vm.vue'
import Flavor from './views/Flavor.vue'
import Image from './views/Image.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/vm',
            name: 'vm',
            component: Vm
        },
        {
            path: '/flavor',
            name: 'flavor',
            component: Flavor
        },
        {
            path: '/image',
            name: 'image',
            component: Image
        }
    ]
})
