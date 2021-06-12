<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div>{{ videoLesson.video_type }}</div>
      <p class="display-1 text--primary">{{ videoLesson.name }}</p>
      <p v-html="videoLesson.description"></p>
      <youtube player-width="360" player-height="202" :video-id="youtubeUrl"></youtube>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="blue darken-4 accent-4" @click="editLesson">Edit</v-btn>
      <v-btn text color="red darken-4 accent-4" @click="deleteLesson">Delete</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { getIdFromURL } from "vue-youtube-embed";
export default {
  props: {
    lesson: { type: Object, required: true }
  },
  data: function() {
    return {
      youtubeUrl: getIdFromURL(this.lesson.link)
    };
  },
  computed: {
    videoLesson: function() {
      return { ...this.lesson };
    },
  },
  created() {},
  methods: {
    editLesson() {
      this.$emit("editVideo", this.videoLesson.id);
    },
    deleteLesson() {
      this.$emit("remove", this.videoLesson.id);
    }
  }
};
</script>
