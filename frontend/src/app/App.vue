<template>
   <Toast />
   <!-- ConfirmDialog must be mounted at the root so useConfirm() works in any child component -->
   <ConfirmDialog />
   <router-view />
</template>