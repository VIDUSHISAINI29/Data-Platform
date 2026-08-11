import { ref } from 'vue';
import { defineStore } from 'pinia';
import { authClient } from '@/plugins/auth-client';
import api from '@/plugins/api';


export const useAuthStore = defineStore('auth', () => {
   const user = ref<any>(null);
   const loading = ref(false);
   const initialized = ref(false);

   const setUser = (newUser: any) => {
      user.value = newUser;
   };

   const fetchSession = async () => {
      try {
         // First verify the session is valid via Better Auth
         const { data } = await authClient.getSession();

         if (!data?.user) {
            user.value = null;
            return;
         }

         // Session is valid — fetch the full profile from users table
         // which always has the latest name, avatar, bio, socials
         const { data: profile } = await api.get('/users/me');
         user.value = {
            ...data.user, // keeps id, email, emailVerified from session
            ...profile, // overwrites name, image/avatar with users table values
         };
      } catch {
         user.value = null;
      } finally {
         initialized.value = true;
      }
   };

   const logout = async (router: any) => {
      await authClient.signOut();
      user.value = null;
      router.push('/sign-in');
   };

   return {
      user,
      loading,
      initialized,
      setUser,
      fetchSession,
      logout
   };
});
