<template>
  <span>
    <v-alert text type="success">
      You have registered successfully. Please Login now.
    </v-alert>
    <v-btn @click="$emit('hideRegistration')" color="success">Login</v-btn>
  </span>
</template>
