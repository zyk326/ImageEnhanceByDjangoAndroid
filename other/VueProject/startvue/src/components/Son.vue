<script setup>
import { ref, defineProps, defineEmits } from "vue";

const pros = defineProps({
  name: String,
  gender: {
    type: String,
    default: "male",
  },
  body: {
    height: Number,
    weight: Number,
  },
});
const emit = defineEmits(["changename"]);
const OnchangeName = () => {
  console.log('in emits')
  emit('changename', pros.name)
}
</script>

<template>
  <div>
    name : {{ pros.name }}
    gender : {{ pros.gender }}
    height : {{ pros.body.height }}
    weight : {{ pros.body.weight }}
    <button @click="OnchangeName">button</button>
  </div>
</template>

<style scoped></style>
