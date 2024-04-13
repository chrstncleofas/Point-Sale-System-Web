import Home from '../views/Home.vue';
import Login from '../components/Login.vue';
import NotFound from '../views/NotFound.vue';
import Cashier from '../components/Cashier.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { path: '/cashier', component: Cashier },
  { path: '/:pathMatch(.*)', component: NotFound }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
