# -*- coding: utf-8 -*-
import os
import re
from settings_markup import SETTINGS_HTML
from exam_lab_markup import EXAM_LAB_HTML
from student_id_markup import STUDENT_ID_STYLES, STUDENT_ID_HTML
from welcome_voice_module import WELCOME_BANNER_HTML
from i18n_dictionary import I18N_JS
from student_identity_js import STUDENT_IDENTITY_JS
from extra_js import EXTRA_JS

print("Generating Master ZYNAX 3.5 with 3D AI Student Identity, Voice Welcome, Localization & Clean Header...")

with open(r'C:\Users\Anurag\.gemini\antigravity\scratch\zynax\build_full_zynax3.py', 'r', encoding='utf-8') as f:
    base_script = f.read()

m = re.search(r"html_code\s*=\s*r?'''([\s\S]*?)'''\s*with open", base_script)
if not m:
    m = re.search(r"html_code\s*=\s*r?'''([\s\S]*)", base_script)

raw_html = m.group(1).strip()

# 1. STRICT TERMINATION AT </html> (Prevents downside file path or script leaks)
end_idx = raw_html.find('</html>')
if end_idx != -1:
    html = raw_html[:end_idx + 7]
    print(f"✓ Cleanly extracted HTML ending at </html> (Length: {len(html)})")
else:
    html = raw_html
    print("Warning: </html> tag not found in base HTML")

# 2. NAV BAR: Update Boss Battle pill to ABES Exam Lab, and ensure NO written text pill for Settings!
old_boss_pill = r'''      <div onclick="switchTab('quiz')" class="nav-tab-pill" data-tab="quiz">
        <span class="pill-title">Boss Battle</span>
        <span class="pill-sub">90m Exam</span>
      </div>'''

new_exam_pill = r'''      <div onclick="switchTab('quiz')" class="nav-tab-pill" data-tab="quiz">
        <span class="pill-title text-[#9875FF]">ABES Exam Lab</span>
        <span class="pill-sub">PYQ Vault</span>
      </div>'''

if old_boss_pill in html:
    html = html.replace(old_boss_pill, new_exam_pill)
    print("✓ Updated Boss Battle to ABES Exam Lab in nav pills")
else:
    print("WARNING: Could not find exact old_boss_pill")

# 3. TOP NAV RIGHT CONTROLS:
# REMOVE any settings gear icon button!
# Replace with Quick Multi-Language Switcher Pill (EN | HI | BN)
old_controls_target = r'''      <!-- Theme Switcher -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition" title="Toggle Theme">
        <span id="theme-icon" class="text-xs">☀️</span>
      </button>'''

new_controls_with_lang_pill = r'''      <!-- Quick Multi-Language Switcher Pill -->
      <div class="hidden sm:flex items-center gap-1 p-1 rounded-xl bg-white/[0.04] border border-white/[0.08]" title="Switch Campus Language (English / हिंदी / বাংলা)">
        <button onclick="setGlobalLanguage('en')" data-lang="en" class="lang-switch-btn px-2 py-0.5 rounded-lg bg-[#D6B66C] text-black font-bold text-[10px]">EN</button>
        <button onclick="setGlobalLanguage('hi')" data-lang="hi" class="lang-switch-btn px-2 py-0.5 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[10px]">HI</button>
        <button onclick="setGlobalLanguage('bn')" data-lang="bn" class="lang-switch-btn px-2 py-0.5 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[10px]">BN</button>
      </div>

      <!-- Theme Switcher -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition" title="Toggle Theme">
        <span id="theme-icon" class="text-xs">☀️</span>
      </button>'''

if old_controls_target in html:
    html = html.replace(old_controls_target, new_controls_with_lang_pill)
    print("✓ Clean header: Removed Settings gear from top nav, added quick Language Switcher (EN | HI | BN)")
else:
    print("WARNING: Could not find old_controls_target")

# 4. Top Bar User Profile Pill links to Settings & Student ID
old_user_pill = r'''      <!-- User Profile Pill -->
      <div onclick="switchTab('auth')" class="cursor-pointer flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-[#141A17] border border-white/[0.08] hover:border-white/[0.2] transition">
        <div class="w-7 h-7 rounded-full bg-[#202938] border border-[#48B8FF]/40 flex items-center justify-center text-[10px] text-[#48B8FF] font-black">
          AB
        </div>
        <div class="text-left hidden sm:block">
          <div class="text-xs font-bold text-white leading-tight">Yo, Anurag</div>
          <div class="text-[9px] text-[#717D77] leading-tight">CSE (AI/ML) · Sec A</div>
        </div>
      </div>'''

new_user_pill = r'''      <!-- User Profile Pill -->
      <div onclick="switchTab('settings')" class="cursor-pointer flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-[#141A17] border border-white/[0.08] hover:border-[#D6B66C]/40 transition" title="Personal Profile & Settings">
        <div id="header-avatar-container" class="w-7 h-7 rounded-full bg-[#202938] border border-[#48B8FF]/40 flex items-center justify-center text-[10px] text-[#48B8FF] font-black overflow-hidden">
          <span id="header-avatar-initials">AB</span>
        </div>
        <div class="text-left hidden sm:block">
          <div class="text-xs font-bold text-white leading-tight flex items-center gap-1">
            <span id="header-student-name">Yo, Anurag</span>
            <span class="text-[9px] text-[#51D6A0]">✓</span>
          </div>
          <div class="text-[9px] text-[#717D77] leading-tight" id="header-student-sub">CSE (AI/ML) · Sec A</div>
        </div>
      </div>'''

if old_user_pill in html:
    html = html.replace(old_user_pill, new_user_pill)
    print("✓ Replaced user pill in top bar to link to Settings with dynamic avatar")

# 5. Update Dashboard Greeting Row with Avatar
old_greeting = r'''        <div>
          <div class="text-xs font-semibold text-[#51D6A0]/90 tracking-wide mb-1 font-mono-code">
            Monday, November 23, 2026
          </div>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-white flex items-baseline gap-2">
            <span>Yo,</span>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#51D6A0] via-[#48B8FF] to-[#9875FF]">ANURAG</span>
          </h1>
          <p class="text-xs text-[#7A8680] mt-1 font-medium">
            CSE (AI/ML) · Section A · ABES Engineering College
          </p>
        </div>'''

new_greeting = r'''        <div class="flex items-center gap-3.5">
          <div id="dash-avatar-container" class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-[#51D6A0] via-[#48B8FF] to-[#9875FF] p-[2px] flex-shrink-0 cursor-pointer shadow-lg hover:scale-105 transition" onclick="switchTab('settings')" title="Manage Personal Profile">
            <div class="w-full h-full rounded-[14px] bg-[#101412] flex items-center justify-center text-lg font-black text-[#51D6A0] overflow-hidden" id="dash-avatar-inner">
              <span id="dash-avatar-initials">AB</span>
            </div>
          </div>
          <div>
            <div class="text-xs font-semibold text-[#51D6A0]/90 tracking-wide mb-1 font-mono-code" id="dash-date-str">
              Monday, November 23, 2026
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-white flex items-baseline gap-2">
              <span>Yo,</span>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#51D6A0] via-[#48B8FF] to-[#9875FF]" id="dash-student-name">ANURAG</span>
            </h1>
            <p class="text-xs text-[#7A8680] mt-1 font-medium" id="dash-student-sub">
              CSE (AI/ML) · Section A · ABES Engineering College · Roll: 2026ABES042
            </p>
          </div>
        </div>'''

if old_greeting in html:
    html = html.replace(old_greeting, new_greeting)
    print("✓ Updated dashboard greeting row with profile avatar")

# 6. INJECT 3D AI STUDENT IDENTITY CARD & VOICE WELCOME BANNER INTO DASHBOARD
greeting_row_anchor = r'''        <button onclick="openGeminiVoiceModal()" class="self-start sm:self-center px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#9875FF] to-[#7648F5] text-white font-bold text-xs shadow-lg shadow-[#9875FF]/25 hover:shadow-[#9875FF]/45 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2">
          <span>Ask Bestie AI</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
        </button>
      </div>'''

dashboard_extra_blocks = greeting_row_anchor + "\n\n" + STUDENT_ID_STYLES + "\n" + WELCOME_BANNER_HTML + "\n" + STUDENT_ID_HTML

if greeting_row_anchor in html:
    html = html.replace(greeting_row_anchor, dashboard_extra_blocks)
    print("✓ Injected 3D AI Student Identity Card & AI Voice Welcome Banner into Dashboard")
else:
    print("WARNING: Could not find greeting_row_anchor")

# 7. Add data-i18n attributes to Dashboard 2x2 grid & stats cards for instant localization
html = html.replace('NEXT UP</span>', 'NEXT UP</span>', 1)
html = html.replace(
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#48B8FF] flex items-center gap-1.5">\n              <span>⚡</span> NEXT UP',
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#48B8FF] flex items-center gap-1.5">\n              <span>⚡</span> <span data-i18n="card_nextup">NEXT UP</span>'
)
html = html.replace(
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#9875FF] flex items-center gap-1.5">\n              <span>⚔️</span> BOSS FIGHT',
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#9875FF] flex items-center gap-1.5">\n              <span>⚔️</span> <span data-i18n="card_bossfight">BOSS FIGHT</span>'
)
html = html.replace(
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#D6B66C]">CHAPTERS LEFT</span>',
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#D6B66C]" data-i18n="card_chapters">CHAPTERS LEFT</span>'
)
html = html.replace(
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#51D6A0] flex items-center gap-1.5">\n              <span>🛡️</span> DON\'T FORGET',
    '<span class="text-[11px] font-bold uppercase tracking-wider text-[#51D6A0] flex items-center gap-1.5">\n              <span>🛡️</span> <span data-i18n="card_dontforget">DON\'T FORGET</span>'
)
html = html.replace(
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code">\n            OVERALL ATTENDANCE',
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code" data-i18n="card_overall_att">\n            OVERALL ATTENDANCE'
)
html = html.replace(
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code">\n            ATTENDANCE BUFFER',
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code" data-i18n="card_att_buffer">\n            ATTENDANCE BUFFER'
)
html = html.replace(
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code">\n            STUDY STREAK',
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code" data-i18n="card_study_streak">\n            STUDY STREAK'
)
html = html.replace(
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code">\n            TARGET SGPA',
    '<div class="text-[10px] font-bold uppercase tracking-wider text-[#7A8680] mb-2 font-mono-code" data-i18n="card_target_sgpa">\n            TARGET SGPA'
)

# 8. TOPIC-WISE LEETCODE & CODECHEF QUESTION HUB (LINKED TO VS CODE)
topic_problems_html = r'''
      <!-- C. TOPIC-WISE LEETCODE & CODECHEF QUESTION HUB (LINKED TO VS CODE) -->
      <div class="ref-card space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <h3 class="font-black text-base text-white">TOPIC-WISE PROBLEM ARENA</h3>
              <span class="text-[10px] px-2 py-0.5 rounded-full bg-[#007ACC]/20 text-[#48B8FF] font-mono-code font-bold">VS CODE LINKED</span>
            </div>
            <p class="text-xs text-[#7F8B85]">Curated LeetCode &amp; CodeChef problems with 1-click launch to local Visual Studio Code.</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-xl bg-white/[0.04] text-[#D6B66C] font-mono-code">12 Curated Questions</span>
          </div>
        </div>

        <!-- Topic Filter Pills -->
        <div class="flex gap-1.5 overflow-x-auto pb-1 text-xs no-scrollbar">
          <button onclick="filterTopicProblems('all')" data-topic="all" class="topic-filter-btn px-3 py-1.5 rounded-xl bg-[#D6B66C] text-black font-bold whitespace-nowrap">All Topics</button>
          <button onclick="filterTopicProblems('arrays')" data-topic="arrays" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">Arrays &amp; Prefix Sum</button>
          <button onclick="filterTopicProblems('pointers')" data-topic="pointers" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">Two Pointers &amp; Sliding Window</button>
          <button onclick="filterTopicProblems('binary')" data-topic="binary" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">Binary Search</button>
          <button onclick="filterTopicProblems('trees')" data-topic="trees" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">Trees &amp; Graphs</button>
          <button onclick="filterTopicProblems('dp')" data-topic="dp" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">Dynamic Programming</button>
          <button onclick="filterTopicProblems('codechef')" data-topic="codechef" class="topic-filter-btn px-3 py-1.5 rounded-xl glass-card text-white whitespace-nowrap">CodeChef Specials</button>
        </div>

        <!-- Topic Problems Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3" id="topic-problems-container">
          <!-- Dynamically populated via renderTopicProblems() -->
        </div>
      </div>
'''

arena_grid_anchor = r'''        <!-- Contest Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3" id="global-contests-grid"></div>
      </div>'''

if arena_grid_anchor in html:
    html = html.replace(arena_grid_anchor, arena_grid_anchor + "\n" + topic_problems_html)
    print("✓ Injected Topic-Wise LeetCode & CodeChef section linked with VS Code into tab-arena")
else:
    print("WARNING: Could not find arena_grid_anchor")

# 9. Replace tab-quiz section with EXAM_LAB_HTML and inject SETTINGS_HTML
quiz_regex = r'<section\s+id="tab-quiz"[\s\S]*?</section>'
if re.search(quiz_regex, html):
    html = re.sub(quiz_regex, EXAM_LAB_HTML + "\n\n" + SETTINGS_HTML, html)
    print("✓ Replaced tab-quiz with EXAM_LAB_HTML and injected SETTINGS_HTML")
else:
    print("WARNING: Could not find tab-quiz section")

# 10. Update verifyOtpNow to trigger Welcome Greeting
old_verify_otp = r'''      if (entered === shown) { alert("✅ Authenticated into ZYNAX 3.0!"); switchTab("dashboard"); }'''
new_verify_otp = r'''      if (entered === shown) {
        alert("✅ Authenticated into ZYNAX!");
        switchTab("dashboard");
        triggerLoginWelcome(APP.studentProfile.name);
      }'''

if old_verify_otp in html:
    html = html.replace(old_verify_otp, new_verify_otp)
    print("✓ Updated verifyOtpNow to trigger Login Welcome audio")

# 11. Fix Gemini Voice Assistant to speak responses in FEMALE VOICE
old_gemini_speak = r'''        if ("speechSynthesis" in window && lang === "en") {
          const utter = new SpeechSynthesisUtterance(reply.substring(0, 150));
          utter.lang = "en-US"; utter.rate = 0.95; utter.pitch = 1;
          window.speechSynthesis.speak(utter);
        }'''

new_gemini_speak = r'''        // Speak aloud with natural Gemini female voice
        speakWithFemaleVoice(reply, lang);'''

if old_gemini_speak in html:
    html = html.replace(old_gemini_speak, new_gemini_speak)
    print("✓ Fixed Gemini voice assistant to always respond with natural female voice")

# 12. Inject I18N_JS, STUDENT_IDENTITY_JS, and EXTRA_JS
old_init = r'''    // =================== INIT ON LOAD ===================
    window.addEventListener("DOMContentLoaded", () => {'''

new_js_bundle = I18N_JS + "\n\n" + STUDENT_IDENTITY_JS + "\n\n" + EXTRA_JS + r'''

    // =================== INIT ON LOAD ===================
    window.addEventListener("DOMContentLoaded", () => {
      // Load saved student profile if exists
      try {
        const savedProf = localStorage.getItem("ZYNAX_STUDENT_PROFILE");
        if (savedProf) {
          const parsed = JSON.parse(savedProf);
          if (parsed && typeof parsed === "object") {
            Object.assign(APP.studentProfile, parsed);
          }
        }
      } catch(e){}

      // Load saved notifications
      try {
        const savedNotif = localStorage.getItem("ZYNAX_NOTIFICATIONS");
        if (savedNotif) APP.notifications = JSON.parse(savedNotif);
      } catch(e){}

      // Load saved voice settings
      try {
        const savedVoice = localStorage.getItem("ZYNAX_VOICE_SETTINGS");
        if (savedVoice) APP.voiceSettings = JSON.parse(savedVoice);
      } catch(e){}

      // Load saved language preference
      const savedLang = localStorage.getItem("zynax-lang") || "en";
      applyLanguage(savedLang);

      syncProfileAcrossApp();
      renderTopicProblems();
      renderVaultDocuments();
      renderQuestionBank();
      renderMockPapers();
      renderLeaderboardTable();

      // Trigger Login Welcome Greeting once per session
      if (!sessionStorage.getItem("zynax_welcomed")) {
        sessionStorage.setItem("zynax_welcomed", "1");
        setTimeout(() => {
          triggerLoginWelcome(APP.studentProfile.name);
        }, 600);
      } else {
        // Show welcome banner for easy replay
        const banner = document.getElementById("zynax-welcome-banner");
        if (banner) banner.classList.remove("hidden");
      }'''

if old_init in html:
    html = html.replace(old_init, new_js_bundle)
    print("✓ Injected I18N_JS, STUDENT_IDENTITY_JS, EXTRA_JS and updated DOMContentLoaded")
else:
    print("WARNING: Could not find exact old_init")

# Output files
out_path = r'C:\Users\Anurag\.gemini\antigravity\scratch\zynax\index.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Master index.html generated successfully! ({len(html)} bytes)")

preview_path = r'C:\Users\Anurag\.gemini\antigravity\scratch\zynax\public\preview.html'
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Copied to public preview: {preview_path}")

brain_app_path = r'C:\Users\Anurag\.gemini\antigravity\brain\644051a1-140d-47f0-a51e-a2debe855178\zynax_app.html'
with open(brain_app_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Copied to brain artifact: {brain_app_path}")
