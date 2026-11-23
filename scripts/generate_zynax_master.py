# -*- coding: utf-8 -*-
import os
import re
from settings_markup import SETTINGS_HTML
from exam_lab_markup import EXAM_LAB_HTML
from extra_js import EXTRA_JS

print("Generating Master ZYNAX 3.5 with Latest Fixes...")

with open(r'C:\Users\Anurag\.gemini\antigravity\scratch\zynax\build_full_zynax3.py', 'r', encoding='utf-8') as f:
    base_script = f.read()

m = re.search(r"html_code\s*=\s*r?'''([\s\S]*?)'''\s*with open", base_script)
if not m:
    m = re.search(r"html_code\s*=\s*r?'''([\s\S]*)", base_script)

raw_html = m.group(1).strip()

# 1. FIX DOWNSIDE OUTPATH LEAKAGE: Strictly terminate at </html>
end_idx = raw_html.find('</html>')
if end_idx != -1:
    html = raw_html[:end_idx + 7]
    print(f"✓ Cleanly extracted HTML ending at </html> (Length: {len(html)})")
else:
    html = raw_html
    print("Warning: </html> tag not found in base HTML")

# 2. NAV BAR: Update Boss Battle pill to ABES Exam Lab, and DO NOT add written text pill for Settings!
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
    print("✓ Updated Boss Battle to ABES Exam Lab (No written text pill for settings in nav)")
else:
    print("WARNING: Could not find exact old_boss_pill")

# 3. ADD DEDICATED SETTINGS GEAR ICON IN TOP NAV RIGHT CONTROLS
old_controls_target = r'''      <!-- Theme Switcher -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition" title="Toggle Theme">
        <span id="theme-icon" class="text-xs">☀️</span>
      </button>'''

new_controls_with_settings_icon = r'''      <!-- Dedicated Settings Gear Icon Button -->
      <button onclick="switchTab('settings')" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] hover:border-[#D6B66C]/40 transition relative" title="Settings & Personal Profile (8 Categories)">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
        </svg>
      </button>

      <!-- Theme Switcher -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition" title="Toggle Theme">
        <span id="theme-icon" class="text-xs">☀️</span>
      </button>'''

if old_controls_target in html:
    html = html.replace(old_controls_target, new_controls_with_settings_icon)
    print("✓ Added sleek dedicated Settings Gear Icon button in top controls")
else:
    print("WARNING: Could not find old_controls_target")

# 4. Update Top Bar User Profile Pill to link to Settings
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
            <div class="text-xs font-semibold text-[#51D6A0]/90 tracking-wide mb-1 font-mono-code">
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

# 6. IN THE CONTESTS TAB: ADD TOPIC-WISE LEETCODE & CODECHEF QUESTIONS LINKED WITH VS CODE
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

# 7. Replace tab-quiz section with EXAM_LAB_HTML and inject SETTINGS_HTML
quiz_regex = r'<section\s+id="tab-quiz"[\s\S]*?</section>'
if re.search(quiz_regex, html):
    html = re.sub(quiz_regex, EXAM_LAB_HTML + "\n\n" + SETTINGS_HTML, html)
    print("✓ Replaced tab-quiz with EXAM_LAB_HTML and injected SETTINGS_HTML")
else:
    print("WARNING: Could not find tab-quiz section")

# 8. Fix Gemini Voice Assistant to speak responses in FEMALE VOICE
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
else:
    print("WARNING: Could not find old_gemini_speak, checking regex...")

# 9. Inject EXTRA_JS right before INIT ON LOAD and update DOMContentLoaded
old_init = r'''    // =================== INIT ON LOAD ===================
    window.addEventListener("DOMContentLoaded", () => {'''

new_init = EXTRA_JS + r'''

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

      syncProfileAcrossApp();
      renderTopicProblems();
      renderVaultDocuments();
      renderQuestionBank();
      renderMockPapers();
      renderLeaderboardTable();'''

if old_init in html:
    html = html.replace(old_init, new_init)
    print("✓ Injected EXTRA_JS and updated DOMContentLoaded initialization")
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
