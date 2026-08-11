<script setup lang="ts">
   import { ref } from 'vue';

   const props = defineProps<{
      modalOpen: boolean;
   }>();

   const emit = defineEmits(['update:modalOpen', 'create']);

   const name = ref('');
   const description = ref('');

   const projectNameLimit = 30;
   const projectDescriptionLimit = 50;

   const close = () => {
      emit('update:modalOpen', false);
   };

   const createProject = () => {
      emit('create', {
         name: name.value,
         description: description.value,
      });

      close();

      name.value = '';
      description.value = '';
   };
</script>

<template>

      <div
         v-if="props.modalOpen"
         class="tw-fixed tw-inset-0 tw-z-50 tw-flex tw-items-center tw-justify-center tw-bg-black/60 tw-backdrop-blur-sm">
         <div class="project-modal tw-w-[420px] tw-rounded-2xl tw-p-6">
            <!-- Header -->
            <div class="tw-mb-6">
               <h2 class="tw-text-2xl tw-font-bold tw-text-white">
                  Create New Project
               </h2>

               <p class="tw-mt-1 tw-text-sm tw-text-pulse-grayText">
                  Organize and monitor your APIs beautifully.
               </p>
            </div>

            <!-- Project Name -->
            <div class="tw-mb-5">
               <FloatLabel variant="in">
                  <InputText
                     id="projectName"
                     v-model="name"
                     :maxlength="projectNameLimit"
                     autocomplete="off"
                     class="tw-w-full tw-bg-transparent tw-text-gray-200" />

                  <label for="projectName">Project Name</label>
               </FloatLabel>

               <div
                  class="tw-mt-1 tw-text-right tw-text-xs tw-text-pulse-grayText">
                  {{ name.length }}/{{ projectNameLimit }}
               </div>
            </div>

            <!-- Description -->
            <div class="tw-mb-6">
               <FloatLabel variant="in">
                  <Textarea
                     id="projectDescription"
                     v-model="description"
                     rows="4"
                     :maxlength="projectDescriptionLimit"
                     autocomplete="off"
                     class="tw-w-full tw-resize-none tw-bg-transparent tw-text-gray-200" />

                  <label for="projectDescription">
                     Project Description (optional)
                  </label>
               </FloatLabel>

               <div
                  class="tw-mt-1 tw-text-right tw-text-xs tw-text-pulse-grayText">
                  {{ description.length }}/{{ projectDescriptionLimit }}
               </div>
            </div>
            <!-- Actions -->
            <div class="tw-flex tw-justify-end tw-gap-3">
               <button
                  @click="close"
                  class="tw-rounded-xl tw-border tw-border-pulse-border tw-bg-white/5 tw-px-5 tw-py-2.5 tw-text-sm tw-font-medium tw-text-gray-300 tw-transition-all hover:tw-border-gray-500 hover:tw-bg-white/10 hover:tw-text-white">
                  Cancel
               </button>

               <button
                  @click="createProject"
                  class="tw-rounded-xl tw-border tw-border-cyan-400/40 tw-bg-cyan-400/10 tw-px-5 tw-py-2.5 tw-text-sm tw-font-semibold tw-text-cyan-300 tw-transition-all hover:tw-border-cyan-300 hover:tw-bg-cyan-400/20 hover:tw-shadow-[0_0_20px_rgba(34,211,238,0.25)]">
                  Create Project
               </button>
            </div>
         </div>
      </div>
  
</template>

<style scoped>
   /* Modal Card */
   :deep(.project-modal) {
      background: linear-gradient(
         180deg,
         rgba(14, 21, 33, 0.98) 0%,
         rgba(4, 7, 16, 0.98) 100%
      );

      border: 1px solid rgba(34, 211, 238, 0.15);

      box-shadow:
         0 0 0 1px rgba(34, 211, 238, 0.05),
         0 0 30px rgba(34, 211, 238, 0.08),
         0 0 80px rgba(213, 252, 91, 0.04);

      backdrop-filter: blur(12px);
   }

   /* Input + Textarea */
   :deep(.p-inputtext),
   :deep(.p-textarea) {
      width: 100%;
      background: rgba(255, 255, 255, 0.02) !important;

      border: 1px solid #1f2937 !important;

      color: #e5e7eb !important;

      border-radius: 12px;

      transition:
         all 0.25s ease,
         box-shadow 0.25s ease;

      padding: 0.9rem 1rem;
   }

   /* Placeholder */
   :deep(.p-inputtext::placeholder),
   :deep(.p-textarea::placeholder) {
      color: #6b7280;
   }

   /* Hover */
   :deep(.p-inputtext:hover),
   :deep(.p-textarea:hover) {
      border-color: rgba(34, 211, 238, 0.35) !important;
   }

   /* Focus */
   :deep(.p-inputtext:focus),
   :deep(.p-textarea:focus) {
      border-color: #22d3ee !important;

      box-shadow:
         0 0 0 1px rgba(34, 211, 238, 0.6),
         0 0 15px rgba(34, 211, 238, 0.18) !important;

      background: rgba(255, 255, 255, 0.03) !important;
   }

   /* Filled */
   :deep(.p-inputtext.p-filled),
   :deep(.p-textarea.p-filled) {
      border-color: rgba(34, 211, 238, 0.5) !important;
   }

   /* Float Label */
   :deep(.p-floatlabel label) {
      color: #9ca3af !important;
      transition: all 0.2s ease;
   }

   /* Focus Label */
   :deep(.p-floatlabel:has(.p-inputtext:focus) label),
   :deep(.p-floatlabel:has(.p-textarea:focus) label) {
      color: #22d3ee !important;
   }

   /* Filled Label */
   :deep(.p-floatlabel:has(.p-filled) label) {
      color: #67e8f9 !important;
   }

   /* Remove resize */
   :deep(.p-textarea) {
      resize: none;
   }

   /* Animation */
   .fade-enter-active,
   .fade-leave-active {
      transition: opacity 0.2s ease;
   }

   .fade-enter-from,
   .fade-leave-to {
      opacity: 0;
   }
</style>
