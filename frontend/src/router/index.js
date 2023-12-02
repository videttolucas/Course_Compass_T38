import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Courses from '../views/CoursesView.vue'
import Schedule from '../views/ScheduleView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/courses',
    name: 'courses',
    component: Courses
  },
  {
    path: '/schedule',
    name: 'schedule',
    component: Schedule
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
