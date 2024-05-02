<template>
  <div class="bg-white md:bg-darkGrayishBlue min-h-screen flex items-start justify-center py-10">
    <div class="bg-white md:bg-white container mt-10 mx-auto px-4 md:px-8 py-8 rounded-lg md:shadow-lg w-full max-w-md">
      <h6 class="text-xl md:text-2xl font-bold text-center mb-6 text-yellow-900">Point of Sales System</h6>
      <form @submit.prevent="login" class="mb-4 xxl:m-3">
        <div class="mb-6 relative">
          <input v-model="username" class="shadow appearance-none border rounded w-full py-2 px-3 md:px-10 text-gray-700 leading-tight focus:outline-none focus:shadow-outline pl-10 xxl:pl-3" type="text" placeholder="Enter your username..">
          <img src="../components/icons/Username-Icon.png" class="absolute left-3 top-2 w-5 h-5" alt="Username Icon">
        </div>
        <div class="mb-6 relative">
          <input v-model="password" class="shadow appearance-none border rounded w-full py-2 px-3 md:px-10 text-gray-700 leading-tight focus:outline-none focus:shadow-outline pl-10 xxl:pl-3" type="password" placeholder="Enter your password..">
          <img src="../components/icons/Password-Icon.png" class="absolute left-3 top-2 w-5 h-5" alt="Password Icon">
        </div>
        <div class="flex items-center justify-between">
          <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline block text-center">Log In</button>
          <a class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800" href="#">Forgot Password?</a>
        </div>
      </form>
      <h6 class="text-xs text-center mt-6 text-yellow-900">&#169; Christian Cleofas All right reserved</h6>
    </div>
    <div v-if="showModal" class="fixed z-10 inset-0 overflow-y-auto" aria-labelledby="modal-title" role="dialog" aria-modal="true">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true"></div>
        <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-green-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
                  Login Successful
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    You have successfully logged in. Redirecting to Cashier page...
                  </p>
                </div>
              </div>
            </div>
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
  const username = ref('');
  const password = ref('');
  const showModal = ref(false);

  const login = async () => {
      try {
          const response = await axios.post('http://127.0.0.1:8000/login', {
              username: username.value,
              password: password.value
          });

          if (response.data.jwt) {
              localStorage.setItem('jwt', response.data.jwt);
              showModal.value = true;
              setTimeout(() => {
                  router.push('/cashier');
              }, 400);
          } else {
              alert('Login failed. Please check your credentials.');
          }
      } catch (error) {
          console.error('Error:', error);
          alert('An error occurred. Please try again later.');
      }
  };
</script>
