<template>
    <span v-if="isMobile()" :style="mybgcolor">
      <h3 class="text-center">{{year}}</h3>
      <Syllabus
        v-for="(item, index) in syllabus"
        v-bind:syllabus="item"
        v-bind:index="index"
        v-bind:key="item.id"
        v-bind:bgcolor="bgcolor"
      ></Syllabus>
    </span>

    <span v-else :style="mybgcolor">
      <v-grid >
        <v-row align="stretch" class="ma-2">
          <v-col>
            <h1>{{year}}</h1>
          </v-col>
          <Syllabus
            v-for="(item, index) in syllabus"
            v-bind:syllabus="item"
            v-bind:bgcolor="bgcolor"
            v-bind:index="index"
            v-bind:key="item.id"
          ></Syllabus>
        </v-row>
      </v-grid>
    </span>
</template>

<script>
import Syllabus from "@/components/syllabus/Syllabus.vue";
export default {
  components: {
    Syllabus
  },
  props: {
    year: { type: String, required: true },
    syllabus: { type: Array, required: true },
    bgcolor: { type: String, required: false }
  },
  data: function() {
    return {
      mybgcolor: {
        backgroundColor: this.bgcolor,
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
