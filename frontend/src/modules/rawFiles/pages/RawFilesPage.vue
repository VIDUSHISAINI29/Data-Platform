<script setup lang="ts">
   import { ref, onMounted, computed } from 'vue';
   import { getRawFilesList } from '../api/rawFiles.api';
   import { useFileStore } from '@/shared/store/fileStore';
   import axios from 'axios';

   const VITE_BACKEND_URL = import.meta.env.VITE_API_URL;
   const fileStore = useFileStore();
   const query = ref(`
      SELECT *
      FROM data
      LIMIT 2
   `);
   const loadingQueryResult = ref(false);
   const errorOfQuery = ref('');
   const rows = computed(() => {
      return fileStore.currentFile?.data ?? [];
   });
   const columns = computed(() => {
      return fileStore.currentFile?.columns ?? [];
   });


   const getSelectedFilePreview = async () => {
      try {
         let response = await axios.get(
            `${VITE_BACKEND_URL}/reads/file-preview/${fileStore.currentFileName}`,
         );
         fileStore.currentFile = response?.data;
         console.log('current file data - ', response?.data);
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

   

   const queryResult = ref<{
      columns: string[];
      data: Record<string, any>[];
   } | null>(null);

   const runQuery = async () => {
      if (!query.value.trim()) {
         return;
      }

      loadingQueryResult.value = true;
      errorOfQuery.value = '';

      try {
         const response = await axios.post(
            `${VITE_BACKEND_URL}/query/query-file`,
            {
               file_name: fileStore.currentFileName,
               query: query.value,
            },
         );

         queryResult.value = response.data;
         fileStore.currentFile = queryResult.value?.result;
         console.log('query result - ', queryResult.value);
         // await getSelectedFilePreview();
      } catch (err: any) {
         errorOfQuery.value = err.response?.data?.detail || 'Failed to execute query';
      } finally {
         loadingQueryResult.value = false;
      }
   };

   const getRawFilesListFunction = async () => {
      try {
         let res = await getRawFilesList();
         fileStore.rawFilesList = res?.files;
         console.log('files raw list - ', res?.files);
      } catch (error: any) {
         if (error.response) {
            console.error('Server Error Data:', error.response.data);
            console.error('Server Status:', error.response.status);

            console.log(
               'error -',
               error.response ||
                  'Something went wrong while reading the raw files list.',
            );
         } else {
            console.error('Read failed:', error.message);
         }
      }
   };

   onMounted(async () => {
      console.log('row - ', fileStore.currentFile);
      console.log('col - ', columns);
      await getRawFilesListFunction();
   });
</script>

<template>
   <div class="tw-m-1 tw-flex tw-flex-col tw-gap-2 tw-p-2">
      <div>
         <!-- SQL Editor -->
         <div class="tw-flex tw-flex-col tw-gap-2">
            <div class="tw-flex tw-items-center tw-justify-between">
               <span class="tw-font-semibold">SQL Query</span>

              <div class="tw-flex tw-gap-2">
                <Button
                  label="Run Query"
                  icon="pi pi-play"
                  class="tw-border-blue-600 tw-bg-blue-600"
                  :loading="loadingQueryResult"
                  @click="runQuery" />

                <Button
                  label="Transform File"
                  icon="pi pi-bolt"
                  class="tw-border-blue-200 tw-text-blue-600 tw-bg-blue-200 "
                  :loading="loadingQueryResult"
                  @click="runQuery" />
              </div>
            </div>

            <textarea
               v-model="query"
               class="tw-min-h-[220px] tw-w-full tw-rounded-lg tw-border tw-p-4 tw-font-mono tw-text-sm"
               placeholder="Write your SQL query..."
               spellcheck="false" />
         </div>

         <!-- Error -->
         <Message v-if="errorOfQuery" severity="error">
            {{ errorOfQuery }}
         </Message>

         <!-- Result -->
         <div v-if="0" class="tw-overflow-x-auto"></div>
         <div>
            <div class="w-full">
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
