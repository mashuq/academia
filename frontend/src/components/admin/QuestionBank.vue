<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>Question Bank </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="disableAddButtons"
            @click="showMcqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>Multiple Choice Question</v-btn
          >

          <v-btn
            :disabled="disableAddButtons"
            @click="showSqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>Short Question
          </v-btn>

          <v-btn
            :disabled="disableAddButtons"
            @click="showBqDialog"
            text
            color="primary"
            ><v-icon dark> mdi-plus </v-icon>Broad Question</v-btn
          >
        </v-toolbar>
      </v-col>
    </v-row>
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
          v-model="session"
          :items="sessions"
          label="Session"
          item-text="name"
          item-value="id"
        ></v-autocomplete>
      </v-col>
    </v-row>

    <v-dialog v-model="mcqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Multiple Choice Question</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.question"
                  label="Question"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.choice1"
                  label="Choice 1"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="mcq.choice2"
                  label="Choice 2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.choice3"
                  label="Choice 1"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field
                  v-model="mcq.choice4"
                  label="Choice 2"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="mcq.correct_choice"
                  label="Correct Choice"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="mcq.mark" label="Mark"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideMcqDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveMcq">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="sqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Short Question</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="sq.question"
                  label="Question"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="sq.mark" label="Mark"></v-text-field>
              </v-col>
              <v-col> </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideSqDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveSq">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="bqDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Broad Question</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="bq.question"
                  label="Question"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="bq.mark" label="Mark"></v-text-field>
              </v-col>
              <v-col> </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideBqDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveBq">
            Save
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
          <v-toolbar-title>Multiple Choice Questions</v-toolbar-title>
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
          <v-toolbar-title>Short Questions</v-toolbar-title>
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
          <v-toolbar-title>Broad Questions</v-toolbar-title>
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
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Question", value: "question" },
      { text: "Choice 1", value: "choice1" },
      { text: "Choice 2", value: "choice2" },
      { text: "Choice 3", value: "choice3" },
      { text: "Choice 4", value: "choice4" },
      { text: "Correct Choice", value: "correct_choice" },
      { text: "Mark", value: "mark" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    sqHeaders: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Question", value: "question" },
      { text: "Mark", value: "mark" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    bqHeaders: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Question", value: "question" },
      { text: "Mark", value: "mark" },
      { text: "Actions", value: "actions", sortable: false },
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
