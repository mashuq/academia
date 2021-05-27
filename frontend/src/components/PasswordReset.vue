<template>
  <span>
    <v-card elevation="5">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <h3>পাসওয়ার্ড রিসেট করুন</h3>
        <form @submit.prevent="submit">
          <v-row>
            <v-col>
              <validation-provider v-slot="{ errors }" name="ইমেইল" rules="required|email">
                <v-text-field v-model="email" :error-messages="errors" label="ইমেইল" email></v-text-field>
              </validation-provider>
            </v-col>
          </v-row>
          <vue-recaptcha @verify="verify" :sitekey="siteKey" :loadRecaptchaScript="true"></vue-recaptcha>
          <v-btn class="mr-4" color="primary" type="submit" :disabled="invalid">পাসওয়ার্ড রিসেট করুন</v-btn>
          <v-btn @click="clear">সব মুছে নতুন করে শুরু করুন</v-btn>
        </form>
      </validation-observer>
    </v-card>

    <v-snackbar v-model="snackbar">
      {{ error }}
      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">Close</v-btn>
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
import VueRecaptcha from "vue-recaptcha";
import { localize } from "vee-validate";
import { required } from "vee-validate/dist/rules";
extend("required", {
  ...required,
  message: "{_field_} দিতেই হবে"
});
import bd from "vee-validate/dist/locale/bd.json";
localize("bd", bd);

import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode
} from "vee-validate";

setInteractionMode("eager");

import { noauth_post } from "@/service/service";

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    VueRecaptcha
  },
  data: () => ({
    email: null,
    error: null,
    snackbar: false,
    recaptchaVerified: false,
    recaptchaResponse: null,
      siteKey: process.env.VUE_APP_RECAPTCHA_SITE_KEY
  }),

  methods: {
    verify(response) {
      this.recaptchaVerified = true;
      this.recaptchaResponse = response;
    },
    async submit() {
      this.$refs.observer.validate();
      if (!this.recaptchaVerified) {
        this.error = "দয়া করে 'I am not a robot' এ ক্লিক করুন";
        this.snackbar = true;
        return;
      }
      let response = await noauth_post("/password_reset/", {
        email: this.email,
        "g-recaptcha-response": this.recaptchaResponse,
      });
      let error = "";
      if (response.ok) {
        this.$emit("passwordResetComplete");
      }else if(response.status == 406){
        error = "You are not registered. Please register.";
      }else if(response.status == 503){
        error = "Error sending email. Please try again later.";
      }else{
        error = "An error occurred. Please contact : support@nlquran.com" 
      }
      this.error = error;
      this.snackbar = true;
    },
    clear() {
      this.username = null;
      this.password = null;
      this.$refs.observer.reset();
    }
  }
};
</script>
