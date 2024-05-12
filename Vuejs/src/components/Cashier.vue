<template>
   <div v-if="authenticated">
      <Navbar />
      <div id="main-container">
         <div class="container">
            <Main /> 
            <Rightside :firstName="firstName"/>
         </div>
      </div>
   </div>
   <div v-else>
      <div class="flex flex-col items-center justify-center h-screen">
         <h1 class="text-4xl font-bold text-red-500">404 Not Found</h1>
         <p class="text-lg text-gray-600 mt-4">The requested page could not be found.</p>
      </div>
   </div>
</template>

<script setup>
   import Navbar from './Navbar.vue';
   import Rightside from './Rightside.vue';
   import Main from './Main.vue';
   import { useRouter } from 'vue-router';
   import { ref, onMounted  } from 'vue';
   // Variables
   const authenticated = ref(false);
   const router = useRouter();
   const firstName = ref('');
   // Middleware is_authenticated
   onMounted(() => {
      const jwt = localStorage.getItem('jwt');
      authenticated.value = !!jwt;
      if (!authenticated.value) {
         router.push('/');
      }
      firstName.value = localStorage.getItem('firstName') || '';
   });
</script>
<!-- Style Section -->
<style scoped>
   body{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
   }
   #main-container{
      max-width: 1150px;
      margin: auto;
   }
   .container{
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 15px;
      margin-top: 70px;
   }

   @media (max-width: 430px) {
      #main-container{
         display: flex;
         justify-content: center;
         height: 50vh;
      }
      .container {
         display: flex;
         flex-direction: column;
         gap: 20px;
      }
   }

   @media screen and (max-width: 768px) {
      #main-container{
         display: flex;
         justify-content: center;
         height: 50vh;
      }
      .container {
         display: flex;
         flex-direction: column;
         gap: 15px;
      }
   }
</style>