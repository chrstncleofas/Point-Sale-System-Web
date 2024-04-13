<template>
    <nav class="bg-gray-800 p-4 flex items-center justify-between">
      <div class="flex items-center">
        <span class="text-white text-lg font-semibold">POS System</span>
      </div>
      <div>
        <button @click="goToLogin" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Login</button>
      </div>
    </nav>
</template>
  
<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();
const goToLogin = () => {
    router.push('/login');
};
</script>
  