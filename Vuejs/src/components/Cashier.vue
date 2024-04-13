<template>
  <div>
    <!-- Top Navbar -->
    <nav class="bg-gray-800 p-4 flex justify-between items-center">
      <!-- Branding -->
      <h1 class="text-white text-lg font-bold">Point of Sales System</h1>
      <!-- Logout Button -->
      <button @click="logout" class="text-white bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg">Logout</button>
    </nav>

    <!-- Content -->
    <div class="flex flex-col lg:flex-row h-screen">
      <!-- Sidebar -->
      <div class="bg-gray-800 text-white lg:w-64 flex-none">
        <!-- Sidebar content here -->
        <div class="p-4">
          <h2 class="text-lg font-bold mb-4">Menu</h2>
          <!-- Sample links -->
          <router-link to="/products" class="block py-2 px-4 text-white hover:bg-gray-700">Products</router-link>
          <router-link to="/sales" class="block py-2 px-4 text-white hover:bg-gray-700">Sales</router-link>
          <router-link to="/reports" class="block py-2 px-4 text-white hover:bg-gray-700">Reports</router-link>
        </div>
      </div>

      <!-- Main Content -->
      <div class="flex-grow p-4 lg:p-8">
        <!-- Main content here -->
        <h2 class="text-2xl font-bold mb-4">Welcome to the Cashier Page</h2>
        <!-- Sample content -->
        <p>Here you can manage your sales, view reports, and more.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useToast } from 'vue-toastification'; // Kung gumagamit ka ng toast para sa notipikasyon

const router = useRouter();
const toast = useToast();

// Function to handle logout
const logout = async () => {
  try {
    // Gumawa ng HTTP request para sa logout endpoint
    const response = await axios.post('http://127.0.0.1:8000/api/logout');
    
    // Suriin kung ang request ay matagumpay
    if (response.status === 200) {
      // Kung matagumpay ang pag-logout, i-redirect ang user sa login page
      router.push('/login');
      
      // Ipakita ang success message gamit ang toast
      toast.success('Logged out successfully.');
    } else {
      // Kung may hindi inaasahang error sa pag-logout, ipakita ang error message
      toast.error('An error occurred while logging out.');
    }
  } catch (error) {
    // Kapag may error sa pag-logout, ipakita ang error message
    toast.error('An error occurred while logging out.');
    console.error('Error logging out:', error);
  }
};
</script>

<style scoped>

</style>
