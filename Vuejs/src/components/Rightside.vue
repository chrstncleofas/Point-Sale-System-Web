<template>
    <div class="right-side">
      <div class="table-container">
        <table class="shadow-2xl shadow-gray-100">
          <thead class="p-3">
            <tr>
              <th>Item Name</th>
              <th>Qty</th>
              <th>Price</th>
              <th>Delete</th>
            </tr>
          </thead>
          <tbody class="text-center">
            <tr v-for="(item, index) in cartItems" :key="index">
              <td>{{ item.ProductName }}</td>
              <td>
                <div class="flex items-center justify-center">
                  <button @click="decrement(item)" class="px-2 py-1 rounded-l bg-gray-200">
                    <i class="fas fa-minus"></i>
                  </button>
                  <input type="text" :value="item.quantity" class="px-1 py-1 text-center w-16" disabled />
                  <button @click="increment(item)" class="px-2 py-1 rounded-r bg-gray-200">
                    <i class="fas fa-plus"></i>
                  </button>
                </div>
              </td>
              <td>{{ item.totalPrice }}</td>
              <td>
                <button @click="removeFromCart(index)"><i class="fas fa-trash"></i></button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="section-b bg-gray-800 text-white">
        <div class="content">
          <div>
            <h5 class="font-bold">Subtotal</h5>
            <h5 class="font-bold">Total</h5>
          </div>
          <div class="amout">
            <h6>{{ formatCurrency(subtotal) }}</h6>
            <h6>Php 550</h6>
          </div>
        </div>
        <div class="section-c mt-5">
          <div class="mb-3 fields">
            <label for="" class="mb-2">Amount:</label>
            <input type="text" class="h-9 rounded text-neutral-950 pl-3">
          </div>
          <div class="fields">
            <label for="" class="mb-2">Change:</label>
            <input type="text" class="h-9 rounded text-neutral-950 pl-3">
          </div>
        </div>
        <div class="button">
          <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-11 h-9 rounded mt-4 float-right">
            Pay
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed, watch } from 'vue';
  import { useStore } from 'vuex';
  
  const store = useStore();
  const cartItems = computed(() => store.getters.cartItems);
  
  // Compute subtotal and total price
  const subtotal = computed(() => {
    return cartItems.value.reduce((acc, item) => acc + item.totalPrice, 0);
  });
  
  const total = computed(() => {
    // Here you can add any additional charges like tax or shipping if needed
    return subtotal.value;
  });
  
  // Format currency function
  const formatCurrency = (amount) => {
    if (typeof amount !== 'number') {
      return 'Php 0.00'; // default value or handle error accordingly
    }
    return 'Php ' + amount.toFixed(2);
  };
  
  // Remove item from cart
  const removeFromCart = (index) => {
    store.dispatch('removeFromCart', index);
  };
  
  // Increment quantity of item
  const increment = (item) => {
    const index = cartItems.value.findIndex(cartItem => cartItem.ProductID === item.ProductID);
    if (index !== -1) {
      store.dispatch('incrementQuantity', index);
    }
  };
  
  // Decrement quantity of item
  const decrement = (item) => {
    const index = cartItems.value.findIndex(cartItem => cartItem.ProductID === item.ProductID);
    if (index !== -1 && cartItems.value[index].quantity > 1) {
      store.dispatch('decrementQuantity', index);
    }
  };
  
  // Watch cartItems for changes and recompute subtotal accordingly
  watch(cartItems, () => {
    // Recompute subtotal
    subtotal.value = cartItems.value.reduce((acc, item) => acc + item.totalPrice, 0);
  });
  </script>
<style scoped>
  .right-side {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  .table-container {
    width: 100%;
    background-color: #fff;
    max-height: 300px;
    overflow-y: auto;
  }
  .table-container table {
    width: 100%;
    border-collapse: collapse;
  }
  .table-container th, .table-container td {
    padding: 8px;
    border: 1px solid #ddd;
  }
  .section-b {
    padding: 25px;
  }
  .section-b h5 {
    line-height: 2.2;
  }
  .content {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
  .amout {
    display: flex;
    justify-content: flex-end;
    flex-direction: column;
    align-items: last baseline;
  }
  .content h6 {
    line-height: 2.2;
  }
  .section-c {
    display: flex;
    flex-direction: column;
  }
  .fields {
    display: flex;
    flex-direction: column;
  }
  .button {
    display: flex;
    justify-content: flex-end;
  }
</style>
  