<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div>{{ videoLesson.video_type }}</div>
      <p class="display-1 text--primary">
        {{ videoLesson.name }}
      </p>
      <youtube
        player-width="360"
        player-height="202"
        :video-id="youtubeUrl"
      ></youtube>
    </v-card-text>
  </v-card>
</template>

<script>
import { getIdFromURL } from "vue-youtube-embed";
export default {
  props: {
    lesson: { type: Object, required: true },
  },
  data: function() {
    return {
      videoLesson: { ...this.lesson },
      youtubeUrl: getIdFromURL(this.lesson.link),
    };
  },
  created() {},
  methods: {
  },
};
</script>
