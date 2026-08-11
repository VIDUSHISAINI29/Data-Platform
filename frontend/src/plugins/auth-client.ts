import { createAuthClient } from 'better-auth/vue';

/*
   Better Auth client for Vue 3.
   baseURL points to the backend — all /api/auth/* routes are handled
   server-side by the mounted handler in app.ts.

   Better Auth uses HTTP-only cookies for sessions.
   The browser sends the cookie automatically on every request —
   no manual token attachment needed in api.ts interceptors.
*/
export const authClient = createAuthClient({
   baseURL: import.meta.env.VITE_AUTH_URL,
   basePath: '/api/auth', // tells the client where Better Auth is mounted
      fetchOptions: {
        credentials: "include",
    },
});
