<template>
   <Navbar />
   <div id="main-container">
      <div class="container">
         <Main /> 
         <Rightside />
      </div>
   </div>
</template>

<script setup>
import Navbar from './Navbar.vue';
import Rightside from './Rightside.vue';
import Main from './Main.vue';
</script>

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