<template>
  <v-card class="mx-auto">
    <v-card-text>
      <p class="display-1 text--primary">
        {{ linkLesson.name }}
      </p>
      <p v-html="linkLesson.description"></p>
      <h4><a target="_blank" :href="linkLesson.link">{{linkLesson.title}}</a></h4>
    </v-card-text>
    <v-card-actions>
      <v-btn text color="red darken-4 accent-4" @click="deleteLesson">
        Delete
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    lesson: { type: Object, required: true },
  },
  data: function() {
    return {
      linkLesson: { ...this.lesson },
    };
  },
  created() {},
  methods: {
    deleteLesson() {
      this.$emit("remove", this.linkLesson.id);
    },
  },
};
</script>
