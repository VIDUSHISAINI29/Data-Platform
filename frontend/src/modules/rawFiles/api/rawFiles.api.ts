import { apiGet } from "@/plugins/api";

export const getRawFilesList = async() => {
    return apiGet('/reads/read-raw-files-list');
}