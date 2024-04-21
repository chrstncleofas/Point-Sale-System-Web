<template>
    <div class="products bg-gray-800 shadow-gray-600">
        <div class="p-4">
            <input type="text" class="w-full h-8 pl-5 pb-5 pt-5 rounded" placeholder="Search">
            <span class="icons-class">
                <i class="fas fa-search"></i>
            </span>
        </div>
        <div class="category p-3">
            <span class="bg-brightRed rounded p-1 font-semibold text-white text-xs mr-2">All</span>
            <span class="bg-brightRedLight rounded p-1 font-semibold text-white text-xs mr-2">Shorts</span>
            <span class="bg-brightRedLight rounded p-1 font-semibold text-white text-xs mr-2">T-shirt</span>
        </div>
        <div class="item-container">
            <div class="item bg-white">
                <img src="../components/icons/Product-01.jpg" class="w-15 h-15">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
            <div class="item bg-white">
                <img src="../components/icons/Product-02.jpg" class="w-15 h-15 mb-2">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
            <div class="item bg-white">
                <img src="../components/icons/Product-05.jpg" class="w-15 h-15">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
            <div class="item bg-white">
                <img src="../components/icons/Product-04.jpg" class="w-15 h-15">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
            <div class="item bg-white mt-5">
                <img src="../components/icons/Product-03.jpg" class="w-15 h-15">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
            <div class="item bg-white mt-5">
                <img src="../components/icons/Product-01.jpg" class="w-15 h-15">
                <h6 class="font-bold">Short One</h6>
                <p class="text-xs font-semibold">Php 200</p>
                <button type="submit" class="bg-brightRed shadow-lg shadow-slate-900 w-20 h-7 rounded mt-4 float-right text-xs text-white">Add to Cart</button>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
.products{
    width: 100%;
    max-height: 830px;
}
.icons-class{
    position: absolute;
    top: 95px;
    left: 775px;
}
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
</style>