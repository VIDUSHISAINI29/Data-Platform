<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import ProgressSpinner from "primevue/progressspinner";

const waitInSeconds = ref(0);

onMounted(() => {
   const interval = setInterval(() => {
      waitInSeconds.value += 1;
   }, 1000);

   onUnmounted(() => {
      clearInterval(interval);
   });
});
</script>

<template>
   <div
      class="card tw-full tw-relative tw-flex tw-items-center tw-justify-center">
      <!-- Progress Spinner -->
      <ProgressSpinner
         style="width: 100px; height: 100px"
         strokeWidth="3"
         fill="transparent"
         animationDuration=".5s"
         aria-label="Custom ProgressSpinner" />
      <!-- Centered Seconds -->
      <!-- <div class="tw-text-md tw-absolute tw-font-bold">
         {{ waitInSeconds }}s
      </div> -->
   </div>
</template>

<style scoped>
:deep(.p-progressspinner-circle) {
   stroke: #22D3EE !important;
   filter: drop-shadow(0 0 6px rgba(6,182,212,0.6));
}
</style>
