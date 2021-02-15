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
          <v-list-item
            v-for="link in links"
            :key="link.name"
            link
            v-on:click="listAction(link.link)"
          >
            <v-list-item-icon>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ link.label }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-col>
    <v-col :cols="10">
      <CourseCategory v-if="showCourseCategory" />
      <Course v-if="showCourse" />
      <Section v-if="showSection" />
      <Session v-if="showSession" />
      <QuestionBank v-if="showQuestionBank" />
      <SessionVisibility v-if="showSessionVisibility" />
    </v-col>
  </v-row>
</template>

<script>
import CourseCategory from "@/components/admin/CourseCategory.vue";
import Course from "@/components/admin/Course.vue";
import Section from "@/components/admin/Section.vue";
import Session from "@/components/admin/Session.vue";
import QuestionBank from "@/components/admin/QuestionBank.vue";
import SessionVisibility from "@/components/admin/SessionVisibility.vue";

export default {
  components: {
    CourseCategory,
    Course,
    Section,
    Session,
    QuestionBank,
    SessionVisibility
  },
  data: () => ({
    links: [
      { label: "Course Categories", link: "courseCategory" },
      { label: "Courses", link: "course" },
      { label: "Sections", link: "section" },
      { label: "Sessions", link: "session" },
      { label: "Question Bank", link: "questionBank" },
      { label: "Section Visibility", link: "sessionVisibility" },
    ],
    showCourseCategory: false,
    showCourse: false,
    showSection: false,
    showSession: false,
    showQuestionBank: false,
    showSessionVisibility: false,
  }),
  methods: {
    listAction(value) {
      this.hideAll();
      switch (value) {
        case "courseCategory":
          this.showCourseCategory = true;
          break;
        case "course":
          this.showCourse = true;
          break;
        case "section":
          this.showSection = true;
          break;
        case "session":
          this.showSession = true;
          break;
        case "questionBank":
          this.showQuestionBank = true;
          break;
        case "sessionVisibility":
          this.showSessionVisibility = true;
          break;
        default:
          console.log(value);
      }
    },
    hideAll() {
      this.showCourseCategory = false;
      this.showCourse = false;
      this.showSection = false;
      this.showSession = false;
      this.showQuestionBank = false;
      this.showSessionVisibility = false;
    },
  },
};
</script>
