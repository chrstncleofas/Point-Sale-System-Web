<template>
  <div class="item-container">
      <div v-for="product in products" :key="product.ProductID" class="item bg-white mb-5">
          <img src="../components/icons/Product-01.jpg" class="w-15 h-15 product-img">
          <h6 class="font-bold hidden">{{ product.ProductID }}</h6>
          <h6 class="font-bold">{{ product.ProductName }}</h6>
          <p class="text-xs font-semibold">Php {{ product.SellingPrice }}</p>
          <p class="text-xs font-semibold hidden">{{ product.Description }}</p>
          <button type="submit" @click="addToCart(product)" class="bg-brightRed shadow-box w-20 h-7 rounded mt-4 float-right text-xs text-white btn-Add">Add to Cart</button>
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

  fetchProducts();
  const addToCart = (product) => {
    store.dispatch('addToCart', product);
  };
  
</script>

<style scoped>
.item-container{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  height: 900px;
  overflow-y: auto;
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

@media screen and (max-width: 430px) {
  .item-container{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    overflow-y: auto;
    height: 50vh;
  }
  .item{
    width: 90%;
    height: 170px;
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
  }
  .item h6{
    font-size: 10px;
  }
  .item p{
    font-size: 8.5px;
  }
  .item .btn-Add{
    width: 60px;
    font-size: 9px;
    height: 20px;
    margin-top: 1px;
  }
}

@media screen and (max-width: 550px) {
  .item-container{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    height: 50vh;
    overflow-y: auto;
  }
  .item{
    width: 90%;
    height: 170px;
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
  }
  .item h6{
    font-size: 10px;
  }
  .item p{
    font-size: 8.5px;
  }
  .item .btn-Add{
    width: 60px;
    font-size: 9px;
    height: 20px;
    margin-top: 9px;
  }
  .item img.product-img{
    width: 85%;
    height: 59%;
    text-align: center;
    margin-left: 10px;
  }
}

@media screen and (min-width: 568px) {
  .item-container{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    height: 60vh;
    overflow-y: auto;
  }
  .item{
    width: 90%;
    height: 210px;
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
  }
  .item h6{
    font-size: 12px;
  }
  .item p{
    font-size: 10px;
  }
  .item .btn-Add{
    width: 73px;
    font-size: 12px;
    height: 30px;
    margin-top: 10px;
  }
}

@media screen and (min-width: 768px) {
  .item-container{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    height: 65vh;
    overflow-y: auto;
  }
  .item{
    width: 90%;
    height: 225px;
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
  }
  .item h6{
    font-size: 11px;
  }
  .item p{
    font-size: 9px;
  }
  .item .btn-Add{
    width: 65px;
    font-size: 10px;
    height: 22px;
    margin-top: 10px;
  }
}

</style>
