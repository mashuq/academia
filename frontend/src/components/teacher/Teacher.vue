<template>
  <v-row no-gutters>
    <v-col :cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title class="title">শিক্ষক/শিক্ষিকা প্যানেল</v-list-item-title>
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
      <Assessment v-if="showAssessment" />
    </v-col>
  </v-row>
</template>

<script>
import Assessment from "@/components/teacher/Assessment.vue";

export default {
  components: {
    Assessment,
  },
  data: () =>
    ({
    links: [
      { label: "পরীক্ষা", link: "assessment", icon : 'mdi-stairs' },
    ],
    showAssessment: false,
  }),
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
    },
  },
};
</script>
