import { createStore } from 'vuex';

export default createStore({
  state: {
    cart: [],
  },
  mutations: {
    addToCart(state, product) {
      const existingItemIndex = state.cart.findIndex(item => item.ProductID === product.ProductID);
      if (existingItemIndex !== -1) {
        // If item already exists in cart, update quantity and total price
        state.cart[existingItemIndex].quantity++;
        state.cart[existingItemIndex].totalPrice = state.cart[existingItemIndex].quantity * product.SellingPrice;
      } else {
        // If item does not exist in cart, add it with quantity and total price
        state.cart.push({ ...product, quantity: 1, totalPrice: product.SellingPrice });
      }
    },
    incrementQuantity(state, index) {
      // Increment quantity and update total price
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
  },
  getters: {
    cartItems(state) {
      return state.cart;
    },
  },
});
