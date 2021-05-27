<template>
  <span>

    
    <template v-if="showLogin && !isMobile()">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্ট্রেশন করেন নি?</v-col>
                <v-col>
                  <v-btn @click="showRegistrationDialog" color="primary">রেজিস্ট্রেশন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">পাসওয়ার্ড ভুলে গিয়েছেন?</v-col>
                <v-col>
                  <v-btn @click="showPasswordResetDialog" color="warning">পাসওয়ার্ড রিসেট করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <Login />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showLogin && isMobile()">
      <v-row no-gutters>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্ট্রেশন করেন নি?</v-col>
                <v-col>
                  <v-btn @click="showRegistrationDialog" color="primary">রেজিস্ট্রেশন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">পাসওয়ার্ড ভুলে গিয়েছেন?</v-col>
                <v-col>
                  <v-btn @click="showPasswordResetDialog" color="warning">পাসওয়ার্ড রিসেট করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <Login />
        </v-col>
      </v-row>
    </template>


    <template v-if="showRegistration && !isMobile()">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্টার করে ফেলেছেন?</v-col>
                <v-col>
                  <v-btn @click="showLoginDialog" color="success">লগইন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">পাসওয়ার্ড ভুলে গিয়েছেন?</v-col>
                <v-col>
                  <v-btn @click="showPasswordResetDialog" color="warning">পাসওয়ার্ড রিসেট করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <Registration @registrationComplete="showRegistrationCompleteDialog" />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showRegistration && isMobile()">
      <v-row no-gutters>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্টার করে ফেলেছেন?</v-col>
                <v-col>
                  <v-btn @click="showLoginDialog" color="success">লগইন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">পাসওয়ার্ড ভুলে গিয়েছেন?</v-col>
                <v-col>
                  <v-btn @click="showPasswordResetDialog" color="warning">পাসওয়ার্ড রিসেট করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <Registration @registrationComplete="showRegistrationCompleteDialog" />
        </v-col>
      </v-row>
    </template>

    <template v-if="showPasswordReset && !isMobile()">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্টার করে ফেলেছেন?</v-col>
                <v-col>
                  <v-btn @click="showLoginDialog" color="success">লগইন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্ট্রেশন করেন নি?</v-col>
                <v-col>
                  <v-btn @click="showRegistrationDialog" color="primary">রেজিস্ট্রেশন করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <PasswordReset @passwordResetComplete="showPasswordResetCompleteDialog" />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showPasswordReset && isMobile()">
      <v-row no-gutters>
        <v-col>
          <v-container>
            <v-grid>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্টার করে ফেলেছেন?</v-col>
                <v-col>
                  <v-btn @click="showLoginDialog" color="success">লগইন করুন</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col class="text-right">শিক্ষার্থী হিসেবে রেজিস্ট্রেশন করেন নি?</v-col>
                <v-col>
                  <v-btn @click="showRegistrationDialog" color="primary">রেজিস্ট্রেশন করুন</v-btn>
                </v-col>
              </v-row>
            </v-grid>
          </v-container>
          <PasswordReset @passwordResetComplete="showPasswordResetCompleteDialog" />
        </v-col>
      </v-row>
    </template>


    <template v-if="showStudent">
      <Student />
    </template>
    <template v-if="showNonStudent">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <NonStudent />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showRegistrationComplete">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <RegistrationComplete @hideAll="hideAll" />
        </v-col>
        <v-col></v-col>
      </v-row>
    </template>
    <template v-if="showPasswordResetComplete">
      <v-row no-gutters>
        <v-col></v-col>
        <v-col>
          <PasswordResetComplete @hideAll="hideAll"/>
        </v-col>
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
import Registration from "@/components/Registration.vue";
import RegistrationComplete from "@/components/RegistrationComplete.vue";
import PasswordReset from "@/components/PasswordReset.vue";
import PasswordResetComplete from "@/components/PasswordResetComplete.vue";
export default {
  components: {
    Login,
    NonStudent,
    Student,
    Registration,
    RegistrationComplete,
    PasswordReset,
    PasswordResetComplete
  },
  data() {
    return {
      showRegistration: false,
      showRegistrationComplete: false,
      showPasswordReset: false,
      showPasswordResetComplete: false
    };
  },
  computed: {
    showLogin: function() {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials) {
        return false;
      }
      if (this.showRegistration || this.showPasswordReset || this.showRegistrationComplete || this.showPasswordResetComplete) {
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
    }
  },
  methods: {
    hideAll: function(){
      this.showRegistration = false;
      this.showRegistrationComplete = false;
      this.showPasswordReset = false;
      this.showPasswordResetComplete = false;
    },
    showRegistrationDialog: function() {
      this.hideAll();
      this.showRegistration = true;
    },
    showLoginDialog: function() {
      this.hideAll();
    },
    showRegistrationCompleteDialog: function() {
      this.hideAll();
      this.showRegistrationComplete = true;
    },
    hideAllRegistration: function() {
      this.hideAll();
    },
    showPasswordResetDialog: function(){
      this.hideAll();
      this.showPasswordReset = true;
    },
    showPasswordResetCompleteDialog: function(){
      this.hideAll();
      this.showPasswordResetComplete = true;
    },
    isMobile() {
      if (
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        )
      ) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>
