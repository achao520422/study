import { createRouter, createWebHistory} from 'vue-router'
import {useAuthStore} from "@/store.js";


const routes = [
    {path: '/', component: () => import( '@/page/HomeView.vue')},
    {path: '/login', component: () => import( '@/page/LoginView.vue')},
    {path: '/info', component: () => import( '@/page/InfoView.vue')},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    console.log(to)
    if (to.path === '/login') {
        useAuthStore().needAuth()
    }else {
        useAuthStore().disableAuth()
    }
    console.log(useAuthStore().isAuthenticated)
    next()
})

export default router