import Vue from 'vue'
import VueRouter from 'vue-router'
import AnimeSearch from "@/components/AnimeSearch";
import Results from "@/components/Results";
import Error from "@/components/Error";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'AnimeSearch',
        component: AnimeSearch
    },
    {
        path: '/results',
        name: 'Results',
        component: Results,
    },
    {
        path: '/error',
        name: 'Error',
        component: Error,
    }
]

const router = new VueRouter({
    mode: 'history',
    hash: false,
    routes
})

export default router
