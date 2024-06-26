<template>
    <div class="right-side">
      <div class="cashier-transid">
        <div class="content">
          <div class="idTrans">
            <input class="txtTransaction" type="text" :id="transactionID" value="TRAN001">
          </div>
          <div class="cashierContent">
            <h6 class="text-xs" id="cashierName"><span class="font-bold">Cashier Name:</span> {{ firstName }}</h6>
            <h6 class="text-xs" id="date_time"><span class="font-bold">Date & Time:</span> 04-23-2024 - 10:00</h6>
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
              <th class="text-xs font-semibold">Image</th>
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
              <td><img :src="item.ImageURL" alt="Product Image" style="width: 100px; height: auto;"></td>
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
  import { computed, watch, ref, onMounted, defineProps } from 'vue';
  import { useStore } from 'vuex';
  import axios from 'axios';
  
  const store = useStore();
  const url = 'http://127.0.0.1:8000'

  const change = ref(0);
  const transactionID = ref('TRAN001');
  const showSuccessModal = ref(false);

  // Fetch the firstName from localStorage on component mount
  const props = defineProps({
    firstName: String // Define the type of the prop
  });

  const cartItems = computed(() => {
    return store.getters.cartItems.map(item => ({
      ...item,
      ImageURL: getImageUrl(item.ImageURL)
    }));
  });

  const subtotal = computed(() => {
    return cartItems.value.reduce((acc, item) => 
        acc + item.totalPrice, 0
      );
    });

  let amount = '';
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

  const handlePayment = async (firstName) => {
    try {
      await saveToDatabase(firstName);
      showSuccessModal.value = true;
      setTimeout(() => {
        location.reload();
      }, 1000);
    } catch (error) {
      console.error('Error saving data:', error);
    }
  };

  const saveToDatabase = async () => {
    try {
      const promises = cartItems.value.map(async (item) => {
        const payload = {
          TransactionID: transactionID.value,
          ProductID: item.ProductID,
          ProductName: item.ProductName,
          Description: item.Description,
          Qty: parseInt(item.quantity),
          UnitPrice: parseFloat(item.SellingPrice),
          TotalAmount: parseFloat(subtotal.value),
          DateTime: new Date().toISOString(),
          CashierName: props.firstName
        };
        const response = await axios.post('http://127.0.0.1:8000/saveTransaction/', payload);
        console.log('Data saved successfully:', response.data);
    });
    await Promise.all(promises);
    showSuccessModal.value = true;
    setTimeout(() => {
      location.reload();
    }, 1000);
    } catch(error) {
      console.error('Error saving data:', error);
    }
  };

  const getImageUrl = (image) => `${image.startsWith('/') ? url : ''}${image}`;

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
  .idTrans input{
    border: #ddd 1px solid;
  }
  .txtTransaction{
    width: 120px;
    font-weight: bold;
    text-align: center;
  }
</style>
  