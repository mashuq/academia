<template>
  <span v-if="isMobile()">
    <p class="display-1 text--primary">{{ noteLesson.name }}</p>
    <small v-html="noteLesson.description"></small>
    <h4>
      <a target="_blank" rel="noopener noreferrer" :href="src">View / Download Note</a>
    </h4>
  </span>
  <v-card class="mx-auto" v-else>
    <v-card-text>
      <p class="display-1 text--primary">{{ noteLesson.name }}</p>
      <p v-html="noteLesson.description"></p>
      <h4>
        <a target="_blank" rel="noopener noreferrer" :href="src">View / Download Note</a>
      </h4>
      <pdf v-if="showPreview" :src="src" style="display: inline-block; width: 360px;"></pdf>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="deep-purple accent-4" @click="preview">{{previewButtonText}}</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import pdf from "vue-pdf";
export default {
  components: {
    pdf
  },
  props: {
    lesson: { type: Object, required: true }
  },
  data: function() {
    return {
      noteLesson: { ...this.lesson },
      src: process.env.VUE_APP_API_BASE_URL + this.lesson.note,
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
