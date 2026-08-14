<script setup lang="ts">
import { useRoute } from 'vue-router';

const menuItems = [
    {
        name: 'Upload File',
        icon: 'pi-cloud-upload',
        routes: ['/upload-file'],
    },
    {
        name: 'Transform',
        icon: 'pi-folder',
        routes: ['/projects', '/project/'],
    },
];

const route = useRoute();
const isActive = (item: typeof menuItems[number]) => {
    return item.routes.some(path => route.path.startsWith(path));
};
</script>
<template>
<div class=" tw-w-full tw-flex tw-p-2 tw-flex-col tw-max-w-52">
    <div class=" tw-border-b-[1px] tw-flex tw-justify-center tw-items-center">
        <!-- <img class="tw-w-40 tw-p-1" src="/images/logo.png" alt=""> -->
         <span class="tw-text-blue-600 tw-text-2xl tw-pb-2 tw-font-bold">Data-Platform</span>
    </div>
    <div class="tw-flex tw-flex-col tw-py-3 tw-text-blue-600  tw-border-b-[1px] tw-text-sm tw-gap-2">
       <div
  v-for="(menuItem, index) in menuItems"
  :key="index"
  :class="[
    'tw-py-2 tw-px-4 tw-transition-colors hover:tw-bg-blue-100 tw-duration-300 tw-cursor-pointer tw-rounded-md tw-flex tw-items-center tw-gap-2',
    isActive(menuItem)
      ? 'tw-bg-blue-600 tw-text-white'
      : ''
  ]"
  @click="$router.push(menuItem.routes[0])"
>
  <i
    :class="[
      menuItem.icon,
      'pi tw-text-sm tw-duration-300 tw-transition-colors',
      isActive(menuItem) ? 'tw-text-white' : ' tw-text-blue-600'
    ]"
  ></i>

  <span class="tw-font-semibold">
    {{ menuItem.name }}
  </span>
</div>
    </div>
    <!-- <div class="tw-flex tw-flex-col tw-py-4 tw-text-gray-300 tw-border-b-[1px] tw-text-sm tw-gap-2">
        <div class="">
            <span class="tw-text-[12px] tw-text-gray-300">Recent Projects</span>
        </div>

        <div class="tw-bg-gradient-to-r tw-from-pulse-cyan  tw-to-pulse-lime tw-p-[1px] tw-rounded-md" v-for="(project, index) in projects" :key="index">
            <div  class="tw-p-2 tw-bg-pulse-bg tw-w-full tw-cursor-pointer tw-rounded-md tw-flex tw-items-center tw-justify-center tw-gap-2 ">
              
                <span class="tw-text-gray-300 tw-text-sm tw-font-semibold">{{ project.name }}</span>
            </div>
        </div>

        <div class="tw-bg-gradient-to-r tw-from-pulse-cyan  tw-to-pulse-lime tw-p-[1px] tw-rounded-md">
            <div  class="tw-p-1 tw-bg-pulse-bg tw-cursor-pointer tw-rounded-md tw-flex tw-items-center tw-justify-center tw-gap-1 ">
                <span class="tw-text-pulse-cyan tw-text-2xl tw-mb-[4px] tw-text-center tw-rounded-md">+</span>
                <span class="tw-text-pulse-cyan tw-text-sm tw-font-semibold">View All Projects</span>
            </div>
        </div>

     
    </div> -->
</div>

</template>