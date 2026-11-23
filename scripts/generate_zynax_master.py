# -*- coding: utf-8 -*-
import os
import re
from settings_markup import SETTINGS_HTML
from exam_lab_markup import EXAM_LAB_HTML
from extra_js import EXTRA_JS

print("Generating Master ZYNAX 3.5...")

with open(r'C:\Users\Anurag\.gemini\antigravity\scratch\zynax\build_full_zynax3.py', 'r', encoding='utf-8') as f:
    base_script = f.read()

m = re.search(r"html_code\s*=\s*r?'''([\s\S]*?)'''\s*with open", base_script)
if not m:
    m = re.search(r"html_code\s*=\s*r?'''([\s\S]*)", base_script)

html = m.group(1).strip()
print(f"Original HTML length: {len(html)}")

# 1. Update Navigation Bar: Add Settings pill and update Boss Battle pill
old_boss_pill = r'''      <div onclick="switchTab('quiz')" class="nav-tab-pill" data-tab="quiz">
        <span class="pill-title">Boss Battle</span>
        <span class="pill-sub">90m Exam</span>
      </div>'''

new_exam_and_settings_pills = r'''      <div onclick="switchTab('quiz')" class="nav-tab-pill" data-tab="quiz">
        <span class="pill-title text-[#9875FF]">ABES Exam Lab</span>
        <span class="pill-sub">PYQ Vault</span>
      </div>
      <div onclick="switchTab('settings')" class="nav-tab-pill" data-tab="settings">
        <span class="pill-title text-[#D6B66C]">Settings</span>
        <span class="pill-sub">Profile (8)</span>
      </div>'''

if old_boss_pill in html:
    html = html.replace(old_boss_pill, new_exam_and_settings_pills)
    print("✓ Replaced boss pill with exam lab & settings pills in desktop nav")
else:
    print("WARNING: Could not find exact old_boss_pill")

# 2. Update Top Bar User Profile Pill to open Settings with dynamic avatar & name
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
else:
    print("WARNING: Could not find exact old_user_pill")

# 3. Update Dashboard Greeting Row with Avatar
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
else:
    print("WARNING: Could not find exact old_greeting")

# 4. Replace tab-quiz section with EXAM_LAB_HTML and inject SETTINGS_HTML
quiz_regex = r'<section\s+id="tab-quiz"[\s\S]*?</section>'
if re.search(quiz_regex, html):
    html = re.sub(quiz_regex, EXAM_LAB_HTML + "\n\n" + SETTINGS_HTML, html)
    print("✓ Replaced tab-quiz with EXAM_LAB_HTML and injected SETTINGS_HTML")
else:
    print("WARNING: Could not find tab-quiz section")

# 5. Inject EXTRA_JS right before INIT ON LOAD and update DOMContentLoaded
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

      syncProfileAcrossApp();
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
