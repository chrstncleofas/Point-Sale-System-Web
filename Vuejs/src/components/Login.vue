<template>
  <div class="bg-darkGrayishBlue container mx-auto mt-11 p-5 rounded-lg shadow-lg">
    <h6 class="text-2xl font-bold text-center mb-2 text-lime-50">Welcome to our Point of Sales System</h6>
    <div class="grid md:grid-cols-2 gap-4">
      <!-- Icon Section -->
      <div class="flex items-center justify-center">
        <img src="../components/icons/Pos-Icon.png" class="w-9/12" alt="POS Icon">
      </div>
      <!-- Form Section -->
      <div class="flex flex-col justify-center">
        <form @submit.prevent="login" class="bg-white shadow-md rounded-lg px-4 md:px-8 py-8 mb-4">
          <div class="mb-4 relative">
            <input v-model="username" class="shadow appearance-none border rounded w-full py-2 px-10 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="Enter your username here">
            <img src="../components/icons/Username-Icon.png" class="absolute left-3 top-2 w-5 h-5" alt="Username Icon">
          </div>
          <div class="mb-4 relative">
            <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-10 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="password" placeholder="Enter your password here">
            <img src="../components/icons/Password-Icon.png" class="absolute left-3 top-2 w-5 h-5" alt="Password Icon">
          </div>
          <div class="flex items-center justify-between">
            <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full md:w-auto">
              Log In
            </button>
            <a class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">
              Forgot Password?
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const router = useRouter();
const username = ref('');
const password = ref('');
const toast = useToast();

const login = async () => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/login', {
            username: username.value,
            password: password.value
        });

        if (response.data.jwt) {
            toast.success('Login successful! Redirecting to Cashier page...');
            router.push('/cashier');
        } else {
            toast.error('Login failed. Please check your credentials.');
        }
    } catch (error) {
        console.error('Error:', error);
        toast.error('An error occurred. Please try again later.');
    }
};
</script>