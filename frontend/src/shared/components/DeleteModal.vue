<script setup lang="ts">
   const props = defineProps<{
      modalOpen: boolean;
      deleteObjectName: string;
   }>();

   const emit = defineEmits(['delete:modalOpen', 'confirm']);

   const close = () => {
      emit('delete:modalOpen', false);
   };

   const confirmDelete = () => {
      emit('confirm');
      close();
   };
</script>

<template>
   <transition name="fade">
      <div
         v-if="modalOpen"
         class="tw-fixed tw-inset-0 tw-z-50 tw-flex tw-items-center tw-justify-center tw-bg-black/60 tw-backdrop-blur-sm">
         <div
            class="tw-w-[420px] tw-rounded-2xl tw-border tw-border-red-500/20 tw-bg-[#070b14] tw-p-6 tw-shadow-[0_0_40px_rgba(239,68,68,0.15)]">
            <!-- Icon -->
            <div
               class="tw-mb-5 tw-flex tw-h-14 tw-w-14 tw-items-center tw-justify-center tw-rounded-full tw-bg-red-500/10">
               <i class="pi pi-trash tw-text-2xl tw-text-red-400"></i>
            </div>

            <!-- Heading -->
            <div class="tw-flex tw-flex-col tw-gap-2">
               <h2 class="tw-text-2xl tw-font-bold tw-text-white">
                  Delete {{ deleteObjectName }}
               </h2>

               <p class="tw-text-sm tw-leading-6 tw-text-pulse-grayText">
                  Are you sure you want to delete
                  <span class="tw-font-semibold tw-text-white">
                     {{ deleteObjectName }}
                  </span>
                  ?

                  <br />
                  <br />

                  This action cannot be undone. All the data will be permanently
                  deleted.
               </p>
            </div>

            <!-- Actions -->
            <div class="tw-mt-8 tw-flex tw-justify-end tw-gap-3">
               <button
                  @click="close"
                  class="tw-rounded-xl tw-border tw-border-pulse-border tw-bg-white/5 tw-px-5 tw-py-2.5 tw-text-sm tw-font-medium tw-text-gray-300 tw-transition-all hover:tw-bg-white/10">
                  Cancel
               </button>

               <button
                  @click="confirmDelete"
                  class="tw-rounded-xl tw-border tw-border-red-500/30 tw-bg-red-500/10 tw-px-5 tw-py-2.5 tw-text-sm tw-font-semibold tw-text-red-400 tw-transition-all hover:tw-bg-red-500/20 hover:tw-shadow-[0_0_20px_rgba(239,68,68,0.25)]">
                  Delete 
               </button>
            </div>
         </div>
      </div>
   </transition>
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
</style>
