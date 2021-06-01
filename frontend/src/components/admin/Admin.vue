<template>
  <v-row no-gutters>
    <v-col :cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title"> এডমিন প্যানেল </v-list-item-title>
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
      <CourseCategory v-if="showCourseCategory" />
      <Course v-if="showCourse" />
      <Section v-if="showSection" />
      <Session v-if="showSession" />
      <QuestionBank v-if="showQuestionBank" />
      <SessionVisibility v-if="showSessionVisibility" />
      <Student v-if="showStudent" />
      <Teacher v-if="showTeacher" />
      <SectionTeacher v-if="showSectionTeacher" />
      <StudentSection1 v-if="showStudentSection1" />
      <StudentSection2 v-if="showStudentSection2" />
      <Testimonial v-if="showTestimonial" />
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
import Student from "@/components/admin/Student.vue";
import Teacher from "@/components/admin/Teacher.vue";
import SectionTeacher from "@/components/admin/SectionTeacher.vue";
import StudentSection1 from "@/components/admin/StudentSection1.vue";
import StudentSection2 from "@/components/admin/StudentSection2.vue";
import Testimonial from "@/components/admin/Testimonial.vue";

export default {
  components: {
    CourseCategory,
    Course,
    Section,
    Session,
    QuestionBank,
    SessionVisibility,
    Student,
    Teacher,
    SectionTeacher,
    StudentSection1,
    StudentSection2,
    Testimonial
  },
  data: () => ({
    links: [
      { label: "কোর্স ক্যাটেগরি", link: "courseCategory", icon : 'mdi-concourse-ci' },
      { label: "কোর্স", link: "course", icon: 'mdi-compass-rose' },
      { label: "সেকশন", link: "section", icon: 'mdi-tree' },
      { label: "সেশন", link: "session", icon: 'mdi-turtle'  },
      { label: "প্রশ্ন সম্ভার", link: "questionBank", icon: 'mdi-pulse'  },
      { label: "সেশন দৃশ্যমানতা", link: "sessionVisibility", icon: 'mdi-drama-masks'  },
      { label: "শিক্ষার্থী", link: "student", icon: 'mdi-sail-boat'  },
      { label: "শিক্ষক/শিক্ষিকা", link: "teacher", icon: 'mdi-diamond-stone'  },
      { label: "সেকশনের শিক্ষক/শিক্ষিকা", link: "sectionTeacher", icon: 'mdi-laptop'  },
      { label: "শিক্ষার্থী কোর্স/সেকশন ১", link: "studentSection1", icon: 'mdi-codepen'  },
      { label: "শিক্ষার্থী কোর্স/সেকশন ২", link: "studentSection2", icon: 'mdi-umbrella'  },
      { label: "শিক্কার্থীদের মন্তব্য", link: "testimonial", icon: 'mdi-star'  },
    ],
    showCourseCategory: false,
    showCourse: false,
    showSection: false,
    showSession: false,
    showQuestionBank: false,
    showSessionVisibility: false,
    showStudent: false,
    showTeacher: false,
    showSectionTeacher: false,
    showStudentSection1: false,
    showStudentSection2: false,
    showTestimonial: false,
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
        case "student":
          this.showStudent = true;
          break;
        case "teacher":
          this.showTeacher = true;
          break;
        case "sectionTeacher":
          this.showSectionTeacher = true;
          break;
        case "studentSection1":
          this.showStudentSection1 = true;
          break;
        case "studentSection2":
          this.showStudentSection2 = true;
          break;
        case "testimonial":
          this.showTestimonial = true;
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
      this.showStudent = false;
      this.showTeacher = false;
      this.showSectionTeacher = false;
      this.showStudentSection1 = false;
      this.showStudentSection2 = false;
      this.showTestimonial = false;
    },
  },
};
</script>
