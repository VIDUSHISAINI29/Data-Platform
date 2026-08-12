<script setup lang="ts">
import { watchEffect, ref } from 'vue';
import axios from 'axios'

const selectedFile = ref<File | null>(null);
const handleFileUpload = (event: any) => {
    const ifFiles = event.target.files
    if(ifFiles && ifFiles.length > 0){
        selectedFile.value = ifFiles[0]
    }
}

const uploadFile = async () => {
  if (!selectedFile.value) return;

  const formData = new FormData();
  // 'file' must match the parameter name expected by your FastAPI endpoint
  formData.append('file', selectedFile.value);

 try {
  const response = await axios.post('http://127.0.0.1:8000/api/v1/uploads/upload-file', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  console.log('Upload success:', response.data);
} catch (error: any) {
  // This will print the actual validation or server error payload from FastAPI
  if (error.response) {
    console.error('Server Error Data:', error.response.data);
    console.error('Server Status:', error.response.status);
  } else {
    console.error('Upload failed:', error.message);
  }
}
};

</script>

<template>
    <div class="tw-flex tw-flex-col tw-gap-4 tw-p-4">
       <div>
        <input class="tw-cursor-pointer" type="file" accept=".csv, .parquet, .xls, xlsx" @change="handleFileUpload" />
       </div>
       <div>
        <button @click="uploadFile" class="tw-bg-blue-700 tw-cursor-pointer tw-text-white tw-px-4 tw-py-2 tw-rounded-md">Upload File</button>
       </div>
    </div>
</template>