<script setup>
// import Person from "./components/Person.vue" --- ref
// import Book from "./components/Book.vue";  --- reactive
// import Syntax from "./components/Syntax.vue";  --Syntax
// import LifeCycle from './components/LifeCycle.vue';
// import {ref} from "vue"
import Father from "@/components/Father.vue"

// let flag = ref(true)

// const changeflag = () => {
//   flag.value = !flag.value
// }
</script>

<template>
  <!-- <Person></Person> -->
  <!-- <Book></Book> -->
   <!-- <Syntax></Syntax> -->
  <!-- <LifeCycle v-if="flag"></LifeCycle>
  <button @click="changeflag">toggle</button> -->
  <Father></Father>
</template>

<style scoped></style>
