<template>
  <v-card class="mx-auto">
    <v-card-text>
      <div>{{ audioLesson.audio_type }}</div>
      <p class="display-1 text--primary">
        {{ audioLesson.name }}
      </p>
      <span v-html="this.audioLesson.embed"></span>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    lesson: { type: Object, required: true },
  },
  data: function() {
    return {
      audioLesson: { ...this.lesson },
    };
  },
  created() {},
  methods: {
  },
};
</script>
