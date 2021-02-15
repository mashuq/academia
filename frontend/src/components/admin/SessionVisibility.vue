<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>Session Visibility </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-autocomplete
          v-model="course"
          :items="courses"
          label="Course"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-autocomplete
          v-model="section"
          :items="sections"
          label="Section"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="sessions"
          :single-select="singleSelect"
          item-key="id"
          show-select
          hide-default-footer
        >
        </v-data-table>
        <v-layout v-if="showSave" class="d-flex justify-center">
          <v-btn class="mr-4" color="primary" @click="saveVisibility"
            >Save Visibililtiy</v-btn
          >
        </v-layout>
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar">
      {{ message }}
      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<script>
import { get, post } from "@/service/service.js";

export default {
  computed: {
    showSave: function() {
      if (this.sessions && this.sessions.length > 0) {
        return true;
      }
      return false;
    },
  },
  methods: {
    async saveVisibility() {
      let data = [];
      this.selected.forEach((element) => {
        data.push({
          session: element.id,
          section: this.section,
          visible: true,
        });
      });
      console.log(data);
      console.log(this.section);
      let response = await post("/save_session_section_visibility/", {
        visible_list: data,
        section: this.section,
      });
      if (response.ok) {
        this.message = "Visibility Save Succesfully";
        this.snackbar = true;
      } else {
        this.message = "Error Saving visibility, please try again";
        this.snackbar = true;
      }
    },
    async initSessions() {
      let response = await post("/sessions_by_course/", {
        course: this.course,
      });
      if (response.ok) {
        let data = await response.json();
        this.sessions = data;
      }
    },
    async initSections() {
      let response = await post("/sections_by_course/", {
        course: this.course,
      });
      if (response.ok) {
        let data = await response.json();
        this.sections = data;
      }
    },
    async initCourses() {
      let response = await get("/courses/");
      if (response.ok) {
        let data = await response.json();
        this.courses = data.results;
      }
    },
    async initSessionSections() {
      let response = await post("/list_session_section/", {
        section: this.section,
      });
      if (response.ok) {
        let data = await response.json();
        data.forEach((element) => {
          if (element.visible) {
            this.selected.push({ id: element.session });
          }
        });
      }
    },
  },
  components: {},
  data: () => ({
    course: null,
    courses: [],
    session: null,
    sessions: [],
    section: null,
    sections: [],
    singleSelect: false,
    selected: [],
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Session", value: "name" },
    ],
    message: null,
    snackbar: false,
  }),
  created() {
    this.initCourses();
  },
  watch: {
    course: async function(val) {
      if (val) {
        this.session = null;
        this.initSections();
      }
    },
    section: async function(val) {
      if (val) {
        this.selected = [];
        await this.initSessions();
        this.initSessionSections();
      }
    },
    selected: function(val) {
      console.log(val);
    },
  },
};
</script>
