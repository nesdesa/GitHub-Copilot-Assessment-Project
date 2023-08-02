<script setup>
import { RouterLink, RouterView } from 'vue-router';
import Sidemenu from './components/Sidemenu.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <el-card body-style="background-color: '#545c64';">
          <Sidemenu />
        </el-card>
        
      </el-aside>
      <div class="content">
        <el-header class="header-title">
          <el-card class="header-card">
            <h1>Contact Management System</h1>
          </el-card>
        </el-header>
        <el-main><RouterView /></el-main>
      </div>
    </el-container>
  </div>
</template>

<style scoped>
.common-layout {
  margin-left: 10%;
  margin-right: 10%;
}
.content {
  width: 100%;
}

.sidemenu-card{
  background-color: "#545c64";
}

.header-title{
  height: fit-content;
}

.header-card{
  min-height: 100px;
  display: flex;
  align-items: center;
}

</style>