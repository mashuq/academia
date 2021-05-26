<template>
  <span v-if="isMobile()">
    <p class="display-1 text--primary">{{ videoLesson.name }}</p>
    <small v-html="videoLesson.description"></small>
    <youtube player-width="360" player-height="202" :video-id="youtubeUrl"></youtube>
  </span>
  <v-card class="mx-auto" v-else>
    <v-card-text>
      <div>{{ videoLesson.video_type }}</div>
      <p class="display-1 text--primary">{{ videoLesson.name }}</p>
      <p v-html="videoLesson.description"></p>
      <youtube player-width="360" player-height="202" :video-id="youtubeUrl"></youtube>
    </v-card-text>
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
      videoLesson: { ...this.lesson },
      youtubeUrl: getIdFromURL(this.lesson.link)
    };
  },
  created() {},
  methods: {
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
