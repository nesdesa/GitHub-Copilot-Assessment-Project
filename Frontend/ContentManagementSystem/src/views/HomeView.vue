<template>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h1>Contacts</h1>
        <el-button type="primary">New Contact</el-button>
      </div>
    </template>
    <el-table :data="filteredData" style="width: 100%">
      <el-table-column label="Name" prop="name" />
      <el-table-column label="Address" prop="address" />
      <el-table-column label="Email" prop="email" />
      <el-table-column label="Contact No." prop="contact_number" />
      <el-table-column align ="right">
        <template #header>
          <el-input v-model="search" size="small" placeholder="Search.." />
        </template>
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
            >Edit</el-button
          >
          <el-button
            size="small"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >Delete</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </el-card>
</template>

<script setup>

import { ref, computed, onMounted, watch } from 'vue';
import axios from 'axios';


// table data from api using axios
const tableData = ref([]);
const search = ref('');

function getTableData() {
  axios
    .get('http://127.0.0.1:8000/list?search=' + search.value)
    .then((response) => {
      tableData.value = response.data;
      console.log(tableData.value);
    })
    .catch((error) => {
      console.log(error);
    });
}

const filteredData = computed(() => {
  return tableData.value;
});

onMounted(() => {
  getTableData();
});

watch(search, () => {
  getTableData();
});

function handleDelete(index, row) {
  console.log(index, row);
}

function handleEdit(index, row) {
  console.log(index, row);
}


</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-card {
  width: 100%;
}
</style>
