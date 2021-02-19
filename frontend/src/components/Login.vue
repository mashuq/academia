<template>
  <span>
    <v-card elevation="5">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <h3>লগ ইন করুন</h3>
        <form @submit.prevent="submit">
          <validation-provider
            v-slot="{ errors }"
            name="ইউজারনেম"
            rules="required"
          >
            <v-text-field
              v-model="username"
              :error-messages="errors"
              label="ইউজারনেম"
              required
            ></v-text-field>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="পাসওয়ার্ড"
            rules="required"
          >
            <v-text-field
              v-model="password"
              :error-messages="errors"
              label="পাসওয়ার্ড"
              type="password"
              required
            ></v-text-field>
          </validation-provider>
          <v-btn class="mr-4" color="primary" type="submit" :disabled="invalid">
            লগ ইন করুন
          </v-btn>
          <v-btn @click="clear"> সব মুছে নতুন করে শুরু করুন </v-btn>
        </form>
      </validation-observer>
    </v-card>

    <v-snackbar v-model="snackbar">
      {{ error }}
      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<style scoped>
.v-card {
  padding: 20px;
}
</style>

<script>
import { localize } from 'vee-validate';
import { required } from "vee-validate/dist/rules";
extend('required', {
    ...required,
    message: '{_field_} দিতেই হবে',
})
import bd from 'vee-validate/dist/locale/bd.json';
localize('bd', bd);

import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";

setInteractionMode("eager");

import { login } from "@/service/service";

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    username: null,
    password: null,
    error: null,
    snackbar: false,
  }),

  methods: {
    async submit() {
      this.$refs.observer.validate();
      let response = await login(this.username, this.password);
      if (response.ok) {
        let data = await response.json();
        let credentials = {
          access_token: data.access,
          refresh_token: data.refresh,
          user: data.user,
          roles: data.roles,
        };
        this.$store.dispatch("global/login", credentials);
      } else {
        let data = await response.json();
        this.error = data.detail;
        this.snackbar = true;
      }
    },
    clear() {
      this.username = null;
      this.password = null;
      this.$refs.observer.reset();
    },
  },
};
</script>
