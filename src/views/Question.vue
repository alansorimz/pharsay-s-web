<script setup>
import axios from 'axios';
import { computed, ref, watch } from 'vue';
import Modal from '../components/Modal.vue'

const generateSoal = ref('')
const parseTrees = ref([]);
const showQuestions = ref(false)
const errorRes = ref({
  show: false,
  message: ""
})
const dataTooltips = ref([
  'Soal tipe definisi',
  'Soal tipe objek/subjek',
  'Soal tipe fungsi',
  'Soal tipe tahapan',
  'Soal tipe lokasi',
  'Soal tipe waktu',
  'Soal tipe sebab/akibat',
  'Soal tipe validasi',
  // 'Soal tipe klasifikasi',
  'Soal tipe jawaban singkat',
  'Soal tipe analisis'
])

const generateParseTree = async () => {
  try {
    if (generateSoal.value.trim() === '') return;
    const response = await axios.post('http://127.0.0.1:5000/test', {
      // sentence: generateSoal.value, // Replace with your sentence
      sentences: generateSoal.value,
    });

    // const json = await response.json()

    // Assuming the response data is an array of parse trees
    parseTrees.value = response.data.result; //ubah sesuai dengan kebutuhan
    // Handle the response data as needed
  } catch (error) {
    errorRes.value = {
      show: true,
      message: error.response.data.error
    }
  }
};

const removeRedundantWords = (sentence) => {
  let strArr = sentence.split(" ")

  strArr.forEach((word, idx) => {
    const nextIdx = idx + 1;
    if (word === strArr[nextIdx]) strArr.splice(nextIdx, 1)
  });

  const normalizedSentence = strArr.join(" ")
  return normalizedSentence
}

const concateSentences = computed(() => {
  return parseTrees.value.map((tree) => removeRedundantWords(tree))
})

const hideModal = () => {
  errorRes.value = {
    ...errorRes.value,
    show: false
  }
};

watch(parseTrees, () => {
  if (concateSentences.value?.length && concateSentences.value?.length != 0) showQuestions.value = true
})

</script>

<template>
  <div class="w-100 min-h-screen bg-[#F2F2F2]">
    <div class="m-auto w-4/5 pt-14 pb-10">
      <div id="app" class="grid grid-cols-12 gap-6">
        <div class="col-span-12 lg:col-span-4 bg-white p-6 font-bold text-xl text-slate-900 rounded-xl">
          <form @submit.prevent="generateParseTree">
            <h1>Mulai Generate Soal</h1>
            <div class=" relative mt-10">
              <label for="name-with-label" class="text-gray-700">
                Subject (*Materi)
              </label>
              <textarea id="sentenceInput" rows="7"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 shadow-sm mt-2"
                name="sentence" v-model="generateSoal" placeholder="Tulis kalimat anda...."
                @keyup.enter="generateParseTree"></textarea>
            </div>
            <button type="submit" class="mt-10 button bg-[#4C37EE] text-white px-4 py-3 rounded-lg w-full">Generate
              Soal</button>
          </form>
        </div>

        <div class="col-span-12 lg:col-span-8 bg-white p-6 font-bold text-xl text-slate-900 rounded-xl">
          <h1>Hasil generate soal</h1>
          <section v-if="showQuestions" v-for="(_tree, index) in  parseTrees " :key="index" class="mb-5 mt-3">
            <div>
              <span
                class="tooltip tooltip-top text-xs bg-slate-700 px-2 py-0.5 rounded-md text-white text-opacity-90 font-medium cursor-pointer"
                :data-tooltip="dataTooltips[index] ?? '-'">
                Soal Tipe {{ index + 1 }}
              </span>
              <p v-if="concateSentences[index] != '-'" class="mt-1 text-base font-bold text-slate-900">{{
                concateSentences[index] }}</p>
              <p v-else class="mt-1 text-sm font-medium text-gray-500">Tipe soal tidak mendukung kalimat ini</p>
            </div>
          </section>
          <section v-else class="h-full flex items-center justify-center min-h-[150px]">
            <p class="text-sm text-gray-500">Belum ada daftar pertanyaan</p>
          </section>
        </div>
      </div>
    </div>
  </div>
  <Modal :show="errorRes.show" title="Peringatan!" :message="errorRes.message" @close="hideModal" />
</template>

