import { extendLogin } from "@/service/service";

const global = {
  namespaced: true,

  state() {
    return {
      credentials: null,
    };
  },
  mutations: {
    setCredentials(state, credentials) {
      state.credentials = credentials;
    },
    unsetCredentials(state) {
      state.credentials = null;
    },
    setAccessToken(state, partialCredential) {
      state.credentials.access_token = partialCredential.access_token;
    },
  },
  actions: {
    login({ commit }, credentials) {
        commit("setCredentials", credentials);
    },
    async extendLogin({ commit, state }) {
      let response = await extendLogin(state.credentials.refresh_token);
      if (response.ok) {
        let data = await response.json();
        let partialCredentials = {
          access_token: data.access,
        };
        commit("setAccessToken", partialCredentials);
      }
    },
    logout({ commit }) {
      commit("unsetCredentials");
    },
  },
  getters: {
    getCredentials(state) {
      return state.credentials;
    },
  },
};

export default global;
