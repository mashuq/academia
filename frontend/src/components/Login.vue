<template>
 <v-card
  elevation="5">
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
        <v-btn class="mr-4" color="primary" type="submit" :disabled="invalid"> submit </v-btn>
        <v-btn @click="clear"> clear </v-btn>
      </form>
    </validation-observer>
  </v-card>
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

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    username: null,
    password: null,
  }),

  methods: {
    submit() {
      this.$refs.observer.validate();
      console.log(process.env.VUE_APP_BASE_URL);
      this.$store.dispatch("global/login", {
        username: this.username,
        password: this.password,
      });
    },
    clear() {
      this.username = null;
      this.password = null;
      this.$refs.observer.reset();
    },
  },
};
</script>