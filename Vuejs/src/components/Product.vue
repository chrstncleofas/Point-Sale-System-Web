<template>
  <div class="item-container">
      <div v-for="product in products" :key="product.ProductID" class="item bg-white mb-5">
          <img src="../components/icons/Product-01.jpg" class="w-15 h-15">
          <h6 class="font-bold">{{ product.ProductName }}</h6>
          <p class="text-xs font-semibold">Php {{ product.SellingPrice }}</p>
          <button type="submit" @click="addToCart(product)" class="bg-brightRed shadow-box w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
      </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
const products = ref([]);

async function fetchProducts() {
try {
  const response = await fetch('http://127.0.0.1:8000/inventory');
  const data = await response.json();
  products.value = data;
} catch (error) {
  console.error('Error fetching products:', error);
}
}

const addToCart = (product) => {
  store.dispatch('addToCart', product);
};

fetchProducts();
</script>

<style scoped>
.item-container{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  overflow-y: auto;
  max-height: 1000px;
  padding: 20px;
}
.item{
  width: 90%;
  height: 240px;
  background-color: #fff;
  padding: 10px;
  border-radius: 5px;
}
.shadow-box{
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.668);
}
</style>
