<template>
  <span>
    <v-card elevation="5">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <v-card-title>Login</v-card-title>
        <form @submit.prevent="submit">
          <validation-provider
            v-slot="{ errors }"
            name="Username"
            rules="required"
          >
            <v-text-field
              v-model="username"
              :error-messages="errors"
              label="Username"
              required
            ></v-text-field>
          </validation-provider>

          <validation-provider
            v-slot="{ errors }"
            name="Password"
            rules="required"
          >
            <v-text-field
              v-model="password"
              :error-messages="errors"
              label="Password"
              type="password"
              required
            ></v-text-field>
          </validation-provider>
          <v-btn class="mr-4" color="primary" type="submit" :disabled="invalid">
            submit
          </v-btn>
          <v-btn @click="clear"> clear </v-btn>
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
import { required } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});
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
      }else{
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
