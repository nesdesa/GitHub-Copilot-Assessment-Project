<template>
  <div>
    <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <h1>Contacts</h1>
            <el-button type="primary" @click="handleCreate()">New Contact</el-button>
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
              <el-button size="small" @click="handleEdit(scope.row)"
                >Edit</el-button
              >
              <el-popconfirm title="Confirm delete?" @confirm="handleDelete(scope.row)">
                <template #reference>
                  <el-button size="small" type="danger">Delete</el-button>
                </template>
              </el-popconfirm>
              
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          :hide-on-single-page="paginationIsHidden"
          :total="total"
          v-model="currentPage"
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
        />
      </el-card>
      <ContactFormDialog :dialog-form-visible="dialogFormVisible" :form="form" @submittedForm="handleConfirm"/>
  </div>
  
</template>

<script setup>

import { ref, computed, onMounted, watch } from 'vue';
import axios from 'axios';
import ContactFormDialog from '../components/ContactFormDialog.vue';
import { ElMessage } from 'element-plus';
import { inject } from 'vue'

const api = inject('api')

// table data from api using axios
const tableData = ref([]);
const search = ref('');
const paginationIsHidden = ref(false);
const total = ref(0);
const currentPage = ref(1);

function getTableData() {
  axios
    .get(
      api +'/list?search=' + 
      search.value +
      '&ordering=' + 
      'name' + 
      '&page=' + 
      currentPage.value)
    .then((response) => {
      tableData.value = response.data.results;
      total.value = response.data.count;
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

watch(tableData, () => {
  if (total <= 1) {
    paginationIsHidden.value = true;
  }
  else {
    paginationIsHidden.value = false;
  }
});


function handleCurrentChange(val) {
  currentPage.value = val;
  getTableData();
}


// create, edit and delete functions
const form = ref({
  id: '',
  name: '',
  address: '',
  email: '',
  contact_number: '',
});
const dialogFormVisible = ref(false);
const isNew = ref(true);

function handleCreate() {
  form.value = {
    id: '',
    name: '',
    address: '',
    email: '',
    contact_number: '',
  }
  dialogFormVisible.value = true;
  isNew.value = true;
}

function handleDelete(row) {
  axios
    .delete(api + '/person/' + row.id)
    .then((response) => {
      getTableData();
      ElMessage({
        message: 'Contact successfully deleted.',
        type: 'success',
      })
    })
    .catch((error) => {
      console.log(error);
      ElMessage({
        message: 'Oops, something went wrong when deleting contact. Check console for more details',
        type: 'error',
      })
    });
}

function handleEdit(row) {
  form.value = {
    id: row.id,
    name: row.name,
    address: row.address,
    email: row.email,
    contact_number: row.contact_number,
  }
  dialogFormVisible.value = true;
  isNew.value = false;
}

function handleConfirm(submittedForm) {
  form.value = submittedForm;
  dialogFormVisible.value = false;
  if (isNew.value == true) {
    postForm();
  }
  else {
    putForm();
  }
}

function postForm() {
  axios
    .post(api + '/person/', form.value)
      .then((response) => {
        getTableData();
        ElMessage({
          message: 'Contact successfully created.',
          type: 'success',
        })
      })
      .catch((error) => {
        console.log(error);
        ElMessage({
          message: 'Oops, something went wrong when creating contact. Check console for more details',
          type: 'error',
        })
      });
}

function putForm() {
  axios
    .put(api + '/person/' + form.value.id, form.value)
      .then((response) => {
        getTableData();
        ElMessage({
          message: 'Contact successfully created.',
          type: 'success',
        })
      })
      .catch((error) => {
        console.log(error);
        ElMessage({
          message: 'Oops, something went wrong when creating contact. Check console for more details',
          type: 'error',
        })
      });
}

watch (form, () => {
  console.log(form.value);
})

</script>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.box-card {
  width: 100%;
  min-height: 500px;
  max-height: 100vh;
}
</style>
