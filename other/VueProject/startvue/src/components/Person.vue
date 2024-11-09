<script setup name="Person">
import { ref } from "vue";

let name = ref("ZYK");
let person = ref({
  username : 'zyk',
  age : 18
})

const onUpdateUsername = () => {
  name.value = "LJJ"
}

const onUpdateUserage = () => {
  person.value.age += 1
}

</script>

<template>
  <h1>this is a person name{{ name }}</h1>
  <div>
    <button @click = "onUpdateUsername">click to change name</button>
  </div>

  <h1>this is a person age{{ person.age }}</h1>
  <div>
    <button @click = "onUpdateUserage">click to change age</button>
  </div>
</template>

<style scoped></style>
