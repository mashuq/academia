<template>
  <span>
    <v-data-table
      :headers="headers"
      :items="teachers"
      :options.sync="options"
      :server-items-length="totalTeachers"
      :loading="loading"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
      }"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Teachers</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Teacher
              </v-btn>
            </template>
            <Appointment @appointmentComplete="appointmentComplete"/>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="headline"
                >Are you sure you want to delete this item?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete"
                  >Cancel</v-btn
                >
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >OK</v-btn
                >
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
    </v-data-table>
    <v-snackbar v-model="snackbar">
      একটি সমস্যা হয়েছে, পুনরায় চেষ্টা করুন 

      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<script>
import { get, del } from "@/service/service.js";
import Appointment from "@/components/Appointment.vue";
import moment from "moment";
export default {
  components: {
    Appointment
  },
  data: () => ({
    totalTeachers: 0,
    loading: true,
    options: {},
    snackbar: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "Name", value: "name" },
      { text: "ইউজারনেম", value: "user.username" },
      { text: "Email", value: "user.email" },
      { text: "Gender", value: "gender" },
      { text: "Date of Birth", value: "date_of_birth" },
      { text: "Date Joined", value: "user.date_joined" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    teachers: [],
    editedIndex: -1,
    editedItem: {
      name: "",
    },
    defaultItem: {
      name: "",
    },
  }),

  computed: {
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
    options: {
      handler() {
        this.initialize();
      },
      deep: true,
    },
    teachers(){
      if(this.teachers){
        this.teachers.forEach(element => {
          element.date_of_birth = moment(element.date_of_birth).format("DD MMM YYYY")
          element.user.date_joined = moment(element.user.date_joined).format("DD MMM YYYY")
        });
      }
    }
  },

  created() {
    this.initialize();
  },

  methods: {
    appointmentComplete(){
      this.dialog = false;
      this.initialize();
    },
    async initialize() {
      let response = await get(`/teachers/?page=${this.options.page}`);
      if (response.ok) {
        let data = await response.json();
        this.teachers = data.results;
        this.totalTeachers = data.count;
      } else {
        this.snackbar = true;
      }
      this.loading = false;
    },

    editItem(item) {
      this.editedIndex = this.teachers.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.teachers.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    async deleteItemConfirm() {
      let response = await del(`/teachers/${this.editedItem.id}/`);
      if (!response.ok) {
        this.snackbar = true;
      }
      this.closeDelete();
      await this.initialize();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },
  },
};
</script>
