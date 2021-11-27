import Vue from 'vue'
import VueRouter from 'vue-router'
import AnimeSearch from "@/components/AnimeSearch";
import Results from "@/components/Results";

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
        // props: route => ({query: route.query.q})
    }
]

const router = new VueRouter({
    mode: 'history',
    hash: false,
    routes
})

export default router
