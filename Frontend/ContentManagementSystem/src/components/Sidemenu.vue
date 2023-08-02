<template>
    <div class="box-card">
        <img src="../assets/fullscale_logo.png" alt="Full Scale Logo">
        <el-divider border-style="double" />
        <el-menu
            default-active="1"
            class="el-menu-vertical"
            active-text-color="#2ab52e"
            background-color="transparent"
        >
            <RouterLink to="/" class="menu-link">
                <el-menu-item index="1">
                    <el-icon><House /></el-icon>
                    <h1>Home</h1>
                </el-menu-item>
            </RouterLink>
            <RouterLink to="/details" class="menu-link">
                <el-menu-item index="2">
                    <el-icon><User /></el-icon>
                    <h1>Details</h1>
                </el-menu-item>
            </RouterLink>
        </el-menu>
    </div>
    
    
</template>
    
<script setup> 
import { RouterLink } from 'vue-router'
import {
  House,
  User
} from '@element-plus/icons-vue'

</script>

<style scoped>
img {
    width: 100%;
    max-height: 200px;
    object-fit: contain;
}
.box-card {
    width: 100%;
    height: 75vh;
    display: flex;
    flex-direction: column;
}
.menu-link {
  text-decoration: none;
  color: #333; /* Change the link color to your desired color */
}

/* Optionally, you can add some hover effects for better appearance */
.menu-link:hover {
  color: #2ab52e; /* Change the hover color to your desired color */
}
</style>