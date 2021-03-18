<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-parallax src="https://nlquran.b-cdn.net/hero2.jpg">
            <v-container fill-height fluid>
              <v-row align="center" justify="center">
                <h2 class="quote">
                  কুরআন বোঝার প্রতি মানুষকে উদ্বুদ্ধ করা ও কুরআন কেন্দ্রিক বিভিন্ন ধরনের জ্ঞান সমাজের বুকে ও ভার্চুয়াল জগতে ছড়িয়ে দেওয়ার মানসে প্রতিষ্ঠিত হয়েছে
                  <b>‘নূরুল কুরআন’</b>। নানাবিধ কর্মসূচির পাশাপাশি এর রয়েছে একাডেমিক কার্যক্রম। যেখানে আরবীভাষা ও সাহিত্যসহ কুরআন-হাদীস-ফিকহ-আকীদা ইত্যাদী শরীয়তের বিভিন্ন বিষয়ে রয়েছে পেইড ও ফ্রি কোর্সসমূহ।
                </h2>
              </v-row>
            </v-container>
          </v-parallax>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <h2 class="text-center">একাডেমির বৈশিষ্ট্য</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-list>
          <v-list-item v-for="(characteristics, i) in characteristics1" :key="i" class="dark">
            <v-list-item-avatar>
              <v-icon>mdi-star</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>{{characteristics}}</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col>
        <v-list>
          <v-list-item v-for="(characteristics, i) in characteristics2" :key="i" class="dark">
            <v-list-item-avatar>
              <v-icon>mdi-star</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>{{characteristics}}</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col>
        <v-list>
          <v-list-item v-for="(characteristics, i) in characteristics3" :key="i" class="dark">
            <v-list-item-avatar>
              <v-icon>mdi-star</v-icon>
            </v-list-item-avatar>
            <v-list-item-content>{{characteristics}}</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="16" sm="6">
        <h2>একাডেমির উদ্দেশ্য</h2>

        <v-list>
          <v-list-item>
            <v-list-item-action>
              <v-icon>mdi-book-open-variant</v-icon>
            </v-list-item-action>

            <v-list-item-content>কুরআনের প্রতি মানুষদের আগ্রহী করে তোলা।</v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-action>
              <v-icon>mdi-abjad-arabic</v-icon>
            </v-list-item-action>

            <v-list-item-content>আরবীভাষার চর্চাকে ব্যাপক ও সহজতর করা।</v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-action>
              <v-icon>mdi-school</v-icon>
            </v-list-item-action>

            <v-list-item-content>জেনারেল শিক্ষিত ভাই-বোনদের কাছে দ্বীনের প্রয়োজনীয় ইলম পৌঁছে দেওয়া।</v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col cols="16" sm="6">
        <h2 class="text-right">যোগাযোগ</h2>
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-right">
                <a
                  target="_blank"
                  href="https://www.facebook.com/NLQURAN"
                >https://www.facebook.com/NLQURAN</a>
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-facebook</v-icon>
            </v-list-item-action>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-right">
                <a
                  target="_blank"
                  href="https://www.youtube.com/c/NurulQuran887"
                >https://www.youtube.com/c/NurulQuran887</a>
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-youtube</v-icon>
            </v-list-item-action>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-right">
                <a href="mailto:nurulquran887@gmail.com">nurulquran887@gmail.com</a>
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-email</v-icon>
            </v-list-item-action>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-right">
                <a href="tel:+8801700946569">+8801700946569</a>
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-phone</v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>

    <v-row class="dark">
      <v-col cols="12" sm="4" fill-height fluid>
        <v-img align="center" justify="center" src="https://nlquran.b-cdn.net/main_ustadh.jpg"></v-img>
      </v-col>
      <v-col cols="20" sm="8">
        <v-text>
          <h2>একাডেমির পরিচালক ও প্রতিষ্ঠাতার পরিচিতি</h2>
          <p></p>
          <h3>আবদুল্লাহ আল মাসউদ</h3>
          <p></p>
          <p>জন্ম ১৯৯২ সাল ১৬ জানুয়ারিতে। জন্মস্থান নোয়াখালি জেলার সোনাইমুড়ি উপজেলার আমিশাপাড়া ইউনিয়নের কেশারখিল গ্রামে।</p>
          <p>মক্তব গমনের মধ্য দিয়ে তার পড়ালেখার হাতেখড়ি। এরপর ক'বছর নিজ গ্রামের প্রাথমিক বিদ্যালয়ে পড়াশোনা। তারপর ঢাকার টিকাটুলি জামে মসজিদে অবস্থিত 'তাহফীজুল কুরআন মাদরাসায়' ভর্তি হন এবং সেখান থেকেই হিফজ সমাপন করেন। এরপর ভর্তি হন ঢাকার বিখ্যাত ধর্মীয় বিদ্যাপীঠ যাত্রাবাড়ি বড় মাদরাসায়। সেখান থেকেই অত্যন্ত কৃতিত্বের সঙ্গে তাকমীলে হাদীস সমাপন করেন এবং মাদরাসাসমূহের সম্মিলিত শিক্ষাবোর্ড 'আলহাইআতুল উলইয়া' এর কেন্দ্রিয় পরীক্ষায় মেধাতালিকায় ১২তম স্থান অর্জন করেন এবং উক্ত প্রতিষ্ঠান থেকেই উলুমুল হাদীস ও ইসলামী আইন বিষয়ে উচ্চতর ডিগ্রি নেন।</p>
          <p>লেখালেখির সাথে যুক্ত আছেন অনেকদিন ধরে। অনুবাদের পাশাপাশি প্রবন্ধ ও গবেষণাধর্মী মৌলিক রচনাতেও তিনি মনোযোগী। মৌলিক, অনূদিত ও সম্পাদিত─ সব মিলিয়ে তাঁর প্রকাশিত বইয়ের সংখ্যা চল্লিশেরও অধিক। বইগুলোর তালিকা দেখতে ক্লিক করুন এখানে</p>
          <p>নূরুল কুরআন একাডেমি প্রতিষ্ঠার মাধ্যমে জেনারেল শিক্ষিত মানুষজনের জন্য আরবীভাষা, নাহু-সরফ, আদব, তরজমাতুল কুরআন ও অর্থ বুঝে কুরআন পড়ার বিশেষ একটি কোর্সসহ বিভিন্ন ইলমী বিষয়ের পাঠদান করে যাচ্ছেন। আগামীতে একে অনন্য উচ্চতায় নিয়ে যেতে তিনি বদ্ধপরিকর।</p>
        </v-text>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="mx-auto" outlined v-for="(teacher, i) in teachers1" :key="i">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">{{teacher.title}}</div>
              <div class="headline">{{teacher.name}}</div>
              <sub>{{teacher.education}}</sub>
            </v-list-item-content>
            <v-list-item-avatar tile size="80" color="grey">
              <img src="https://nlquran.b-cdn.net/male_teacher.jpg" v-if="teacher.gender == 'male'" />
              <img
                src="https://nlquran.b-cdn.net/female_teacher.jpg"
                v-if="teacher.gender == 'female'"
              />
            </v-list-item-avatar>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col>
        <v-card class="mx-auto" outlined v-for="(teacher, i) in teachers2" :key="i">
          <v-list-item three-line>
            <v-list-item-content>
              <div class="overline mb-4">{{teacher.title}}</div>
              <div class="headline">{{teacher.name}}</div>
              <sub>{{teacher.education}}</sub>
            </v-list-item-content>
            <v-list-item-avatar tile size="80" color="grey">
              <img src="https://nlquran.b-cdn.net/male_teacher.jpg" v-if="teacher.gender == 'male'" />
              <img
                src="https://nlquran.b-cdn.net/female_teacher.jpg"
                v-if="teacher.gender == 'female'"
              />
            </v-list-item-avatar>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <vueper-slides
          autoplay
         :bullets="false"
          :visible-slides="1"
          slide-multiple
          :slide-ratio="1 / 4"
          fixed-height="420px"
          :arrows-outside="true"
          >
          <vueper-slide
            v-for="(slide, i) in testimonials"
            :key="i"
            :title="'<b>' + slide.name + '</b><br /><b>' + slide.identity +'</b>'"
            :content=" '<br/><i>' + slide.testimonial + '</i>' "
          />
        </vueper-slides>
      </v-col>
    </v-row>
  </v-container>
</template>

         


<style scoped>
.quote {
  margin: 50px;
  text-align: center;
  color: #fff;
  font-weight: 800;
  text-shadow: 3px 3px #000;
}

.dark {
  background-color: #f5f5f5;
}

.testimonial {
  margin: 50px;
  background-color: #f5f5f5;
  padding: 50px;
}

blockquote {
  font-family: Georgia, serif;
  font-size: 20px;
  font-style: italic;
  margin: 0.25em 0;
  padding: 0.35em 40px;
  line-height: 1.45;
  position: relative;
  color: #383838;
}

blockquote:before {
  display: block;
  padding-left: 10px;
  content: "\201C";
  font-size: 80px;
  position: absolute;
  left: -20px;
  top: -20px;
  color: #7a7a7a;
}

blockquote cite {
  color: #999999;
  font-size: 14px;
  display: block;
  margin-top: 5px;
}

blockquote cite:before {
  content: "\2014 \2009";
}
</style>

<script>
import { noauth_get } from "@/service/service.js";
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
export default {
  components: { VueperSlides, VueperSlide },
  data: () => ({
    testimonials: [],
    characteristics1: [
      "শিক্ষার্থীদের প্রতি সবিশেষ যত্ন প্রদান",
      "প্রতিটি ক্লাস সাজানো-গোছানো",
      "প্রতিটি বিষয়ে সুন্দর শিট প্রদান",
      "নিয়মিত পরীক্ষার ব্যবস্থা"
    ],
    characteristics2: [
      "যোগ্য শিক্ষক-শিক্ষিকাদের তত্ত্বাবধান",
      "পর্দা নিশ্চিত করতে নারী-পুরুষ আলাদা সেকশন",
      "নারীদের জন্য নারী শিক্ষিকা",
      "আমল-আখলাক গঠনের প্রতিও গুরুত্বদান"
    ],
    characteristics3: [
      "মাঝেমাঝে আত্মশুদ্ধিমূলক মজলিসের ব্যবস্থা",
      "কোর্স শেষে সার্টিফিকেট প্রদান",
      "পেইড ও ফ্রি দুই ধরনের কোর্সের ব্যবস্থা",
      "অর্থনৈতিকভাবে দুর্বলদের জন্য হাফ/ফুল স্কলারশিপের ব্যবস্থা"
    ],
    teachers1: [
      {
        name: "হাফেজ মাওলানা মুফতি হাফিজুর রহমান",
        education:
          "পড়াশোনা : দাওরা হাদীস ও উচ্চতর ইসলামী আইন ও গবেষণা বিভাগ (ইফতা) জামিয়া ইসলামিয়া দারুল উলুম মাদানিয়া, যাত্রাবাড়ি ঢাকা।",
        gender: "male",
        title: "সহকারী শিক্ষক"
      },
      {
        name: "মাওলানা শরীফুল ইসলাম",
        education:
          "পড়াশোনা : দাওরা হাদীস ও উচ্চতর হাদীস বিভাগ (তাখাসসুস ফি উলুমিল হাদীস) জামিয়া ইসলামিয়া দারুল উলুম মাদানিয়া, যাত্রাবাড়ি ঢাকা।",
        gender: "male",
        title: "সহকারী শিক্ষক"
      },
      {
        name: "হাফেজ মাওলানা মুফতি ইকবাল হুসাইন",
        education:
          "পড়াশোনা : দাওরা হাদীস ও উচ্চতর ইসলামী আইন ও গবেষণা বিভাগ (ইফতা) জামিয়া ইসলামিয়া দারুল উলুম মাদানিয়া, যাত্রাবাড়ি ঢাকা।",
        gender: "male",
        title: "সহকারী শিক্ষক"
      },
      {
        name: "আলেমা আসমা ইসরাত",
        education:
          "পড়াশোনা : দাওরা হাদীস, ১৫ পারা হিফজ মাদরাসা খাদিজা বিনতে খুয়াইলিদ (রা.), মানিকগঞ্জ।",
        gender: "female",
        title: "সহকারী শিক্ষিকা"
      }
    ],
    teachers2: [
      {
        name: "যাইনাব জামীলা",
        education:
          "ডিপ্লোমা, আর্কিটেকচার টেকনোলোজি, ঢাকা পলিটেকনিক ইন্সটিটিউট। এরাবিক ল্যাঙ্গুয়েজ, আসলাফ এরাবিক একাডেমি ও উলুমুল কুরআন একাডেমি।",
        gender: "female",
        title: "সহকারী শিক্ষিকা"
      },
      {
        name: "হাফেজা আলেমা তাওহীদা মাহমুদ",
        education: "পড়াশোনা : দাওরা হাদীস, রামপুরা জাতীয় মহিলা মাদরাসা",
        gender: "female",
        title: "সহকারী শিক্ষিকা"
      },
      {
        name: "হাফেজা জান্নাতুল ফিরদাউস",
        education:
          "পড়াশোনা : হিফজ, মিফতাহুল জান্নাত হিফজুল কুরআন মাদরাসা, গাইবান্ধা। HSC, গাইবান্ধা মহিলা কলেজ, গাইবান্ধা।",
        gender: "female",
        title: "সহকারী শিক্ষিকা"
      },
      {
        name: "হাফেজা উম্মে মুমতাহিনা",
        education:
          "হিফজ, সাওদা বিনতে জামআ মহিলা মাদরাসা, নারিন্দা, ঢাকা। কিতাব বিভাগ, জামিয়া ইসলামিয়া মহিলা মাদরাসা, কামরাঙ্গিরচর, ঢাকা।",
        gender: "female",
        title: "সহকারী শিক্ষিকা"
      }
    ]
  }),

  created() {
    this.initialize();
  },
  methods: {
    async initialize() {
      let response = await noauth_get(`/home_testimonials/`);
      if (response.ok) {
        let data = await response.json();
        this.testimonials = data;
      }
    }
  }
};
</script>
