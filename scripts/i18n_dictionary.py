# -*- coding: utf-8 -*-
"""
Centralized Multi-Language Localization System for ZYNAX (EN, HI, BN)
Translates the full application UI seamlessly in-place without page reload.
Preserves dates, times, student numbers, rolls, and user inputs.
"""

I18N_JS = r'''
    // =========================================================================
    // CENTRALIZED MULTI-LANGUAGE TRANSLATION DICTIONARY (EN, HI, BN)
    // =========================================================================

    const ZYNAX_TRANSLATIONS = {
      en: {
        app_tagline: "Your Campus. Your Intelligence. 4-Year Companion.",
        tab_vibe: "Vibe Check",
        tab_vibe_sub: "Today",
        tab_arena: "Code Arena",
        tab_arena_sub: "Contests",
        tab_unstop: "Unstop Radar",
        tab_unstop_sub: "Hackathons",
        tab_journey: "4-Year AI",
        tab_journey_sub: "Companion",
        tab_resume: "Resume AI",
        tab_resume_sub: "LinkedIn",
        tab_timetable: "Daily Grind",
        tab_timetable_sub: "Timetable",
        tab_attendance: "Pull Up",
        tab_attendance_sub: "Attendance",
        tab_planner: "Study Arc",
        tab_planner_sub: "Planner",
        tab_bestie: "Bestie AI",
        tab_bestie_sub: "Voice/Chat",
        tab_notes: "Brain Dump",
        tab_notes_sub: "Notes",
        tab_exam: "ABES Exam Lab",
        tab_exam_sub: "PYQ Vault",
        tab_tools: "Virtual Tools",
        tab_tools_sub: "15 Tools",
        tab_docs: "The Stash",
        tab_docs_sub: "PDFs",
        tab_showtime: "Showtime",
        tab_showtime_sub: "Slides",
        tab_auth: "Lock In",
        tab_auth_sub: "Auth",
        
        card_nextup: "NEXT UP",
        card_bossfight: "BOSS FIGHT",
        card_chapters: "CHAPTERS LEFT",
        card_dontforget: "DON'T FORGET",
        card_overall_att: "OVERALL ATTENDANCE",
        card_att_buffer: "ATTENDANCE BUFFER",
        card_study_streak: "STUDY STREAK",
        card_target_sgpa: "TARGET SGPA",
        btn_ask_bestie: "Ask Bestie AI",
        
        campus_id_title: "MY CAMPUS IDENTITY",
        campus_id_subtitle: "Interactive 3D digital credentials with AI-powered strength analysis & photo studio enhancement.",
        flip_card_btn: "Flip Card",
        download_pdf_btn: "Download ID (PDF)",
        share_profile_btn: "Share Profile",
        upload_new_photo: "Upload Photo",
        reanalyze_ai: "Re-analyze Strengths",
        your_strengths_title: "Your Strengths & AI Analysis",
        strengths_desc: "AI evaluates voluntary student inputs (skills, solved problems, hackathon projects, academic records) to reveal verified abilities and growth pathways.",

        welcome_spoken: "Welcome, {NAME}! Welcome to ZYNAX. Your campus, your intelligence, your 4-year companion.",
        welcome_banner_title: "Welcome to ZYNAX 3.5, {NAME}!",
        welcome_banner_sub: "Your campus, your intelligence, your 4-year companion.",
        btn_replay: "Replay Audio 🔊",
        btn_mute: "Mute",
        btn_unmute: "Unmute"
      },
      hi: {
        app_tagline: "आपका कैंपस। आपकी बुद्धिमत्ता। 4-वर्षीय साथी।",
        tab_vibe: "वाइब चेक",
        tab_vibe_sub: "आज का दिन",
        tab_arena: "कोड एरेना",
        tab_arena_sub: "प्रतियोगिताएं",
        tab_unstop: "अनस्टॉप रडार",
        tab_unstop_sub: "हैकाथॉन",
        tab_journey: "4-वर्षीय AI",
        tab_journey_sub: "साथी",
        tab_resume: "रेज़्यूमे AI",
        tab_resume_sub: "लिंक्डइन",
        tab_timetable: "डेली ग्राइंड",
        tab_timetable_sub: "समय सारणी",
        tab_attendance: "पुल अप",
        tab_attendance_sub: "उपस्थिति",
        tab_planner: "स्टडी आर्क",
        tab_planner_sub: "योजनाकार",
        tab_bestie: "बेस्टी AI",
        tab_bestie_sub: "आवाज़/चैट",
        tab_notes: "ब्रेन डंप",
        tab_notes_sub: "नोट्स",
        tab_exam: "एबीईएस परीक्षा लैब",
        tab_exam_sub: "पीवाईक्यू वॉल्ट",
        tab_tools: "वर्चुअल टूल्स",
        tab_tools_sub: "15 उपकरण",
        tab_docs: "द स्टैश",
        tab_docs_sub: "पीडीएफ़",
        tab_showtime: "शो-टाइम",
        tab_showtime_sub: "स्लाइड्स",
        tab_auth: "लॉग इन",
        tab_auth_sub: "प्रमाणीकरण",

        card_nextup: "अगली कक्षा",
        card_bossfight: "मुख्य परीक्षा",
        card_chapters: "बचे हुए अध्याय",
        card_dontforget: "याद रखें",
        card_overall_att: "कुल उपस्थिति",
        card_att_buffer: "उपस्थिति बफर",
        card_study_streak: "अध्ययन स्ट्रीक",
        card_target_sgpa: "लक्ष्य एसजीपीए",
        btn_ask_bestie: "बेस्टी AI से पूछें",

        campus_id_title: "मेरी कैंपस पहचान",
        campus_id_subtitle: "AI-संचालित ताकत विश्लेषण और फोटो स्टूडियो संवर्धन के साथ इंटरैक्टिव 3D डिजिटल पहचान पत्र।",
        flip_card_btn: "कार्ड पलटें",
        download_pdf_btn: "आईडी पीडीएफ डाउनलोड करें",
        share_profile_btn: "प्रोफाइल साझा करें",
        upload_new_photo: "फोटो अपलोड करें",
        reanalyze_ai: "पुनः विश्लेषण करें",
        your_strengths_title: "आपकी ताकत और क्षमताएं",
        strengths_desc: "AI सत्यापित क्षमताओं और विकास के अवसरों को उजागर करने के लिए स्वैच्छिक छात्र इनपुट का विश्लेषण करता है।",

        welcome_spoken: "स्वागत है, {NAME}! ZYNAX में आपका स्वागत है। आपका कैंपस, आपकी बुद्धिमत्ता, आपका 4-वर्षीय साथी।",
        welcome_banner_title: "ZYNAX 3.5 में आपका स्वागत है, {NAME}!",
        welcome_banner_sub: "आपका कैंपस, आपकी बुद्धिमत्ता, आपका 4-वर्षीय साथी।",
        btn_replay: "ऑडियो दोबारा सुनें 🔊",
        btn_mute: "म्यूट करें",
        btn_unmute: "अनम्यूट करें"
      },
      bn: {
        app_tagline: "আপনার ক্যাম্পাস। আপনার বুদ্ধিমত্তা। ৪-বছরের সঙ্গী।",
        tab_vibe: "ভাইব চেক",
        tab_vibe_sub: "আজকের দিন",
        tab_arena: "কোড এরিনা",
        tab_arena_sub: "প্রতিযোগিতা",
        tab_unstop: "আনস্টপ রাডার",
        tab_unstop_sub: "হ্যাকাথন",
        tab_journey: "৪-বছরের AI",
        tab_journey_sub: "সঙ্গী",
        tab_resume: "রেজিউমে AI",
        tab_resume_sub: "লিঙ্কডইন",
        tab_timetable: "ডেইলি গ্রাইন্ড",
        tab_timetable_sub: "সময়সূচী",
        tab_attendance: "পুল আপ",
        tab_attendance_sub: "উপস্থিতি",
        tab_planner: "স্টাডি আর্ক",
        tab_planner_sub: "প্ল্যানার",
        tab_bestie: "বেস্টি AI",
        tab_bestie_sub: "ভয়েস/চ্যাট",
        tab_notes: "ব্রেন ডাম্প",
        tab_notes_sub: "নোটস",
        tab_exam: "এবিইএস পরীক্ষা ল্যাব",
        tab_exam_sub: "পিওয়াইকিউ ভল্ট",
        tab_tools: "ভার্চুয়াল টুলস",
        tab_tools_sub: "১৫টি টুল",
        tab_docs: "দ্য স্ট্যাশ",
        tab_docs_sub: "পিডিএফ",
        tab_showtime: "শো-টাইম",
        tab_showtime_sub: "স্লাইড",
        tab_auth: "লগ ইন",
        tab_auth_sub: "অথেন্টিকেশন",

        card_nextup: "পরবর্তী ক্লাস",
        card_bossfight: "মূল পরীক্ষা",
        card_chapters: "বাকি থাকা অধ্যায়",
        card_dontforget: "ভুলবেন না",
        card_overall_att: "মোট উপস্থিতি",
        card_att_buffer: "উপস্থিতি বাফার",
        card_study_streak: "স্টাডি স্ট্রিক",
        card_target_sgpa: "টার্গেট এসজিপিএ",
        btn_ask_bestie: "বেস্টি AI কে জিজ্ঞাসা করুন",

        campus_id_title: "আমার ক্যাম্পাস পরিচয়",
        campus_id_subtitle: "AI চালিত শক্তি বিশ্লেষণ এবং ফটো স্টুডিও বর্ধন সহ ইন্টারেক্টিভ 3D ডিজিটাল আইডি।",
        flip_card_btn: "কার্ড উল্টান",
        download_pdf_btn: "আইডি পিডিএফ ডাউনলোড করুন",
        share_profile_btn: "প্রোফাইল শেয়ার করুন",
        upload_new_photo: "ছবি আপলোড করুন",
        reanalyze_ai: "পুনরায় শক্তি বিশ্লেষণ",
        your_strengths_title: "আপনার দক্ষতা ও শক্তি",
        strengths_desc: "AI যাচাইকৃত ক্ষমতা এবং বৃদ্ধির পথ প্রদর্শন করতে ছাত্রের ইনপুট বিশ্লেষণ করে।",

        welcome_spoken: "স্বাগতম, {NAME}! ZYNAX-এ আপনাকে স্বাগতম। আপনার ক্যাম্পাস, আপনার বুদ্ধিমত্তা, আপনার ৪-বছরের সঙ্গী।",
        welcome_banner_title: "ZYNAX 3.5-এ স্বাগতম, {NAME}!",
        welcome_banner_sub: "আপনার ক্যাম্পাস, আপনার বুদ্ধিমত্তা, আপনার ৪-বছরের সঙ্গী।",
        btn_replay: "অডিও পুনরায় শুনুন 🔊",
        btn_mute: "মিউট",
        btn_unmute: "আনমিউট"
      }
    };

    function applyLanguage(lang) {
      const targetLang = (lang && ZYNAX_TRANSLATIONS[lang]) ? lang : "en";
      APP.activeLang = targetLang;
      localStorage.setItem("zynax-lang", targetLang);

      const dict = ZYNAX_TRANSLATIONS[targetLang];
      if (!dict) return;

      // Update data-i18n elements
      document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (dict[key]) {
          let text = dict[key];
          if (text.includes("{NAME}")) {
            const firstName = (APP.studentProfile && APP.studentProfile.name) ? APP.studentProfile.name.split(" ")[0] : "Anurag";
            text = text.replace("{NAME}", firstName);
          }
          el.innerText = text;
        }
      });

      // Update Top Nav Pills
      const navMap = [
        { tab: "dashboard", title: dict.tab_vibe, sub: dict.tab_vibe_sub },
        { tab: "arena", title: dict.tab_arena, sub: dict.tab_arena_sub },
        { tab: "unstop", title: dict.tab_unstop, sub: dict.tab_unstop_sub },
        { tab: "journey", title: dict.tab_journey, sub: dict.tab_journey_sub },
        { tab: "resume", title: dict.tab_resume, sub: dict.tab_resume_sub },
        { tab: "timetable", title: dict.tab_timetable, sub: dict.tab_timetable_sub },
        { tab: "attendance", title: dict.tab_attendance, sub: dict.tab_attendance_sub },
        { tab: "planner", title: dict.tab_planner, sub: dict.tab_planner_sub },
        { tab: "bestie", title: dict.tab_bestie, sub: dict.tab_bestie_sub },
        { tab: "notes", title: dict.tab_notes, sub: dict.tab_notes_sub },
        { tab: "quiz", title: dict.tab_exam, sub: dict.tab_exam_sub },
        { tab: "tools", title: dict.tab_tools, sub: dict.tab_tools_sub },
        { tab: "docs", title: dict.tab_docs, sub: dict.tab_docs_sub },
        { tab: "showtime", title: dict.tab_showtime, sub: dict.tab_showtime_sub },
        { tab: "auth", title: dict.tab_auth, sub: dict.tab_auth_sub }
      ];

      navMap.forEach(item => {
        const pill = document.querySelector(`.nav-tab-pill[data-tab="${item.tab}"]`);
        if (pill) {
          const titleEl = pill.querySelector(".pill-title");
          const subEl = pill.querySelector(".pill-sub");
          if (titleEl) titleEl.innerText = item.title;
          if (subEl) subEl.innerText = item.sub;
        }
      });

      // Update quick language pill state
      document.querySelectorAll(".lang-switch-btn").forEach(btn => {
        if (btn.getAttribute("data-lang") === targetLang) {
          btn.className = "lang-switch-btn px-2 py-0.5 rounded-lg bg-[#D6B66C] text-black font-bold text-[10px]";
        } else {
          btn.className = "lang-switch-btn px-2 py-0.5 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[10px]";
        }
      });

      // Update radio in settings if present
      const radios = document.querySelectorAll("input[name='lang-pref']");
      radios.forEach(r => {
        r.checked = (r.value === targetLang);
      });
    }

    function setGlobalLanguage(lang) {
      applyLanguage(lang);
    }
'''
