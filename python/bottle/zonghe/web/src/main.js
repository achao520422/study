import './assets/main.css'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'

import router from './router'
const pinia = createPinia()
const app = createApp(App)
app.use(ElementPlus)
app.use(pinia)
app.use(router)
app.mount('#app')
