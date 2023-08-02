<template>
  <el-card>
    <template #header>
      <div class="card-header">
        <h1>Contact Details</h1>
      </div>
    </template>
    <el-form 
      :model="form" 
      label-width="120px"
      label-position="left"
      class="form-container">
      <el-form-item label="Name" :disabled="false">
        <el-autocomplete
          v-model="form.name"
          :fetch-suggestions="querySearchAsync"
          placeholder="Type Name"
          @select="handleSelect"
          :trigger-on-focus="false"
        />
      </el-form-item>
      <el-form-item label="Address" >
        <el-input v-model="form.address" :disabled="isDisabled"/>
      </el-form-item>
      <el-form-item label="Email">
        <el-input v-model="form.email" :disabled="isDisabled"/>
      </el-form-item>
      <el-form-item label="Contact Number">
        <el-input v-model="form.contact_number" :disabled="isDisabled"/>
      </el-form-item>
    </el-form>
    <div class="card-footer">
      <el-button 
        @click="isDisabled = !isDisabled" 
        v-show="isDisabled == true && form.id != ''">Edit</el-button>
      <el-button type="primary" 
        @click="handleUpdate" 
        v-show="isDisabled == false">Update</el-button>
        <el-popconfirm title="Confirm delete?" @confirm="handleDelete">
          <template #reference>
            <el-button type="danger" :disabled="isDisabled">Delete</el-button>
          </template>
        </el-popconfirm>
    </div>
  </el-card>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch } from 'vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'

interface LinkItem {
  id: string
  name: string
  email: string
  address: string
  contact_number: string
  value: string
}

const links = ref<LinkItem[]>([])

const loadAll = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/person');
    const dataWithAdditionalField = response.data.map((item) => ({
      ...item,
      value: item.name,
    }));
    return dataWithAdditionalField;
  } catch (error) {
    console.log(error);
    return [];
  }
};
let timeout: any;
const querySearchAsync = (queryString: string, cb: (arg: any) => void) => {
  const results = queryString
    ? links.value.filter(createFilter(queryString))
    : links.value
  
  clearTimeout(timeout)
  timeout = setTimeout(() => {
    cb(results)
  }, 3000 * Math.random())
}
const createFilter = (queryString: string) => {
  return (contact: LinkItem) => {
    return (
      contact.name.toLowerCase().indexOf(queryString.toLowerCase()) === 0 || 
      contact.email.toLowerCase().indexOf(queryString.toLowerCase()) === 0
    )
  }
}

onMounted(async () => {
  links.value = await loadAll();
  console.log("links", links.value);
})


const form = ref({
  id: '',
  name: '',
  email: '',
  address: '',
  contact_number: '',
})

const handleSelect = (item: LinkItem) => {
  form.value.id = item.id
  form.value.name = item.name
  form.value.email = item.email
  form.value.address = item.address
  form.value.contact_number = item.contact_number
}

const isDisabled = ref(true)

const handleUpdate = async () => {
  try {
    const response = await axios.put('http://127.0.0.1:8000/person/' + form.value.id, form.value);
    links.value = await loadAll();
    ElMessage({
      message: 'Contact successfully updated.',
      type: 'success',
    });
    isDisabled.value = !isDisabled.value
  } catch (error) {
    console.log(error);
    ElMessage({
      message: 'Oops, something went wrong when updating contact. Check console for more details.',
      type: 'error',
    });
  }
};

const handleDelete = async () => {
  try {
    const response = await axios.delete('http://127.0.0.1:8000/person/' + form.value.id);
    links.value = await loadAll();
    ElMessage({
      message: 'Contact successfully deleted.',
      type: 'success',
    });
    form.value.name = ''
  } catch (error) {
    console.log(error);
    ElMessage({
      message: 'Oops, something went wrong when deleting contact. Check console for more details.',
      type: 'error',
    });
  }
};

watch(
  () => form.value.name,
  (newValue, oldValue) => {
    if (newValue === '') {
      form.value.id = ''
      form.value.email = ''
      form.value.address = ''
      form.value.contact_number = ''
    } else {
      const item = links.value.find((item) => item.name === newValue);
      if (item) {
        form.value.id = item.id || '';
        form.value.email = item.email || '';
        form.value.address = item.address || '';
        form.value.contact_number = item.contact_number || '';
      } else {
        // If the newValue is not found in the list.value array, clear the fields.
        form.value.id = '';
        form.value.email = '';
        form.value.address = '';
        form.value.contact_number = '';
        isDisabled.value = true;
      }
    }
  }
);

</script>

<style scoped>
.card-footer{
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 0;
}

.form-container, .card-footer{
  margin: 0 20%;
}
</style>
