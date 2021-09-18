import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";

import BootstrapVue from "bootstrap-vue"; // Import Bootstrap here
import Vue from "vue";
import App from "./App.vue";
import router from "./router";

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
