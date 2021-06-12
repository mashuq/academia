<template>
  <span>
    <v-container>
      <v-btn @click="showCreateVideoDialog" color="red" class="ma-2 white--text">
        New Video Lesson
        <v-icon right dark>mdi-youtube</v-icon>
      </v-btn>
      <v-btn @click="showCreateAudioDialog" color="orange" class="ma-2 white--text">
        New Audio Lesson
        <v-icon right dark>mdi-soundcloud</v-icon>
      </v-btn>
      <v-btn @click="showCreateNoteDialog" color="red darken-4" class="ma-2 white--text">
        New Note
        <v-icon right dark>mdi-file-pdf-box</v-icon>
      </v-btn>
      <v-btn @click="showCreateLinkDialog" color="blue darken-4" class="ma-2 white--text">
        New Link
        <v-icon right dark>mdi-link</v-icon>
      </v-btn>
    </v-container>
    <AudioLesson
      @remove="removeLesson"
      @editAudio="editAudio"
      v-for="(item, index) in audioLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></AudioLesson>
    <VideoLesson
      @remove="removeLesson"
      @editVideo="editVideo"
      v-for="(item, index) in videoLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></VideoLesson>
    <NoteLesson
      @remove="removeLesson"
      @editNote="editNote"
      v-for="(item, index) in noteLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></NoteLesson>
    <LinkLesson
      @remove="removeLesson"
      @editLink="editLink"
      v-for="(item, index) in linkLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></LinkLesson>

    <v-dialog v-model="dialogDeleteLesson" max-width="500px">
      <v-card>
        <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteLesson">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteLessonConfirm">OK</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="videoDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Video Lesson</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field v-model="videoLesson.name" label="Lesson Name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="videoLesson.link" label="Link"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <tiptap-vuetify
                  v-model="videoLesson.description"
                  label="Description"
                  :extensions="extensions"
                ></tiptap-vuetify>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select
                  v-model="videoLesson.video_type"
                  :items="videoTypes"
                  label="Video Type"
                  item-text="key"
                  item-value="value"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideVideoDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveVideoLesson">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="audioDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Audio Lesson</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field v-model="audioLesson.name" label="Lesson Name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea v-model="audioLesson.embed" label="Embed Code"></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <tiptap-vuetify
                  v-model="audioLesson.description"
                  label="Description"
                  :extensions="extensions"
                ></tiptap-vuetify>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select
                  v-model="audioLesson.audio_type"
                  :items="audioTypes"
                  label="audio Type"
                  item-text="key"
                  item-value="value"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideAudioDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveAudioLesson">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="noteDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Note</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field v-model="noteLesson.name" label="Lesson Name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-file-input
                  show-size
                  label="Upload Note"
                  v-model="noteLesson.note"
                  accept="application/msword, application/vnd.ms-excel, application/vnd.ms-powerpoint, text/plain, application/pdf"
                ></v-file-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <tiptap-vuetify
                  v-model="noteLesson.description"
                  label="Description"
                  :extensions="extensions"
                ></tiptap-vuetify>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideNoteDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveNoteLesson">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="linkDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">New Link Lesson</span>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field v-model="linkLesson.name" label="Lesson Name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="linkLesson.title" label="Link Title"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field v-model="linkLesson.link" label="Link"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <tiptap-vuetify
                  v-model="linkLesson.description"
                  label="Description"
                  :extensions="extensions"
                ></tiptap-vuetify>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideLinkDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="saveLinkLesson">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </span>
</template>

<script>
import AudioLesson from "@/components/admin/AudioLesson.vue";
import VideoLesson from "@/components/admin/VideoLesson.vue";
import NoteLesson from "@/components/admin/NoteLesson.vue";
import LinkLesson from "@/components/admin/LinkLesson.vue";
import { get, post, del, multipart_post, put, multipart_patch } from "@/service/service.js";
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
  History
} from "tiptap-vuetify";
export default {
  props: {
    sessionId: Number
  },
  components: {
    AudioLesson,
    VideoLesson,
    NoteLesson,
    LinkLesson,
    TiptapVuetify
  },
  data: function() {
    return {
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
              levels: [1, 2, 3]
            }
          }
        ],
        Bold,
        Code,
        HorizontalRule,
        Paragraph,
        HardBreak
      ],
      audioLessons: [],
      videoLessons: [],
      noteLessons: [],
      linkLessons: [],
      videoLesson: {
        id: null,
        name: "",
        link: "",
        description: "",
        video_type: "YOUTUBE",
        session: this.sessionId
      },
      audioLesson: {
        id: null,
        name: "",
        embed: "",
        description: "",
        audio_type: "SOUNDCLOUD",
        session: this.sessionId
      },
      noteLesson: {
        id: null,
        name: "",
        note: "",
        description: "",
        session: this.sessionId
      },
      linkLesson: {
        id: null,
        name: "",
        title: "",
        link: "",
        description: "",
        session: this.sessionId
      },
      videoTypes: [{ key: "Youtube", value: "YOUTUBE" }],
      audioTypes: [{ key: "SoundCloud", value: "SOUNDCLOUD" }],
      removeId: null,
      dialogDeleteLesson: false,
      videoDialog: false,
      audioDialog: false,
      noteDialog: false,
      linkDialog: false
    };
  },
  methods: {
    async deleteLessonConfirm() {
      let response = await del(`/lessons/${this.removeId}/`);
      if (response.ok) {
        await this.init();
      }
      this.closeDeleteLesson();
    },
    showLessonDeleteDialog() {
      this.dialogDeleteLesson = true;
    },
    closeDeleteLesson() {
      this.dialogDeleteLesson = false;
    },
    async init_audio() {
      let response = await post("/audio_lessons_by_session/", {
        session: this.sessionId
      });
      if (response.ok) {
        let data = await response.json();
        this.audioLessons = data;
      }
    },
    async init_video() {
      let response = await post("/video_lessons_by_session/", {
        session: this.sessionId
      });
      if (response.ok) {
        let data = await response.json();
        this.videoLessons = data;
      }
    },
    async init_note() {
      let response = await post("/note_lessons_by_session/", {
        session: this.sessionId
      });
      if (response.ok) {
        let data = await response.json();
        this.noteLessons = data;
      }
    },
    async init_link() {
      let response = await post("/link_lessons_by_session/", {
        session: this.sessionId
      });
      if (response.ok) {
        let data = await response.json();
        this.linkLessons = data;
      }
    },
    async init() {
      this.init_audio();
      this.init_video();
      this.init_note();
      this.init_link();
    },
    async removeLesson(id) {
      this.removeId = id;
      this.showLessonDeleteDialog();
    },
    // Video
    async editVideo(id) {
      let response = await get(`/video_lessons/${id}/`);
      if (response.ok) {
        this.videoLesson = await response.json();
      }
      this.showEditVideoDialog();
    },
    showEditVideoDialog() {
      this.videoDialog = true;
    },
    showCreateVideoDialog() {
      this.clearVideo();
      this.videoDialog = true;
    },
    hideVideoDialog() {
      this.videoDialog = false;
    },
    async saveVideoLesson() {
      let response = null;
      if (null == this.videoLesson.id) {
        response = await post("/video_lessons/", this.videoLesson);
      } else {
        response = await put(`/video_lessons/${this.videoLesson.id}/`, this.videoLesson);
      }
      if (response.ok) {
        this.init_video();
        this.clearVideo();
      }
      this.hideVideoDialog();
    },
    clearVideo() {
      this.videoLesson.id = null;
      this.videoLesson.name = "";
      this.videoLesson.link = "";
      this.videoLesson.description = "";
    },
    // Audio
    async editAudio(id) {
      let response = await get(`/audio_lessons/${id}/`);
      if (response.ok) {
        this.audioLesson = await response.json();
      }
      this.showEditAudioDialog();
    },
    showEditAudioDialog() {
      this.audioDialog = true;
    },
    showCreateAudioDialog() {
      this.clearAudio();
      this.audioDialog = true;
    },
    hideAudioDialog() {
      this.audioDialog = false;
    },
    async saveAudioLesson() {
      let response = null;
      if (null == this.audioLesson.id) {
        response = await post("/audio_lessons/", this.audioLesson);
      } else {
        response = await put(`/audio_lessons/${this.audioLesson.id}/`, this.audioLesson);
      }
      if (response.ok) {
        this.init_audio();
        this.clearAudio();
      }
      this.hideAudioDialog();
    },
    clearAudio() {
      this.audioLesson.id = null;
      this.audioLesson.name = "";
      this.audioLesson.embed = "";
      this.audioLesson.description = "";
    },
    //Note
    async editNote(id) {
      let response = await get(`/note_lessons/${id}/`);
      if (response.ok) {
        this.noteLesson = await response.json();
      }
      this.noteLesson.note = null;
      this.showEditNoteDialog();
    },
    showEditNoteDialog() {
      this.noteDialog = true;
    },
    showCreateNoteDialog() {
      this.clearNote();
      this.noteDialog = true;
    },
    hideNoteDialog() {
      this.noteDialog = false;
    },
    async saveNoteLesson() {
      let response = null;
      if (null == this.noteLesson.id) {
        response = await multipart_post("/note_lessons/", this.noteLesson);
      } else {
        if (!this.noteLesson.note) {
          delete this.noteLesson.note;
        }
        response = await multipart_patch(`/note_lessons/${this.noteLesson.id}/`, this.noteLesson);
      }
      if (response.ok) {
        this.init_note();
        this.clearNote();
      }
      this.hideNoteDialog();
    },
    clearNote() {
      this.noteLesson.id = null;
      this.noteLesson.name = "";
      this.noteLesson.note = "";
      this.noteLesson.description = "";
    },
    //Link
    async editLink(id) {
      let response = await get(`/link_lessons/${id}/`);
      if (response.ok) {
        this.linkLesson = await response.json();
      }
      this.showEditLinkDialog();
    },
    showEditLinkDialog() {
      this.linkDialog = true;
    },
    showCreateLinkDialog() {
      this.clearLink();
      this.linkDialog = true;
    },
    hideLinkDialog() {
      this.linkDialog = false;
    },
    clearLink() {
      this.linkLesson.id = null;
      this.linkLesson.name = "";
      this.linkLesson.link = "";
      this.linkLesson.title = "";
      this.linkLesson.description = "";
    },
    async saveLinkLesson() {
      let response = null;
      if (null == this.linkLesson.id) {
        response = await post("/link_lessons/", this.linkLesson);
      } else {
        response = await put(`/link_lessons/${this.linkLesson.id}/`, this.linkLesson);
      }
      if (response.ok) {
        this.init_link();
        this.clearLink();
      }
      this.hideLinkDialog();
    }
  },
  created() {
    this.init();
  }
};
</script>
