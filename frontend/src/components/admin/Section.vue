<template>
  <span>
    <v-data-table
      :headers="headers"
      :items="sections"
      sort-by="calories"
      class="elevation-1"
      hide-default-footer
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Sections</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="800px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                New Section
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>

              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col>
                      <v-autocomplete
                        v-model="editedItem.course"
                        :items="courses"
                        label="Course"
                        item-text="name"
                        item-value="id"
                      ></v-autocomplete>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-text-field
                        v-model="editedItem.name"
                        label="Section name"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-checkbox
                        v-model="editedItem.visible"
                        label="Visible"
                      ></v-checkbox>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-menu
                        v-model="fromMenu"
                        :close-on-content-click="false"
                        max-width="290"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            :value="computedFromDate"
                            clearable
                            label="Start Date"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                            @click:clear="editedItem.start_date = null"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="editedItem.start_date"
                          @change="fromMenu = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-col>
                    <v-col>
                      <v-menu
                        v-model="toMenu"
                        :close-on-content-click="false"
                        max-width="290"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            :value="computedToDate"
                            clearable
                            label="End Date"
                            readonly
                            v-bind="attrs"
                            v-on="on"
                            @click:clear="editedItem.end_date = null"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="editedItem.end_date"
                          @change="toMenu = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">
                  Cancel
                </v-btn>
                <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
              </v-card-actions>
            </v-card>
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
        <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
        <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
      </template>
    </v-data-table>
    <v-snackbar v-model="snackbar">
      An error occurred. Please try again.

      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </span>
</template>

<script>
import { get, post, del, put } from "@/service/service.js";
import moment from "moment";
import { format, parseISO } from 'date-fns'

export default {
  data: () => ({
    fromMenu: false,
    toMenu: false,
    courses: [],
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
      { text: "Course", value: "course" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    sections: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      start_date: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
      end_date: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
      visible: true,
      course: 0,
    },
    defaultItem: {
      name: "",
      start_date: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
      end_date: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
      visible: true,
      course: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Section" : "Edit Section";
    },
    computedFromDate() {
      console.log(this.editedItem.start_date);
      return this.editedItem.start_date
        ? moment(this.editedItem.start_date).format("dddd, MMMM Do YYYY")
        : "";
    },
    computedToDate() {
      return this.editedItem.end_date
        ? moment(this.editedItem.end_date).format("dddd, MMMM Do YYYY")
        : "";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    async initialize() {
      let response = await get("/sections/");
      if (response.ok) {
        let data = await response.json();
        this.sections = data.results;
      } else {
        this.snackbar = true;
      }

      response = await get("/courses/");
      if (response.ok) {
        let data = await response.json();
        this.courses = data;
      }
    },

    async editItem(item) {
      this.editedIndex = this.sections.indexOf(item);
      let response = await get(`/sections/${item.id}/`);
      if (!response.ok) {
        this.snackbar = true;
        return;
      }
      let data = await response.json();
      this.editedItem = data;
      console.log(data);
      this.editedItem.start_date = format(parseISO(data.start_date), 'yyyy-MM-dd');
      this.editedItem.end_date = format(parseISO(data.end_date), 'yyyy-MM-dd');
      console.log(2);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.sections.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    async deleteItemConfirm() {
      let response = await del(`/sections/${this.editedItem.id}/`);
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

    async save() {
      this.editedItem.start_date = moment(this.editedItem.start_date).toISOString();
      this.editedItem.end_date = moment(this.editedItem.end_date).toISOString();

      if (this.editedItem.id) {
        if (!this.editedItem.image) {
          delete this.editedItem.image;
        }
        let response = await put(
          `/sections/${this.editedItem.id}/`,
          this.editedItem
        );
        if (response.ok) {
          this.initialize();
        } else {
          this.snackbar = true;
        }
      } else {
        let response = await post("/sections/", this.editedItem);
        if (response.ok) {
          this.initialize();
        } else {
          this.snackbar = true;
        }
      }
      this.close();
    },
  },
};
</script>
