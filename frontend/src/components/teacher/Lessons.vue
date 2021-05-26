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
    <LinkLesson
      v-for="(item, index) in linkLessons"
      v-bind:lesson="item"
      v-bind:index="index"
      v-bind:key="item.id"
    ></LinkLesson>
  </span>
</template>

<script>
import AudioLesson from "@/components/teacher/AudioLesson.vue";
import VideoLesson from "@/components/teacher/VideoLesson.vue";
import NoteLesson from "@/components/teacher/NoteLesson.vue";
import LinkLesson from "@/components/teacher/LinkLesson.vue";
import { post} from "@/service/service.js";
export default {
  props: {
    sessionId: Number,
  },
  components: {
    AudioLesson,
    VideoLesson,
    NoteLesson,
    LinkLesson,
  },
  data: function() {
    return {
      audioLessons: [],
      videoLessons: [],
      noteLessons: [],
      linkLessons: [],
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
      linkLesson: {
        name: "",
        title: "",
        link: "",
        session: this.sessionId,
      },
      videoTypes: [{ key: "Youtube", value: "YOUTUBE" }],
      audioTypes: [{ key: "SoundCloud", value: "SOUNDCLOUD" }],
    };
  },
  methods: {
    async init_audio() {
      let response = await post("/audio_lessons_by_session_teacher/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.audioLessons = data;
      }
    },
    async init_video() {
      let response = await post("/video_lessons_by_session_teacher/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.videoLessons = data;
      }
    },
    async init_note() {
      let response = await post("/note_lessons_by_session_teacher/", {
        session: this.sessionId,
      });
      if (response.ok) {
        let data = await response.json();
        this.noteLessons = data;
      }
    },
    async init_link() {
      let response = await post("/link_lessons_by_session_teacher/", {
        session: this.sessionId,
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
  },
  created() {
    this.init();
  },
};
</script>
