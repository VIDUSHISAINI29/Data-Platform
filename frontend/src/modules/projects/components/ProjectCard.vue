<script setup lang="ts">
   const props = defineProps<{
      mainText: string;
      subText: number | string;
      gradientFrom: string;
      // shadow: string;
      status: string;
      statusBg: string;
      statusText: string;
      endpointsCount: number;
      uptimePercentage: number;
      incidentsCount: number;
      timeOfCreation: string;
   }>();
   
</script>

<template>
   <div
      :class="[
         'tw-w-[300px] tw-cursor-pointer tw-rounded-xl tw-bg-gradient-to-br tw-via-pulse-border tw-to-pulse-border tw-p-[1px] 2xl:tw-w-[350px]',
         // props.shadow,
         props.gradientFrom,
      ]">
      <div class="tw-w-full tw-rounded-xl tw-bg-pulse-bg tw-p-5">
         <div class="tw-flex tw-w-full tw-flex-col tw-gap-5">
            <div class="tw-flex tw-items-center tw-justify-between">
               <div>
                  <div class="tw-text-lg tw-line-clamp-1 tw-break-all tw-text-white">
                     <span>{{ props.mainText }}</span>
                  </div>
                  <div class="tw-text-[12px] tw-line-clamp-1 tw-break-all tw-text-pulse-grayText">
                     <span>{{ props.subText }}</span>
                  </div>
               </div>
               <div>
                  <span
                     :class="[
                        'tw-rounded-full tw-px-2 tw-py-1 tw-text-[10px]',
                        props.statusBg,
                        props.statusText,
                     ]">
                     {{ props.status }}
                  </span>
               </div>
            </div>
            <div class="tw-flex tw-justify-between tw-text-white">
               <div
                  class="tw-flex tw-flex-col tw-items-center tw-justify-center">
                  <div class="tw-text-pulse-grayText">
                     <span class="tw-text-sm tw-text-white">
                        {{ props.endpointsCount }}
                     </span>
                  </div>
                  <div class="tw-text-[12px] tw-text-pulse-grayText">
                     <span>Endpoints</span>
                  </div>
               </div>
               <div
                  class="tw-flex tw-flex-col tw-items-center tw-justify-center">
                  <div class="tw-text-pulse-grayText">
                     <span class="tw-text-sm tw-text-white">
                        {{ props.uptimePercentage }}%
                     </span>
                  </div>
                  <div class="tw-text-[12px] tw-text-pulse-grayText">
                     <span>Uptime</span>
                  </div>
               </div>
               <div
                  class="tw-flex tw-flex-col tw-items-center tw-justify-center">
                  <div class="tw-text-pulse-grayText">
                     <span class="tw-text-sm tw-text-white">
                        {{ props.incidentsCount }}
                     </span>
                  </div>
                  <div class="tw-text-[12px] tw-text-pulse-grayText">
                     <span>Incidents</span>
                  </div>
               </div>
            </div>

            <div class="tw-w-full">
               <div class="tw-h-[1px] tw-bg-gray-800"></div>
               <div class="tw-flex tw-items-center tw-justify-between tw-mt-1">
                  <div>
                     <span class="tw-text-[10px] tw-text-pulse-grayText">
                        Created {{ props.timeOfCreation }} 
                     </span>
                  </div>
                  <div>
                     <i class="pi pi-ellipsis-h tw-text-sm tw-mt-3 tw-text-pulse-grayText"></i>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<style scoped></style>
