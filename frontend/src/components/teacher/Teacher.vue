<template>
  <v-row no-gutters>
    <v-col :cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title">শিক্ষক/শিক্ষিকা প্যানেল</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle class="subtitle">আমার কোর্সসমূহ</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <template v-if="!courses.length">
          <v-container>
            <v-alert dense outlined type="warning">আপনাকে কোন কোর্সের শিক্ষক হিসেবে নিয়োগ দেয়া হয়নি।</v-alert>
          </v-container>
        </template>
        <v-list v-else dense nav>
          <v-list-item
            v-for="course in courses"
            :key="course.id"
            course
            v-on:click="courseAction(course)"
          >
            <v-list-item-icon>
              <v-icon>mdi-star</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <div>{{ course.courseName }}</div>
              <sub>({{course.sectionName}})</sub>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list dense nav>
          <v-list-item
            v-for="link in links"
            :key="link.name"
            link
            v-on:click="listAction(link.link)"
          >
            <v-list-item-icon>
              <v-icon>{{link.icon}}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ link.label }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-col>
    <v-col :cols="10">
      <Assessment v-if="showAssessment" />
      <Course v-bind:courseInformation="courseInformation" v-if="showCourse" />
    </v-col>
  </v-row>
</template>

<script>
import Assessment from "@/components/teacher/Assessment.vue";
import Course from "@/components/teacher/Course.vue";
import { get } from "@/service/service.js";

export default {
  components: {
    Assessment,
    Course,
  },
  data: () =>
    ({
    links: [
      { label: "পরীক্ষা", link: "assessment", icon : 'mdi-stairs' },
    ],
    showAssessment: false,
    courseObj: {},
    courses: [],
    section: null,
    course: null,
    courseName: null,
    sectionName: null,
    showCourse: false
  }),
  created() {
    this.initCourses();
  },
  computed: {
    courseInformation: function() {
      return this.courseObj;
    }
  },
  methods: {
    listAction(value) {
      this.hideAll();
      switch (value) {
        case "assessment":
          this.showAssessment = true;
          break;
        default:
          console.log(value);
      }
    },
    hideAll() {
      this.showAssessment = false;
      this.showCourse = false;
    },
    courseAction(value) {
      this.hideAll();
      let courseObj = {};
      courseObj.section = value.sectionId;
      courseObj.course = value.courseId;
      courseObj.courseName = value.courseName;
      courseObj.sectionName = value.sectionName;
      this.courseObj = courseObj;
      this.showCourse = true;
    },
    async initCourses() {
      let response = await get("/list_detailed_sections_for_teacher/");
      if (response.ok) {
        let data = await response.json();
        this.courses = [];
        data.forEach(element => {
          this.courses.push({
            sectionId: element["section"]["id"],
            courseId: element["section"]["course_id"],
            courseName: element["section"]["course"],
            sectionName: element["section"]["name"]
          });
        });
      }
    }
  },
};
</script>
