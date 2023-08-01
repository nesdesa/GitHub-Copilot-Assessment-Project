<template>
    <el-card class="box-card">
        <img src="../assets/fullscale_logo.png" alt="Full Scale Logo">
        <el-divider border-style="double" />
        <el-menu
            default-active="1"
            class="el-menu-vertical"
        >
            <el-menu-item index="1">
                <RouterLink to="/" class="menu-link"><h1>Home</h1></RouterLink>
            </el-menu-item>
            <el-menu-item index="2">
                <RouterLink to="/details" class="menu-link"><h1>Details</h1></RouterLink>
            </el-menu-item>
        </el-menu>
    </el-card>
    
</template>
    
<script setup> 
import { RouterLink } from 'vue-router'
</script>

<style scoped>
img {
    width: 100%;
    max-height: 200px;
    object-fit: contain;
}
.box-card {
    width: 200px;
    height: 100vh;
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
  background-color: #f5f5f5; /* Add a background color on hover */
}
</style>