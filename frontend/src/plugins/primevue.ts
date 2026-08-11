import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import ConfirmationService from 'primevue/confirmationservice';
import Aura from '@primeuix/themes/aura';
import 'primeicons/primeicons.css';

export function setupPrimeVue(app: any) {
   app.use(PrimeVue, {
      ripple: true,
      theme: {
         preset: Aura,
         options: {
            darkModeSelector: '.tw-dark',
         },
      },
   });

   app.use(ToastService);
   // Required for useConfirm() + <ConfirmDialog /> to work anywhere in the app
   app.use(ConfirmationService);
}
