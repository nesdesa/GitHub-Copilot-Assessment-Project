<script setup>
import { RouterLink, RouterView } from 'vue-router';
import Sidemenu from './components/Sidemenu.vue';
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <Sidemenu />
      </el-aside>
      <el-container>
        <el-header>
          <el-card>
            <h1>Contact Management System</h1>
          </el-card>
        </el-header>
        <el-main><RouterView /></el-main>
      </el-container>
    </el-container>
  </div>
</template>
