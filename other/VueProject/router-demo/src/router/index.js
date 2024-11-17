import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({   
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },{
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    }
  ],
})

//全局导航守卫
let isAuthenticated = true
router.beforeEach((to, from) => {
  //如果没有授权则不鞥跳转,就要跳转到登录页面
  if(!isAuthenticated && to != 'login'){
    return {name: 'login'}
  }
})

export default router
