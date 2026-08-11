import { apiPost } from '@/plugins/api';

export const syncUser = async (payload: any) => {
   return apiPost('/auth/sync', payload);
};

export const signUp = async (formData: object) => {
   return apiPost('/auth/sign-up/email', formData);
}
export const signIn = async (formData: object) => {
   return apiPost('/auth/sign-in/email', formData);
}