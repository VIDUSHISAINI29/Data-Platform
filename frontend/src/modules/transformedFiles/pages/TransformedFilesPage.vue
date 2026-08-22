<script setup lang="ts">
   import { ref, onMounted, computed } from 'vue';
   import { useFileStore } from '@/shared/store/fileStore';
   import {
      getTransformedFilesList,
      queryTransformedFile,
   } from '../api/transformedFiles.api';
   import axios from 'axios';

   const VITE_BACKEND_URL = import.meta.env.VITE_API_URL;
   const fileStore = useFileStore();
   const rows = computed(() => {
      return fileStore.currentFile?.data ?? [];
   });
   const columns = computed(() => {
      return fileStore.currentFile?.columns ?? [];
   });

   const getSelectedFilePreview = async () => {
      try {
         let response = await axios.get(
            `${VITE_BACKEND_URL}/reads/transformed-file-preview/${fileStore.currentFileName}`,
         );
         fileStore.currentFile = response?.data;
         console.log('res - ', response?.data);
      } catch (error: any) {
         if (error.response) {
            console.error('Server Error Data:', error.response.data);
            console.error('Server Status:', error.response.status);

            console.log(
               'error -',
               error.response ||
                  'Something went wrong while reading preview of the file.',
            );
         } else {
            console.error('Preview Read failed:', error.message);
         }
      }
   };

   const query = ref(`
SELECT *
FROM data
LIMIT 2
`);

   const loading = ref(false);
   const error = ref('');

   const queryResult = ref<{
      columns: string[];
      data: Record<string, any>[];
   } | null>(null);

   const runQuery = async () => {
      if (!query.value.trim()) {
         return;
      }

      loading.value = true;
      error.value = '';

      try {
         const response = await queryTransformedFile({
            file_name: fileStore.currentFileName,
            query: query.value,
         });

         queryResult.value = response.result;
         fileStore.currentFile = queryResult.value;
         console.log('query result - ', response.result);
         //  await getSelectedFilePreview()
      } catch (err: any) {
         error.value = err.response?.data?.detail || 'Failed to execute query';
         console.log('err in querying raw file - ', err);
      } finally {
         loading.value = false;
      }
   };

   const getTransformedFilesListFunction = async () => {
      try {
         let res = await getTransformedFilesList();
         fileStore.transformedFilesList = res?.files;
         console.log('files transformed list - ', res?.files);
      } catch (error: any) {
         if (error.response) {
            console.error('Server Error Data:', error.response.data);
            console.error('Server Status:', error.response.status);
            console.error('Server Status:', error.response.status);

            console.log(
               'error -',
               error.response ||
                  'Something went wrong while reading the raw files list.',
            );
         } else {
            console.error('Read failed:', error);
         }
      }
   };

   onMounted(async () => {
      await getTransformedFilesListFunction();
      console.log('row - ', fileStore.currentFile);
      console.log('col - ', columns);
   });
</script>

<template>
   <div class="tw-m-1 tw-flex tw-flex-col tw-gap-2 tw-p-2">
      <div>
         <!-- SQL Editor -->
         <div class="tw-flex tw-flex-col tw-gap-2">
            <div class="tw-flex tw-items-center tw-justify-between">
               <span class="tw-font-semibold">SQL Query</span>

               <Button
                  label="Run Query"
                  icon="pi pi-play"
                  class="tw-border-blue-600 tw-bg-blue-600"
                  :loading="loading"
                  @click="runQuery" />
            </div>

            <textarea
               v-model="query"
               class="tw-min-h-[220px] tw-w-full tw-rounded-lg tw-border tw-p-4 tw-font-mono tw-text-sm"
               placeholder="Write your SQL query..."
               spellcheck="false" />
         </div>

         <!-- Error -->
         <Message v-if="error" severity="error">
            {{ error }}
         </Message>

         <!-- Result -->
         <div v-if="queryResult" class="tw-overflow-x-auto">
            <span class="tw-mt-6 tw-px-1 tw-text-lg tw-font-semibold ">
               {{ fileStore.currentFileName }}
            </span>
         </div>
         <div>
            <div v-if="rows" class="w-full">
               <DataTable
                  :value="rows"
                  paginator
                  :rows="5"
                  tableStyle="min-width: 50rem">
                  <Column
                     v-for="(col, index) in columns"
                     :field="col"
                     :header="col" />
               </DataTable>
            </div>
         </div>
      </div>
   </div>
</template>

<style scoped></style>
