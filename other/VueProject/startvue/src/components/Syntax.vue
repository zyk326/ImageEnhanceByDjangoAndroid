<script setup>
import { ref, computed, watch, reactive } from "vue";

let username = ref("zyk");

const onUpdateUsername = () => {
  username.value = "ZYK";
};

const code = ref(
  "<h1 style = 'background-color : pink'>欢迎来到my universal</h1>"
);

let chl = ref("a");

const onUpdateBGcolor = () => {
  chl.value = "box";
};

let music = ref([
  { name: "xlaq", author: "ljj" },
  { name: "tbd", author: "zj" },
  { name: "theshow", author: "ljj" },
]);

const sortedList = () => {
  music.value.sort((x, y) => {
    let a = Math.random();
    let b = Math.random();
    return a - b;
  });
};

const onChangeWebsite = (event) => {
  // event.preventDefault();
  window.location = "https://www.360.com";
};

let height = ref(0)
let weight = ref(0)
let area = computed(() => {
  return height.value * weight.value
})

let nums = ref(0)
const onChangePlusOne = () => {
  nums.value += 1
}
watch(nums, (newValue, oldValue) => {
  console.log(newValue);
})

let home = reactive({
  name : 'zyk',
  member : 5
})

const onChangeName = () => {
  home.name += '1'
}
watch(() => home.name, (newValue, oldValue) => {
  console.log(newValue)
})
</script>

<template>
  <h1 :class="chl">{{ username }}</h1>
  <button @click="onUpdateUsername">button</button>

  <div v-html="code"></div>

  <div><button @click="onUpdateBGcolor">change color</button></div>

  <div>
    <table>
      <thead>
        <tr>
          <td>序号</td>
          <td>名字</td>
          <td>作者</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(song, index) in music" :key="song.name">
          <td><input type="text" placeholder="song.name" /></td>
          <td>{{ song.name }}</td>
          <td>{{ song.author }}</td>
        </tr>
      </tbody>
    </table>
    <button @click="sortedList">sorted</button>
  </div>

  <div>
    <a href="https://www.baidu.com" @click.prevent="onChangeWebsite($event)"
      >热链接</a
    >
  </div>

  <div>
    <input type="text" v-model="weight">宽
    <input type="text" v-model="height">高
    面积:{{ area }}
  </div>

  <div>
    数字:{{ nums }}
    <button @click="onChangePlusOne">dianji+1</button>
  </div>

  <div>{{ home.name }} {{ home.member }}
    <button @click="onChangeName">click to change name</button>
  </div>

</template>

<style scoped>
.box {
  background-color: red;
}
.a {
  background-color: beige;
}
</style>
