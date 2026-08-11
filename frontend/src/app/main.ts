import '@/style.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { createHead } from '@unhead/vue/client'
import * as Sentry from '@sentry/vue';

import App from '@/app/App.vue';
import router from '@/app/router';
import '@/plugins/openpanel';

import { useAuthStore } from '@/modules/auth/store/auth.store';
import { setupPrimeVue } from '@/plugins/primevue';

const app = createApp(App);
const pinia = createPinia();
const head = createHead();  // add

app.use(pinia);
app.use(head);  // add

Sentry.init({
   app,
   dsn: import.meta.env.VITE_SENTRY_DSN,
   environment: import.meta.env.MODE,
   integrations: [Sentry.browserTracingIntegration({ router })],
   tracesSampleRate: 0.2,
   replaysSessionSampleRate: 0,
   replaysOnErrorSampleRate: 0,
});

const auth = useAuthStore();
await auth.fetchSession();

app.use(router);
setupPrimeVue(app);
app.mount('#app');