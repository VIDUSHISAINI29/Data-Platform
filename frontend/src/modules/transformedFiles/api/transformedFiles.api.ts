import { apiGet, apiPost } from "@/plugins/api";

export const getTransformedFilesList = async() => {
    return apiGet('/reads/read-transformed-files-list');
}

interface queryFilePayload {
    file_name: string|null,
    query: string
}

export const queryTransformedFile = async(payload: queryFilePayload) => {
    return apiPost('/query/query-transformed-file', payload);
}