<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>প্রশ্ন সম্ভার</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="disableAddButtons"
            @click="showMcqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>বহুনির্বাচনি প্রশ্ন</v-btn
          >

          <v-btn
            :disabled="disableAddButtons"
            @click="showSqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>সংক্ষিপ্ত প্রশ্ন
          </v-btn>

          <v-btn
            :disabled="disableAddButtons"
            @click="showBqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>রচনামূলক প্রশ্ন</v-btn
          >
        </v-toolbar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-autocomplete
          v-model="course"
          :items="courses"
          label="কোর্স"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
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

    <v-dialog v-model="mcqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">নতুন বহুনির্বাচনি প্রশ্ন</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.question"
                  label="প্রশ্ন"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.choice1"
                  label="উত্তর ১"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="mcq.choice2"
                  label="উত্তর ২"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.choice3"
                  label="উত্তর ৩"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="mcq.choice4"
                  label="উত্তর ৪"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.correct_choice"
                  label="সঠিক উত্তর"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="mcq.mark" label="নম্বর"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideMcqDialog">
            বাতিল
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveMcq">
            সংরক্ষণ
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="sqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">নতুন সংক্ষিপ্ত প্রশ্ন</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="sq.question"
                  label="প্রশ্ন"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="sq.mark" label="নম্বর"></v-text-field>
              </v-col>
              <v-col> </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideSqDialog">
            বাতিল
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveSq">
            সংরক্ষণ
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="bqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">নতুন রচনামূলক প্রশ্ন</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="bq.question"
                  label="প্রশ্ন"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="bq.mark" label="নম্বর"></v-text-field>
              </v-col>
              <v-col> </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideBqDialog">
            বাতিল
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveBq">
            সংরক্ষণ
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page=5
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
          <v-icon small @click="deleteMcq(item.id)"> mdi-delete </v-icon>
        </template>
      </v-data-table>
    </template>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page=5
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
          <v-icon small @click="deleteSq(item.id)"> mdi-delete </v-icon>
        </template>
      </v-data-table>
    </template>

    <template v-if="showQuestions">
      <v-data-table
        items-per-page=5
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
          <v-icon small @click="deleteBq(item.id)"> mdi-delete </v-icon>
        </template>
      </v-data-table>
    </template>
  </span>
</template>

<script>
import { get, post, del } from "@/service/service.js";

export default {
  computed: {
    disableAddButtons: function() {
      if (this.session) {
        return false;
      }
      return true;
    },
    showQuestions: function() {
      if (this.session) {
        return true;
      }
      return false;
    },
  },
  methods: {
    async deleteMcq(id) {
      let response = await del(`/mcq/${id}/`);
      if (response.ok) {
        this.initMcq();
      }
    },
    async deleteSq(id) {
      let response = await del(`/sq/${id}/`);
      if (response.ok) {
        this.initSq();
      }
    },
    async deleteBq(id) {
      let response = await del(`/bq/${id}/`);
      if (response.ok) {
        this.initBq();
      }
    },
    async initMcq() {
      let response = await post(
        `/list_mcq_by_session/`,
        {
          session: this.session,
          page: this.optionsMcq.page,
        }
      );
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
    async initSessions() {
      let response = await post("/sessions_by_course/", {
        course: this.course,
      });
      if (response.ok) {
        let data = await response.json();
        this.sessions = data;
      }
    },
    async initCourses() {
      let response = await get("/courses/");
      if (response.ok) {
        let data = await response.json();
        this.courses = data;
      }
    },
    async saveMcq() {
      let response = await post("/mcq/", {
        ...this.mcq,
        session: this.session,
      });
      if (response.ok) {
        this.initMcq();
        this.hideMcqDialog();
        this.msq = {
          mark: 1,
          question: null,
          choice1: null,
          choice2: null,
          choice3: null,
          choice4: null,
          correct_choice: null,
        };
      }
    },
    hideMcqDialog() {
      this.mcqDialog = false;
    },
    showMcqDialog() {
      this.mcqDialog = true;
    },
    async saveSq() {
      let response = await post("/sq/", {
        ...this.sq,
        session: this.session,
      });
      if (response.ok) {
        this.initSq();
        this.hideSqDialog();
        this.sq = {
          mark: 5,
          question: null,
        };
      }
    },
    hideSqDialog() {
      this.sqDialog = false;
    },
    showSqDialog() {
      this.sqDialog = true;
    },
    async saveBq() {
      let response = await post("/bq/", {
        ...this.bq,
        session: this.session,
      });
      if (response.ok) {
        this.initBq();
        this.hideBqDialog();
        this.bq = {
          mark: 10,
          question: null,
        };
      }
    },
    hideBqDialog() {
      this.bqDialog = false;
    },
    showBqDialog() {
      this.bqDialog = true;
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
      { text: "সম্পাদনা", value: "actions", sortable: false },
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
      { text: "সম্পাদনা", value: "actions", sortable: false },
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
      { text: "সম্পাদনা", value: "actions", sortable: false },
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
    mcqDialog: false,
    mcqs: [],
    mcq: {
      mark: 1,
      question: null,
      choice1: null,
      choice2: null,
      choice3: null,
      choice4: null,
      correct_choice: null,
    },
    sqDialog: false,
    sqs: [],
    sq: {
      mark: 5,
      question: null,
    },
    bqDialog: false,
    bqs: [],
    bq: {
      mark: 10,
      question: null,
    },
  }),
  created() {
    this.initCourses();
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
