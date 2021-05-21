<template>
  <v-card v-if="isMobile()" :style="mybgcolor">
    <v-card-title>{{syllabus.title}}</v-card-title>
    <v-card-text>
      <ol>
        <li v-for="item in syllabus.body" :key="item">{{ item }}</li>
      </ol>
    </v-card-text>
  </v-card>
  <v-col v-else>
    <v-card :style="mybgcolor">
      <v-card-title>{{syllabus.title}}</v-card-title>
      <v-card-text>
        <ol>
          <li v-for="item in syllabus.body" :key="item">{{ item }}</li>
        </ol>
      </v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    bgcolor: { type: String, required: false },
    syllabus: { type: Object, required: true }
  },
  data: function() {
    return {
      mybgcolor: {
        backgroundColor: this.bgcolor
      }
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
