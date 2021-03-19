<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title><b>{{courseName}}, <i>{{sectionName}}</i></b></v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-expansion-panels focusable popout v-model="panel">
          <draggable v-model="sessions" tag="span" style="width:100%">
            <v-expansion-panel v-for="session in sessions" :key="session.id">
              <v-expansion-panel-header>{{
                session.name
              }}</v-expansion-panel-header>
              <v-expansion-panel-content>
                <Lessons v-bind:sessionId="session.id" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </draggable>
        </v-expansion-panels> </v-col
    ></v-row>
  </span>
</template>

<script>
import draggable from "vuedraggable";
import { post } from "@/service/service.js";
import Lessons from "@/components/student/Lessons.vue";

export default {
  props: {
    section: { type: Number, required: true },
    course: { type: Number, required: true },
    courseName: { type: String, required: true },
    sectionName: { type: String, required: true },
  },
  computed: {
    
  },
  methods: {
    async initSessions() {
      let response = await post("/sessions_by_course_student/", {
        course: this.course,
        section: this.section
      });
      if (response.ok) {
        let data = await response.json();
        this.sessions = data;
      }
    },
  },
  components: {
    draggable,
    Lessons,
  },
  data: () => ({
    sessionId: 0,
    sessionName: null,
    sessions: [],
    panel: [],
  }),
  created() {
    this.initSessions();
  },
  watch: {
    
  },
};
</script>
