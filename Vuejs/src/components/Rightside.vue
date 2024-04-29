<template>
    <div class="right-side">
      <div class="cashier-transid">
        <div class="content">
          <div>
            <input type="text" :id="transactionID" value="TRAN001">
          </div>
          <div>
            <h6 id="cashierName">TianTzy</h6>
            <h6 id="date_time">04-23-2024 - 10:00</h6>
          </div>
        </div>
      </div>
      <div class="table-container">
        <table class="shadow-2xl shadow-gray-100">
          <thead class="p-3">
            <tr>
              <th class="text-xs font-semibold">No.</th>
              <th class="text-xs font-semibold">Name</th>
              <th class="text-xs font-semibold">Description</th>
              <th class="text-xs font-semibold">Qty</th>
              <th class="text-xs font-semibold">Price</th>
              <th class="text-xs font-semibold">Total</th>
              <th class="text-xs font-semibold">Action</th>
            </tr>
          </thead>
          <tbody class="text-center">
            <tr v-for="(item, index) in cartItems" :key="index">
              <td id="product_id" class="text-xs font-light">{{ item.ProductID }}</td>
              <td id="productName" class="text-xs font-light">{{ item.ProductName }}</td>
              <td id="description" class="text-xs font-light">{{ item.Description }}</td>
              <td class="text-xs font-light">
                <div class="flex items-center justify-center">
                  <button @click="decrement(item)" class="px-2 py-1 rounded-l bg-gray-200">
                    <i class="fas fa-minus"></i>
                  </button>
                  <input id="qty" type="text" :value="item.quantity" class="px-1 py-1 text-center w-16" disabled />
                  <button @click="increment(item)" class="px-2 py-1 rounded-r bg-gray-200">
                    <i class="fas fa-plus"></i>
                  </button>
                </div>
              </td>
              <td id="unitPrice" class="unit-price text-slate-900 text-xs font-light">{{ formatCurrency(item.SellingPrice) }}</td>
              <td class="text-xs font-light">{{ formatCurrency(item.totalPrice) }}</td>
              <td class="text-xs font-light">
                <button @click="removeFromCart(index)"><i class="fas fa-trash"></i></button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="section-b bg-gray-800 text-white">
        <div class="content">
          <div>
            <h5 class="font-bold">Total Amount</h5>
          </div>
          <div class="amout">
            <h6 id="totalAmount">{{ formatCurrency(subtotal) }}</h6>
          </div>
        </div>
        <div class="section-c mt-5">
          <div class="mb-3 fields">
            <label for="" class="mb-2">Amount:</label>
            <input type="number" class="h-9 rounded text-neutral-950 pr-1 text-right" v-model="amount" @keyup.enter="handleEnterKeyPress" placeholder="₱0.00">
          </div>
          <div class="fields">
            <label for="" class="mb-2">Change:</label>
            <input type="text" class="h-9 rounded text-neutral-950 pr-5 text-right" :value="formatCurrency(change)">
          </div>
        </div>
        <div class="button">
          <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-11 h-9 rounded mt-4 float-right" @click="handlePayment()"> 
            Pay
          </button>
        </div>
      </div>
    </div>
    <!-- Modal for Transaction Success -->
    <div class="modal" v-if="showSuccessModal">
      <div class="modal-content">
        <p>Transaction Success</p>
      </div>
    </div>
  </template>
  
 <script setup>
  import { computed, watch, ref } from 'vue';
  import { useStore } from 'vuex';
  import axios from 'axios';
  
  const store = useStore();
  const cartItems = computed(() => store.getters.cartItems);
  const change = ref(0);
  const transactionID = ref('TRAN001');
  let amount = '';
  const showSuccessModal = ref(false);

  const handlePayment = async () => {
    try {
      await saveToDatabase();
      showSuccessModal.value = true;
      setTimeout(() => {
        location.reload();
      }, 600);
    } catch (error) {
      console.error('Error saving data:', error);
    }
  };
  
  const subtotal = computed(() => {
    return cartItems.value.reduce((acc, item) => 
        acc + item.totalPrice, 0
      );
    });
  
  const computeChange = () => {
    const inputAmount = parseFloat(amount);
    if (!isNaN(inputAmount)) {
      change.value = inputAmount - subtotal.value;
    } else {
      change.value = 0;
    }
    change.value = parseFloat(change.value.toFixed(2));
  };

  const handleEnterKeyPress = (event) => {
    if (event.key === 'Enter') {
      console.log('Enter key pressed');
      computeChange();
    }
  };

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('en-PH', {
      style: 'currency',
      currency: 'PHP',
    }).format(value);
  };
  
  const removeFromCart = (index) => {
    store.dispatch('removeFromCart', index);
  };
  
  const increment = (item) => {
    const index = cartItems.value.findIndex(cartItem => cartItem.ProductID === item.ProductID);
    if (index !== -1) {
      store.dispatch('incrementQuantity', index);
    }
  };

  const decrement = (item) => {
    const index = cartItems.value.findIndex(cartItem => cartItem.ProductID === item.ProductID);
    if (index !== -1 && cartItems.value[index].quantity > 1) {
      store.dispatch('decrementQuantity', index);
    }
  };
  
  watch(cartItems, () => {
    subtotal.value = cartItems.value.reduce((acc, item) => 
      acc + item.totalPrice, 0
    );
  });

  async function saveToDatabase() {
    try {
      const item = cartItems.value[0];
      const payload = {
        TransactionID: transactionID.value,
        ProductID: item.ProductID,
        ProductName: item.ProductName,
        Description: item.Description,
        Qty: parseInt(item.quantity),
        UnitPrice: parseFloat(item.SellingPrice),
        TotalAmount: parseFloat(subtotal.value),
        DateTime: new Date().toISOString(),
        CashierName: 'TianTzy'
      };

      const response = await axios.post('http://127.0.0.1:8000/saveTransaction/', payload);
      console.log('Data saved successfully:', response.data);
    } catch(error) {
      console.error('Error saving data:', error);
    }
  }

</script>

<style scoped>
  /* Modal styles */
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
  }
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
  