<template>
  <v-card class="mx-auto">
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
      <v-btn text color="blue darken-4 accent-4" @click="editLesson">Edit</v-btn>
      <v-btn text color="red darken-4 accent-4" @click="deleteLesson">Delete</v-btn>
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
      showPreview: false
    };
  },
  created() {},
  methods: {
    editLesson() {
      this.$emit("editNote", this.noteLesson.id);
    },
    deleteLesson() {
      this.$emit("remove", this.noteLesson.id);
    },
    preview() {
      this.showPreview = !this.showPreview;
    }
  },
  computed: {
    src: function(){
      return process.env.VUE_APP_API_BASE_URL + this.lesson.note;
    },
    noteLesson: function() {
      return { ...this.lesson };
    },
    previewButtonText: function() {
      return this.showPreview ? "Hide Preview" : "Show Preview";
    }
  }
};
</script>
