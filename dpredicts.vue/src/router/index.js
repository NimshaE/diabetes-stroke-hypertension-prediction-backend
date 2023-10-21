import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import HomeView from '../views/HomeView.vue'
 
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Prediction from '../views/Prediction.vue'
import Result from '../views/Result.vue'
import ResultList from '../views/ResultList.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import UpdatePassword from '../views/UpdatePassword.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/prediction',
    name: 'Prediction',
    component: Prediction
  },
  {
    path: '/result',
    name: 'results',
    component: Result,
    props: (route) => ({ predictions: route.params.predictions }),
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/result-list',
    name: 'ResultsList',
    component: ResultList,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/forgotpassword',
    name: 'ForgotPassword',
    component: ForgotPassword,
  },
  {
    path: '/update-password',
    name: 'UpdatePassword',
    component: UpdatePassword,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated){
    next({ name: 'Login', query: {to: to.path} });
  } else {
    next()
  }
})
export default router
