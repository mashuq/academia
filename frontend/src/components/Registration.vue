<template>
  <span>
    <v-card elevation="5">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <v-card-title>রেজিস্ট্রেশন করুন</v-card-title>
        <form @submit.prevent="submit">
          <v-grid>
            <v-row>
              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Username"
                  rules="required|max:150|alpha_num"
                >
                  <v-text-field
                    v-model="username"
                    :error-messages="errors"
                    label="ইউজারনেম"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>

              <v-col>
                <validation-provider v-slot="{ errors }" name="ইমেইল" rules="required|email">
                  <v-text-field v-model="email" :error-messages="errors" label="ইমেইল" email></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Name"
                  rules="required|max:128|alpha_spaces"
                >
                  <v-text-field v-model="name" :error-messages="errors" label="নাম" required></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-label>লিঙ্গ</v-label>
                <v-radio-group v-model="gender" mandatory>
                  <v-radio label="পুরুষ" value="MALE"></v-radio>
                  <v-radio label="মহিলা" value="FEMALE"></v-radio>
                </v-radio-group>
              </v-col>
              <v-col>
                <v-menu
                  ref="menu"
                  v-model="menu"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <validation-provider v-slot="{ errors }" name="Birthday" rules="required">
                      <v-text-field
                        v-model="formattedDate"
                        label="জন্ম তারিখ"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        :error-messages="errors"
                        v-on="on"
                        required
                      ></v-text-field>
                    </validation-provider>
                  </template>
                  <v-date-picker
                    ref="picker"
                    v-model="date"
                    :max="new Date().toISOString().substr(0, 10)"
                    min="1950-01-01"
                    @change="save"
                  ></v-date-picker>
                </v-menu>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Password"
                  rules="required|password:@Confirm|max:20"
                >
                  <v-text-field
                    v-model="password"
                    :error-messages="errors"
                    label="পাসওয়ার্ড"
                    type="password"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>
              <v-col>
                <validation-provider v-slot="{ errors }" name="Confirm" rules="required|max:20">
                  <v-text-field
                    v-model="repassword"
                    :error-messages="errors"
                    label="কনফার্ম পাসওয়ার্ড"
                    type="password"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>
            <vue-recaptcha @verify="verify" :sitekey="siteKey" :loadRecaptchaScript="true"></vue-recaptcha>
            <v-btn class="mr-4" color="primary" type="submit" :disabled="invalid">রেজিস্ট্রেশন করুন</v-btn>
            <v-btn @click="clear">সব মুছে নতুন করে শুরু করুন</v-btn>
          </v-grid>
        </form>
      </validation-observer>
    </v-card>
    <v-snackbar v-model="snackbar" timeout="-1">
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
import {
  required,
  email,
  alpha_num,
  max,
  alpha_spaces
} from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode
} from "vee-validate";
import moment from "moment";
import { register } from "@/service/service";

setInteractionMode("eager");

extend("email", email);
extend("alpha_num", alpha_num);
extend("max", max);
extend("required", {
  ...required,
  message: "{_field_} can not be empty"
});
extend("alpha_spaces", alpha_spaces);
extend("password", {
  params: ["target"],
  validate(value, { target }) {
    return value === target;
  },
  message: "Password confirmation does not match"
});

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
    VueRecaptcha
  },
  data: () => ({
    username: null,
    password: null,
    repassword: null,
    name: null,
    email: null,
    gender: null,
    date: null,
    menu: false,
    error: null,
    snackbar: false,
    recaptchaVerified: false,
    recaptchaResponse: null,
    siteKey: process.env.VUE_APP_RECAPTCHA_SITE_KEY
  }),
  computed: {
    formattedDate: function() {
      if (this.date) {
        return moment(this.date).format("DD-MM-YYYY");
      }
      return null;
    }
  },
  methods: {
    verify(response) {
      this.recaptchaVerified = true;
      this.recaptchaResponse = response;
    },
    async submit() {
      this.$refs.observer.validate();
      if(!this.recaptchaVerified){
        this.error = "দয়া করে 'I am not a robot' এ ক্লিক করুন";
        this.snackbar = true;
        return;
      }
      let date = moment(this.date).toISOString();
      let response = await register(
        this.username,
        this.password,
        this.name,
        this.email,
        this.gender,
        date,
        this.recaptchaResponse
      );
      if (response.ok) {
        this.$emit("registrationComplete");
      } else {
        let data = await response.json();
        let error = "";
        if ("username" in data) {
          error += "Username already exists";
        }
        if ("email" in data) {
          if (error) {
            error += " and ";
          }
          error += "Email already exists";
        }
        this.error = error;
        this.snackbar = true;
      }
    },
    clear() {
      this.username = null;
      this.password = null;
      this.name = null;
      this.email = null;
      this.gender = null;
      this.date = null;
      this.repassword = null;
      this.$refs.observer.reset();
    },
    save(date) {
      this.$refs.menu.save(date);
    }
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  }
};
</script>
