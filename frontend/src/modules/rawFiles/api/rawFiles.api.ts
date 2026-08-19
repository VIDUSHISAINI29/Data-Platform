import { apiGet, apiPost } from "@/plugins/api";

export const getRawFilesList = async() => {
    return apiGet('/reads/read-raw-files-list');
}

interface queryFilePayload {
    file_name: string,
    query: string
}

export const queryFile = async(payload: queryFilePayload) => {
    return apiPost('/query/query-file', payload);
}

export const TransformFile = async(payload: queryFilePayload) => {
    return apiPost('/query/transform-file', payload);
}