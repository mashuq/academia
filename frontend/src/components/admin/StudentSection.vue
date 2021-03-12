<template>
  <span>
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
    </v-row>
    <v-data-table
      :headers="headers"
      :items="students"
      :options.sync="options"
      :server-items-length="totalStudents"
      :loading="loading"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
      }"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>শিক্ষার্থী</v-toolbar-title>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <template v-if="item.enrolled == 'NOT_KNOWN'">-</template>
        <template v-if="item.enrolled == 'NOT_ENROLLED'">ভর্তি নেই <v-btn color="primary" @click="enrol(item.id)"> ভর্তি করুন  </v-btn></template>
        <template v-if="item.enrolled == 'ENROLLED'">ভর্তি রয়েছে<v-btn color="error" @click="cancelEnrollment(item.enrolmentId)"> ভর্তি বাতিল করুন   </v-btn></template>
      </template>
    </v-data-table>
    <v-snackbar v-model="snackbar">
      একটি সমস্যা হয়েছে, পুনরায় চেষ্টা করুন
      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">Close</v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<script>
import { get, post } from "@/service/service.js";
import moment from "moment";
export default {
  components: {
  },
  data: () => ({
    totalStudents: 0,
    loading: true,
    options: {},
    snackbar: false,
    dialog: false,
    headers: [
      {
        text: "আইডি",
        align: "start",
        sortable: false,
        value: "id"
      },
      { text: "নাম", value: "name" },
      { text: "ইউজারনেম", value: "user.username" },
      { text: "ইমেইল", value: "user.email" },
      { text: "লিঙ্গ", value: "gender" },
      { text: "জন্মতারিখ", value: "date_of_birth" },
      { text: "যোগদানের তারিখ", value: "user.date_joined" },
      { text: "সম্পাদনা", value: "actions", sortable: false }
    ],
    students: [],
    course: null,
    courses: [],
    section: null,
    sections: [],
    editedIndex: -1,
    editedItem: {
      name: ""
    },
    defaultItem: {
      name: ""
    }
  }),

  watch: {
    options: {
      handler() {
        this.initStudent();
      },
      deep: true
    },
    students() {
      if (this.students) {
        this.students.forEach(element => {
          element.date_of_birth = moment(element.date_of_birth).format(
            "DD MMM YYYY"
          );
          element.user.date_joined = moment(element.user.date_joined).format(
            "DD MMM YYYY"
          );
        });
      }
    },
    course: async function(val) {
      if (val) {
        this.session = null;
        this.initSections();
      }
    },
    section: async function(val) {
      if (val) {
        this.initEnrollment();
      }
    }
  },

  created() {
    this.initStudent();
    this.initCourses();
  },

  methods: {
    async enrol(student){
      let response = await post("/save_enrolment/", {
        section: this.section,
        student: student,
      });
      if(response.ok){
        this.initEnrollment();
      }
    },
    async cancelEnrollment(enrolmentId){
      let response = await post("/delete_enrolment/", {
        enrolment: enrolmentId
      });
      if(response.ok){
        this.initEnrollment();
      }
    },
    async initCourses() {
      let response = await get("/courses/");
      if (response.ok) {
        let data = await response.json();
        this.courses = data;
      }
    },
    async initSections() {
      let response = await post("/sections_by_course/", {
        course: this.course
      });
      if (response.ok) {
        let data = await response.json();
        this.sections = data;
      }
    },
    async initEnrollment() {
      let students = [];
      this.students.forEach(function(item) {
        students.push(item.id);
      });
      let response = await post("/get_student_section/", {
        students: students,
        section: this.section
      });
      if (response.ok) {
        let data = await response.json();
        let students = this.students;
        students.forEach(function(student) {
          student.enrolled = "NOT_ENROLLED";
        });

        data.forEach(function(enrollment) {
          students.forEach(function(student) {
            if (enrollment.student == student.id) {
              student.enrolled = "ENROLLED";
              student.enrolmentId = enrollment.id;
            }
          });
        });
      }
    },
    async initStudent() {
      let response = await get(`/students/?page=${this.options.page}`);
      if (response.ok) {
        let data = await response.json();
        data.results.forEach(function(item) {
          item.enrolled = "NOT_KNOWN";
        });
        this.students = data.results;
        this.totalStudents = data.count;
      } else {
        this.snackbar = true;
      }
      if (this.section) {
        this.initEnrollment();
      }
      this.loading = false;
    },

  }
};
</script>
