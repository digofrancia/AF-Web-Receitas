import { createRouter, createWebHistory } from 'vue-router'

import siteLayout from '../layouts/siteLayout.vue'
import Receita from '../components/Receita.vue'
import Home from '../components/Home.vue'
import Categorias from '../components/Categorias.vue';

const routes = [
  {
    path: '/',
    component: siteLayout,
    redirect: '/home',
    children: [
      {
        path: '/home',
        name: "Home",
        component: Home
      },
      {
        path: '/home/:category/:name',
        name: "Receita",
        component: Receita
      },
      {
        path: '/categorias/:name',
        name: "categorias",
        component: Categorias
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router