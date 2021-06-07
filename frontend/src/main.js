import Vue from "vue"
import "./plugins/axios"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import VueSocketIO from "vue-socket.io"

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: "http://localhost:5000"
  })
)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount("#app")
