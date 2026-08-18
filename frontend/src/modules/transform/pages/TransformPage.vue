<script setup lang="ts">
   import { ref, onMounted, computed } from 'vue';
   import { useFileStore } from '@/shared/store/fileStore';

   const fileStore = useFileStore();
 const rows = computed(() => {
  return fileStore.currentFile?.data ?? []
})
  const columns = computed(() => {
  return fileStore.currentFile?.columns ?? []
})

   onMounted(() => {
    console.log('row - ',fileStore.currentFile)
    console.log('col - ',columns)
   })

</script>

<template>
   <div class="tw-m-1 tw-flex tw-flex-col tw-gap-2 tw-p-2">
      <div>Transform</div>
      <div>
            <div class="w-full">
               <DataTable  :value="rows" paginator :rows="5" tableStyle="min-width: 50rem">
                  <Column v-for="(col, index) in columns" :field="col" :header="col" />
               </DataTable>
            </div>
      </div>
   </div>
</template>

<style scoped></style>
