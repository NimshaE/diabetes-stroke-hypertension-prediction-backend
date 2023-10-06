<template>
  <section class="section with-background-image">
    <router-view/>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
      cartTotalLength() {
          let totalLength = 0

          for (let i = 0; i < this.cart.items.length; i++) {
              totalLength += this.cart.items[i].quantity
          }

          return totalLength
      }
  }
}
</script>
<style lang="scss">
@import '../node_modules/bulma';
html, body {
  overflow: hidden;
  height: 100%;
  margin: 0;
  padding: 0;
}
.background-image {
    background-image: url('./assets/act-clinica.jpg');
    background-size: cover;
    background-position: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.centered-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.login-page {
  position: relative;
  height: 100vh; 
  overflow: hidden;
}
.transparent-form {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 15px;
  width: 80%;
  max-width: 400px;
}
.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
}
.left-panel {
  width: 30%;
  background-color: rgba(255, 255, 255, 0.5);
  height: 100%;
}
.centered-panel-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.right-panel {
  width: 70%;
}
.input{
  border-radius: 20px;
}
.button {
  border-radius: 25px;
  color: white;
  background-color: #2F80ED;
  width: 100%;
}
.button:hover {
  border-radius: 25px;
  color: #2F80ED;
  background-color: white;
  width: 100%;
  border-color: #2F80ED;
  font-weight: bold;
}
.hyper-link {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px; 
}
.hr-line {
  width: 40%; /* Adjust the width of the horizontal rule as needed */
  margin: 0;
  border: none;
  border-top: 0.5px; /* Style the horizontal rule as needed */
}
.or-text {
  width: 20px;
  margin: 5px;
  text-align: center;
}
.or-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.lds-dual-ring {
  display: inline-block;
  width: 60px;
  height: 60px;
}
.lds-dual-ring::after {
  content: "";
  display: block;
  width: 44px;
  height: 44px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #2F80ED;
  border-color: #2F80ED transparent #2F80ED transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
