<script setup lang="ts">
   // import AppHeader from './AppHeader.vue';
   import { watch, ref } from 'vue';
   import { useAuthStore } from '@/modules/auth/store/auth.store';
   import { useToastNotification } from '@/shared/composables/useToastNotification';
   import AppSidebar from './AppSidebar.vue'

   const auth = useAuthStore();
   const toastNotification = useToastNotification();

   // const welcomed = ref(false);

   // watch(
   //    () => auth.user,
   //    (user) => {
   //       if (!user || welcomed.value) return;

   //       // Better Auth user shape: { name, email, image }
   //       // Previously read user_metadata.full_name (Supabase) — always undefined
   //       const name = user.name || 'Builder';

   //       toastNotification(
   //          'success',
   //          `Welcome ${name}`,
   //          'You are now logged in',
   //       );

   //       welcomed.value = true;
   //    },
   //    { immediate: true },
   // );
</script>

<template>
   <div class="tw-flex tw-min-h-screen lg:tw-flex-row tw-justify-center tw-flex-col">
      <!-- <AppHeader /> -->
      <AppSidebar class="lg:tw-flex tw-hidden" />
      <main class="tw-flex-1 tw-max-w-[1500px] tw-justify-center tw-overflow-auto">
         <router-view />
      </main>
   </div>
</template>
