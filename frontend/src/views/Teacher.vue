<template>
  <span>
    <template v-if="showLogin">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><Login /></v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showTeacher">
      <Teacher />
    </template>
    <template v-if="showNonTeacher">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><NonTeacher /></v-col>
        <v-col></v-col>
      </v-row>
    </template>
  </span>
</template>


<script>
import Login from "@/components/Login.vue";
import NonTeacher from "@/components/teacher/NonTeacher.vue";
import Teacher from "@/components/teacher/Teacher.vue";
import _ from "lodash";
export default {
  components: {
    Login,
    NonTeacher,
    Teacher,
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
    showTeacher: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && _.includes(credentials.roles, "teacher")) {
        return true;
      }
      return false;
    },
    showNonTeacher: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && !_.includes(credentials.roles, "teacher")) {
        return true;
      }
      return false;
    },
  },
};
</script>


