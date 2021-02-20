import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/admin",
    name: "Admin",
    component: () =>
      import(/* webpackChunkName: "admin" */ "../views/Admin.vue"),
  },
  {
    path: "/Student",
    name: "Student",
    component: () =>
      import(/* webpackChunkName: "student" */ "../views/Student.vue"),
  },
  {
    path: "/Teacher",
    name: "Teacher",
    component: () =>
      import(/* webpackChunkName: "teacher" */ "../views/Teacher.vue"),
  },
];

const router = new VueRouter({
  routes
})

export default router
