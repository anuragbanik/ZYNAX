# -*- coding: utf-8 -*-
"""
ZYNAX Master Generator Pipeline
Generates production index.html, public/preview.html, and brain artifacts with:
- Apple-inspired Liquid Glass Design System
- Floating Liquid Glass Dock Navigation Menu (Access to all 16 sections)
- Reorganized Dashboard with Primary Triad (1. Attendance, 2. Boss Flight, 3. Next Up)
- 3D Sliding Feature Carousel
- Advanced 3D Student Identity Card with Front & Back Profiles, AI Strengths, Photo Studio, Contact Links & QR
- Dedicated Achievements Showcase at the very bottom of the webpage
- Liquid Glass Student Authentication & Account Suite (Sign In, Register, Forgot Password, Show/Hide Password, Validation)
- Smooth Cursor Sensor (Desktop Lerp tracking, magnetic hover, touch-disabled)
- Soft Natural English Female Voice Welcome Experience & Gemini Companion
- Topic-wise LeetCode & CodeChef Arena with VS Code 1-Click launcher
- ABES Exam Lab & AKTU PYQ Vault
"""

import sys
import os
import re

# Add scripts directory to module lookup
scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

from settings_markup import SETTINGS_HTML
from exam_lab_markup import EXAM_LAB_HTML
from student_id_markup import STUDENT_ID_STYLES, STUDENT_ID_HTML
from welcome_voice_module import WELCOME_OVERLAY_HTML, WELCOME_BANNER_HTML
from student_identity_js import STUDENT_IDENTITY_JS
from extra_js import EXTRA_JS
from liquid_glass_styles import LIQUID_GLASS_STYLES
from auth_system_markup import AUTH_SYSTEM_HTML
from dashboard_reorg_markup import FLOATING_LIQUID_NAV_HTML, DASHBOARD_TRIAD_AND_CAROUSEL_HTML, ACHIEVEMENTS_SECTION_HTML
from liquid_cursor_and_features_js import LIQUID_FEATURES_JS

print("Generating Master ZYNAX 3.5 with Liquid Glass UI & 3D Experience...")

zynax_root = os.path.dirname(scripts_dir)
base_py_path = os.path.join(zynax_root, 'build_full_zynax3.py')

with open(base_py_path, 'r', encoding='utf-8') as f:
    base_script = f.read()

m = re.search(r"html_code\s*=\s*r?'''([\s\S]*?)'''\s*with open", base_script)
if not m:
    m = re.search(r"html_code\s*=\s*r?'''([\s\S]*)", base_script)

raw_html = m.group(1).strip()

# 1. STRICT TERMINATION AT </html> (Prevents downside file path or script leaks)
end_idx = raw_html.find('</html>')
if end_idx != -1:
    html = raw_html[:end_idx + 7]
    print(f"✓ Cleanly extracted base HTML ending at </html> (Length: {len(html)})")
else:
    html = raw_html
    print("Warning: </html> tag not found in base HTML")

# 2. INJECT LIQUID_GLASS_STYLES into <head>
if '</head>' in html:
    html = html.replace('</head>', LIQUID_GLASS_STYLES + '\n</head>')
    print("✓ Injected LIQUID_GLASS_STYLES before </head>")
else:
    print("WARNING: </head> not found")

# 3. REPLACE HEADER with FLOATING_LIQUID_NAV_HTML
header_match = re.search(r'<header[\s\S]*?</header>', html)
if header_match:
    html = html[:header_match.start()] + FLOATING_LIQUID_NAV_HTML + html[header_match.end():]
    print("✓ Replaced <header> with FLOATING_LIQUID_NAV_HTML")
else:
    print("WARNING: <header> not found")

# 4. UPDATE DASHBOARD GREETING ROW with profile avatar
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

# 5. INJECT VOICE BANNER, PRIMARY TRIAD (Attendance, Boss Flight, Next Up), 3D CAROUSEL & 3D STUDENT ID CARD
greeting_row_anchor = r'''        <button onclick="openGeminiVoiceModal()" class="self-start sm:self-center px-5 py-2.5 rounded-2xl bg-gradient-to-r from-[#9875FF] to-[#7648F5] text-white font-bold text-xs shadow-lg shadow-[#9875FF]/25 hover:shadow-[#9875FF]/45 hover:scale-[1.02] active:scale-95 transition-all flex items-center gap-2">
          <span>Ask Bestie AI</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
        </button>
      </div>'''

dashboard_top_blocks = (
    greeting_row_anchor + "\n\n" +
    WELCOME_BANNER_HTML + "\n\n" +
    DASHBOARD_TRIAD_AND_CAROUSEL_HTML + "\n\n" +
    STUDENT_ID_STYLES + "\n" +
    STUDENT_ID_HTML
)

if greeting_row_anchor in html:
    html = html.replace(greeting_row_anchor, dashboard_top_blocks)
    print("✓ Injected Voice Banner, Primary Triad, 3D Carousel & 3D Student ID into tab-dashboard")
else:
    print("WARNING: greeting_row_anchor not found")

# 6. INJECT ACHIEVEMENTS_SECTION_HTML AT THE VERY BOTTOM OF #tab-dashboard
cube_end_anchor = r'''            <div class="cube-stats-face face-bt">
              <span class="text-[9px] uppercase font-bold text-[#D6B66C]">ZYNAX</span>
              <span class="text-lg font-black text-[#D6B66C] mt-1">3.0</span>
              <span class="text-[9px] text-[#7F8B85]">ABES EC</span>
            </div>
          </div>
        </div>
      </div>'''

if cube_end_anchor in html:
    html = html.replace(cube_end_anchor, cube_end_anchor + "\n\n" + ACHIEVEMENTS_SECTION_HTML)
    print("✓ Injected ACHIEVEMENTS_SECTION_HTML at the bottom of tab-dashboard")
else:
    print("WARNING: cube_end_anchor not found")

# 7. REPLACE tab-auth WITH LIQUID GLASS STUDENT AUTHENTICATION & ACCOUNT SUITE
auth_regex = r'<section\s+id="tab-auth"[\s\S]*?</section>'
if re.search(auth_regex, html):
    html = re.sub(auth_regex, AUTH_SYSTEM_HTML, html)
    print("✓ Replaced tab-auth with Liquid Glass AUTH_SYSTEM_HTML")
else:
    print("WARNING: tab-auth not found")

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
    print("WARNING: arena_grid_anchor not found")

# 9. Replace tab-quiz section with EXAM_LAB_HTML and inject SETTINGS_HTML
quiz_regex = r'<section\s+id="tab-quiz"[\s\S]*?</section>'
if re.search(quiz_regex, html):
    html = re.sub(quiz_regex, EXAM_LAB_HTML + "\n\n" + SETTINGS_HTML, html)
    print("✓ Replaced tab-quiz with EXAM_LAB_HTML and injected SETTINGS_HTML")
else:
    print("WARNING: tab-quiz section not found")

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

# 11. Fix Gemini Voice Assistant to English soft female voice
old_gemini_header = r'''          <p class="text-[11px] text-[#7F8B85]">Connected: sk-tinyfish-shMmh...zaHPEU · EN/HI/BN</p>
        </div>
        <div class="flex items-center gap-2">
          <select id="gemini-lang-select" class="px-2 py-1 rounded bg-black/50 border border-white/[0.1] text-xs text-white" onchange="changeAssistantLang(this.value)">
            <option value="en">English</option>
            <option value="hi">हिंदी (Hindi)</option>
            <option value="bn">বাংলা (Bengali)</option>
          </select>'''

new_gemini_header = r'''          <p class="text-[11px] text-[#7F8B85]">Connected: sk-tinyfish-shMmh...zaHPEU · English Voice Active</p>
        </div>
        <div class="flex items-center gap-2">'''

if old_gemini_header in html:
    html = html.replace(old_gemini_header, new_gemini_header)
    print("✓ Removed Bestie AI modal language dropdown selector")

html = html.replace("Yo Anurag! Ask me anything in English, Hindi, or Bengali", "Yo Anurag! Ask me anything")

old_gemini_speak = r'''        if ("speechSynthesis" in window && lang === "en") {
          const utter = new SpeechSynthesisUtterance(reply.substring(0, 150));
          utter.lang = "en-US"; utter.rate = 0.95; utter.pitch = 1;
          window.speechSynthesis.speak(utter);
        }'''

new_gemini_speak = r'''        // Speak aloud with soft natural Gemini female voice in English
        speakWithFemaleVoice(reply);'''

if old_gemini_speak in html:
    html = html.replace(old_gemini_speak, new_gemini_speak)
    print("✓ Fixed Gemini voice assistant to always respond with soft English female voice")

# 12. INJECT FULL-SCREEN ANIMATED WELCOME SCREEN OVERLAY (Before </body>)
if '</body>' in html:
    html = html.replace('</body>', WELCOME_OVERLAY_HTML + '\n</body>')
    print("✓ Injected Full-Screen Animated Welcome Screen Overlay into document body")

# 13. INJECT COMPLETE JAVASCRIPT BUNDLE
old_init = r'''    // =================== INIT ON LOAD ===================
    window.addEventListener("DOMContentLoaded", () => {'''

new_js_bundle = (
    STUDENT_IDENTITY_JS + "\n\n" +
    EXTRA_JS + "\n\n" +
    LIQUID_FEATURES_JS + r'''

    // =================== INIT ON LOAD ===================
    window.addEventListener("DOMContentLoaded", () => {
      // Set English as permanent language
      APP.activeLang = "en";

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

      // Load remembered username into Sign In form
      try {
        const rem = localStorage.getItem("ZYNAX_REMEMBERED_USER");
        if (rem) {
          const signinUser = document.getElementById("signin-username");
          const signinRem = document.getElementById("signin-remember");
          if (signinUser) signinUser.value = rem;
          if (signinRem) signinRem.checked = true;
        }
      } catch(e){}

      syncProfileAcrossApp();
      renderTopicProblems();
      renderVaultDocuments();
      renderQuestionBank();
      renderMockPapers();
      renderLeaderboardTable();

      // Keyboard shortcut to dismiss welcome modal (Escape or Enter)
      window.addEventListener("keydown", (e) => {
        if (e.key === "Escape" || e.key === "Enter") {
          const m = document.getElementById("zynax-welcome-modal");
          if (m && !m.classList.contains("opacity-0")) {
            dismissWelcomeModal();
          }
        }
      });

      // Trigger Login Welcome Greeting once per login session
      if (!sessionStorage.getItem("zynax_welcomed")) {
        sessionStorage.setItem("zynax_welcomed", "1");
        setTimeout(() => {
          triggerLoginWelcome(APP.studentProfile.name);
        }, 500);
      }'''
)

if old_init in html:
    html = html.replace(old_init, new_js_bundle)
    print("✓ Injected STUDENT_IDENTITY_JS, EXTRA_JS, LIQUID_FEATURES_JS and updated DOMContentLoaded")
else:
    print("WARNING: Could not find exact old_init")

# Clean up any leftover test files
test_file = os.path.join(scripts_dir, 'test_master_gen.py')
if os.path.exists(test_file):
    try: os.remove(test_file)
    except: pass
inspect_file = os.path.join(scripts_dir, 'inspect_dashboard.py')
if os.path.exists(inspect_file):
    try: os.remove(inspect_file)
    except: pass

# Output files
out_path = os.path.join(zynax_root, 'index.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Master index.html generated successfully! ({len(html)} bytes)")

preview_path = os.path.join(zynax_root, 'public', 'preview.html')
os.makedirs(os.path.dirname(preview_path), exist_ok=True)
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Copied to public preview: {preview_path}")

brain_app_path = r'C:\Users\Anurag\.gemini\antigravity\brain\644051a1-140d-47f0-a51e-a2debe855178\zynax_app.html'
with open(brain_app_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Copied to brain artifact: {brain_app_path}")

brain_embed_path = r'C:\Users\Anurag\.gemini\antigravity\brain\644051a1-140d-47f0-a51e-a2debe855178\zynax_embed.html'
with open(brain_embed_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"✓ Copied to brain embed artifact: {brain_embed_path}")
