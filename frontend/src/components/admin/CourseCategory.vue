<template>
  <span>
    <v-data-table
      :headers="headers"
      :items="courseCateories"
      :options.sync="options"
      :server-items-length="totalCourseCategories"
      :loading="loading"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
      }"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>কোর্স ক্যাটেগরি</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                নতুন কোর্স ক্যাটেগরি
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
                      <v-text-field
                        v-model="editedItem.name"
                        label="ক্যাটেগরির নাম"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="red darken-1" text @click="close">
                  বাতিল
                </v-btn>
                <v-btn color="blue darken-1" text @click="save">
                  সংরক্ষণ
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="headline"
                >এটি আসলেই মুছে ফেলতে চান?</v-card-title
              >
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="red darken-1" text @click="closeDelete">না</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                  >জী</v-btn
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
import { get, post, del, put } from "@/service/service.js";
export default {
  data: () => ({
    totalCourseCategories: 0,
    loading: true,
    options: {},
    snackbar: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "আইডি",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "ক্যাটেগরি", value: "name" },
      { text: "একশন", value: "actions", sortable: false },
    ],
    courseCateories: [],
    editedIndex: -1,
    editedItem: {
      name: "",
    },
    defaultItem: {
      name: "",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1
        ? "নতুন কোর্স ক্যাটেগরি"
        : "কোর্স ক্যাটেগরি সম্পাদনা";
    },
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
  },

  created() {
    this.initialize();
  },

  methods: {
    async initialize() {
      if (this.options && this.options.page) {
        let response = await get(
          `/course_categories/?page=${this.options.page}`
        );
        if (response.ok) {
          let data = await response.json();
          this.courseCateories = data.results;
          this.totalCourseCategories = data.count;
        } else {
          this.snackbar = true;
        }
        this.loading = false;
      }
    },

    editItem(item) {
      this.editedIndex = this.courseCateories.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.courseCateories.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    async deleteItemConfirm() {
      let response = await del(`/course_categories/${this.editedItem.id}/`);
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
      if (this.editedItem.id) {
        let response = await put(
          `/course_categories/${this.editedItem.id}/`,
          this.editedItem
        );
        if (response.ok) {
          this.initialize();
        } else {
          this.snackbar = true;
        }
      } else {
        let response = await post("/course_categories/", this.editedItem);
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
