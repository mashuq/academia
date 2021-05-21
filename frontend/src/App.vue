<template>
  <v-app>
    <v-app-bar dense app v-if="isMobile()">
      <v-tabs>
        <v-tab to="/">হোম</v-tab>
        <!-- <v-tab to="/About">কোর্স সমূহ</v-tab> -->
        <v-tab to="/Syllabus">পাঠ্যক্রম</v-tab>
        <v-tab to="/Student">শিক্ষার্থী</v-tab>
        <v-tab to="/Teacher">শিক্ষক/শিক্ষিকা</v-tab>
        <v-tab to="/Admin">এডমিন</v-tab>
        <v-tab v-on:click="logout" v-if="showLogout">লগ আউট করুন</v-tab>
        <!-- <v-tab to="/About">আমাদের সম্পর্কে</v-tab> -->
        <!-- <v-tab to="/About">যোগাযোগ করুন</v-tab> -->
      </v-tabs>
    </v-app-bar>

    <v-app-bar dense app v-else>
      <v-app-bar-title style="width: 300px">নূরুল কুরআন একাডেমি</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-tabs>
        <v-tab to="/">হোম</v-tab>
        <!-- <v-tab to="/About">কোর্স সমূহ</v-tab> -->
        <v-tab to="/Syllabus">পাঠ্যক্রম</v-tab>
        <v-tab to="/Student">শিক্ষার্থী</v-tab>
        <v-tab to="/Teacher">শিক্ষক/শিক্ষিকা</v-tab>
        <v-tab to="/Admin">এডমিন</v-tab>
        <!-- <v-tab to="/About">আমাদের সম্পর্কে</v-tab> -->
        <!-- <v-tab to="/About">যোগাযোগ করুন</v-tab> -->
      </v-tabs>
      <v-spacer></v-spacer>
      <v-btn v-on:click="logout" v-if="showLogout" rounded color="error" dark>লগ আউট করুন</v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <v-col class="text-center" cols="12">
        Copyright &copy; {{ new Date().getFullYear() }}
        <strong>নূরুল কুরআন একাডেমি</strong>
        <v-spacer></v-spacer>
        <v-btn icon target="_blank" href="https://www.facebook.com/NLQURAN">
          <v-icon size="24px">mdi-facebook</v-icon>
        </v-btn>
        <v-btn icon target="_blank" href="https://www.youtube.com/c/NurulQuran887">
          <v-icon size="24px">mdi-youtube</v-icon>
        </v-btn>
        <v-btn icon href="mailto:nurulquran887@gmail.com">
          <v-icon size="24px">mdi-email</v-icon>
        </v-btn>
         <v-btn icon href="tel:+8801700946569">
          <v-icon size="24px">mdi-phone</v-icon>
        </v-btn>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
//import HelloWorld from './components/HelloWorld';

export default {
  name: "App",

  components: {
    //HelloWorld,
  },

  data: () => ({
    //
  }),
  methods: {
    logout: function() {
      this.$store.dispatch("global/logout");
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
    },
  },
  computed: {
    showLogout: function() {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials) {
        return true;
      }
      return false;
    }
  }
};
</script>
