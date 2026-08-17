import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useFileStore = defineStore('file', () => {
    const currentFile = ref<File | null>(null)

    return{
        currentFile
    }
})