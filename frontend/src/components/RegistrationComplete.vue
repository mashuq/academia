<template>
  <span>
    <v-alert text type="success">
    আপনার রেজিস্ট্রেশন সফল, দয়া করে লগইন করুন।
    </v-alert>
    <v-btn @click="$emit('hideAll')" color="success">লগইন করুন</v-btn>
  </span>
</template>
