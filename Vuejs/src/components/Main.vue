<template>
    <div class="products bg-gray-800 shadow-gray-600">
        <div class="p-4">
            <input type="text" class="w-full h-8 pl-5 pb-5 pt-5 rounded" placeholder="Search">
        </div>
        <div class="category p-3">
            <span class="bg-brightRed rounded p-1 font-semibold text-white text-xs mr-2">All</span>
            <span class="bg-brightRedLight rounded p-1 font-semibold text-white text-xs mr-2">Shorts</span>
            <span class="bg-brightRedLight rounded p-1 font-semibold text-white text-xs mr-2">T-shirt</span>
        </div>
        <Product />
    </div>
</template>

<script setup>
import Product from './Product.vue';
</script>

<style scoped>
.products{
    width: 100%;
    max-height: 830px;
}

</style>