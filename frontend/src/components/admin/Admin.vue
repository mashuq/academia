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
      </v-list>
    </v-navigation-drawer>
  </v-col>
  <v-col :cols="10">
    <CourseCategory v-if="showCourseCategory" />
  </v-col>
</v-row>
</template>


<script>
import CourseCategory from "@/components/admin/CourseCategory.vue";

export default {
  components: {
    CourseCategory,
  },
  data: () => ({
    showCourseCategory: false,
  }),
  methods: {
    listAction(value) {
      console.log(value);
      if(value == 'courseCategory'){
        console.log('yay');
        this.showCourseCategory = true;
      }
    },
  },
};
</script>