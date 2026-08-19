import { apiGet, apiPost } from "@/plugins/api";

export const getTransformedFilesList = async() => {
    return apiGet('/reads/read-transformed-files-list');
}
