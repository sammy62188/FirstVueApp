import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import About from '@/components/About.vue'
import Garri from '@/components/Garri.vue'
import Honey from '@/components/Honey.vue'
import Groundnut from '@/components/Groundnut.vue'
import Contact from '@/components/contact.vue'

Vue.use(VueRouter)
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/garri',
    name: 'Garri',
    component: Garri
  },
  {
    path: '/groundnut',
    name: 'Groundnut',
    component: Groundnut
  },
  {
    path: '/honey',
    name: 'Honey',
    component: Honey
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router
