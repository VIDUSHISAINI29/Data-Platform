<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const selectedFile = ref<File | null>(null);

const handleFileUpload = (event: any) => {
  const ifFiles = event.target.files;

  if (ifFiles && ifFiles.length > 0) {
    selectedFile.value = ifFiles[0];
  }
};

const uploadFile = async () => {
  if (!selectedFile.value) return;

  const formData = new FormData();
  formData.append('file', selectedFile.value);

  try {
    const response = await axios.post(
      'http://127.0.0.1:8000/api/v1/uploads/upload-file',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    console.log('Upload success:', response.data);
  } catch (error: any) {
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
  <div
    class="tw-min-h-screen tw-bg-slate-50 tw-flex tw-items-center tw-justify-center tw-p-6"
  >
    <div class="tw-w-full tw-max-w-2xl">

      <!-- Header -->
      <div class="tw-text-center tw-mb-8">
        <div
          class="tw-mx-auto tw-mb-4 tw-w-14 tw-h-14 tw-rounded-2xl
                 tw-bg-blue-600 tw-flex tw-items-center tw-justify-center
                 tw-shadow-lg tw-shadow-blue-600/20"
        >
          <svg
            class="tw-w-7 tw-h-7 tw-text-white"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.8"
              d="M12 16V4m0 0L8 8m4-4 4 4M4 16.5v1A2.5 2.5 0 006.5 20h11a2.5 2.5 0 002.5-2.5v-1"
            />
          </svg>
        </div>

        <h1
          class="tw-text-3xl tw-font-bold tw-text-slate-900 tw-tracking-tight"
        >
          Upload your data
        </h1>

        <p class="tw-mt-2 tw-text-slate-500 tw-text-sm">
          Upload a file to get started with your data
        </p>
      </div>

      <!-- Upload Card -->
      <div
        class="tw-bg-white tw-rounded-2xl tw-border tw-border-slate-200
               tw-shadow-xl tw-shadow-slate-200/50 tw-p-6 sm:tw-p-8"
      >

        <!-- Upload Area -->
        <label
          class="tw-relative tw-flex tw-flex-col tw-items-center
                 tw-justify-center tw-w-full tw-min-h-[260px]
                 tw-rounded-xl tw-border-2 tw-border-dashed
                 tw-border-slate-300 tw-bg-slate-50
                 hover:tw-border-blue-400 hover:tw-bg-blue-50/40
                 tw-transition-all tw-duration-200 tw-cursor-pointer"
        >
          <input
            type="file"
            accept=".csv,.parquet,.xls,.xlsx"
            class="tw-hidden"
            @change="handleFileUpload"
          />

          <!-- Upload Icon -->
          <div
            class="tw-w-16 tw-h-16 tw-rounded-full
                   tw-bg-blue-100 tw-flex tw-items-center
                   tw-justify-center tw-mb-5"
          >
            <svg
              class="tw-w-8 tw-h-8 tw-text-blue-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.8"
                d="M12 16V4m0 0L8 8m4-4 4 4M4 16.5v1A2.5 2.5 0 006.5 20h11a2.5 2.5 0 002.5-2.5v-1"
              />
            </svg>
          </div>

          <p class="tw-text-base tw-font-semibold tw-text-slate-800">
            Choose a file to upload
          </p>

          <p class="tw-mt-1 tw-text-sm tw-text-slate-500">
            Click here to browse your files
          </p>

          <div
            class="tw-mt-5 tw-flex tw-items-center tw-gap-2
                   tw-text-xs tw-text-slate-400"
          >
            <span
              class="tw-px-2.5 tw-py-1 tw-rounded-md tw-bg-white
                     tw-border tw-border-slate-200"
            >
              CSV
            </span>

            <span
              class="tw-px-2.5 tw-py-1 tw-rounded-md tw-bg-white
                     tw-border tw-border-slate-200"
            >
              Parquet
            </span>

            <span
              class="tw-px-2.5 tw-py-1 tw-rounded-md tw-bg-white
                     tw-border tw-border-slate-200"
            >
              XLS
            </span>

            <span
              class="tw-px-2.5 tw-py-1 tw-rounded-md tw-bg-white
                     tw-border tw-border-slate-200"
            >
              XLSX
            </span>
          </div>
        </label>

        <!-- Selected File -->
        <div
          v-if="selectedFile"
          class="tw-mt-5 tw-flex tw-items-center tw-justify-between
                 tw-gap-4 tw-p-4 tw-rounded-xl tw-bg-blue-50
                 tw-border tw-border-blue-100"
        >
          <div class="tw-flex tw-items-center tw-gap-3 tw-min-w-0">
            <div
              class="tw-w-10 tw-h-10 tw-shrink-0 tw-rounded-lg
                     tw-bg-blue-100 tw-flex tw-items-center
                     tw-justify-center"
            >
              <svg
                class="tw-w-5 tw-h-5 tw-text-blue-600"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.8"
                  d="M7 3h7l5 5v13H7a2 2 0 01-2-2V5a2 2 0 012-2z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="1.8"
                  d="M14 3v6h6"
                />
              </svg>
            </div>

            <div class="tw-min-w-0">
              <p
                class="tw-text-sm tw-font-semibold tw-text-slate-800
                       tw-truncate"
              >
                {{ selectedFile.name }}
              </p>

              <p class="tw-text-xs tw-text-slate-500 tw-mt-0.5">
                {{ (selectedFile.size / 1024 / 1024).toFixed(2) }} MB
              </p>
            </div>
          </div>

          <span
            class="tw-shrink-0 tw-text-xs tw-font-medium
                   tw-text-green-600 tw-bg-green-50
                   tw-px-2.5 tw-py-1 tw-rounded-full"
          >
            Ready
          </span>
        </div>

        <!-- Upload Button -->
        <button
          @click="uploadFile"
          :disabled="!selectedFile"
          class="tw-mt-6 tw-w-full tw-flex tw-items-center
                 tw-justify-center tw-gap-2 tw-py-3.5 tw-px-5
                 tw-rounded-xl tw-font-semibold tw-text-sm
                 tw-transition-all tw-duration-200"
          :class="
            selectedFile
              ? 'tw-bg-blue-600 hover:tw-bg-blue-700 tw-text-white tw-shadow-lg tw-shadow-blue-600/20'
              : 'tw-bg-slate-100 tw-text-slate-400 tw-cursor-not-allowed'
          "
        >
          <svg
            class="tw-w-5 tw-h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.8"
              d="M12 16V4m0 0L8 8m4-4 4 4M4 16.5v1A2.5 2.5 0 006.5 20h11a2.5 2.5 0 002.5-2.5v-1"
            />
          </svg>

          Upload File
        </button>

        <!-- Footer -->
        <p class="tw-text-center tw-text-xs tw-text-slate-400 tw-mt-4">
          Your file will be securely uploaded for processing.
        </p>
      </div>
    </div>
  </div>
</template>