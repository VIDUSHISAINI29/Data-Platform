<script setup lang="ts">
import { watchEffect, ref } from 'vue';

const selectedFile = ref<File | null>(null);
const handleFileUpload = (event: any) => {
    const ifFiles = event.target.files
    if(ifFiles && ifFiles.length > 0){
        selectedFile.value = ifFiles[0]
    }
}

const uploadFile = async() => {

    if(!selectedFile.value) return;

    const formData = new FormData();

    formData.append('file', selectedFile.value)

}

</script>

<template>
    <div class="tw-flex tw-flex-col tw-gap-4 tw-p-4">
       <div>
        <input class="tw-cursor-pointer" type="file" accept=".csv, .parquet, .xls, xlsx" @change="handleFileUpload" />
       </div>
       <div>
        <button class="tw-bg-blue-700 tw-cursor-pointer tw-text-white tw-px-4 tw-py-2 tw-rounded-md">Upload File</button>
       </div>
    </div>
</template>