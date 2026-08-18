<script setup lang="ts">
   import { useRoute } from 'vue-router';
   import axios, { all } from 'axios';
   import { ref, onMounted, computed, watchEffect, watch } from 'vue';
   import { useFileStore } from '@/shared/store/fileStore';

   const fileStore = useFileStore();
   const menuItems = [
      {
         name: 'Upload File',
         icon: 'pi-cloud-upload',
         routes: ['/upload-file'],
      },
      {
         name: 'Transform',
         icon: 'pi-folder',
         routes: ['/transform'],
      },
   ];

   const VITE_BACKEND_URL = import.meta.env.VITE_API_URL;
   const allFilesList = ref<File | null>(null);
   const selectedFile = ref<string | null>(null);
   const showFiles = ref(false);

   const getFilesList = async () => {
      try {
         let response = await axios.get(`${VITE_BACKEND_URL}/reads/read-files`);
         allFilesList.value = response?.data?.files;
         console.log('files = ', allFilesList.value);
      } catch (error: any) {
         if (error.response) {
            console.error('Server Error Data:', error.response.data);
            console.error('Server Status:', error.response.status);

            console.log(
               'error -',
               error.response || 'Something went wrong while reading the file.',
            );
         } else {
            console.error('Read failed:', error.message);
         }
      }
   };

   const route = useRoute();
   const isActive = (item: (typeof menuItems)[number]) => {
      return item.routes.some((path) => route.path.startsWith(path));
   };
   const isTransformActive = computed(() => {
      return route.path === '/transform';
   });

   const selectFile = (fileName: string) => {
      selectedFile.value = fileName;
      fileStore.currentFileName = fileName;
      console.log('selected-file', typeof(selectedFile.value))
   };

   const getSelectedFilePreview = async() => {
      try {
         let response = await axios.get(`${VITE_BACKEND_URL}/reads/file-preview/${selectedFile.value}`);
         fileStore.currentFile = response?.data
         console.log('res - ',response?.data)
         fileStore.currentFileName = selectedFile.value
      } catch (error: any) {
         if (error.response) {
            console.error('Server Error Data:', error.response.data);
            console.error('Server Status:', error.response.status);

            console.log(
               'error -',
               error.response || 'Something went wrong while reading preview of the file.',
            );
         } else {
            console.error('Preview Read failed:', error.message);
         }
      }
   }

   watch(selectedFile, async() => {
      await getSelectedFilePreview();
   })

   onMounted(async () => {
      await getFilesList();
   });
</script>
<template>
   <div class="tw-flex tw-w-full tw-max-w-64 tw-flex-col tw-p-2">
      <div class="tw-flex tw-items-center tw-justify-center tw-border-b-[1px]">
         <!-- <img class="tw-w-40 tw-p-1" src="/images/logo.png" alt=""> -->
         <span class="tw-pb-2 tw-text-2xl tw-font-bold tw-text-blue-600">
            Data-Platform
         </span>
      </div>   
      <div
         class="tw-flex tw-flex-col tw-gap-2 tw-border-b-[1px] tw-py-3 tw-text-sm tw-text-blue-600">
         <div
            v-for="(menuItem, index) in menuItems"
            :key="index"
            class="tw-flex tw-flex-col tw-justify-center"
            @click="$router.push(menuItem.routes[0])">
            <div
               :class="[
                  'tw-flex tw-cursor-pointer tw-justify-between tw-rounded-md tw-px-4 tw-py-2 tw-transition-colors tw-duration-300 hover:tw-bg-blue-100',
                  isActive(menuItem)
                     ? 'tw-bg-blue-600 tw-text-white hover:tw-bg-blue-600'
                     : '',
               ]">
               <div class="tw-flex tw-items-center tw-gap-2">
                  <i
                     :class="[
                        menuItem.icon,
                        'pi tw-text-sm tw-transition-colors tw-duration-300',
                        isActive(menuItem)
                           ? 'tw-text-white'
                           : 'tw-text-blue-600',
                     ]"></i>
                  <span class="tw-font-semibold">
                     {{ menuItem.name }}
                  </span>
               </div>
               <div>
                  <i
                     v-if="menuItem.name === 'Transform'"
                     :class="[
                        menuItem.icon,
                        'pi tw-text-sm tw-transition-colors tw-duration-300',
                        isActive(menuItem)
                           ? 'pi-angle-down tw-text-white'
                           : 'pi-angle-right tw-text-blue-600',
                     ]"></i>
               </div>
            </div>
            <div
              
               v-if="
                  allFilesList &&
                  isTransformActive &&
                  menuItem.name === 'Transform'
               "
               v-for="(file, index) in allFilesList"
                
               :class="['flex tw-my-1 tw-cursor-pointer tw-flex-col tw-rounded-md  tw-py-2 tw-transition-colors tw-duration-300 hover:tw-bg-blue-100', selectedFile == file ? 'tw-bg-blue-200' : 'tw-bg-blue-50']">
               <div @click="selectFile(file)" class="tw-flex tw-items-center tw-gap-2 tw-pl-3">
                
                  <i
                     class="pi pi-arrow-right tw-pt-1 tw-text-[10px] tw-font-light"></i>
                  <span>
                     {{ file }}
                  </span>
               </div>
            </div>
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
