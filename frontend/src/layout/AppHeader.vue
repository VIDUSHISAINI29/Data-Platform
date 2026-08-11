<script setup lang="ts">
   import { useRouter, useRoute } from 'vue-router';
   import { useAuthStore } from '@/modules/auth/store/auth.store';
   import { ref, computed, watch } from 'vue';

   const router = useRouter();
   const route = useRoute();
   const auth = useAuthStore();

   const menu = ref();
   const avatarError = ref(false);
   const mobileOpen = ref(false);

   const userInitial = computed(() => {
      const name = auth.user?.name || auth.user?.email || 'U';
      return name.charAt(0).toUpperCase();
   });

   const items = [
      {
         label: 'My Dashboard',
         icon: 'pi pi-chart-bar',
         command: () => router.push('/my-tools'),
      },
      {
         label: 'Settings',
         icon: 'pi pi-cog',
         command: () => router.push('/settings'),
      },
      {
         label: 'Submit Tool',
         icon: 'pi pi-plus',
         command: () => router.push('/submit'),
      },
      { separator: true },
      {
         label: 'Logout',
         icon: 'pi pi-sign-out',
         command: async () => {
            await auth.logout(router);
            router.push('/');
         },
      },
   ];

   const goToSubmit = () => {
      if (!auth.user) {
         router.push({ name: 'login', query: { redirect: '/submit' } });
         return;
      }
      router.push('/submit');
   };

   const isActive = (path: string) => route.path === path;

   // Close drawer on route change — handles back button and programmatic navigation
   watch(
      () => route.path,
      () => {
         mobileOpen.value = false;
      },
   );

   const mobileNav = (fn: () => void) => {
      mobileOpen.value = false;
      fn();
   };
</script>

<template>
   <header
      class="tw-sticky tw-top-0 tw-z-[100] tw-border-b tw-border-neutral-800 tw-bg-neutral-950/80 tw-backdrop-blur-md"
      role="banner">
      <div
         class="tw-mx-auto tw-flex tw-h-16 tw-max-w-6xl tw-items-center tw-justify-between tw-px-6">
         <!-- Logo -->
         <div
            class="tw-flex tw-cursor-pointer tw-items-center tw-transition-opacity hover:tw-opacity-80"
            role="link"
            aria-label="RocketLaunch home"
            tabindex="0"
            @click="router.push('/')"
            @keydown.enter="router.push('/')">
            <!-- <img
               src="/images/rocketlaunch_logo.svg"
               alt="RocketLaunch"
               class="tw-h-10" /> -->
         </div>

         <!-- Desktop nav -->
         <nav
            class="tw-hidden tw-items-center tw-gap-8 tw-text-sm tw-font-bold tw-uppercase tw-tracking-widest tw-text-neutral-400 md:tw-flex"
            aria-label="Main navigation">
            <button
               class="tw-transition-colors hover:tw-text-white"
               :class="{ 'tw-text-white': isActive('/') }"
               :aria-current="isActive('/') ? 'page' : undefined"
               @click="router.push('/')">
               Explore
            </button>
            <button
               class="tw-transition-colors hover:tw-text-white"
               :class="{ 'tw-text-white': isActive('/tools') }"
               :aria-current="isActive('/tools') ? 'page' : undefined"
               @click="router.push('/tools')">
               Directory
            </button>
            <button
               class="tw-transition-colors hover:tw-text-white"
               :class="{ 'tw-text-white': isActive('/submit') }"
               :aria-current="isActive('/submit') ? 'page' : undefined"
               @click="goToSubmit">
               Launch
            </button>
            <button
               v-if="auth.user"
               class="tw-transition-colors hover:tw-text-white"
               :class="{ 'tw-text-white': isActive('/my-tools') }"
               :aria-current="isActive('/my-tools') ? 'page' : undefined"
               @click="router.push('/my-tools')">
               Dashboard
            </button>
         </nav>

       
      </div>
   </header>

 

</template>

<style scoped>
   .fade-enter-active,
   .fade-leave-active {
      transition: opacity 0.2s ease;
   }
   .fade-enter-from,
   .fade-leave-to {
      opacity: 0;
   }

   .slide-enter-active,
   .slide-leave-active {
      transition: transform 0.25s ease;
   }
   .slide-enter-from,
   .slide-leave-to {
      transform: translateX(100%);
   }
</style>
