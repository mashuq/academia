import Vue from 'vue'
import Vuex from 'vuex'

import admin from './admin';
import global from './global';

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    admin,
    global
  },
  plugins: [createPersistedState()],
})
