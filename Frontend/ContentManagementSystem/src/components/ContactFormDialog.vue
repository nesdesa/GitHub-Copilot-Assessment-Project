<template>
    <el-dialog v-model="isVisible" title="Contact Form" width="30%">
        <el-form :model="form">
            <el-form-item label="Name" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Address" :label-width="formLabelWidth">
                <el-input v-model="form.address" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Email" :label-width="formLabelWidth">
                <el-input v-model="form.email" autocomplete="off" />
            </el-form-item>
            <el-form-item label="Contact Number" :label-width="formLabelWidth">
                <el-input v-model="form.contact_number" autocomplete="off" />
            </el-form-item>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="handleConfirm">
                Confirm
                </el-button>
            </span>
        </template>
    </el-dialog>

</template>


<script setup>
import { ref, watch } from 'vue';
const props  = defineProps(['dialogFormVisible','form']);
const emit = defineEmits(['submittedForm']);
const formLabelWidth = '140px';

const isVisible = ref(false);
const form = ref({
    id: '',
    name: '',
    address: '',
    email: '',
    contact_number: ''
});

watch(props, () => {
    isVisible.value = props.dialogFormVisible;
    form.value = props.form;
})

function handleConfirm(){
    emit('submittedForm', form.value);
}
</script>


