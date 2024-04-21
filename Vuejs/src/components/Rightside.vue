<template>
    <div class="right-side">
        <div class="table-container">
            <table class="shadow-2xl shadow-gray-100">
                <thead class="p-3">
                    <tr>
                        <th>Item Name</th>
                        <th>Image</th>
                        <th>Qty</th>
                        <th>Price</th>
                        <th>Product Info</th>
                        <th>Delete</th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <tr v-for="(row, index) in rows" :key="index">
                        <td>Shoes Item {{ index + 1 }}</td>
                        <td><img src="../components/icons/Product-01.jpg" class="w-10 h-10"></td>
                        <td>
                            <div class="flex items-center justify-center">
                                <button @click="decrement(index)" class="px-2 py-1 rounded-l bg-gray-200">
                                    <i class="fas fa-minus"></i>
                                </button>
                                <input type="text" v-model="row.value" class="px-1 py-1 text-center w-16" />
                                <button @click="increment(index)" class="px-2 py-1 rounded-r bg-gray-200">
                                    <i class="fas fa-plus"></i>
                                </button>
                            </div>
                        </td>
                        <td>10,000</td>
                        <td>Sample Info</td>
                        <td>
                            <button><i class="fas fa-trash"></i></button>
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
                    <h6>Php 500</h6>
                    <h6>Php 550</h6>
                </div>
            </div>
            <div class="section-c mt-5">
                <div class="mb-3 fields">
                    <label for="" class="mb-2">Amount:</label>
                    <input type="text" class="h-9 rounded">
                </div>
                <div class="fields">
                    <label for="" class="mb-2">Change:</label>
                    <input type="text" class="h-9 rounded">
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
import { ref } from 'vue';

const rows = ref([
  { value: 0 },
  { value: 0 },
  { value: 0 }
]);

const increment = (index) => {
  rows.value[index].value++;
};

const decrement = (index) => {
  rows.value[index].value--;
};
</script>

<style scoped>
.right-side{
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.table-container{
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
.section-b{
    padding: 25px;
}
.section-b h5{
    line-height: 2.2;
}
.section-b .content{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
}
.content .amout{
    display: flex;
    justify-content: flex-end;
    flex-direction: column;
    align-items: last baseline;
}
.content h6{
    line-height: 2.2;
}
.section-c{
    display: flex;
    flex-direction: column;
}
.section-c .fields{
    display: flex;
    flex-direction: column;
}
</style>