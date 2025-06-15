<script setup>
import {reactive} from "vue";
import axios from "axios";

const  userInfo = reactive({
  username: "",
  password: "",
})
function login(){
  axios.post("http://localhost:8080/api",userInfo).then(res => {
    console.log(res)
  }).catch(err=>{
    console.log(err)
  })
}
</script>

<template>
<div class="box">
  <div class="container">
    <input v-model="userInfo.username"/>
    <input v-model="userInfo.password"/>
    <button @click="login">登陆</button>
  </div>
</div>
</template>

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.container *{
  margin-top: 20px;
}
</style>