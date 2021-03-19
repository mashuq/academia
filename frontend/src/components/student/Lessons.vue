<template>
  <span>
    <AudioLesson
      v-for="(item, index) in audioLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></AudioLesson>
    <VideoLesson
      v-for="(item, index) in videoLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></VideoLesson>
    <NoteLesson
      v-for="(item, index) in noteLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></NoteLesson>
  </span>
</template>

<script>
import AudioLesson from "@/components/student/AudioLesson.vue";
import VideoLesson from "@/components/student/VideoLesson.vue";
import NoteLesson from "@/components/student/NoteLesson.vue";
import { post} from "@/service/service.js";
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
    async init_audio() {
      let response = await post("/audio_lessons_by_session_student/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.audioLessons = data;
      }
    },
    async init_video() {
      let response = await post("/video_lessons_by_session_student/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.videoLessons = data;
      }
    },
    async init_note() {
      let response = await post("/note_lessons_by_session_student/", {
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
  },
  created() {
    this.init();
  },
};
</script>
