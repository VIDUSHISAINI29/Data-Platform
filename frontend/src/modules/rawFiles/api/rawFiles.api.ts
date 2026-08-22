import { apiGet, apiPost } from '@/plugins/api';

export const getRawFilesList = async () => {
   return apiGet('/reads/read-raw-files-list');
};

interface queryFilePayload {
   file_name: string | null;
   query: string;
}

export interface QueryFileResponse {
   message: string;
   result: {
      columns: string[];
      data: Record<string, any>[];
   };
}

export const queryFile = async (payload: queryFilePayload,): Promise<QueryFileResponse> => {
   return apiPost<QueryFileResponse>('/query/query-raw-file', payload);
};

export const TransformFile = async (payload: queryFilePayload) => {
   return apiPost('/query/transform-file', payload);
};
