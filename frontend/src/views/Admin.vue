<template>
  <span>
    <template v-if="showLogin">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><Login /></v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showAdmin">
      <Admin />
    </template>
    <template v-if="showNonAdmin">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><NonAdmin /></v-col>
        <v-col></v-col>
      </v-row>
    </template>
  </span>
</template>


<script>
import Login from "@/components/Login.vue";
import NonAdmin from "@/components/admin/NonAdmin.vue";
import Admin from "@/components/admin/Admin.vue";
import _ from "lodash";
export default {
  components: {
    Login,
    NonAdmin,
    Admin,
  },
  data() {
    return {
      greeting: "Hello",
    };
  },
  computed: {
    showLogin: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials) {
        return false;
      }
      return true;
    },
    showAdmin: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && _.includes(credentials.roles, "admin")) {
        return true;
      }
      return false;
    },
    showNonAdmin: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && !_.includes(credentials.roles, "admin")) {
        return true;
      }
      return false;
    },
  },
};
</script>


