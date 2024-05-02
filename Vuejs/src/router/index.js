// import Home from '../views/Home.vue';
import Login from '../components/Login.vue';
import NotFound from '../views/NotFound.vue';
import Cashier from '../components/Cashier.vue';
import Product from '../components/Product.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  // { path: '/', component: Home },
  { path: '/', component: Login },
  { path: '/cashier', component: Cashier, meta: { requiresAuth: true } },
  { path: '/product', component: Product, meta: { requiresAuth: true } },
  { path: '/404', component: NotFound },
  { path: '/:pathMatch(.*)', component: NotFound }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
