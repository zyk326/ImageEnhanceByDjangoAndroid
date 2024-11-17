<script setup>
import { reactive } from "vue";

let csl = reactive({
  name: "沉思錄",
  author: "馬可奧勒留",
});

const onUpdateBookInfo = () => {
  Object.assign(csl, {
    name: "沉思录",
    author: "马可奥勒留",
  });
};
</script>

<template>
  <h1>name is {{ csl.name }} authot is {{ csl.author }}</h1>
  <button @click="onUpdateBookInfo">button</button>
</template>

<style scoped></style>
