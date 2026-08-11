import { useToast } from "primevue/usetoast";

type ToastSeverity = "success" | "info" | "warn" | "error";

export const useToastNotification = () => {
   const toast = useToast();

   return (
      severity: ToastSeverity,
      summary: string,
      detail: string,
      life: number = 3000,
   ) => {
      toast.add({
         severity,
         summary,
         detail,
         life,
      });
   };
};
