<template>
  <span>
    <v-card elevation="5">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <v-card-title>Appoint</v-card-title>
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
                    label="Username"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>

              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Email"
                  rules="required|email"
                >
                  <v-text-field
                    v-model="email"
                    :error-messages="errors"
                    label="Email"
                    email
                  ></v-text-field>
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
                  <v-text-field
                    v-model="name"
                    :error-messages="errors"
                    label="Name"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <v-label>Gender</v-label>
                <v-radio-group v-model="gender" mandatory>
                  <v-radio label="Male" value="MALE"></v-radio>
                  <v-radio label="Female" value="FEMALE"></v-radio>
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
                    <validation-provider
                      v-slot="{ errors }"
                      name="Birthday"
                      rules="required"
                    >
                      <v-text-field
                        v-model="formattedDate"
                        label="Birthday date"
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
                  name="Biography"
                  rules="required"
                >
                  <v-textarea
                    v-model="biography"
                    :error-messages="errors"
                    label="Biography"
                    required
                  ></v-textarea>
                </validation-provider>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Biography"
                  rules="required"
                >
                  <v-file-input
                    show-size
                    label="Profile Picture"
                    v-model="profilePicture"
                    accept="image/*"
                    :error-messages="errors"
                    required
                  ></v-file-input>
                </validation-provider>
              </v-col>
              <v-col>
                <v-select
                  v-model="teacherType"
                  :items="teacherTypes"
                  label="Teacher Type"
                  item-text="key"
                  item-value="value"
                ></v-select>
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
                    label="Password"
                    type="password"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>
              <v-col>
                <validation-provider
                  v-slot="{ errors }"
                  name="Confirm"
                  rules="required|max:20"
                >
                  <v-text-field
                    v-model="repassword"
                    :error-messages="errors"
                    label="Confirm Password"
                    type="password"
                    required
                  ></v-text-field>
                </validation-provider>
              </v-col>
            </v-row>
            <v-btn
              class="mr-4"
              color="primary"
              type="submit"
              :disabled="invalid"
            >
              submit
            </v-btn>
            <v-btn @click="clear"> clear </v-btn>
          </v-grid>
        </form>
      </validation-observer>
    </v-card>
    <v-snackbar v-model="snackbar" timeout="-1">
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
import {
  required,
  email,
  alpha_num,
  max,
  alpha_spaces,
} from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import moment from "moment";
import { appoint } from "@/service/service";

setInteractionMode("eager");

extend("email", email);
extend("alpha_num", alpha_num);
extend("max", max);
extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});
extend("alpha_spaces", alpha_spaces);
extend("password", {
  params: ["target"],
  validate(value, { target }) {
    return value === target;
  },
  message: "Password confirmation does not match",
});

export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    username: null,
    password: null,
    name: null,
    email: null,
    gender: null,
    biography: null,
    profilePicture: null,
    teacherType: null,
    date: null,
    menu: false,
    error: null,
    snackbar: false,
    teacherTypes: [
      { key: "Main", value: "MAIN" },
      { key: "Assistant", value: "ASSISTANT" },
    ],
  }),
  computed: {
    formattedDate: function() {
      if (this.date) {
        return moment(this.date).format("DD-MM-YYYY");
      }
      return null;
    },
  },
  methods: {
    async submit() {
      this.$refs.observer.validate();
      let date = moment(this.date).toISOString();
      let response = await appoint(
        this.username,
        this.password,
        this.name,
        this.email,
        this.gender,
        date
      );
      if (response.ok) {
        this.$emit("appointmentComplete");
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
      this.$refs.observer.reset();
    },
    save(date) {
      this.$refs.menu.save(date);
    },
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    },
  },
};
</script>
