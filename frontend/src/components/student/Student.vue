<template>
  <v-row v-if="isMobile()">
    <v-list dense nav>
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
    <Course
      v-bind:section="section"
      v-bind:course="course"
      v-bind:sectionName="sectionName"
      v-bind:courseName="courseName"
      v-if="showCourse"
    />
  </v-row>
  <v-row no-gutters v-else>
    <v-col :cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title">শিক্ষার্থী প্যানেল</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-subtitle class="subtitle">আমার কোর্সসমূহ</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list dense nav>
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
      </v-navigation-drawer>
    </v-col>
    <v-col :cols="10">
      <Course
        v-bind:section="section"
        v-bind:course="course"
        v-bind:sectionName="sectionName"
        v-bind:courseName="courseName"
        v-if="showCourse"
      />
    </v-col>
  </v-row>
</template>

<script>
import { get } from "@/service/service.js";
import Course from "@/components/student/Course.vue";

export default {
  components: {
    Course
  },
  data: () => ({
    courses: [],
    section: null,
    course: null,
    courseName: null,
    sectionName: null,
    showCourse: false
  }),
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
    courseAction(value) {
      this.section = value.sectionId;
      this.course = value.courseId;
      this.courseName = value.courseName;
      this.sectionName = value.sectionName;
      this.showCourse = true;
    },
    hideAll() {
      this.showCourse = false;
    },
    async initCourses() {
      let response = await get("/list_sections_for_student/");
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
  created() {
    this.initCourses();
  }
};
</script>
