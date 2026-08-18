import { defineStore } from 'pinia'
import { ref } from 'vue'

interface FilePreview {
  columns: string[]
  data: Record<string, unknown>[]
}

export const useFileStore = defineStore('file', () => {
    const currentFile = ref<FilePreview | null>(null)
    const currentFileName = ref<string | null>(null)

    return{
        currentFile,
        currentFileName
    }
})