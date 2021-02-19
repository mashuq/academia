<template>
  <span>
    <v-data-table
      :headers="headers"
      :items="courses"
      :options.sync="options"
      :server-items-length="totalCourses"
      :loading="loading"
      class="elevation-1"
      :footer-props="{
        disableItemsPerPage: true,
      }"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>কোর্স</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="800px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
                নতুন কোর্স
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
                        label="কোর্সের নাম"
                      ></v-text-field>
                    </v-col>
                    <v-col>
                      <v-text-field
                        v-model="editedItem.code"
                        label="কোড"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <label class="v-label">পরিচিতি</label>
                      <tiptap-vuetify
                        v-model="editedItem.description"
                        label="পরিচিতি"
                        :extensions="extensions"
                      ></tiptap-vuetify>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <label class="v-label">পাঠ্যসুচি</label>
                      <tiptap-vuetify
                        v-model="editedItem.curriculum"
                        label="পাঠ্যসুচি"
                        :extensions="extensions"
                      ></tiptap-vuetify>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-file-input
                        show-size
                        label="ছবি"
                        v-model="editedItem.image"
                        accept="image/*"
                      ></v-file-input>
                    </v-col>
                    <v-col>
                      <v-img
                        :src="editedItem.image_url"
                        max-width="250"
                      ></v-img>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-checkbox
                        v-model="editedItem.visible"
                        label="দৃশ্যমান"
                      ></v-checkbox>
                    </v-col>
                    <v-col>
                      <v-select
                        v-model="editedItem.course_category"
                        :items="courseCategories"
                        label="ক্যাটেগরি"
                        item-text="name"
                        item-value="id"
                      ></v-select>
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
import {
  get,
  multipart_post,
  del,
  multipart_patch,
} from "@/service/service.js";
import {
  TiptapVuetify,
  Heading,
  Bold,
  Italic,
  Strike,
  Underline,
  Code,
  Paragraph,
  BulletList,
  OrderedList,
  ListItem,
  Link,
  Blockquote,
  HardBreak,
  HorizontalRule,
  History,
} from "tiptap-vuetify";
export default {
  components: {
    TiptapVuetify,
  },
  data: () => ({
    extensions: [
      History,
      Blockquote,
      Link,
      Underline,
      Strike,
      Italic,
      ListItem,
      BulletList,
      OrderedList,
      [
        Heading,
        {
          options: {
            levels: [1, 2, 3],
          },
        },
      ],
      Bold,
      Code,
      HorizontalRule,
      Paragraph,
      HardBreak,
    ],
    totalCourses: 0,
    loading: true,
    options: {},
    courseCategories: [],
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
      { text: "কোড", value: "code" },
      { text: "নাম", value: "name" },
      { text: "ক্যাটেগরি", value: "course_category" },
      { text: "সম্পাদনা", value: "actions", sortable: false },
    ],
    courses: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      code: "",
      description: "",
      curriculum: "",
      image: "",
      image_url: "",
      visible: true,
      course_category: 0,
    },
    defaultItem: {
      name: "",
      code: "",
      description: "",
      curriculum: "",
      image: "",
      visible: true,
      image_url: "",
      course_category: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "নতুন কোর্স" : "কোর্স সম্পাদনা";
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
    this.initCourseCategory();
    this.initialize();
  },

  methods: {
    async initialize() {
      if (this.options && this.options.page) {
        let response = await get(`/courses/?page=${this.options.page}`);
        if (response.ok) {
          let data = await response.json();
          this.courses = data.results;
          this.totalCourses = data.count;
        } else {
          this.snackbar = true;
        }
        this.loading = false;
      }
    },

    async initCourseCategory() {
      let response = await get("/course_categories/");
      if (response.ok) {
        let data = await response.json();
        this.courseCategories = data;
      }
    },

    async editItem(item) {
      this.editedIndex = this.courses.indexOf(item);
      let response = await get(`/courses/${item.id}/`);
      if (!response.ok) {
        this.snackbar = true;
        return;
      }
      let data = await response.json();
      this.editedItem = data;
      this.editedItem.image_url = data.image;
      this.editedItem.image = "";
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.courses.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    async deleteItemConfirm() {
      let response = await del(`/courses/${this.editedItem.id}/`);
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
        if (!this.editedItem.image) {
          delete this.editedItem.image;
        }
        let response = await multipart_patch(
          `/courses/${this.editedItem.id}/`,
          this.editedItem
        );
        if (response.ok) {
          this.initialize();
        } else {
          this.snackbar = true;
        }
      } else {
        let response = await multipart_post("/courses/", this.editedItem);
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
