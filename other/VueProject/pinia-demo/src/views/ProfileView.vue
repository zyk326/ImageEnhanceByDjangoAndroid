<template>
  <div>
    <h1>username: {{ username }}</h1>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "../stores/user";

let username = ref("");

const userStore = useUserStore()

onMounted(() => { 
  username.value = userStore.user.username;
});
</script>

<style scoped></style>
