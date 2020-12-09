import { createWebHistory, createRouter } from "vue-router";
import Prediction from "@/views/Prediction.vue";
import About from "@/views/About.vue";

const routes = [
    {
        path: '/',
        name: 'prediction',
        component: Prediction,
    },
    {
        path: '/about',
        name: 'About',
        component: About,
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;