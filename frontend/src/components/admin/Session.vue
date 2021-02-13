<template>
  <span>
    <v-row>
      <v-col>
        <v-toolbar dense>
          <v-toolbar-title>Sessions </v-toolbar-title>
          <v-spacer></v-spacer>

          <v-btn icon @click="addSession" :disabled="disableAdd">
            <v-icon color="blue darken-2">mdi-plus</v-icon>
          </v-btn>

          <v-btn icon @click="editSession" :disabled="disableEditDelete">
            <v-icon color="green darken-2">mdi-pencil</v-icon>
          </v-btn>

          <v-btn
            icon
            @click="showSessionDeleteDialog"
            :disabled="disableEditDelete"
          >
            <v-icon color="red darken-2">mdi-delete</v-icon>
          </v-btn>
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
    </v-row>
    <v-row v-if="showForm">
      <v-col>
        <v-text-field v-model="sessionName" label="Session"></v-text-field>
        <v-btn color="primary" @click="persistSession">Save</v-btn>
        <v-btn @click="clearSession">Cancel</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-expansion-panels focusable popout v-model="panel">
          <draggable v-model="sessions" tag="span" style="width:100%">
            <v-expansion-panel v-for="session in sessions" :key="session.id">
              <v-expansion-panel-header>{{
                session.name
              }}</v-expansion-panel-header>
              <v-expansion-panel-content>
                <Lessons v-bind:sessionId="session.id" />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </draggable>
        </v-expansion-panels> </v-col
    ></v-row>
    <v-dialog v-model="dialogDeleteSession" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteSession"
            >Cancel</v-btn
          >
          <v-btn color="blue darken-1" text @click="deleteSessionConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </span>
</template>

<script>
import draggable from "vuedraggable";
import { get, post, put, del, patch } from "@/service/service.js";
import Lessons from "@/components/admin/Lessons.vue";

export default {
  computed: {
    disableAdd() {
      if (this.course) {
        return false;
      } else {
        return true;
      }
    },
    disableEditDelete() {
      if (this.sessionId) {
        return false;
      } else {
        return true;
      }
    },
  },
  methods: {
    async deleteSessionConfirm() {
      let response = await del(`/sessions/${this.sessionId}/`);
      if (response.ok) {
        await this.initSessions();
      }
      this.closeDeleteSession();
    },
    showSessionDeleteDialog() {
      this.dialogDeleteSession = true;
    },
    closeDeleteSession() {
      this.dialogDeleteSession = false;
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
    addSession() {
      this.sessionId = 0;
      this.showForm = true;
    },
    async editSession() {
      let response = await get(`/sessions/${this.sessionId}/`);
      if (response.ok) {
        let data = await response.json();
        this.sessionName = data.name;
        this.serial = data.serial;
        this.showForm = true;
      }
    },
    clearSession() {
      this.showForm = false;
      this.sessionName = null;
      if (this.panel >= 0) {
        this.sessionId = this.sessions[this.panel].id;
      } else {
        this.sessionId = null;
      }
    },
    async persistSession() {
      if (this.sessionName && this.course) {
        if (this.sessionId) {
          let response = await put(`/sessions/${this.sessionId}/`, {
            name: this.sessionName,
            course: this.course,
            serial: this.serial,
          });
          if (response.ok) {
            this.initSessions();
            this.clearSession();
          }
        } else {
          let response = await post("/sessions/", {
            name: this.sessionName,
            course: this.course,
            serial: 9999,
          });
          if (response.ok) {
            this.initSessions();
            this.clearSession();
          }
        }
      }
    },
  },
  components: {
    draggable,
    Lessons,
  },
  data: () => ({
    showForm: false,
    course: null,
    courses: [],
    sessionId: 0,
    sessionName: null,
    sessions: [],
    panel: [],
    dialogDeleteSession: false,
  }),
  created() {
    this.initCourses();
  },
  watch: {
    sessions: function(val) {
      val.forEach(function(item, index) {
        patch(`/sessions/${item.id}/`, {id: item.id, serial: (index+1)})
      });
    },
    panel: function(val) {
      if (val >= 0) {
        this.sessionId = this.sessions[val].id;
      } else {
        this.sessionId = null;
      }
    },
    course: async function(val) {
      if (val) {
        this.initSessions();
      }
    },
  },
};
</script>
