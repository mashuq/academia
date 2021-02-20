<template>
  <span>
    <template v-if="showAddExamQuestions">
      <AddExamQuestions
        @questionAdded="questionAdded"
        :assessment="this.assessmentName"
        :section="this.section"
        @cancel="hideAddExamQuestionsDialog"
      />
    </template>
    <template v-else>
      <v-row
        ><v-col>
          <v-toolbar dense>
            <v-toolbar-title>পরীক্ষা</v-toolbar-title>
            <v-spacer></v-spacer> </v-toolbar></v-col
      ></v-row>
      <v-row>
        <v-col>
          <template>
            <v-data-table
              v-model="selectedSection"
              :headers="headersSection"
              :items="sections"
              :options.sync="optionsSection"
              :server-items-length="totalSections"
              :loadingSection="loadingSection"
              class="elevation-1"
              :footer-props="{
                disableItemsPerPage: true,
              }"
              show-select
              item-key="id"
              :single-select="singleSelectSection"
            >
              <template v-slot:top>
                <v-toolbar flat>
                  <v-toolbar-title>আপনার সেকশন</v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>
                  <v-spacer></v-spacer>
                </v-toolbar>
              </template>
            </v-data-table>
          </template>
        </v-col>
        <v-col>
          <template>
            <v-data-table
              v-model="selectedAssessment"
              :headers="headersAssessments"
              :items="assessments"
              hide-default-footer
              class="elevation-1"
              show-select
              item-key="id"
              :single-select="singleSelectAssessment"
            >
              <template v-slot:top>
                <v-toolbar flat>
                  <v-toolbar-title>সেকশনের পরীক্ষা সমূহ</v-toolbar-title>
                  <v-divider class="mx-4" inset vertical></v-divider>
                  <v-spacer></v-spacer>
                  <v-btn
                    :disabled="disableAddAssessment"
                    @click="showAssessmentDialog"
                    text
                    color="primary"
                    ><v-icon dark> mdi-plus </v-icon>সেকশনের পরীক্ষা</v-btn
                  >
                  <v-dialog v-model="assessmentDialog" max-width="800px">
                    <v-card>
                      <v-card-title>
                        <span class="headline">নতুন পরীক্ষা</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col>
                              <v-text-field
                                v-model="assessmentItem.name"
                                label="পরীক্ষার নাম"
                              ></v-text-field>
                            </v-col>
                            <v-col>
                              <v-text-field
                                v-model="assessmentItem.contribution"
                                label="সম্পূর্ণ কোর্সের শতকরা হার"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                          <v-row>
                            <v-col>
                              <v-dialog
                                ref="dialogStartDate"
                                v-model="startDateModal"
                                :return-value.sync="assessmentItem.startDate"
                                persistent
                                width="290px"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="assessmentItem.startDate"
                                    label="শুরুর দিন"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-date-picker
                                  v-model="assessmentItem.startDate"
                                  scrollable
                                >
                                  <v-spacer></v-spacer>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="startDateModal = false"
                                  >
                                    Cancel
                                  </v-btn>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="
                                      $refs.dialogStartDate.save(
                                        assessmentItem.startDate
                                      )
                                    "
                                  >
                                    OK
                                  </v-btn>
                                </v-date-picker>
                              </v-dialog>
                            </v-col>
                            <v-col>
                              <v-dialog
                                ref="dialogStartTime"
                                v-model="startTimeModal"
                                :return-value.sync="assessmentItem.startTime"
                                persistent
                                width="290px"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="assessmentItem.startTime"
                                    label="শুরুর সময়"
                                    prepend-icon="mdi-clock-time-four-outline"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-time-picker
                                  v-if="startTimeModal"
                                  v-model="assessmentItem.startTime"
                                  full-width
                                >
                                  <v-spacer></v-spacer>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="startTimeModal = false"
                                  >
                                    Cancel
                                  </v-btn>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="
                                      $refs.dialogStartTime.save(
                                        assessmentItem.startTime
                                      )
                                    "
                                  >
                                    OK
                                  </v-btn>
                                </v-time-picker>
                              </v-dialog>
                            </v-col>
                            <v-col>
                              <v-dialog
                                ref="dialogEndDate"
                                v-model="endDateModal"
                                :return-value.sync="assessmentItem.endDate"
                                persistent
                                width="290px"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="assessmentItem.endDate"
                                    label="শেষ দিন"
                                    prepend-icon="mdi-calendar"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-date-picker
                                  v-model="assessmentItem.endDate"
                                  scrollable
                                >
                                  <v-spacer></v-spacer>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="endDateModal = false"
                                  >
                                    Cancel
                                  </v-btn>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="
                                      $refs.dialogEndDate.save(
                                        assessmentItem.endDate
                                      )
                                    "
                                  >
                                    OK
                                  </v-btn>
                                </v-date-picker>
                              </v-dialog>
                            </v-col>
                            <v-col>
                              <v-dialog
                                ref="dialogEndTime"
                                v-model="endTimeModal"
                                :return-value.sync="assessmentItem.endTime"
                                persistent
                                width="290px"
                              >
                                <template v-slot:activator="{ on, attrs }">
                                  <v-text-field
                                    v-model="assessmentItem.endTime"
                                    label="শেষ সময় "
                                    prepend-icon="mdi-clock-time-four-outline"
                                    readonly
                                    v-bind="attrs"
                                    v-on="on"
                                  ></v-text-field>
                                </template>
                                <v-time-picker
                                  v-if="endTimeModal"
                                  v-model="assessmentItem.endTime"
                                  full-width
                                >
                                  <v-spacer></v-spacer>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="endTimeModal = false"
                                  >
                                    Cancel
                                  </v-btn>
                                  <v-btn
                                    text
                                    color="primary"
                                    @click="
                                      $refs.dialogEndTime.save(
                                        assessmentItem.endTime
                                      )
                                    "
                                  >
                                    OK
                                  </v-btn>
                                </v-time-picker>
                              </v-dialog>
                            </v-col>
                          </v-row>
                        </v-container>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="red darken-1"
                          @click="hideAssessmentDialog"
                          text
                        >
                          বাতিল
                        </v-btn>
                        <v-btn
                          color="blue darken-1"
                          @click="saveAsessment"
                          text
                        >
                          সংরক্ষণ
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>
            </v-data-table>
          </template>
        </v-col>
        <v-col>
          <v-data-table
            :headers="headersQueestions"
            :items="questions"
            hide-default-footer
            class="elevation-1"
            :items-per-page="-1"
          >
            <template v-slot:top>
              <v-toolbar flat>
                <v-toolbar-title>পরীক্ষার প্রশ্ন সমূহ</v-toolbar-title>
                <v-divider class="mx-4" inset vertical></v-divider>
                <v-spacer></v-spacer>
                <h4>সর্বমোট নম্বর</h4>
                <v-spacer></v-spacer>
                <v-avatar color="teal" size="48">
                  <span class="white--text headline">{{ totalNumber }}</span>
                </v-avatar>
                <v-spacer></v-spacer>
                <v-btn
                  :disabled="disableAddQuestion"
                  @click="showAddExamQuestionsDialog"
                  text
                  color="primary"
                  ><v-icon dark> mdi-plus </v-icon>পরীক্ষার প্রশ্ন</v-btn
                >
              </v-toolbar>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon small @click="deleteQuestion(item.id)"> mdi-delete </v-icon>
            </template>
          </v-data-table>
        </v-col>
      </v-row>
    </template>
  </span>
</template>

<script>
import { get, post } from "@/service/service.js";
import moment from "moment";
import AddExamQuestions from "@/components/teacher/AddExamQuestions.vue";

export default {
  components: {
    AddExamQuestions,
  },
  data: () => ({
    selectedSection: [],
    totalSections: 0,
    loadingSection: true,
    optionsSection: {},

    headersSection: [
      { text: "সেকশন", value: "section.name" },
      { text: "কোর্স", value: "section.course" },
    ],
    sections: [],
    singleSelectSection: true,
    section: null,

    selectedAssessment: [],
    loadingAssessments: true,

    headersAssessments: [
      { text: "পরীক্ষা", value: "name" },
      { text: "%", value: "contribution" },
      { text: "শুরুর দিন ও সময়", value: "start_date" },
      { text: "শেষ দিন ও সময়", value: "end_date" },
    ],
    assessments: [],
    singleSelectAssessment: true,
    assessment: null,
    assessmentName: null,

    snackbar: false,
    assessmentDialog: false,

    assessmentItem: {
      name: null,
      contribution: null,
      assessmentType: "QUIZ",
      startDate: null,
      endDate: null,
      startTime: null,
      endTime: null,
    },
    startDateModal: false,
    startTimeModal: false,
    endDateModal: false,
    endTimeModal: false,

    showAddExamQuestions: false,
    questions: [],
    headersQueestions: [
      { text: "প্রশ্ন", value: "question" },
      { text: "নম্বর", value: "mark" },
      { text: "সম্পাদনা", value: "actions", sortable: false },
    ],
  }),

  computed: {
    disableAddAssessment: function() {
      if (this.section) {
        return false;
      }
      return true;
    },
    disableAddQuestion: function() {
      if (this.assessment) {
        return false;
      }
      return true;
    },
    totalNumber: function() {
      if (this.questions) {
        let total = 0;
        this.questions.forEach((element) => {
          total += element.mark;
          console.log(total + " " + element.mark);
        });
        console.log(total);
        return total;
      }
      return 0;
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
    optionsSection: {
      handler() {
        this.initialize();
      },
      deep: true,
    },
    selectedSection: function(val) {
      if (val && val.length > 0) {
        this.section = val[0].section.id;
        this.questions = [];
        this.initAssessments();
      }
    },
    selectedAssessment: function(val) {
      if (val && val.length > 0) {
        this.assessment = val[0].id;
        this.assessmentName = val[0].name;
        this.initAssessmentQuestions();
      }
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    async deleteQuestion(val){
      let response = await post(`/delete_assessment_question_for_teacher/`, {
        assessment: this.assessment,
        question: val,
      });
      if(response.ok){
        this.initAssessmentQuestions();
      }
    },
    async questionAdded(val) {
      await post(`/save_assessment_question_for_teacher/`, {
        assessment: this.assessment,
        question: val,
      });
    },
    async saveAsessment() {
      this.assessmentDialog = false;
      let startHours = this.assessmentItem.startTime.match(/^(\d+)/)[1];
      let startMinutes = this.assessmentItem.startTime.match(/:(\d+)/)[1];
      let endHours = this.assessmentItem.endTime.match(/^(\d+)/)[1];
      let endMinutes = this.assessmentItem.endTime.match(/:(\d+)/)[1];

      let startDate = moment(this.assessmentItem.startDate).toDate();
      let endDate = moment(this.assessmentItem.endDate).toDate();

      startDate.setHours(startHours);
      startDate.setMinutes(startMinutes);
      endDate.setHours(endHours);
      endDate.setMinutes(endMinutes);

      let response = await post(`/save_assessment_for_teacher/`, {
        name: this.assessmentItem.name,
        contribution: this.assessmentItem.contribution,
        start_date: startDate.toJSON(),
        end_date: endDate.toJSON(),
        section: this.section,
      });
      if (response.ok) {
        this.initAssessments();
      }
    },
    showAddExamQuestionsDialog() {
      console.log(this.assessment);
      this.showAddExamQuestions = true;
    },
    hideAddExamQuestionsDialog() {
      this.initAssessmentQuestions();
      this.showAddExamQuestions = false;
    },
    hideAssessmentDialog() {
      this.assessmentDialog = false;
    },
    showAssessmentDialog() {
      this.assessmentDialog = true;
    },
    async initAssessments() {
      if (this.section) {
        let response = await post(`/list_assessment_for_teacher/`, {
          section: this.section,
        });
        if (response.ok) {
          let data = await response.json();
          this.assessments = data;
          this.assessments.forEach((element, index) => {
            this.assessments[index].start_date = moment(
              element.start_date
            ).format("MMMM Do YYYY, h:mm:ss a");
            this.assessments[index].end_date = moment(element.end_date).format(
              "MMMM Do YYYY, h:mm:ss a"
            );
          });
        } else {
          this.snackbar = true;
        }
        this.loadingSection = false;
      }
    },

    async initAssessmentQuestions() {
      if (this.assessment) {
        let response = await post(`/list_assessment_question_for_teacher/`, {
          assessment: this.assessment,
        });
        if (response.ok) {
          let data = await response.json();
          this.questions = data;
        } else {
          this.snackbar = true;
        }
        this.loadingSection = false;
      }
    },

    async initialize() {
      if (this.optionsSection && this.optionsSection.page) {
        let response = await get(
          `/list_sections_for_teacher/?page=${this.optionsSection.page}`
        );
        if (response.ok) {
          let data = await response.json();
          this.sections = data.results;
          this.totalSections = data.count;
        } else {
          this.snackbar = true;
        }
        this.loadingSection = false;
      }
    },
  },
};
</script>
