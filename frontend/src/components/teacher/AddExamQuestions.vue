<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title
            >{{ assessment }} পরীক্ষায় প্রশ্ন যোগ</v-toolbar-title
          >
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="hideAddQuestionDialog">
            <v-icon dark> mdi-arrow-left-bold </v-icon>পরীক্ষায় ফেরত যান
          </v-btn>
        </v-toolbar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-autocomplete
          v-model="session"
          :items="sessions"
          label="সেশন"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
    </v-row>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page="5"
        :headers="mcqHeaders"
        :items="mcqs"
        :options.sync="optionsMcq"
        :server-items-length="totalMcq"
        :loading="loadingMcq"
        class="elevation-1"
        :footer-props="{
          disableItemsPerPage: true,
        }"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>বহুনির্বাচনি প্রশ্ন সম্ভার</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small @click="addItem(item.id)"> mdi-plus </v-icon>
        </template>
      </v-data-table>
    </template>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page="5"
        :headers="sqHeaders"
        :items="sqs"
        :options.sync="optionsSq"
        :server-items-length="totalSq"
        :loading="loadingSq"
        class="elevation-1"
        :footer-props="{
          disableItemsPerPage: true,
        }"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>সংক্ষিপ্ত প্রশ্ন সম্ভার</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small @click="addItem(item.id)"> mdi-plus </v-icon>
        </template>
      </v-data-table>
    </template>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page="5"
        :headers="bqHeaders"
        :items="bqs"
        :options.sync="optionsBq"
        :server-items-length="totalBq"
        :loading="loadingBq"
        class="elevation-1"
        :footer-props="{
          disableItemsPerPage: true,
        }"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>রচনামূলক প্রশ্ন সম্ভার</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
          </v-toolbar>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small @click="addItem(item.id)"> mdi-plus </v-icon>
        </template>
      </v-data-table>
    </template>

    <v-snackbar v-model="snackbar">
      {{ assessment }} পরীক্ষায় প্রশ্ন যোগ করা হয়েছে

      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<script>
import { get, post } from "@/service/service.js";

export default {
  props: {
    section: { type: Number, required: true },
    assessment: { type: String, required: true },
  },
  computed: {
    showQuestions: function() {
      if (this.session) {
        return true;
      }
      return false;
    },
  },
  methods: {
    addItem(val){
      this.snackbar = false;
      this.$emit("questionAdded", val);
      this.snackbar = true;
    },
    hideAddQuestionDialog() {
      this.$emit("cancel");
    },
    async initMcq() {
      let response = await post(`/list_mcq_by_session/`, {
        session: this.session,
        page: this.optionsMcq.page,
      });
      if (response.ok) {
        let data = await response.json();
        this.mcqs = data.result;
        this.totalMcq = data.count;
        this.loadingMcq = false;
      }
    },
    async initSq() {
      let response = await post("/list_sq_by_session/", {
        session: this.session,
        page: this.optionsSq.page,
      });
      if (response.ok) {
        let data = await response.json();
        this.sqs = data.result;
        this.totalSq = data.count;
        this.loadingSq = false;
      }
    },
    async initBq() {
      let response = await post("/list_bq_by_session/", {
        session: this.session,
        page: this.optionsBq.page,
      });
      if (response.ok) {
        let data = await response.json();
        this.bqs = data.result;
        this.totalBq = data.count;
        this.loadingBq = false;
      }
    },
    async initCourse() {
      let response = await get(`/sections/${this.section}/`);
      if (response.ok) {
        let data = await response.json();
        this.course = data.course;
      }
    },
    async initSessions() {
      let response = await post("/sessions_by_course/", {
        course: this.course,
      });
      if (response.ok) {
        let data = await response.json();
        this.sessions = data;
      }
    },
  },
  components: {},
  data: () => ({
    mcqHeaders: [
      {
        text: "আইডি ",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "প্রশ্ন", value: "question" },
      { text: "উত্তর ১", value: "choice1" },
      { text: "উত্তর ২", value: "choice2" },
      { text: "উত্তর ৩", value: "choice3" },
      { text: "উত্তর ৪", value: "choice4" },
      { text: "সঠিক উত্তর", value: "correct_choice" },
      { text: "নম্বর", value: "mark" },
      { text: "প্রশ্ন যোগ", value: "actions", sortable: false },
    ],
    sqHeaders: [
      {
        text: "আইডি ",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "প্রশ্ন", value: "question" },
      { text: "নম্বর", value: "mark" },
      { text: "প্রশ্ন যোগ", value: "actions", sortable: false },
    ],
    bqHeaders: [
      {
        text: "আইডি ",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "প্রশ্ন", value: "question" },
      { text: "নম্বর", value: "mark" },
      { text: "প্রশ্ন যোগ", value: "actions", sortable: false },
    ],
    totalMcq: 0,
    loadingMcq: true,
    optionsMcq: {},
    totalSq: 0,
    loadingSq: true,
    optionsSq: {},
    totalBq: 0,
    loadingBq: true,
    optionsBq: {},
    course: null,
    courses: [],
    session: 0,
    sessions: [],
    snackbar: false,
  }),
  created() {
    this.initCourse();
  },
  watch: {
    course: async function(val) {
      if (val) {
        this.session = null;
        this.initSessions();
      }
    },
    session: async function(val) {
      if (val) {
        this.initMcq();
        this.initSq();
        this.initBq();
      }
    },
    optionsMcq: {
      handler() {
        this.initMcq();
      },
      deep: true,
    },
    optionsSq: {
      handler() {
        this.initSq();
      },
      deep: true,
    },
    optionsBq: {
      handler() {
        this.initBq();
      },
      deep: true,
    },
  },
};
</script>
