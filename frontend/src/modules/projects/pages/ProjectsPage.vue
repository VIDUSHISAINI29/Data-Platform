<script setup lang="ts">
import { ref, onMounted } from 'vue';
import createProjectForm from '@/modules/projects/components/CreateProjectForm.vue';
import ProgressSpinner from '@/shared/components/ProgressSpinner.vue';
import { getAllProjectForUser, createProject } from '../api/project.api';
import PorjectCard from '../components/ProjectCard.vue';
import { useRouter, useRoute } from 'vue-router';
import { useToastNotification } from '@/shared/composables/useToastNotification';
import { formatTimeAgo } from '../composables/formatTime';

const router = useRouter();
const route = useRoute();
const toast = useToastNotification();
const loading = ref(true);

type Project = {
   id: string;
   name: string;
   slug: string;
   description?: string;
   createdAt: string;   
}

 type newProject = {
      name: string;
      description?: string;
   };

 const openForm = ref(false);
  const projectsList = ref<Project[]>([]);

  const colorsForProjects = [
    {
      gradientFrom: 'tw-from-pulse-purple',
      shadow: 'tw-shadow-[0_0_15px_rgba(124,58,237,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-cyan',
      shadow: 'tw-shadow-[0_0_15px_rgba(6,182,212,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-blue',
      shadow: 'tw-shadow-[0_0_15px_rgba(25,91,253,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-pink',
      shadow: 'tw-shadow-[0_0_15px_rgba(255,0,149,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-green',
      shadow: 'tw-shadow-[0_0_15px_rgba(34,197,94,0.3)]',
    },
     {
      gradientFrom: 'tw-from-pulse-lime',
      shadow: 'tw-shadow-[0_0_15px_rgba(132,204,22,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-error',
      shadow: 'tw-shadow-[0_0_15px_rgba(239,68,68,0.3)]',
    },
    {
      gradientFrom: 'tw-from-pulse-warning',
      shadow: 'tw-shadow-[0_0_15px_rgba(245,158,11,0.3)]',
    }
]

   const getProjects = async () => {
      loading.value = true;
      try {
         const data = await getAllProjectForUser();
         console.log('data -', data);
         projectsList.value = data;
      } catch (error) {
         console.error('Error fetching projects:', error);
      }
      finally {
         loading.value = false;
      }
   };

  const createProjectFunction = async (formData: newProject) => {
      try {
         if (!formData.name.trim()) {
            alert('Project name is required');
            return;
         }
         const newProject = await createProject(formData);
         //  projectsList.value.push(newProject);
         console.log('New project created:', newProject);
         await getProjects();
         toast('success', 'Congratulations!', 'Project created successfully');
      } catch (error) {
         console.error('Error creating project:', error);
      }
   };



function openDetails(projectId: string) {
   router.push(`/projects/${projectId}`);
}

   onMounted(async () => {
      await getProjects();
   });
 
</script>
<template>
<div class="tw-py-2 tw-px-4 tw-w-full">
      <div v-if="!loading">
         <div v-if="!route.params.projectId" class="tw-flex tw-flex-col tw-gap-10">
          <div class="tw-flex tw-items-center tw-justify-between tw-text-4xl">
            <div class="tw-flex tw-gap-1 tw-flex-col">
               <span class="tw-font-semibold tw-text-white">Projects</span>
               <span class="tw-text-sm tw-text-pulse-grayText">
                  Manage and monitor all your projects in one place.
               </span>
            </div>
            <div>
               <div
                  class="tw-rounded-md  tw-bg-gradient-to-r tw-from-pulse-cyan tw-to-pulse-lime tw-p-[1px]">
                  <div @click="openForm=true"
                     class=" tw-flex tw-cursor-pointer tw-items-center tw-justify-center tw-gap-1 tw-rounded-md tw-bg-pulse-bg tw-px-2 tw-py-1">
                     <span
                        class="tw-mb-[4px] tw-rounded-md tw-text-center tw-text-2xl tw-text-pulse-cyan">
                        +
                     </span>
                     <span
                        class="tw-text-sm tw-font-semibold tw-text-pulse-cyan">
                        Create Project
                     </span>
                  </div>
               </div>
            </div>
         </div>

         <div v-if="projectsList.length" class="tw-flex tw-gap-6 tw-flex-wrap">
             <PorjectCard  v-for="(project, index) in projectsList" @click="openDetails(project.id)"
             :key="index"
               :mainText="project.name"
               :subText="project.description || 'No description'"
               :gradientFrom="colorsForProjects[index % colorsForProjects.length].gradientFrom"
   :shadow="colorsForProjects[index % colorsForProjects.length].shadow"
               status="Active"
               statusBg="tw-bg-pulse-green/20"
                statusText="tw-text-pulse-green"
                :endpointsCount="12"
                :uptimePercentage="99.9"
                :incidentsCount="3"
               :timeOfCreation="formatTimeAgo(project.createdAt)"
                />
         </div>
         <div class="tw-flex tw-justify-center tw-items-center tw-h-[60vh]" v-else>
            <p class="tw-text-pulse-grayText">
               No project created. Create One
            </p>
            
         </div>

          <createProjectForm
      class="transition-all tw-duration-300 tw-scale-105"
         :modalOpen="openForm"
         @update:modalOpen="openForm = $event"
         @create="createProjectFunction" />
    </div>
    <router-view v-else />
      </div>

     <div class="tw-flex tw-h-screen tw-items-center tw-justify-center" v-else>
         <ProgressSpinner />
      </div>
</div>

</template>