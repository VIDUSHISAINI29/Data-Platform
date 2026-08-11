<script setup lang="ts">
   import { reactive, ref } from 'vue';
   import { signUp, signIn } from '../api/auth.api';
   import { useRoute, useRouter } from 'vue-router';
   import { authClient } from '@/plugins/auth-client';
   import {useToastNotification} from "@/shared/composables/useToastNotification";

   const route = useRoute();
   const router = useRouter();
   const toast = useToastNotification();
   const authPageShowcase = [
      // {
      //    name: 'Real-time Monitoring',
      //    icon: 'pi-wave-pulse',
      //    description: 'Check your APIs every minute, 24/7',
      // },
      // {
      //    name: 'Instant Alerts',
      //    icon: 'pi-bell',
      //    description: 'Get notified the moment something breaks',
      // },
      {
         name: 'Developer First',
         icon: 'pi-folder',
         description: 'Clean dashboard, powerful insights',
      },
   ];
   const tabs = ref([
      { title: 'Sign In', value: '0' },
      { title: 'Sign Up', value: '1' },
   ]);

   const loginForm = reactive({
      email: '',
      password: '',
   });
   const createAccountForm = reactive({
      name: '',
      email: '',
      password: '',
   });

   const activeTab = ref('0'); // Sign In by default

   // import { usePageMeta } from '@/shared/composables/usePageMeta';

   // usePageMeta({
   //    title: 'Login',
   //    path: '/login',
   // });

   const signInWithEmail = async () => {
      console.log('Attempting to sign in with email:', loginForm);
      try {
         await signIn(loginForm);
         console.log('Attempting to sign in with email:', loginForm);
         router.push('/');
      } catch (error) {
         toast('error', 'Login Failed', `${error}`);
         console.error('Login failed:', error);
      }
   };
   const signUpWithEmail = async () => {
      try {
         if(createAccountForm.name.trim() === '' || createAccountForm.email.trim() === '' || createAccountForm.password.trim() === '') {
            toast('error', 'Validation Error', 'All fields are required');
            return;
         }
         await signUp(createAccountForm);
         toast('success', 'Account Created', 'Sign in now!');
          activeTab.value = '0'; // Switch to Sign In tab
         router.push('/sign-in');
      } catch (error) {
         toast('error', 'Sign Up Failed', `${error}`);
         console.error('Sign up failed:', error);
      }
   };

   // // Redirect back to the page the user was on before being sent to login.
   // // callbackURL is passed to Better Auth — after OAuth completes, the user
   // // lands back on whatever page triggered the login prompt.
   const callbackURL = `${window.location.origin}${route.query.redirect || '/'}`;

   const loginWithGoogle = async () => {
      console.log(callbackURL);

      await authClient.signIn.social({
         provider: 'google',
         callbackURL,
      });
   };

   const loginWithGithub = async () => {
      await authClient.signIn.social({
         provider: 'github',
         callbackURL,
      });
   };
</script>

<template>
   <div
      class="tw-flex tw-min-h-screen tw-items-center tw-justify-center tw-bg-pulse-bg tw-p-3">
      <div
         class="tw-flex tw-w-full tw-max-w-[1000px] tw-items-center tw-justify-center tw-gap-5 tw-rounded-lg tw-border tw-border-pulse-border tw-p-3">
         <div class="tw-bg- tw-flex tw-w-1/2 tw-flex-col tw-gap-5 tw-p-2">
            <div class="tw-flex tw-w-full tw-items-center tw-justify-start">
               <img class="tw-w-36" src="/images/logo.png" alt="" />
            </div>
            <div
               class="tw-w-44 tw-rounded-2xl tw-bg-pulse-cyan/10 tw-p-1 tw-text-center tw-text-[10px] tw-text-pulse-cyan">
               <span>API Monitoring for Developers</span>
            </div>
            <div class="tw-flex tw-flex-col">
               <span class="tw-p-1 tw-text-4xl tw-font-semibold tw-text-white">
                  Never miss a
               </span>
               <span
                  class="tw-bg-gradient-to-r tw-from-pulse-cyan tw-to-pulse-lime tw-bg-clip-text tw-p-1 tw-text-4xl tw-font-semibold tw-text-transparent">
                  failing API again.
               </span>
            </div>
            <div class="tw-flex tw-flex-col">
               <span class="tw-text-sm tw-text-gray-400">
                  Pulse monitors your APIs 24/7, alerts you instantly,
               </span>
               <span class="tw-text-sm tw-text-gray-400">
                  and gives you the insights you need to ship with confidence.
               </span>
            </div>

            <div
               class="tw-h-[250px] tw-flex tw-justify-center tw-items-center tw-w-[400px] tw-rounded-2xl tw-bg-gradient-to-br tw-from-pulse-cyan tw-to-pulse-lime ">
               <img
                  class="tw-h-[248px] tw-w-[398px] tw-rounded-2xl"
                  src="/images/dashboard-overview.png"
                  alt="" />
            </div>
         </div>

         <!-- <div class="tw-flex tw-flex-col tw-gap-3">
               <div
                  v-for="(showcase, index) in authPageShowcase"
                  :key="index"
                  :class="[
                     'tw-flex tw-p-1 tw-items-center tw-gap-3 tw-rounded-md tw-transition-colors tw-duration-300',
                  ]">
                  <div
                     class="tw-h-8 tw-w-8 tw-rounded-md tw-border-pulse-cyan tw-bg-pulse-cyan/10 tw-p-1 tw-text-center">
                     <i
                        :class="[
                           showcase.icon,
                           'pi tw-text-sm tw-text-pulse-cyan tw-transition-colors tw-duration-300',
                        ]"></i>
                  </div>
                  <div class="tw-flex tw-flex-col">
                     <span class="tw-text-sm tw-font-semibold tw-text-gray-200">
                        {{ showcase.name }}
                     </span>
                     <span class="tw-text-[11px] tw-text-gray-400">
                        {{ showcase.description }}
                     </span>
                  </div>
               </div>
            </div> -->

         <div class="tw-w-full lg:tw-w-1/2">
            <div
               class="tw-w-11/12 tw-rounded-xl tw-bg-gradient-to-br tw-from-pulse-cyan tw-to-pulse-lime tw-p-[2px]">
               <div
                  class="tw-flex tw-w-full tw-flex-col tw-gap-3 tw-rounded-xl tw-bg-pulse-bg tw-p-3 tw-shadow-pulse-cyan">
                  <div class="tw-flex tw-flex-col tw-items-center">
                     <div>
                        <img
                           class="tw-w-20"
                           src="/images/logoOnly.png"
                           alt="Pulse Logo" />
                     </div>
                     <span class="tw-text-xl tw-font-semibold tw-text-white">
                        Welcome to Pulse
                     </span>
                     <span class="tw-text-[13px] tw-text-gray-400">
                        Monitor your APIs, ship with confidence.
                     </span>
                  </div>

                  <div>
                     <div>
                        <Tabs v-model:value="activeTab">
                           <TabList class="tw-bg-pulse-bg">
                              <Tab
                                 class="tw-tex tw-bg-pulse-bg"
                                 v-for="tab in tabs"
                                 :value="tab.value">
                                 {{ tab.title }}
                              </Tab>
                           </TabList>
                           <TabPanels class="tw-bg-pulse-bg">
                              <TabPanel value="0">
                                 <div
                                    class="tw-mt-3 tw-flex tw-flex-col tw-gap-3">
                                    <FloatLabel variant="in">
                                       <InputText
                                          id="email"
                                          v-model="loginForm.email"
                                          class="tw-w-full tw-border-pulse-border tw-bg-inherit tw-text-gray-200"
                                          autocomplete="off" />
                                       <label for="email">Email</label>
                                    </FloatLabel>
                                    <FloatLabel variant="in">
                                       <Password
                                          id="password"
                                          v-model="loginForm.password"
                                          toggleMask
                                          :feedback="false"
                                          class="tw-w-full"
                                          inputClass="tw-w-full tw-bg-inherit tw-text-gray-200 tw-border-pulse-border" />
                                       <label for="password">Password</label>
                                    </FloatLabel>

                                    <button
                                       @click="signInWithEmail"
                                       class="tw-mt-3 tw-w-full tw-rounded-xl tw-bg-gradient-to-br tw-from-pulse-cyan/70 tw-to-pulse-lime/60 tw-py-3 tw-font-semibold tw-text-white">
                                       Log In
                                    </button>

                                    <div class="tw-flex tw-items-center">
                                       <div
                                          class="tw-h-[1px] tw-flex-1 tw-bg-gray-200"></div>
                                       <span
                                          class="tw-px-4 tw-text-sm tw-text-gray-400">
                                          or
                                       </span>
                                       <div
                                          class="tw-h-[1px] tw-flex-1 tw-bg-gray-200"></div>
                                    </div>
                                 </div>

                                 <div class="tw-mt-3 tw-flex tw-gap-2">
                                    <button
                                       @click="loginWithGoogle"
                                       class="tw-w-full tw-flex-1 tw-items-center tw-justify-center tw-gap-3 tw-rounded-xl tw-border tw-border-gray-300 tw-bg-inherit tw-py-3 tw-font-medium tw-text-pulse-cyan tw-transition hover:tw-shadow-md">
                                       <!-- Replace this image with your own -->
                                       <i
                                          class="pi pi-google tw-h-5 tw-w-5 tw-text-pulse-cyan" />

                                       Go with Google
                                    </button>
                                    <button
                                       @click="loginWithGithub"
                                       class="tw-w-full tw-flex-1 tw-items-center tw-justify-center tw-gap-3 tw-rounded-xl tw-border tw-border-gray-300 tw-bg-inherit tw-py-3 tw-font-medium tw-text-pulse-cyan tw-transition hover:tw-shadow-md">
                                       <!-- Replace this image with your own -->
                                       <i
                                          class="pi pi-github tw-h-5 tw-w-5 tw-text-pulse-cyan" />

                                       Go with Github
                                    </button>
                                 </div>
                              </TabPanel>

                              <TabPanel value="1">
                                 <div class="tw-flex tw-flex-col tw-gap-3">
                                    <FloatLabel variant="in">
                                       <InputText
                                          id="name"
                                          v-model="createAccountForm.name"
                                          class="tw-w-full tw-border-pulse-border tw-bg-inherit tw-text-gray-200"
                                          autocomplete="off" />
                                       <label for="name">Name</label>
                                    </FloatLabel>
                                    <FloatLabel variant="in">
                                       <InputText
                                          id="email"
                                          v-model="createAccountForm.email"
                                          class="tw-w-full tw-border-pulse-border tw-bg-inherit tw-text-gray-200"
                                          autocomplete="off" />
                                       <label for="email">Email</label>
                                    </FloatLabel>
                                    <FloatLabel variant="in">
                                       <Password
                                          id="password"
                                          v-model="createAccountForm.password"
                                          toggleMask
                                          :feedback="false"
                                          class="tw-w-full"
                                          inputClass="tw-w-full tw-bg-inherit tw-text-gray-200 tw-border-pulse-border" />
                                       <label for="password">Password</label>
                                    </FloatLabel>

                                    <button
                                       @click="signUpWithEmail"
                                       class="tw-mt-3 tw-w-full tw-rounded-xl tw-bg-gradient-to-br tw-from-pulse-cyan/70 tw-to-pulse-lime/60 tw-py-3 tw-font-semibold tw-text-white">
                                       Create Account
                                    </button>
                                 </div>
                              </TabPanel>
                           </TabPanels>
                        </Tabs>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</template>

<style scoped>
   :deep(.p-tablist-active-bar) {
      background-color: #22d3ee;
      padding: 1px;
   }
   :deep(.p-tab.p-tab-active) {
      color: #22d3ee; /* cyan */
   }
   :deep(.p-tablist) {
      display: flex;
   }
   :deep(.p-tablist-next-button) {
      display: hidden;
   }

   :deep(.p-tab) {
      flex: 1;
      justify-content: center;
      text-align: center;
      font-weight: 500;
   }
   :deep(.p-tab:hover) {
      color: #67e8f9; /* lighter cyan */
   }
   /* Focus states */
   :deep(.p-floatlabel:has(.p-inputtext:focus) label),
   :deep(.p-floatlabel:has(.p-textarea:focus) label),
   :deep(.p-floatlabel:has(.p-autocomplete.p-inputwrapper-focus) label),
   :deep(.p-floatlabel:has(.p-password.p-inputwrapper-focus) label) {
      color: #67e8f9 !important;
      
   }

   /* Filled state */
   :deep(.p-floatlabel:has(.p-filled) label),
   :deep(.p-floatlabel:has(.p-password .p-filled) label) {
      color: #67e8f9 !important;
   }
</style>
