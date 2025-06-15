<script setup>
import {useAuthStore} from "@/store.js";
</script>

<template>
  <div class="tab" v-if="!useAuthStore().isAuthenticated">
    <router-link to="/">首页</router-link>
    <router-link to="/login" class="mid">登陆</router-link>
    <router-link to="/info">个人</router-link>
  </div>
  <router-view></router-view>
</template>

<style scoped>
.tab {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: end;

}


.tab * {
  text-decoration: none;
  color:black;
  padding-right: 15px;
}
</style>
