import Vue from 'vue';
import VueRouter from 'vue-router';
import Prediction from './views/Prediction';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'prediction',
            component: Prediction,
        },
    ],
});