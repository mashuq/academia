<template>
  <span v-if="isMobile()">
    <p class="display-1 text--primary">{{ linkLesson.name }}</p>
    <small v-html="linkLesson.description"></small>
    <h4>
      <a target="_blank" rel="noopener noreferrer" :href="linkLesson.link">{{linkLesson.title}}</a>
    </h4>
  </span>
  <v-card class="mx-auto" v-else>
    <v-card-text>
      <p class="display-1 text--primary">{{ linkLesson.name }}</p>
      <p v-html="linkLesson.description"></p>
      <h4>
        <a target="_blank" rel="noopener noreferrer" :href="linkLesson.link">{{linkLesson.title}}</a>
      </h4>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  components: {
    
  },
  props: {
    lesson: { type: Object, required: true }
  },
  data: function() {
    return {
      linkLesson: { ...this.lesson },
      src: process.env.VUE_APP_API_BASE_URL + this.lesson.link,
      showPreview: false
    };
  },
  created() {},
  methods: {
    preview() {
      this.showPreview = !this.showPreview;
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
    }
  },
  computed: {
    previewButtonText: function() {
      return this.showPreview ? "Hide Preview" : "Show Preview";
    }
  }
};
</script>
