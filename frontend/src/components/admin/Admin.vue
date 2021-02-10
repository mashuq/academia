<template>
  <v-row no-gutters>
    <v-col :cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title"> Admin Panel </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list dense nav>
          <v-list-item link v-on:click="listAction('courseCategory')">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Course Categories</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link v-on:click="listAction('course')">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Courses</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link v-on:click="listAction('section')">
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Sections</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-col>
    <v-col :cols="10">
      <CourseCategory v-if="showCourseCategory" />
      <Course v-if="showCourse" />
      <Section v-if="showSection" />
    </v-col>
  </v-row>
</template>

<script>
import CourseCategory from "@/components/admin/CourseCategory.vue";
import Course from "@/components/admin/Course.vue";
import Section from "@/components/admin/Section.vue";

export default {
  components: {
    CourseCategory,
    Course,
    Section,
  },
  data: () => ({
    showCourseCategory: false,
    showCourse: false,
    showSection: false,
  }),
  methods: {
    listAction(value) {
      this.hideAll()
      if (value == "courseCategory") {
        this.showCourseCategory = true;
      }
      else if (value == "course") {
        this.showCourse = true;
      }
      else if (value == "section") {
        this.showSection = true;
      }
    },
    hideAll(){
      this.showCourseCategory = false;
      this.showCourse = false;
      this.showSection = false;
    }
  },
};
</script>
