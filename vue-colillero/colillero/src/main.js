import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Inicio from './components/Inicio';
import MenuColillero from './components/MenuColillero';

const app = createApp(App);

app.use(createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Inicio },
        { path: '/menu', component: MenuColillero }
    ]
}));

app.mount('#app');
