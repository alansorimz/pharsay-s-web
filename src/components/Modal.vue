<script setup>
const emit = defineEmits(['close'])

const closeModal = () => {
    emit('close');
};

const props = defineProps({
    show: Boolean,
    title: String,
    message: String
})
</script>

<template>
    <input class="modal-state" id="modal-1" type="checkbox" v-model="props.show" />
    <div class="modal">
        <div class="modal-content flex flex-col gap-5">
            <h2 class="text-xl text-slate-800 font-bold">{{ props.title }}</h2>
            <span>{{ props.message }}</span>
            <div class="flex">
                <button class="btn btn-block" @click="closeModal">Tutup</button>
            </div>
        </div>
    </div>
</template>