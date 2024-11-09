<script setup>
import Son from "./Son.vue";
import Slot from "./Slot.vue";

let name = "zyk";
const onChangeName = (name) => {
  console.log(name);
};
</script>

<template>
  <Son
    @changename="onChangeName"
    :name="name"
    :body="{ height: 120, weight: 160 }"
  ></Son>

  <Slot>
    <template #header="scope"> s zheshi{{ scope.onename }} </template>
    <template #default="scope">
    这是mian的 {{ scope.onename }}
    </template>
    <template #gloop="scope"> nihao{{ scope.onename }} </template>
  </Slot>
</template>

<style scoped></style>
