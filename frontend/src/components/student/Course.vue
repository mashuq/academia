<template>
  <span v-if="isMobile()">
    <h4 class="text-center">
      {{courseInformation.courseName}},
      <i>{{courseInformation.sectionName}}</i>
    </h4>
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
              {{courseInformation.courseName}},
              <i>{{courseInformation.sectionName}}</i>
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
    courseInformation: { type: Object, required: true }
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
        course: this.courseInformation.course,
        section: this.courseInformation.section
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
  watch: {
    courseInformation() {
      this.initSessions();
    }
  }
};
</script>
