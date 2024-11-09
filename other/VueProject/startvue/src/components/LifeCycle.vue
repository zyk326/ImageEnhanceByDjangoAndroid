<script setup>
import { ref, onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted } from "vue";

// 创建阶段
console.log("setup");
let name = ref(0);
const onnameUpdated = () => {
  name.value += 1;
};

// 挂载阶段
onBeforeMount(() => {
  console.log("beforemount");
});
onMounted(() => {
  console.log("mounted");
});

// 更新阶段
onBeforeUpdate(() => {
  console.log("beforeupdate");
});
onUpdated(() => {
  console.log("updated");
});

// 卸载阶段
onBeforeUnmount(() => {
  console.log("beforeunmount")
})
onUnmounted(() => {
  console.log("unmount")
})
</script>

<template>
  <div>
    {{ name }}
    <button @click="onnameUpdated">button</button>
  </div>
</template>

<style scoped></style>
