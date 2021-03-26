<template>
  <span v-if="isMobile()">
    <v-expansion-panels focusable popout v-model="panel">
      <v-expansion-panel v-for="session in sessions" :key="session.id">
        <v-expansion-panel-header>
          {{
          session.name
          }}
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <Lessons v-bind:sessionId="session.id" />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </span>
  <span v-else>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>
            <b>
              {{courseName}},
              <i>{{sectionName}}</i>
            </b>
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-expansion-panels focusable popout v-model="panel">
          <v-expansion-panel v-for="session in sessions" :key="session.id">
            <v-expansion-panel-header>
              {{
              session.name
              }}
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <Lessons v-bind:sessionId="session.id" />
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </span>
</template>

<script>
import { post } from "@/service/service.js";
import Lessons from "@/components/student/Lessons.vue";

export default {
  props: {
    section: { type: Number, required: true },
    course: { type: Number, required: true },
    courseName: { type: String, required: true },
    sectionName: { type: String, required: true }
  },
  computed: {},
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
    },
    async initSessions() {
      let response = await post("/sessions_by_course_student/", {
        course: this.course,
        section: this.section
      });
      if (response.ok) {
        let data = await response.json();
        this.sessions = data;
      }
    }
  },
  components: {
    Lessons
  },
  data: () => ({
    sessionId: 0,
    sessionName: null,
    sessions: [],
    panel: []
  }),
  created() {
    this.initSessions();
  },
  watch: {}
};
</script>
