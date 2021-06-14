<template>
  <span>
    <v-container>
      <v-btn
        @click="showCreateQuizDialog"
        v-if="showCreateQuizButton"
        color="green"
        class="ma-2 white--text"
      >
        New Quiz
        <v-icon right dark>mdi-comment-question</v-icon>
      </v-btn>
      <v-btn @click="showEditQuizDialog" v-else color="green" class="ma-2 white--text">
        Edit Quiz
        <v-icon right dark>mdi-comment-question</v-icon>
      </v-btn>

      <v-dialog v-model="showForm" max-width="500px">
        <v-card>
          <v-card-title>
            <span class="headline">New Link Lesson</span>
          </v-card-title>

          <v-card-text>
            <v-container>
              <v-row>
                <v-col>
                  <v-text-field v-model="quiz.name" label="Quiz Name"></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-text-field v-model="quiz.contribution" label="Contribution"></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-autocomplete
                    v-model="mcq"
                    :items="mcqs"
                    :loading="isLoading"
                    :search-input.sync="search"
                    hide-no-data
                    hide-selected
                    item-text="question"
                    item-value="id"
                    label="Multiple Choice Questions"
                    return-object
                    clearable
                  ></v-autocomplete>
                </v-col>
              </v-row>
              <v-row>
                <v-col v-if="selectedMcqs">
                  <template v-for="(item) in selectedMcqs">
                    <v-list-item :key="item.id">
                      <v-list-item-content>
                        <v-list-item-title v-text="item.question"></v-list-item-title>
                      </v-list-item-content>

                      <v-list-item-action>
                        <v-btn icon @click="deleteMcq(item.id)">
                          <v-icon color="red darken-2">mdi-delete</v-icon>
                        </v-btn>
                      </v-list-item-action>
                    </v-list-item>
                  </template>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="red darken-1" text @click="hideDialog">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="saveQuiz">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </span>
</template>

<script>
import { post } from "@/service/service.js";
export default {
  props: {
    sessionId: Number
  },
  data: () => ({
    selectedMcqs: [],
    mcqs: [],
    isLoading: false,
    mcq: null,
    search: null,
    showCreateQuizButton: true,
    showForm: false,
    quiz: {
      name: "",
      contribution: 0
    }
  }),
  created() {
    this.initQuiz();
  },
  watch: {
    mcq(val) {
      if(val){
      this.selectedMcqs.push(val);
      }
    },
    async search(val) {
      if(!val){
        return;
      }
      if (val.length < 3) {
        return;
      }
      let response = await post(`/search_mcq/`, {
        question: val
      });
      if (response.ok) {
        this.mcqs = await response.json();
      }
    }
  },
  methods: {
    deleteMcq(id){
      this.selectedMcqs = this.selectedMcqs.filter(mcq => {return mcq.id!==id});
    },
    saveQuiz() {},
    showCreateQuizDialog() {
      this.showForm = true;
    },
    hideDialog() {
      this.showForm = false;
    },
    async initQuiz() {
      let response = await post(`/admin_get_quiz/`, {
        session_id: this.sessionId
      });
      if (response.ok) {
        let data = await response.json();
        this.showCreateQuizButton = false;
        console.log(data);
      } else {
        this.showCreateQuizButton = true;
      }
    }
  }
};
</script>
