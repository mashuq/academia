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
      <h4>Multiple Choice Questions</h4>
      <v-simple-table fixed-header height="300px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                ID
              </th>
              <th class="text-left">
                Question
              </th>
              <th class="text-left">
                Choice 1
              </th>
              <th class="text-left">
                Choice 2
              </th>
              <th class="text-left">
                Choice 3
              </th>
              <th class="text-left">
                Choice 4
              </th>
              <th class="text-left">
                Correct Choice
              </th>
              <th class="text-left">
                Mark
              </th>
              <th class="text-left"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in mcqs" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.question }}</td>
              <td>{{ item.choice1 }}</td>
              <td>{{ item.choice2 }}</td>
              <td>{{ item.choice3 }}</td>
              <td>{{ item.choice4 }}</td>
              <td>{{ item.correct_choice }}</td>
              <td>{{ item.mark }}</td>
              <td>
                <v-btn icon @click="deleteMcq(item.id)">
                  <v-icon color="red darken-2">mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </template>

    <template v-if="showQuestions">
      <h4>Short Questions</h4>
      <v-simple-table fixed-header height="300px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                ID
              </th>
              <th class="text-left">
                Question
              </th>
              <th class="text-left">
                Mark
              </th>
              <th class="text-left"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in sqs" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.question }}</td>
              <td>{{ item.mark }}</td>
              <td>
                <v-btn icon @click="deleteSq(item.id)">
                  <v-icon color="red darken-2">mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </template>

    <template v-if="showQuestions">
      <h4>Broad Questions</h4>
      <v-simple-table fixed-header height="300px">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">
                ID
              </th>
              <th class="text-left">
                Question
              </th>
              <th class="text-left">
                Mark
              </th>
              <th class="text-left"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in bqs" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.question }}</td>
              <td>{{ item.mark }}</td>
              <td>
                <v-btn icon @click="deleteBq(item.id)">
                  <v-icon color="red darken-2">mdi-delete</v-icon>
                </v-btn>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
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
      let response = await post("/list_mcq_by_session/", {
        session: this.session,
      });
      if (response.ok) {
        let data = await response.json();
        this.mcqs = data;
      }
    },
    async initSq() {
      let response = await post("/list_sq_by_session/", {
        session: this.session,
      });
      if (response.ok) {
        let data = await response.json();
        this.sqs = data;
      }
    },
    async initBq() {
      let response = await post("/list_bq_by_session/", {
        session: this.session,
      });
      if (response.ok) {
        let data = await response.json();
        this.bqs = data;
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
        this.courses = data.results;
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
  },
};
</script>
