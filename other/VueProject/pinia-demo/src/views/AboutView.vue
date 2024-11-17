<script setup>
import {useCounterStore} from "../stores/counter"

const counterStore = useCounterStore()

const updateCount = () => {
  // 直接更新
  counterStore.count += 1
  console.log(counterStore.count)

  // 批量更新
  counterStore.$patch({
    count: counterStore.count + 2,
    projectname : "zyk"
  })

  // 方法更新
  counterStore.increment()
}
</script>

<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="updateCount">button</button>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
