<template>
  <v-app>
    <v-app-bar dense app>
      <v-app-bar-title style="width: 300px"
        >নুরুল কুরআন একাডেমি</v-app-bar-title
      >
      <v-spacer></v-spacer>
      <v-tabs>
        <v-tab to="/">হোম</v-tab>
        <!-- <v-tab to="/About">কোর্স সমূহ</v-tab> -->
        <v-tab to="/Student">শিক্ষার্থী</v-tab>
        <!-- <v-tab to="/Teacher">শিক্ষক/শিক্ষিকা</v-tab> -->
        <!-- <v-tab to="/Admin">এডমিন</v-tab> -->
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
      <!-- -->
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
    logout: function () {
      this.$store.dispatch("global/logout")

    }
  },
  computed: {
    showLogout: function () {
      let credentials = this.$store.getters["global/getCredentials"];
      if (credentials) {
        return true;
      }
      return false;
    },
  },
};
</script>
