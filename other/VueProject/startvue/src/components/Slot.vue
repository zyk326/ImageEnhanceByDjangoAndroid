<template>
  <div>
    <slot name = "header" :onename="name1"></slot>
  </div>
  <div class="main">
    <slot :onename="name2"></slot>
  </div>
  <div>
    <slot name="gloop" :onename="name3"></slot>
  </div>

</template>

<script setup>
let name1 = 11
let name2 = 12
let name3 = 13
</script>

<style scoped>
.main{
  background: red;
}
</style>
