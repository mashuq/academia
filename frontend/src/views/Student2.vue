<template>
  <span>
    <template v-if="showLogin">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <v-container>
            শিক্ষার্থী হিসেবে রেজিস্টার করেন নি?<v-btn @click="showRegistrationDialog" color="success">রেজিস্টার করুন</v-btn>
          </v-container>
          <Login />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showRegistration">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <v-container>
           শিক্ষার্থী হিসেবে রেজিস্টার করে ফেলেছেন?<v-btn @click="hideRegistrationDialog" color="success">লগইন করুন</v-btn>
          </v-container>
          <Registration @registrationComplete="showRegistrationCompleteDialog"/>
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showStudent"> 
      <Student />
    </template>
    <template v-if="showNonStudent">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><NonStudent /></v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showRegistrationComplete">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col><RegistrationComplete @hideRegistration="hideAllRegistration"/></v-col>
        <v-col></v-col>
      </v-row>
    </template>
  </span>
</template>

<script>
import Login from "@/components/Login.vue";
import NonStudent from "@/components/student/NonStudent.vue";
import Student from "@/components/student/Student.vue";
import _ from "lodash";
import Registration from '@/components/Registration.vue';
import RegistrationComplete from '@/components/RegistrationComplete.vue'
export default {
  components: {
    Login,
    NonStudent,
    Student,
    Registration,
    RegistrationComplete,
  },
  data() {
    return {
      showRegistration: false,
      showRegistrationComplete: false
    };
  },
  computed: {
    showLogin: function() {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials) {
        return false;
      }
      if (this.showRegistration || this.showRegistrationComplete) {
        return false;
      }

      return true;
    },
    showStudent: function() {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && _.includes(credentials.roles, "student")) {
        return true;
      }
      return false;
    },
    showNonStudent: function() {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials && !_.includes(credentials.roles, "student")) {
        return true;
      }
      return false;
    },
  },
  methods: {
    showRegistrationDialog: function(){
      this.showRegistration = true;
      this.showRegistrationComplete = false;
    },
    hideRegistrationDialog: function(){
      this.showRegistration = false;
      this.showRegistrationComplete = false;
    },
    showRegistrationCompleteDialog: function(){
      this.showRegistrationComplete = true;
      this.showRegistration = false;
    },
    hideAllRegistration: function(){
      this.showRegistrationComplete = false;
      this.showRegistration = false;
    }
  }
};
</script>
