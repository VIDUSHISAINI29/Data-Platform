import axios, { AxiosError } from 'axios';
import { authClient } from '@/plugins/auth-client';
import router from '@/app/router';
import type { ApiErrorResponse } from '@/shared/types/api.types';

const api = axios.create({
   baseURL: import.meta.env.VITE_API_URL,
   // Required so the browser sends the Better Auth session cookie
   // on cross-origin requests to the backend API.
   withCredentials: true,
});

/*
   No request interceptor needed for auth.
   Better Auth uses HTTP-only cookies — the browser attaches the session
   cookie automatically on every request. No Bearer token to attach.
*/

/* ===============================
   Global Error Handling
=============================== */

api.interceptors.response.use(
   (response) => response,
   async (error: AxiosError<ApiErrorResponse>) => {
      const status = error.response?.status;

      if (status === 401) {
         await authClient.signOut();
         router.push({ name: 'login' });
      }

      return Promise.reject(
         error.response?.data?.message ||
            error.response?.data?.error ||
            'Unexpected error occurred',
      );
   },
);

/* ===============================
   Typed API Helpers
=============================== */

export async function apiGet<T>(url: string): Promise<T> {
   const response = await api.get<T>(url);
   return response.data;
}

export async function apiPost<T, B = unknown>(
   url: string,
   body: B,
): Promise<T> {
   const response = await api.post<T>(url, body);
   return response.data;
}

export async function apiPatch<T, B = unknown>(
   url: string,
   body: B,
): Promise<T> {
   const response = await api.patch<T>(url, body);
   return response.data;
}

export async function apiDelete<T>(url: string): Promise<T> {
   const response = await api.delete<T>(url);
   return response.data;
}

export default api;
