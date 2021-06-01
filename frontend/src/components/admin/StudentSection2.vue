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
      <v-col>
        <v-switch v-model="enrolled" label="Enrolled?"></v-switch>
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
          <v-spacer></v-spacer>
          <!-- <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
          ></v-text-field> -->
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <template v-if="item.enrolled == 'NOT_KNOWN'">-</template>
        <template v-if="item.enrolled == 'NOT_ENROLLED'">
          ভর্তি নেই
          <v-btn color="primary" @click="enrol(item.id)">ভর্তি করুন</v-btn>
        </template>
        <template v-if="item.enrolled == 'ENROLLED'">
          ভর্তি রয়েছে
          <v-btn color="error" @click="cancelEnrollment(item.enrolmentId)">ভর্তি বাতিল করুন</v-btn>
        </template>
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

function validateEmail(email) {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

export default {
  components: {},
  data: () => ({
    enrolled: true,
    searched: false,
    search: "",
    totalStudents: 0,
    loading: false,
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
    async search(val) {
      if (this.searched && val === "") {
        this.searched = false;
        this.initStudent();
      }

      if (validateEmail(val)) {
        this.searched = true;
        let response = await post("/search_student/", {
          email: val
        });
        if (response.ok) {
          let data = await response.json();
          data.forEach(function(item) {
            item.enrolled = "NOT_KNOWN";
          });
          this.students = data;
          this.totalStudents = data.length;
          if (this.section) this.initEnrollment();
        }
      }
    },
    options: {
      handler() {
        if (this.enrolled) {
          this.initStudent();
        }
        if (!this.enrolled) {
          this.initNonStudent();
        }
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
      if (val && this.enrolled) {
        this.initStudent();
      }
      if (val && !this.enrolled) {
        this.initNonStudent();
      }
    },
    enrolled: async function(val) {
      if(this.options){
        this.options.page = 1;
      }
      if (val) {
        this.initStudent();
      }
      if (!val) {
        this.initNonStudent();
      }
    }
  },

  created() {
    this.initCourses();
  },

  methods: {
    async enrol(student) {
      let response = await post("/save_enrolment/", {
        section: this.section,
        student: student
      });
      if (response.ok) {
        this.initEnrollment();
      }
    },
    async cancelEnrollment(enrolmentId) {
      let response = await post("/delete_enrolment/", {
        enrolment: enrolmentId
      });
      if (response.ok) {
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
      console.log(this.students);
      console.log(students);
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
      if (this.options && this.options.page) {
        this.loading = true;
        let response = await get(
          `/enrolled_students/?page=${this.options.page}&section=${this.section}`
        );
        if (response.ok) {
          let data = await response.json();
          let students = [];
          data.results.forEach(function(item) {
            item.student.enrolled = "NOT_KNOWN";
            students.push(item.student);
          });
          this.students = students;
          this.totalStudents = data.count;
        } else {
          this.snackbar = true;
        }
        this.initEnrollment();
        this.loading = false;
      }
    },
    async initNonStudent() {
      if (this.options && this.options.page) {
        this.loading = true;
        let response = await get(
          `/not_enrolled_students/?page=${this.options.page}&section=${this.section}`
        );
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
        this.initEnrollment();
        this.loading = false;
      }
    }
  }
};
</script>
