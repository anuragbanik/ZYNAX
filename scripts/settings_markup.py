# -*- coding: utf-8 -*-
"""
Markup for Settings & Personal Profile Management (8 Categories)
"""

SETTINGS_HTML = r'''
    <!-- =================================================================
         TAB: SETTINGS & PERSONAL PROFILE MANAGEMENT (8 CATEGORIES)
         ================================================================= -->
    <section id="tab-settings" class="tab-content hidden space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-white/[0.08]">
        <div>
          <h2 class="text-xl font-black flex items-center gap-2 text-white">
            <span>⚙️ SETTINGS &amp; PROFILE</span>
            <span class="text-xs px-2.5 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] font-mono-code font-bold">8 CATEGORIES</span>
          </h2>
          <p class="text-xs text-[#7F8B85]">Manage personal student profile, credentials, appearance, voice AI, and academic privacy.</p>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs font-mono-code text-[#51D6A0] bg-[#51D6A0]/10 px-3 py-1 rounded-xl border border-[#51D6A0]/30 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-[#51D6A0] animate-pulse"></span>
            <span>Profile Sync: Active</span>
          </span>
          <button onclick="saveProfileDetails(true)" class="btn-gold px-4 py-1.5 rounded-xl text-xs font-bold shadow-md">
            Save All Changes
          </button>
        </div>
      </div>

      <!-- Settings Layout: Sidebar Tabs + Content Area -->
      <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
        <!-- Sidebar Navigation (8 Categories) -->
        <div class="lg:col-span-1 space-y-1.5">
          <div class="ref-card p-2 space-y-1">
            <button onclick="switchSettingsCategory('profile')" id="set-cat-profile" class="settings-nav-btn active w-full text-left px-3 py-2 rounded-xl text-xs font-bold flex items-center gap-2 transition bg-[#181E1B] text-white">
              <span>👤</span><span>1. Personal Profile</span>
            </button>
            <button onclick="switchSettingsCategory('appearance')" id="set-cat-appearance" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🎨</span><span>2. Appearance</span>
            </button>
            <button onclick="switchSettingsCategory('notifications')" id="set-cat-notifications" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🔔</span><span>3. Notifications</span>
            </button>
            <button onclick="switchSettingsCategory('voice')" id="set-cat-voice" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🎙️</span><span>4. Voice Assistant</span>
            </button>
            <button onclick="switchSettingsCategory('language')" id="set-cat-language" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🌐</span><span>5. Language</span>
            </button>
            <button onclick="switchSettingsCategory('privacy')" id="set-cat-privacy" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🛡️</span><span>6. Privacy &amp; Security</span>
            </button>
            <button onclick="switchSettingsCategory('memory')" id="set-cat-memory" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🧠</span><span>7. AI Memory</span>
            </button>
            <button onclick="switchSettingsCategory('account')" id="set-cat-account" class="settings-nav-btn w-full text-left px-3 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition text-[#87928B] hover:text-white">
              <span>🎓</span><span>8. Account &amp; Status</span>
            </button>
          </div>
        </div>

        <!-- Main Settings Category Panels -->
        <div class="lg:col-span-3 space-y-5">

          <!-- 1. PERSONAL PROFILE PANEL -->
          <div id="settings-panel-profile" class="settings-panel space-y-5">
            <!-- Profile Avatar Card -->
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white flex items-center gap-2">
                <span>📸 Profile Picture Management</span>
                <span class="text-[10px] px-2 py-0.5 rounded bg-[#D6B66C]/15 text-[#D6B66C]">Instant Real-time Sync</span>
              </h3>
              <div class="flex flex-col sm:flex-row items-center gap-5">
                <!-- Avatar Preview -->
                <div class="relative group">
                  <div id="settings-avatar-display" class="w-24 h-24 rounded-2xl bg-gradient-to-tr from-[#51D6A0] via-[#48B8FF] to-[#9875FF] p-[2px] shadow-xl">
                    <div class="w-full h-full rounded-[14px] bg-[#121614] flex items-center justify-center text-2xl font-black text-[#51D6A0] overflow-hidden" id="settings-avatar-inner">
                      <span id="settings-avatar-initials">AB</span>
                    </div>
                  </div>
                  <div class="absolute -bottom-1 -right-1 w-6 h-6 rounded-full bg-[#51D6A0] border-2 border-[#101412] flex items-center justify-center text-[10px] text-black font-bold">
                    ✓
                  </div>
                </div>

                <!-- Controls -->
                <div class="space-y-2 text-center sm:text-left flex-1">
                  <div class="flex flex-wrap gap-2 justify-center sm:justify-start">
                    <!-- Upload Input -->
                    <input type="file" id="profile-file-input" accept="image/jpeg,image/png,image/webp" class="hidden" onchange="handleProfileUpload(event)" />
                    <button onclick="document.getElementById('profile-file-input').click()" class="btn-gold px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5">
                      <span>📁</span><span>Upload Picture</span>
                    </button>
                    <!-- Camera Capture -->
                    <button onclick="openCameraCaptureModal()" class="btn-purple px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5">
                      <span>📷</span><span>Capture Camera</span>
                    </button>
                    <!-- Crop Reposition -->
                    <button onclick="openCropModal()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-[#F0D28B] flex items-center gap-1.5">
                      <span>✂️</span><span>Crop / Reposition</span>
                    </button>
                    <!-- Remove -->
                    <button onclick="removeProfilePicture()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-red-400 hover:bg-red-500/20 flex items-center gap-1.5">
                      <span>🗑️</span><span>Remove</span>
                    </button>
                  </div>
                  <p class="text-[10px] text-[#7F8B85]">Supported formats: JPG, PNG, WEBP (Max 5MB). Photo updates automatically in the top navigation, greeting, leaderboard, and 4-Year AI companion.</p>
                </div>
              </div>

              <!-- Leaderboard Profile Visibility Toggle -->
              <div class="pt-3 border-t border-white/[0.08] flex items-center justify-between">
                <div>
                  <strong class="text-xs text-white block">Public Leaderboard Visibility</strong>
                  <span class="text-[10px] text-[#7F8B85]">Allow other ABES students to see your profile picture, name, and section on the Exam Arena leaderboard.</span>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" id="profile-visibility-toggle" checked onchange="toggleLeaderboardVisibility(this.checked)" class="sr-only peer" />
                  <div class="w-11 h-6 bg-white/10 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#51D6A0]"></div>
                </label>
              </div>
            </div>

            <!-- Student Academic Details Form -->
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white flex items-center gap-2">
                <span>🎓 Academic Credentials &amp; Identity</span>
                <span class="text-[10px] px-2 py-0.5 rounded bg-[#51D6A0]/15 text-[#51D6A0]">AKTU Verified</span>
              </h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                <div>
                  <label class="text-[#7F8B85] block mb-1">Student Full Name</label>
                  <input type="text" id="prof-name" value="Anurag Banik" class="w-full px-3.5 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]" />
                </div>
                <div>
                  <label class="text-[#7F8B85] block mb-1">College Email Address</label>
                  <input type="email" id="prof-email" value="anurag.banik@abes.ac.in" class="w-full px-3.5 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]" />
                </div>
                <div>
                  <label class="text-[#7F8B85] block mb-1">Admission / University Roll Number</label>
                  <input type="text" id="prof-roll" value="2026ABES042" class="w-full px-3.5 py-2 rounded-xl glass-card text-white text-xs font-mono-code focus:outline-none focus:border-[#D6B66C]" />
                </div>
                <div>
                  <label class="text-[#7F8B85] block mb-1">Branch &amp; Specialization</label>
                  <input type="text" id="prof-branch" value="Computer Science & Engineering (AI/ML)" class="w-full px-3.5 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]" />
                </div>
                <div>
                  <label class="text-[#7F8B85] block mb-1">Section</label>
                  <input type="text" id="prof-section" value="Sec A" class="w-full px-3.5 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]" />
                </div>
                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="text-[#7F8B85] block mb-1">Academic Year</label>
                    <select id="prof-year" class="w-full px-3 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]">
                      <option value="1" selected>Year 1 (Foundation)</option>
                      <option value="2">Year 2 (Skill Dev)</option>
                      <option value="3">Year 3 (Industry)</option>
                      <option value="4">Year 4 (Career)</option>
                    </select>
                  </div>
                  <div>
                    <label class="text-[#7F8B85] block mb-1">Current Semester</label>
                    <select id="prof-sem" class="w-full px-3 py-2 rounded-xl glass-card text-white text-xs focus:outline-none focus:border-[#D6B66C]">
                      <option value="1" selected>Semester 1</option>
                      <option value="2">Semester 2</option>
                      <option value="3">Semester 3</option>
                      <option value="4">Semester 4</option>
                      <option value="5">Semester 5</option>
                      <option value="6">Semester 6</option>
                      <option value="7">Semester 7</option>
                      <option value="8">Semester 8</option>
                    </select>
                  </div>
                </div>
              </div>

              <div class="pt-2 flex justify-end">
                <button onclick="saveProfileDetails(true)" class="btn-emerald px-5 py-2 rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
                  <span>✓</span><span>Save Profile Changes</span>
                </button>
              </div>
            </div>
          </div>

          <!-- 2. APPEARANCE PANEL -->
          <div id="settings-panel-appearance" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white">🎨 Theme &amp; Visual Design System</h3>
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div onclick="setTheme('dark')" class="p-4 rounded-xl ref-card border-2 cursor-pointer transition hover:border-[#D6B66C] border-[#D6B66C]" id="opt-theme-dark">
                  <div class="flex items-center justify-between mb-2">
                    <span class="font-bold text-white">Dark Obsidian (Default)</span>
                    <span class="w-3 h-3 rounded-full bg-[#D6B66C]"></span>
                  </div>
                  <p class="text-[10px] text-[#7F8B85]">Deep matte black, golden highlights, purple and electric blue neon accents.</p>
                </div>
                <div onclick="setTheme('light')" class="p-4 rounded-xl ref-card border-2 cursor-pointer transition hover:border-[#D6B66C]" id="opt-theme-light">
                  <div class="flex items-center justify-between mb-2">
                    <span class="font-bold text-white">Ivory Gold (Light Mode)</span>
                    <span class="w-3 h-3 rounded-full bg-[#121513]"></span>
                  </div>
                  <p class="text-[10px] text-[#7F8B85]">Ivory canvas, champagne gold borders, charcoal cards, high-contrast readable typography.</p>
                </div>
              </div>

              <div class="pt-3 border-t border-white/[0.08] flex items-center justify-between">
                <div>
                  <strong class="text-xs text-white block">Matrix Coding Font Canvas Backdrop</strong>
                  <span class="text-[10px] text-[#7F8B85]">Subtle animated Fira Code matrix text floating in the background.</span>
                </div>
                <input type="checkbox" id="opt-canvas-toggle" checked onchange="toggleMatrixBackdrop(this.checked)" class="accent-[#D6B66C] w-4 h-4 cursor-pointer" />
              </div>
            </div>
          </div>

          <!-- 3. NOTIFICATIONS PANEL -->
          <div id="settings-panel-notifications" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-3">
              <h3 class="text-sm font-black text-white">🔔 Smart Academic Notifications</h3>
              <div class="space-y-3 text-xs">
                <div class="flex items-center justify-between p-2.5 rounded-xl bg-white/[0.03]">
                  <div>
                    <strong class="text-white block">Attendance Armor Warnings</strong>
                    <span class="text-[10px] text-[#7F8B85]">Alert me immediately when any subject drops below 75% attendance.</span>
                  </div>
                  <input type="checkbox" id="notif-att" checked onchange="updateNotificationPref('attendance', this.checked)" class="accent-[#51D6A0] w-4 h-4 cursor-pointer" />
                </div>
                <div class="flex items-center justify-between p-2.5 rounded-xl bg-white/[0.03]">
                  <div>
                    <strong class="text-white block">LeetCode Contest Countdown Alert</strong>
                    <span class="text-[10px] text-[#7F8B85]">Send reminder 1 hour before Weekly &amp; Biweekly contests.</span>
                  </div>
                  <input type="checkbox" id="notif-contest" checked onchange="updateNotificationPref('contest', this.checked)" class="accent-[#D6B66C] w-4 h-4 cursor-pointer" />
                </div>
                <div class="flex items-center justify-between p-2.5 rounded-xl bg-white/[0.03]">
                  <div>
                    <strong class="text-white block">Unstop Hackathon Deadlines</strong>
                    <span class="text-[10px] text-[#7F8B85]">Alert 48 hours before registration closes for saved hackathons.</span>
                  </div>
                  <input type="checkbox" id="notif-hack" checked onchange="updateNotificationPref('hackathon', this.checked)" class="accent-[#48B8FF] w-4 h-4 cursor-pointer" />
                </div>
              </div>
            </div>
          </div>

          <!-- 4. VOICE ASSISTANT PREFERENCES -->
          <div id="settings-panel-voice" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-black text-white">🎙️ Gemini Voice Assistant (Natural Female Voice)</h3>
                  <p class="text-xs text-[#7F8B85]">Configured with smooth, natural female speech synthesis and multi-language support.</p>
                </div>
                <button onclick="testVoiceSpeech()" class="btn-purple px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5">
                  <span>🔊</span><span>Test Voice</span>
                </button>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                <div>
                  <label class="text-[#7F8B85] block mb-1">Voice Personality</label>
                  <select id="voice-persona" onchange="updateVoiceSettings()" class="w-full px-3 py-2 rounded-xl glass-card text-white text-xs">
                    <option value="gemini-female" selected>Gemini Natural Female (Recommended)</option>
                    <option value="gemini-warm">Gemini Warm Studio (Female)</option>
                    <option value="system-female">Native Browser Female Voice</option>
                  </select>
                </div>
                <div>
                  <div class="flex justify-between items-center mb-1">
                    <label class="text-[#7F8B85]">Speaking Rate</label>
                    <span id="voice-rate-val" class="text-[#D6B66C] font-mono-code font-bold">1.0x</span>
                  </div>
                  <input type="range" id="voice-rate" min="0.8" max="1.4" step="0.05" value="1.0" oninput="updateVoiceSettings()" class="w-full accent-[#9875FF]" />
                </div>
              </div>

              <div class="p-3 rounded-xl bg-[#9875FF]/10 border border-[#9875FF]/20 text-[11px] text-[#D8CEFF]">
                <strong>🛡️ Examination Accessibility Guarantee:</strong> Voice assistant reads questions clearly and announces remaining time milestones. It will never provide unauthorized solutions during an active test.
              </div>
            </div>
          </div>

          <!-- 5. LANGUAGE PREFERENCES -->
          <div id="settings-panel-language" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white">🌐 Campus Multi-Language Support</h3>
              <p class="text-xs text-[#7F8B85]">Bestie AI, voice assistant, and exam helpers converse fluently in your selected language.</p>
              <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                <label class="p-3 rounded-xl ref-card flex items-center gap-2 cursor-pointer border hover:border-[#D6B66C]">
                  <input type="radio" name="lang-pref" value="en" checked onchange="setGlobalLanguage('en')" class="accent-[#D6B66C]" />
                  <div><strong class="text-white block">English</strong><span class="text-[9px] text-[#7F8B85]">Default Campus OS</span></div>
                </label>
                <label class="p-3 rounded-xl ref-card flex items-center gap-2 cursor-pointer border hover:border-[#D6B66C]">
                  <input type="radio" name="lang-pref" value="hi" onchange="setGlobalLanguage('hi')" class="accent-[#D6B66C]" />
                  <div><strong class="text-white block">हिंदी (Hindi)</strong><span class="text-[9px] text-[#7F8B85]">प्राकृतिक हिंदी संवाद</span></div>
                </label>
                <label class="p-3 rounded-xl ref-card flex items-center gap-2 cursor-pointer border hover:border-[#D6B66C]">
                  <input type="radio" name="lang-pref" value="bn" onchange="setGlobalLanguage('bn')" class="accent-[#D6B66C]" />
                  <div><strong class="text-white block">বাংলা (Bengali)</strong><span class="text-[9px] text-[#7F8B85]">স্বাভাবিক বাংলা কথোপকথন</span></div>
                </label>
              </div>
            </div>
          </div>

          <!-- 6. PRIVACY & SECURITY -->
          <div id="settings-panel-privacy" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white">🛡️ Privacy &amp; Data Isolation</h3>
              <div class="space-y-3 text-xs">
                <div class="p-3 rounded-xl bg-white/[0.03] space-y-1">
                  <strong class="text-[#51D6A0] block">✓ Strict Student Isolation (Roll: 2026ABES042)</strong>
                  <p class="text-[10px] text-[#7F8B85]">Your uploaded PYQs, test answers, attendance history, and notes are encrypted locally and never leaked to other students.</p>
                </div>
                <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.03]">
                  <div>
                    <strong class="text-white block">Export Complete Student Academic Archive</strong>
                    <span class="text-[10px] text-[#7F8B85]">Download JSON containing profile, test scores, notes, and attendance math.</span>
                  </div>
                  <button onclick="exportStudentDataArchive()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-[#D6B66C]">Export JSON</button>
                </div>
                <div class="flex items-center justify-between p-3 rounded-xl bg-white/[0.03]">
                  <div>
                    <strong class="text-white block">Reset Local Temporary Cache</strong>
                    <span class="text-[10px] text-[#7F8B85]">Clear unsaved question drafts and temporary local states.</span>
                  </div>
                  <button onclick="clearLocalCache()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-red-400">Clear Cache</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 7. AI MEMORY MANAGEMENT -->
          <div id="settings-panel-memory" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <div class="flex items-center justify-between">
                <div>
                  <h3 class="text-sm font-black text-white">🧠 4-Year Student Academic Journey Memory</h3>
                  <span class="text-[10px] text-[#7F8B85]">Persistent memories accumulated across semesters</span>
                </div>
                <button onclick="downloadFourYearMemory()" class="btn-purple px-3 py-1 rounded-xl text-xs font-bold">Download Memory JSON</button>
              </div>
              <div class="p-3 rounded-xl bg-black/40 border border-white/[0.08] text-xs font-mono-code text-[#51D6A0] max-h-48 overflow-y-auto" id="settings-memory-preview">
                Loading academic memory profile...
              </div>
              <div class="flex justify-end gap-2">
                <button onclick="clearRecentChatMemory()" class="glass-card px-3 py-1.5 rounded-xl text-xs text-red-400">Clear Recent Chat Memory</button>
              </div>
            </div>
          </div>

          <!-- 8. ACCOUNT MANAGEMENT -->
          <div id="settings-panel-account" class="settings-panel hidden space-y-4">
            <div class="ref-card p-5 space-y-4">
              <h3 class="text-sm font-black text-white">🎓 Account &amp; Student Verification</h3>
              <div class="p-4 rounded-xl bg-gradient-to-r from-[#181D1A] to-[#121614] border border-[#51D6A0]/40 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-xl bg-[#51D6A0]/20 text-[#51D6A0] flex items-center justify-center font-black text-lg">✓</div>
                  <div>
                    <strong class="text-white text-xs block">ABES Engineering College Verified Student</strong>
                    <span class="text-[10px] text-[#8F9B94]">AKTU Roll: 2026ABES042 · CSE (AI/ML) · Status: Active</span>
                  </div>
                </div>
                <span class="text-xs px-2.5 py-1 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-bold">Authenticated</span>
              </div>
              <div class="pt-2 flex justify-between items-center text-xs">
                <span class="text-[#7F8B85]">Session Active · Client Protected</span>
                <button onclick="switchTab('auth')" class="glass-card px-4 py-2 rounded-xl text-xs font-bold text-red-400 hover:bg-red-500/20">
                  Switch Student Profile / Lock In
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- CAMERA CAPTURE MODAL -->
      <div id="camera-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="ref-card max-w-md w-full p-5 space-y-4 border border-[#9875FF]/40 shadow-2xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <strong class="text-white text-sm flex items-center gap-2">
              <span>📷 Capture Profile Picture</span>
            </strong>
            <button onclick="closeCameraModal()" class="text-white/60 hover:text-white text-lg font-bold">✕</button>
          </div>
          <div class="relative rounded-2xl overflow-hidden bg-black aspect-square flex items-center justify-center border border-white/10">
            <video id="camera-video" autoplay playsinline class="w-full h-full object-cover"></video>
            <canvas id="camera-snap-canvas" class="hidden"></canvas>
            <div id="camera-loading-indicator" class="absolute inset-0 bg-black/80 flex flex-col items-center justify-center text-xs text-white gap-2">
              <span class="w-6 h-6 border-2 border-[#9875FF] border-t-transparent rounded-full animate-spin"></span>
              <span>Requesting Camera Permission...</span>
            </div>
          </div>
          <p class="text-[10px] text-[#7F8B85] text-center">Camera stream runs locally in your browser. No video is ever recorded or transmitted to any server.</p>
          <div class="flex justify-between gap-2">
            <button onclick="closeCameraModal()" class="glass-card px-4 py-2 rounded-xl text-xs font-bold text-white flex-1">Cancel</button>
            <button onclick="snapCameraPhoto()" class="btn-purple px-5 py-2 rounded-xl text-xs font-bold flex-1 flex items-center justify-center gap-1.5">
              <span>📸</span><span>Snap Photo</span>
            </button>
          </div>
        </div>
      </div>

      <!-- CROP & REPOSITION MODAL -->
      <div id="crop-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="ref-card max-w-md w-full p-5 space-y-4 border border-[#D6B66C]/40 shadow-2xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <strong class="text-white text-sm flex items-center gap-2">
              <span>✂️ Crop &amp; Reposition Profile Picture</span>
            </strong>
            <button onclick="closeCropModal()" class="text-white/60 hover:text-white text-lg font-bold">✕</button>
          </div>
          <div class="relative rounded-2xl overflow-hidden bg-black aspect-square flex items-center justify-center border border-white/10">
            <canvas id="crop-canvas" width="300" height="300" class="w-full h-full"></canvas>
            <div class="absolute inset-0 pointer-events-none rounded-full border-2 border-[#D6B66C]/60 shadow-[0_0_0_9999px_rgba(0,0,0,0.5)]"></div>
          </div>
          <div class="space-y-2 text-xs">
            <div class="flex items-center justify-between">
              <span class="text-[#7F8B85]">Zoom / Scale:</span>
              <input type="range" id="crop-scale" min="1" max="2.5" step="0.05" value="1" oninput="renderCropCanvas()" class="w-48 accent-[#D6B66C]" />
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[#7F8B85]">Pan X:</span>
              <input type="range" id="crop-pan-x" min="-100" max="100" step="2" value="0" oninput="renderCropCanvas()" class="w-48 accent-[#D6B66C]" />
            </div>
            <div class="flex items-center justify-between">
              <span class="text-[#7F8B85]">Pan Y:</span>
              <input type="range" id="crop-pan-y" min="-100" max="100" step="2" value="0" oninput="renderCropCanvas()" class="w-48 accent-[#D6B66C]" />
            </div>
          </div>
          <div class="flex justify-between gap-2 pt-1">
            <button onclick="closeCropModal()" class="glass-card px-4 py-2 rounded-xl text-xs font-bold text-white flex-1">Cancel</button>
            <button onclick="applyCroppedImage()" class="btn-gold px-5 py-2 rounded-xl text-xs font-bold flex-1 flex items-center justify-center gap-1.5">
              <span>✓</span><span>Apply Crop</span>
            </button>
          </div>
        </div>
      </div>
    </section>
'''
