<template>
  <div class="bg-gray-800 text-white fixed top-0 left-0 w-full z-50">
    <div class="flex justify-between items-center px-4 py-2">
      <div>
        <img src="../components/icons/Pos-Icon.png" class="w-10 h-10">
      </div>
      <div class="hidden lg:flex justify-">
        <router-link to="/product" class="py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-box-open"></i>
          </span>Products
        </router-link>
        <router-link to="/sales" class="py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-cash-register"></i>
          </span>Sales
        </router-link>
        <router-link to="/reports" class="py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-chart-bar"></i>
          </span>Reports
        </router-link>
      </div>
      <div class="flex items-center space-x-4">
        <button @click="toggleSidebar" class="lg:hidden text-white focus:outline-none">
          <i class="fas fa-bars"></i>
        </button>
        <button @click="openLogoutModal" class="hidden lg:block py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-sign-out-alt"></i>
          </span>Logout
        </button>
      </div>
    </div>
    <div :class="{'block': isSidebarOpen, 'hidden': !isSidebarOpen}" class="lg:hidden">
      <div class="pt-2 pl-4 pr-5">
        <router-link to="/products" class="block py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-box-open"></i>
          </span>Products
        </router-link>
        <router-link to="/sales" class="block py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-cash-register"></i>
          </span>Sales
        </router-link>
        <router-link to="/reports" class="block py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-chart-bar"></i>
          </span>Reports
        </router-link>
        <button @click="openLogoutModal" class="block py-2 px-4 text-white hover:bg-gray-700">
          <span class="mr-2">
            <i class="fas fa-sign-out-alt"></i>
          </span>Logout
        </button>
      </div>
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
</template>

<script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  const showLogoutModal = ref(false);
  const isSidebarOpen = ref(false);

  const openLogoutModal = () => {
    showLogoutModal.value = true;
  };

  const toggleSidebar = () => {
    isSidebarOpen.value = !isSidebarOpen.value;
  };

  const confirmLogout = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/logout');
      if (response.status === 200) {
        localStorage.removeItem('jwt');
        router.push('/');
      } else {
        console.error('An error occurred while logging out.');
      }
    } catch (error) {
      console.error('Error logging out:', error);
    }
  };

  const cancelLogout = () => {
    showLogoutModal.value = false;
  };
</script>
