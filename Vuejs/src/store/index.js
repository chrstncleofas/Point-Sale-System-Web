import { createStore } from 'vuex';

export default createStore({
  state: {
    cart: [],
    change: 0,
  },
  mutations: {
    addToCart(state, product) {
      const existingItemIndex = state.cart.findIndex(item => item.ProductID === product.ProductID);
      if (existingItemIndex !== -1) {
        state.cart[existingItemIndex].quantity++;
        state.cart[existingItemIndex].totalPrice = state.cart[existingItemIndex].quantity * state.cart[existingItemIndex].SellingPrice;
      } else {
        state.cart.push({ ...product, quantity: 1, totalPrice: product.SellingPrice * 1, ImageURL: product.ImageURL });
      }
    },
    incrementQuantity(state, index) {
      state.cart[index].quantity++;
      state.cart[index].totalPrice = state.cart[index].quantity * state.cart[index].SellingPrice;
    },
    decrementQuantity(state, index) {
      if (state.cart[index].quantity > 1) {
        state.cart[index].quantity--;
        state.cart[index].totalPrice = state.cart[index].quantity * state.cart[index].SellingPrice;
      } else {
        state.cart.splice(index, 1);
      }
    },
    removeFromCart(state, index) {
      state.cart.splice(index, 1);
    },
    updateChange(state, newChange) {
      state.change = newChange;
    },
  },
  actions: {
    addToCart({ commit }, product) {
      commit('addToCart', product);
    },
    removeFromCart({ commit }, index) {
      commit('removeFromCart', index);
    },
    incrementQuantity({ commit }, index) {
      commit('incrementQuantity', index);
    },
    decrementQuantity({ commit }, index) {
      commit('decrementQuantity', index);
    },
    updateChange({ commit }, newChange) {
      commit('updateChange', newChange);
    },
  },
  getters: {
    cartItems(state) {
      return state.cart;
    },
    changeValue(state) {
      return state.change;
    },
  },
});
