<script setup>
import axios from 'axios';
import { ref } from 'vue';

const generateSoal = ref('')
const parseTrees = ref([]);

const generateParseTree = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/test', {
      // sentence: generateSoal.value, // Replace with your sentence
      sentences: generateSoal.value,
    });

    // const json = await response.json()

    // Assuming the response data is an array of parse trees
    parseTrees.value = response.data.result; //ubah sesuai dengan kebutuhan

    console.log(response);
    // Handle the response data as needed
  } catch (error) {
    console.error(error);
  }
};

</script>

<template>
  <div class="w-100 h-screen bg-[#F2F2F2]">
    <div class="m-auto w-4/5 pt-14 pb-10">
      <div id="app" class="grid grid-cols-3 gap-6">
        <div class="bg-white p-6 font-bold text-xl text-[#11111] rounded-xl">
          <form @submit.prevent="generateParseTree">
            <h1>Mulai Generate Soal</h1>
            <div class=" relative mt-10">
              <label for="name-with-label" class="text-gray-700">
                Subject (*Materi)
              </label>
              <textarea id="sentenceInput" rows="7"
                class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 shadow-sm mt-2"
                name="sentence" v-model="generateSoal" placeholder="Tulis kalimat anda...."></textarea>
            </div>
            <button type="submit" class="mt-10 button bg-[#4C37EE] text-white px-4 py-3 rounded-lg w-full">Generate
              Soal</button>
          </form>
        </div>

        <div class="col-span-2 bg-white p-6 font-bold text-xl text-[#11111] rounded-xl">
          <h1>Hasil generate soal</h1>
          <div v-for="(tree, index) in parseTrees" :key="index">
            <pre>{{ tree }}</pre>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

