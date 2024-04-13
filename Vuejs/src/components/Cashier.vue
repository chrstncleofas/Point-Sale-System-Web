<template>
  <div>
    <nav class="bg-gray-800 p-4 flex justify-between items-center">
      <h1 class="text-white text-lg font-bold">Point of Sales System</h1>
      <button @click="openLogoutModal" class="text-white bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg">Logout</button>
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
    <!-- Logout Modal -->
    <div v-if="showLogoutModal" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                <!-- Heroicon name: exclamation -->
                <svg class="h-6 w-6 text-red-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.474-1.652 1.688-2.942l-5.226-9.12a1.5 1.5 0 00-2.573 0l-5.226 9.12c-.786 1.29.148 2.942 1.688 2.942z"></path>
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                  Logout Confirmation
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    Are you sure you want to logout?
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button @click="confirmLogout" type="button" class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm">
              Logout
            </button>
            <button @click="cancelLogout" type="button" class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const showLogoutModal = ref(false);

const openLogoutModal = () => {
  showLogoutModal.value = true;
};

const confirmLogout = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/logout');
    
    if (response.status === 200) {
      router.push('/');
    } else {
      console.error('An error occurred while logging out.');
    }
  } catch (error) {
    console.error('Error logging out:', error);
  } finally {
    showLogoutModal.value = false;
  }
};

const cancelLogout = () => {
  showLogoutModal.value = false;
};
</script>
