<template>
  <div>
    <nav class="bg-gray-800 p-4 flex justify-between items-center">
      <h1 class="text-white text-lg font-bold">Point of Sales System</h1>
      <button @click="logout" class="text-white bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg">Logout</button>
    </nav>
    <div class="flex flex-col lg:flex-row h-screen">
      <div class="bg-gray-800 text-white lg:w-64 flex-none">
        <div class="p-4">
          <h2 class="text-lg font-bold mb-4">Menu</h2>
          <router-link to="/products" class="block py-2 px-4 text-white hover:bg-gray-700">Products</router-link>
          <router-link to="/sales" class="block py-2 px-4 text-white hover:bg-gray-700">Sales</router-link>
          <router-link to="/reports" class="block py-2 px-4 text-white hover:bg-gray-700">Reports</router-link>
        </div>
      </div>
      <div class="flex-grow p-4 lg:p-8">
        <h2 class="text-2xl font-bold mb-4">Welcome to the Cashier Page</h2>
        <p>Here you can manage your sales, view reports, and more.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';

const router = useRouter();
const toast = useToast();

const logout = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/logout');
    
    if (response.status === 200) {
      router.push('/login');
      
      toast.success('Logged out successfully.');
    } else {
      toast.error('An error occurred while logging out.');
    }
  } catch (error) {
    toast.error('An error occurred while logging out.');
    console.error('Error logging out:', error);
  }
};
</script>