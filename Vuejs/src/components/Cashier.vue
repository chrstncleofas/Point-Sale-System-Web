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
</style>