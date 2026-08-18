import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/modules/auth/store/auth.store';

const router = createRouter({
   history: createWebHistory(import.meta.env.BASE_URL),
   routes: [
      // {
      //    path: '/sign-in',
      //    name: 'signIn',
      //    component: () => import('@/modules/auth/pages/SignInPage.vue'),
      //    meta: { public: true },
      // },
      {
         path: '/',
         redirect: 'upload-file',
      },

      {
         path: '/',
         component: () => import('@/layout/AppLayout.vue'),
         children: [
           
            {
               path: 'transformed-files',
               name: 'transformedFiles',
               component: () =>
                  import('@/modules/transformedFiles/pages/TransformedFilesPage.vue'),
               // children: [
               //    {
               //       path: ':projectId',
               //       name: 'project-details',
               //       component: () =>
               //          import('@/modules/projects/pages/ProjectDetailsPage.vue'),
               //       props: true,
               //    },
               // ],
            },
            {
               path: '/raw-files',
               name: 'rawFiles',
               component: () => import('@/modules/rawFiles/pages/RawFilesPage.vue')
            },
            {
               path: '/upload-file',
               name: 'uploadFile',
               component: () => import('@/modules/uploadFile/pages/UploadFilePage.vue')
            },
            {
               path: '/upload-file',
               name: 'uploadFile',
               component: () => import('@/modules/uploadFile/pages/UploadFilePage.vue')
            },
            {
               path: '/upload-file',
               name: 'uploadFile',
               component: () => import('@/modules/uploadFile/pages/UploadFilePage.vue')
            },
         ],
      },

      {
         path: '/:pathMatch(.*)*',
         name: 'notfound',
         component: () => import('@/app/NotFound.vue'),
      },
   ],
});

/* ===============================
   Navigation Guard
=============================== */

// router.beforeEach(async (to) => {
//    const auth = useAuthStore();

//    // Always re-fetch session on protected routes to catch expiry.
//    // On public routes, only fetch if not yet initialized.
//    if (to.meta.requiresAuth) {
//       await auth.fetchSession();
//    } else if (!auth.initialized) {
//       await auth.fetchSession();
//    }

//    const isAuthenticated = !!auth.user;

//    if (to.meta.requiresAuth && !isAuthenticated) {
//       return { name: 'signIn', query: { redirect: to.fullPath } };
//    }

//    if (to.meta.public && isAuthenticated) {
//       return { name: 'dashboard' };
//    }
// });

export default router;
