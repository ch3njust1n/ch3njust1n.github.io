/*
Author: Justin Chen
Date: April 5, 2020
*/
import Vue from 'vue'
import App from './App.vue'
import router from './router'
// eslint-disable-next-line

Vue.config.productionTip = false;

new Vue({
	el: '#vue-app',
	router,
	render: h => h(App)
})