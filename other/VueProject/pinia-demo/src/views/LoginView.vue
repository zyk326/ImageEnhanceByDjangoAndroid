<template>
  <div>
    <button @click="onSubmit">login</button>
  </div>
</template>

<script setup>
import {useUserStore} from "../stores/user";

const userStore = useUserStore()

const onSubmit = () => {
  setTimeout(() => {
    // 假设user是从服务端获取的
    let user = {
      username: "ZYK",
      emial: "869550165@qq.com",
      is_active: true,
    };
    userStore.setUser(user);
  }, 1000);
};
</script>

<style scoped></style>
