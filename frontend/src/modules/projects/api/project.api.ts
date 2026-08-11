import { apiPost, apiGet, apiPatch, apiDelete } from '@/plugins/api';

type Project = {
   id: string;
   name: string;
   slug: string;
   description?: string;
   createdAt: string;
};
// type GetProjectsResponse = Project[];
export const getProjectById = async (projectId: string) => {
   return apiGet<Project>(`/projects/${projectId}`);
};
export const getAllProjectForUser = async () => {
   return apiGet<Project[]>('/projects/all-projects');
};

type CreateProjectPayload = {
   name: string;
   description?: string;
};
export const createProject = async (payload: CreateProjectPayload) => {
   return apiPost<CreateProjectPayload>('/projects/create-project', payload);
};
export const updateProject = async (projectId: string, payload: Partial<CreateProjectPayload>) => {
   return apiPatch<CreateProjectPayload>(`/projects/update-project/${projectId}`, payload);
};
export const deleteProject = async (projectId: string) => {
   return apiDelete(`/projects/delete-project/${projectId}`);
}


