<template>
  <span>
    <v-alert text type="success">
    আপনার পাসওয়ার্ড আপনার ইমেইল এ পাঠানো হয়েছে। দয়া করে সেটা দিয়ে লগইন করুন 
    </v-alert>
    <v-btn @click="$emit('hideAll')" color="success">লগইন করুন</v-btn>
  </span>
</template>
