<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div>{{ audioLesson.audio_type }}</div>
      <p class="display-1 text--primary">{{ audioLesson.name }}</p>
      <p v-html="audioLesson.description"></p>
      <span v-html="this.audioLesson.embed"></span>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="blue darken-4 accent-4" @click="editLesson">Edit</v-btn>
      <v-btn text color="red darken-4 accent-4" @click="deleteLesson">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    lesson: { type: Object, required: true }
  },
  computed: {
    audioLesson: function() {
      return { ...this.lesson };
    },
  },
  created() {},
  methods: {
    editLesson() {
      this.$emit("editAudio", this.audioLesson.id);
    },
    deleteLesson() {
      this.$emit("remove", this.audioLesson.id);
    }
  }
};
</script>
