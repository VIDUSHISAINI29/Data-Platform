<script setup lang="ts">
   import { useRouter } from 'vue-router';

   const router = useRouter();

</script>

<template>
   <div
      class="tw-flex tw-min-h-screen tw-flex-col tw-items-center tw-justify-center tw-bg-neutral-950 tw-px-6 tw-text-center">
      <!-- Subtle glow -->
      <div
         class="tw-pointer-events-none tw-absolute tw-h-[400px] tw-w-[600px] tw-rounded-full tw-bg-gradient-to-r tw-from-green-500/5 tw-via-emerald-400/5 tw-to-green-500/5 tw-blur-[100px]" />

      <div class="tw-relative tw-flex tw-flex-col tw-items-center tw-gap-6">
         <!-- Big 404 -->
         <h1
            class="tw-select-none tw-text-[9rem] tw-font-black tw-leading-none tw-tracking-tighter tw-text-neutral-800 md:tw-text-[12rem]">
            404
         </h1>

         <!-- Icon -->
         <div
            class="tw-flex tw-h-16 tw-w-16 tw-items-center tw-justify-center tw-rounded-2xl tw-border tw-border-neutral-800 tw-bg-neutral-900 tw-text-3xl">
            🔭
         </div>

         <div class="tw-flex tw-flex-col tw-gap-2">
            <h2 class="tw-text-2xl tw-font-bold tw-text-white">
               Lost in space
            </h2>
            <p class="tw-max-w-sm tw-text-neutral-500">
               This page doesn't exist or has been moved. Let's get you back to
               the launchpad.
            </p>
         </div>

         <div class="tw-flex tw-flex-col tw-gap-3 sm:tw-flex-row">
            <Button
               label="Back to Home"
               icon="pi pi-home"
               severity="success"
               raised
               class="tw-rounded-xl tw-bg-brandGreen tw-px-8"
               @click="router.push('/')" />
            <Button
               label="Explore Directory"
               icon="pi pi-compass"
               severity="secondary"
               outlined
               class="tw-rounded-xl tw-px-8"
               @click="router.push('/tools')" />
         </div>
      </div>
   </div>
</template>
