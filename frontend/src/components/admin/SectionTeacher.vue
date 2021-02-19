<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>Section Teacher</v-toolbar-title>
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
        <v-autocomplete
          v-model="teacher"
          :items="teachers"
          label="Teacher"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
      <v-col>
        <v-btn
          color="primary"
          :disabled="disableAssignButton"
          @click="assignSectionToTeacher"
          >Assign Section</v-btn
        >
      </v-col>
    </v-row>

    <v-data-table
      items-per-page="10"
      :headers="headers"
      :items="sectionTeachers"
      :options.sync="options"
      :server-items-length="totalItems"
      :loading="loading"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
      }"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Teachers Assigned to Section</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small @click="deleteAssignment(item.id)"> mdi-delete </v-icon>
      </template>
    </v-data-table>

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
import { get, post, del } from "@/service/service.js";

export default {
  computed: {
    showSave: function() {
      if (this.sessions && this.sessions.length > 0) {
        return true;
      }
      return false;
    },
    disableAssignButton: function() {
      if (!this.course || !this.section || !this.teacher) {
        return true;
      }
      return false;
    },
  },
  methods: {
    async assignSectionToTeacher() {
      let response = await post("/section_teachers/", {
        teacher: this.teacher,
        section: this.section,
      });
      if (response.ok) {
        this.initSectionTeachers();
        this.message = "Section assigned to teacher Succesfully";
        this.snackbar = true;
      } else {
        this.message = "Error assigning teacher, may be already assigned ?";
        this.snackbar = true;
      }
    },
    async initSectionTeachers() {
      let response = await get(`/section_teachers/?page=${this.options.page}`);
      if (response.ok) {
        let data = await response.json();
        this.sectionTeachers = data.results;
        this.totalItems = data.count;
      }
      this.loading = false;
    },
    async initTeachers() {
      let response = await get("/teachers/");
      if (response.ok) {
        let data = await response.json();
        this.teachers = data;
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
        this.courses = data;
      }
    },
    async deleteAssignment(id) {
      let response = await del(`/section_teachers/${id}/`);
      if (response.ok) {
        this.initSectionTeachers();
      }
    },
  },
  components: {},
  data: () => ({
    course: null,
    courses: [],
    teacher: null,
    teachers: [],
    section: null,
    sections: [],
    sectionTeachers: [],
    totalItems: 0,
    loading: true,
    options: {},
    headers: [
      { text: "Course", value: "section.course" },
      { text: "Section", value: "section.name" },
      { text: "Teacher", value: "teacher.name" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    message: null,
    snackbar: false,
  }),
  created() {
    this.initCourses();
    this.initTeachers();
    this.initSectionTeachers();
  },
  watch: {
    course: async function(val) {
      if (val) {
        this.session = null;
        this.initSections();
      }
    },
    options: {
      handler() {
        this.initSectionTeachers();
      },
      deep: true,
    },
  },
};
</script>
