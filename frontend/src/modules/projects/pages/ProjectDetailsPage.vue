<script setup lang="ts">
   import { ref, onMounted } from 'vue';
   import {
      getAllProjectForUser,
      getProjectById,
      updateProject,
      deleteProject,
   } from '../api/project.api';
   import {
      getEndpointsByProjectId,
      createEndpoint,
      updateEndpoint,
   } from '../../endpoints/api/endpoint.api';
   import OverviewCard from '../../../shared/components/OverviewCard.vue';
   import { formatTimeAgo } from '../composables/formatTime';
   import UpdateProjectForm from '../components/UpdateProjectForm.vue';
   import DeleteModal from '@/shared/components/DeleteModal.vue';
   import { useToastNotification } from '@/shared/composables/useToastNotification';
   import { useRouter, useRoute } from 'vue-router';
   import ProgressSpinner from '@/shared/components/ProgressSpinner.vue';
   import EndpointsTab from '../../endpoints/components/EndpointsTab.vue';
   import AddEndpointModal from '../../endpoints/components/AddEndpointModal.vue';

   const router = useRouter();
   const route = useRoute();
   const toast = useToastNotification();

   const openUpdateForm = ref(false);
   const openDeleteModal = ref(false);

   type Project = {
      id: string;
      name: string;
      slug: string;
      description?: string;
      createdAt: string;
   };
   type UpdateProjectPayload = {
      name: string;
      description?: string;
   };

   const project = ref<Project | null>(null);

   const getProject = async () => {
      try {
         const data = await getProjectById(route.params.projectId as string);
         project.value = data;
         console.log('pr -', data.name);
      } catch (error) {
         console.error('Error fetching projects:', error);
      }
   };

   const updateProjectFunction = async (formData: UpdateProjectPayload) => {
      try {
         if (!formData.name.trim()) {
            alert('Project name is required');
            return;
         }
         const updatedProject = await updateProject(
            route.params.projectId as string,
            formData,
         );
         //  projectsList.value.push(newProject);
         console.log('Project updated:', updatedProject);
         await getProject();
         toast('success', 'Congratulations', 'Project updated successfully');
      } catch (error) {
         console.error('Error updating project:', error);
      }
   };
   const deleteProjectFunction = async () => {
      try {
         const deletedProject = await deleteProject(
            route.params.projectId as string,
         );
         //  projectsList.value.push(newProject);
         console.log('Project deleted:', deletedProject);
         router.push('/projects');
         toast('success', 'Congratulations', 'Project deleted successfully');
      } catch (error) {
         console.error('Error deleting project:', error);
      }
   };

   const tabs = ref([
      // { title: 'Overview', value: '0' },
      { title: 'Endpoints', value: '0' },
      // { title: 'Incidents', value: '1' },
   ]);

   // # ************ Endpoints Js ************* #  //

   onMounted(async () => {
      await getProject();
   });
</script>

<template>
   <div>
      <div v-if="project" class="tw-flex tw-flex-col tw-gap-4">
         <div class="tw-flex tw-items-center tw-justify-between">
            <div class="tw-flex tw-flex-col tw-gap-2">
               <div
                  @click="router.push('/projects')"
                  class="tw-flex tw-cursor-pointer tw-items-center tw-gap-1 tw-text-[12px] tw-text-pulse-cyan">
                  <i class="pi pi-arrow-left tw-text-[12px]"></i>
                  <span>Back to Projects</span>
               </div>
               <div class="tw-flex tw-flex-col">
                  <span class="tw-text-3xl tw-font-semibold tw-text-white">
                     {{ project?.name }}
                  </span>
                  <span class="tw-text-[13px] tw-text-pulse-grayText">
                     {{ project?.description || 'No description available.' }}
                  </span>
               </div>
            </div>
            <div class="tw-flex tw-flex-col tw-gap-2 tw-py-3">
               <div class="tw-flex tw-gap-3">
                  <div
                     @click="openUpdateForm = true"
                     class="tw-flex tw-cursor-pointer tw-items-center tw-gap-2 tw-rounded-lg tw-border tw-border-pulse-border tw-px-3 tw-py-2">
                     <i
                        class="pi pi-pencil tw-text-sm tw-text-pulse-grayText"></i>
                     <span class="tw-text-sm tw-text-pulse-grayText">
                        Edit project
                     </span>
                  </div>
                  <div
                     @click="openDeleteModal = true"
                     class="tw-flex tw-cursor-pointer tw-items-center tw-gap-2 tw-rounded-lg tw-border tw-border-pulse-error/60 tw-px-3 tw-py-2">
                     <i class="pi pi-trash tw-text-sm tw-text-pulse-error"></i>
                     <span class="tw-text-sm tw-text-pulse-error">
                        Delete project
                     </span>
                  </div>
               </div>
               <div class="tw-flex tw-justify-end">
                  <div
                     class="tw-flex tw-w-[150px] tw-cursor-pointer tw-flex-col tw-justify-center tw-gap-1 tw-rounded-lg tw-border tw-border-pulse-border tw-px-3 tw-py-2">
                     <span class="tw-text-[11px] tw-text-pulse-grayText">
                        Created
                     </span>
                     <span class="tw-text-[13px] tw-text-pulse-grayText">
                        {{ formatTimeAgo(project.createdAt) }}
                     </span>
                  </div>
               </div>
            </div>
         </div>

         <div class="">
            <Tabs value="0">
               <TabList class="tw-w-[400px] tw-bg-pulse-bg">
                  <Tab
                     class="tw-tex tw-bg-pulse-bg"
                     v-for="tab in tabs"
                     :value="tab.value">
                     {{ tab.title }}
                  </Tab>
               </TabList>
               <TabPanels class="tw-bg-pulse-bg">
                  <TabPanel value="0">
                     <!--# Endpoints Tab goes here -->

                     <EndpointsTab />
                  </TabPanel>
                  <TabPanel value="1">
                     <div class="tw-flex tw-flex-col tw-gap-3"></div>
                  </TabPanel>
               </TabPanels>
            </Tabs>

            <!-- Modal -->

            <UpdateProjectForm
               class="transition-all tw-scale-105 tw-duration-300"
               :modalOpen="openUpdateForm"
               :prevName="project?.name"
               :prevDescription="project?.description || ''"
               @update:modalOpen="openUpdateForm = $event"
               @update="updateProjectFunction" />

            <DeleteModal
               :modalOpen="openDeleteModal"
               :deleteObjectName="project?.name"
               @delete:modalOpen="openDeleteModal = $event"
               @confirm="deleteProjectFunction" />
         </div>
      </div>
      <div class="tw-flex tw-h-screen tw-items-center tw-justify-center" v-else>
         <ProgressSpinner />
      </div>
   </div>
</template>

<style scoped>
   /* Tabs css */

   :deep(.p-tablist-tab-list) {
      border-bottom: none !important;
   }

   :deep(.p-tablist-content) {
      border-bottom: none !important;
   }

   :deep(.p-tablist-nav) {
      border: none !important;
   }
   /* Reduce tab header size */
   :deep(.p-tab) {
      flex: unset;
      justify-content: center;
      text-align: center;

      padding: 0.45rem 0.7rem !important;
      font-size: 13px !important;
      font-weight: 500;

      min-height: unset !important;
   }

   /* Smaller tab list gap */
   :deep(.p-tablist-tab-list) {
      gap: 0.5rem;
   }

   /* Remove unnecessary big container height/padding */
   :deep(.p-tablist) {
      padding: 0 !important;
      min-height: unset !important;
   }

   /* Active tab */
   :deep(.p-tab.p-tab-active) {
      color: #22d3ee;
   }

   /* Hover */
   :deep(.p-tab:hover) {
      color: #67e8f9;
   }

   /* Active cyan line */
   :deep(.p-tablist-active-bar) {
      background-color: #22d3ee;
      height: 2px !important;
      border-radius: 999px;
   }

   /* Remove large panel padding */
   :deep(.p-tabpanels) {
      padding: 1rem 0 0 0 !important;
      background: transparent !important;
   }

   :deep(.p-tabpanel) {
      padding: 0 !important;
      background: transparent !important;
   }
   :deep(.p-tablist-active-bar) {
      background-color: #22d3ee;
      padding: 1px;
      border-radius: 20px;
   }
   :deep(.p-tablist-bar) {
      border-radius: 20px;
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
