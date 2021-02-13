<template>
  <span>
    <v-container>
      <v-btn @click="showVideoDialog" color="red" class="ma-2 white--text">
        New Video Lesson
        <v-icon right dark>
          mdi-youtube
        </v-icon>
      </v-btn>
      <v-btn @click="showAudioDialog" color="orange" class="ma-2 white--text">
        New Audio Lesson
        <v-icon right dark>
          mdi-soundcloud
        </v-icon>
      </v-btn>
      <v-btn
        @click="showNoteDialog"
        color="red darken-4"
        class="ma-2 white--text"
      >
        New Note
        <v-icon right dark>
          mdi-file-pdf-box
        </v-icon>
      </v-btn>
    </v-container>
    <AudioLesson
      @remove="removeLesson"
      v-for="(item, index) in audioLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></AudioLesson>
    <VideoLesson
      @remove="removeLesson"
      v-for="(item, index) in videoLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></VideoLesson>
    <NoteLesson
      @remove="removeLesson"
      v-for="(item, index) in noteLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></NoteLesson>

    <v-dialog v-model="dialogDeleteLesson" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDeleteLesson"
            >Cancel</v-btn
          >
          <v-btn color="blue darken-1" text @click="deleteLessonConfirm"
            >OK</v-btn
          >
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
                <v-text-field
                  v-model="videoLesson.name"
                  label="Lesson Name"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="videoLesson.link"
                  label="Link"
                ></v-text-field>
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
          <v-btn color="red darken-1" text @click="hideVideoDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveVideoLesson">
            Save
          </v-btn>
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
                <v-text-field
                  v-model="audioLesson.name"
                  label="Lesson Name"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea
                  v-model="audioLesson.embed"
                  label="Embed Code"
                ></v-textarea>
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
          <v-btn color="red darken-1" text @click="hideAudioDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveAudioLesson">
            Save
          </v-btn>
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
                <v-text-field
                  v-model="noteLesson.name"
                  label="Lesson Name"
                ></v-text-field>
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
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="hideNoteDialog">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="saveNoteLesson">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </span>
</template>

<script>
import AudioLesson from "@/components/admin/AudioLesson.vue";
import VideoLesson from "@/components/admin/VideoLesson.vue";
import NoteLesson from "@/components/admin/NoteLesson.vue";
import { post, del, multipart_post } from "@/service/service.js";
export default {
  props: {
    sessionId: Number,
  },
  components: {
    AudioLesson,
    VideoLesson,
    NoteLesson,
  },
  data: function() {
    return {
      audioLessons: [],
      videoLessons: [],
      noteLessons: [],
      videoLesson: {
        name: "",
        link: "",
        video_type: "YOUTUBE",
        session: this.sessionId,
      },
      audioLesson: {
        name: "",
        embed: "",
        audio_type: "SOUNDCLOUD",
        session: this.sessionId,
      },
      noteLesson: {
        name: "",
        note: "",
        session: this.sessionId,
      },
      videoTypes: [{ key: "Youtube", value: "YOUTUBE" }],
      audioTypes: [{ key: "SoundCloud", value: "SOUNDCLOUD" }],
      removeId: null,
      dialogDeleteLesson: false,
      videoDialog: false,
      audioDialog: false,
      noteDialog: false,
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
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.audioLessons = data;
      }
    },
    async init_video() {
      let response = await post("/video_lessons_by_session/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.videoLessons = data;
      }
    },
    async init_note() {
      let response = await post("/note_lessons_by_session/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.noteLessons = data;
      }
    },
    async init() {
      this.init_audio();
      this.init_video();
      this.init_note();
    },
    async removeLesson(id) {
      this.removeId = id;
      this.showLessonDeleteDialog();
    },
    showVideoDialog() {
      this.videoDialog = true;
    },
    hideVideoDialog() {
      this.videoDialog = false;
    },
    async saveVideoLesson() {
      let response = await post("/video_lessons/", this.videoLesson);
      if (response.ok) {
        this.init();
        this.videoLesson.name = "";
        this.videoLesson.link = "";
      }
      this.hideVideoDialog();
    },
    showAudioDialog() {
      this.audioDialog = true;
    },
    hideAudioDialog() {
      this.audioDialog = false;
    },
    async saveAudioLesson() {
      let response = await post("/audio_lessons/", this.audioLesson);
      if (response.ok) {
        this.init();
        this.audioLesson.name = "";
        this.audioLesson.embed = "";
      }
      this.hideAudioDialog();
    },
    showNoteDialog() {
      this.noteDialog = true;
    },
    hideNoteDialog() {
      this.noteDialog = false;
    },
    async saveNoteLesson() {
      let response = await multipart_post("/note_lessons/", this.noteLesson);
      if (response.ok) {
        this.init();
        this.noteLesson.name = "";
        this.noteLesson.note = "";
      }
      this.hideNoteDialog();
    },
  },
  created() {
    this.init();
  },
};
</script>
