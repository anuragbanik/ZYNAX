# -*- coding: utf-8 -*-
"""
Reorganized Main Dashboard, Floating Liquid Glass Menu, & Achievements Showcase Markup
Features:
1. FLOATING LIQUID GLASS NAVIGATION MENU (Apple frosted glass, access to all 16 sections)
2. PRIMARY TRIAD (First section of the dashboard):
   - Priority 1: Attendance (Overall 75.5%, +3 classes buffer, safe cushion)
   - Priority 2: Boss Flight (MT-02 Physics Exam, 12 days countdown, 51% syllabus)
   - Priority 3: Next Up (Engineering Physics, 10:00-11:00 AM, Room 204, Dr. Verma)
3. 3D SLIDING FEATURE CAROUSEL (Interactive horizontal sliding preview)
4. DEDICATED ACHIEVEMENTS SECTION (At the very bottom of the main webpage)
"""

FLOATING_LIQUID_NAV_HTML = r'''
  <!-- =================================================================
       FLOATING LIQUID GLASS NAVIGATION MENU (APPLE-INSPIRED FROSTED DOCK)
       ================================================================= -->
  <header class="floating-liquid-nav px-4 py-2.5 flex items-center justify-between gap-2">
    <!-- Left Logo Section -->
    <div class="flex items-center gap-3 flex-shrink-0">
      <div onclick="switchTab('dashboard')" class="cursor-pointer flex items-center gap-2 group">
        <div class="w-9 h-9 rounded-xl bg-[#141A17] border border-[#D6B66C]/50 flex items-center justify-center shadow-lg group-hover:scale-105 transition-transform">
          <span class="font-black text-sm text-[#D6B66C]">Z</span>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-black text-base tracking-wider text-white">ZYNAX</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded-full font-bold uppercase tracking-wider bg-[#51D6A0]/20 text-[#51D6A0] border border-[#51D6A0]/30">3.5</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded-full font-bold uppercase tracking-wider bg-[#D6B66C]/20 text-[#D6B66C] border border-[#D6B66C]/30 hidden md:inline">LIQUID GLASS</span>
          </div>
          <span class="text-[10px] text-[#8E9A92] hidden xl:block">Your Campus · Your Intelligence · 4-Year Companion</span>
        </div>
      </div>
    </div>

    <!-- Center Nav Tabs (Scrollable Liquid Glass Pills) -->
    <nav class="hidden lg:flex items-center gap-1 overflow-x-auto py-1 max-w-4xl no-scrollbar">
      <div onclick="switchTab('dashboard')" class="nav-tab-pill active" data-tab="dashboard">
        <span class="pill-title">Vibe Check</span>
        <span class="pill-sub">Today</span>
      </div>
      <div onclick="switchTab('attendance')" class="nav-tab-pill" data-tab="attendance">
        <span class="pill-title text-[#51D6A0]">Attendance</span>
        <span class="pill-sub">Pull Up</span>
      </div>
      <div onclick="switchTab('quiz')" class="nav-tab-pill" data-tab="quiz">
        <span class="pill-title text-[#9875FF]">Boss Flight</span>
        <span class="pill-sub">Exam Lab</span>
      </div>
      <div onclick="switchTab('timetable')" class="nav-tab-pill" data-tab="timetable">
        <span class="pill-title text-[#48B8FF]">Next Up</span>
        <span class="pill-sub">Timetable</span>
      </div>
      <div onclick="switchTab('arena')" class="nav-tab-pill" data-tab="arena">
        <span class="pill-title">Code Arena</span>
        <span class="pill-sub">Contests</span>
      </div>
      <div onclick="switchTab('unstop')" class="nav-tab-pill" data-tab="unstop">
        <span class="pill-title">Unstop Radar</span>
        <span class="pill-sub">Hackathons</span>
      </div>
      <div onclick="switchTab('journey')" class="nav-tab-pill" data-tab="journey">
        <span class="pill-title text-[#D6B66C]">4-Year AI</span>
        <span class="pill-sub">Companion</span>
      </div>
      <div onclick="switchTab('resume')" class="nav-tab-pill" data-tab="resume">
        <span class="pill-title">Resume AI</span>
        <span class="pill-sub">LinkedIn</span>
      </div>
      <div onclick="switchTab('planner')" class="nav-tab-pill" data-tab="planner">
        <span class="pill-title">Study Arc</span>
        <span class="pill-sub">Planner</span>
      </div>
      <div onclick="openGeminiVoiceModal()" class="nav-tab-pill" data-tab="bestie">
        <span class="pill-title text-[#9875FF]">Bestie AI</span>
        <span class="pill-sub">Voice/Chat</span>
      </div>
      <div onclick="switchTab('notes')" class="nav-tab-pill" data-tab="notes">
        <span class="pill-title">Brain Dump</span>
        <span class="pill-sub">Notes</span>
      </div>
      <div onclick="switchTab('tools')" class="nav-tab-pill" data-tab="tools">
        <span class="pill-title">Virtual Tools</span>
        <span class="pill-sub">15 Tools</span>
      </div>
      <div onclick="switchTab('docs')" class="nav-tab-pill" data-tab="docs">
        <span class="pill-title">The Stash</span>
        <span class="pill-sub">PDFs</span>
      </div>
      <div onclick="switchTab('showtime')" class="nav-tab-pill" data-tab="showtime">
        <span class="pill-title">Showtime</span>
        <span class="pill-sub">Slides</span>
      </div>
      <div onclick="switchTab('dashboard'); setTimeout(() => { const el = document.getElementById('section-achievements'); if (el) el.scrollIntoView({behavior:'smooth'}); }, 100);" class="nav-tab-pill" data-tab="achievements">
        <span class="pill-title text-[#D6B66C]">Achievements</span>
        <span class="pill-sub">Showcase</span>
      </div>
      <div onclick="switchTab('auth')" class="nav-tab-pill" data-tab="auth">
        <span class="pill-title text-[#51D6A0]">Lock In</span>
        <span class="pill-sub">Auth</span>
      </div>
    </nav>

    <!-- Right Controls -->
    <div class="flex items-center gap-2 flex-shrink-0">
      <!-- Mobile Menu Toggle Button -->
      <button onclick="toggleMobileMenu()" class="lg:hidden p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-white hover:text-[#D6B66C] transition" title="Toggle Navigation Menu">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
      </button>

      <div class="hidden sm:flex items-center gap-1 px-2.5 py-1 rounded-full bg-white/[0.05] border border-white/[0.08] text-[11px] font-bold text-orange-400">
        <span>🔥</span><span>5d</span>
      </div>
      <div class="hidden md:flex items-center gap-1 px-2.5 py-1 rounded-full bg-[#D6B66C]/10 border border-[#D6B66C]/25 text-[11px] font-bold text-[#D6B66C]">
        <span>⭐</span><span id="header-xp">1,450 XP</span>
      </div>

      <!-- TinyFish API Status Badge -->
      <div class="hidden xl:flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-[#51D6A0]/10 border border-[#51D6A0]/30 text-[10px] font-mono-code font-bold text-[#51D6A0]" title="TinyFish AI Gateway Connected">
        <span class="w-1.5 h-1.5 rounded-full bg-[#51D6A0] animate-pulse"></span>
        <span>TinyFish AI</span>
      </div>

      <!-- Reminder Bell -->
      <button onclick="toggleReminderPanel()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition relative" title="Class Reminders">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg>
        <span class="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-[#51D6A0] animate-pulse"></span>
      </button>

      <!-- Theme Switcher -->
      <button onclick="toggleTheme()" class="p-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#8C9690] hover:text-[#D6B66C] transition" title="Toggle Theme">
        <span id="theme-icon" class="text-xs">☀️</span>
      </button>

      <!-- User Profile Pill -->
      <div onclick="switchTab('settings')" class="cursor-pointer flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-[#141A17] border border-white/[0.08] hover:border-[#D6B66C]/40 transition" title="Personal Profile & Settings">
        <div id="header-avatar-container" class="w-7 h-7 rounded-full bg-[#202938] border border-[#48B8FF]/40 flex items-center justify-center text-[10px] text-[#48B8FF] font-black overflow-hidden">
          <span id="header-avatar-initials">ST</span>
        </div>
        <div class="text-left hidden sm:block">
          <div class="text-xs font-bold text-white leading-tight flex items-center gap-1">
            <span id="header-student-name">Student Account</span>
            <span class="text-[9px] text-[#51D6A0]">✓</span>
          </div>
          <div class="text-[9px] text-[#717D77] leading-tight" id="header-student-sub">Sign In / Switch</div>
        </div>
        <button type="button" onclick="event.stopPropagation(); logoutCurrentStudent();" class="hidden md:inline-flex px-1.5 py-0.5 rounded-md bg-white/[0.05] hover:bg-red-500/20 text-[9px] text-[#8E9A92] hover:text-red-400 transition ml-1" title="Log Out / Switch Account">
          Sign Out
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Liquid Glass Menu Drawer -->
  <div id="mobile-menu-drawer" class="fixed inset-x-0 top-20 z-40 p-4 hidden lg:hidden">
    <div class="liquid-glass-card p-4 space-y-2 border border-[#D6B66C]/30 shadow-2xl">
      <div class="grid grid-cols-2 gap-2 text-xs">
        <button onclick="switchTab('dashboard'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-[#D6B66C]/10 flex items-center gap-2"><span>⚡</span><span>Vibe Check</span></button>
        <button onclick="switchTab('attendance'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-[#51D6A0] font-bold hover:bg-[#51D6A0]/10 flex items-center gap-2"><span>🛡️</span><span>Attendance</span></button>
        <button onclick="switchTab('quiz'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-[#9875FF] font-bold hover:bg-[#9875FF]/10 flex items-center gap-2"><span>⚔️</span><span>Boss Flight</span></button>
        <button onclick="switchTab('timetable'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-[#48B8FF] font-bold hover:bg-[#48B8FF]/10 flex items-center gap-2"><span>📅</span><span>Next Up</span></button>
        <button onclick="switchTab('arena'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>👾</span><span>Code Arena</span></button>
        <button onclick="switchTab('unstop'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>🚀</span><span>Unstop Radar</span></button>
        <button onclick="switchTab('journey'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-[#D6B66C] font-bold hover:bg-[#D6B66C]/10 flex items-center gap-2"><span>🧠</span><span>4-Year AI</span></button>
        <button onclick="switchTab('resume'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>📄</span><span>Resume AI</span></button>
        <button onclick="switchTab('planner'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>⏱️</span><span>Study Arc</span></button>
        <button onclick="openGeminiVoiceModal(); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-[#9875FF] font-bold hover:bg-[#9875FF]/10 flex items-center gap-2"><span>💬</span><span>Bestie AI</span></button>
        <button onclick="switchTab('notes'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>📝</span><span>Brain Dump</span></button>
        <button onclick="switchTab('tools'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>🧰</span><span>Virtual Tools</span></button>
        <button onclick="switchTab('docs'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>📁</span><span>The Stash</span></button>
        <button onclick="switchTab('showtime'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-white/[0.04] text-left text-white font-bold hover:bg-white/[0.08] flex items-center gap-2"><span>📽️</span><span>Showtime</span></button>
        <button onclick="switchTab('dashboard'); setTimeout(() => { const el = document.getElementById('section-achievements'); if (el) el.scrollIntoView({behavior:'smooth'}); }, 100); toggleMobileMenu();" class="p-2.5 rounded-xl bg-[#D6B66C]/10 text-left text-[#D6B66C] font-bold flex items-center gap-2"><span>🏆</span><span>Achievements</span></button>
        <button onclick="switchTab('auth'); toggleMobileMenu();" class="p-2.5 rounded-xl bg-[#51D6A0]/10 text-left text-[#51D6A0] font-bold flex items-center gap-2"><span>🔐</span><span>Account Login</span></button>
      </div>
    </div>
  </div>
'''

DASHBOARD_TRIAD_AND_CAROUSEL_HTML = r'''
      <!-- =================================================================
           PRIMARY TRIAD SECTION: ATTENDANCE · BOSS FLIGHT · NEXT UP
           (Prominently displayed in the FIRST section of the Main Dashboard)
           ================================================================= -->
      <div class="space-y-4 pt-1" id="primary-triad-section">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] font-mono-code font-bold uppercase tracking-wider">
              PRIORITY ZERO · ACADEMIC VITALS
            </span>
            <span class="text-xs text-[#7F8B85] hidden sm:inline">Daily Grind Core Metrics</span>
          </div>
          <span class="text-xs text-[#51D6A0] font-mono-code font-bold flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-[#51D6A0] animate-pulse"></span>
            <span>Real-time Live Sync</span>
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">

          <!-- 1. ATTENDANCE CARD (HERO PRIORITY 1) -->
          <div onclick="switchTab('attendance')" class="liquid-glass-card p-5 group cursor-pointer relative overflow-hidden border-2 hover:border-[#51D6A0]/70 transition-all duration-300">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-black uppercase tracking-wider text-[#51D6A0] flex items-center gap-1.5 font-mono-code">
                  <span>🛡️</span> 1. ATTENDANCE ARMOR
                </span>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-bold font-mono-code">
                  SAFE ZONE
                </span>
              </div>

              <!-- Main Attendance Metric Display -->
              <div class="flex items-baseline justify-between">
                <div>
                  <div class="text-3xl sm:text-4xl font-black text-white tracking-tight flex items-baseline gap-1" id="triad-overall-att">
                    75.5%
                  </div>
                  <p class="text-[10px] text-[#7F8B85] font-medium pt-0.5">Above 75% Mandatory AKTU Barrier</p>
                </div>
                <div class="text-right">
                  <div class="text-lg font-black text-[#D6B66C] font-mono-code" id="triad-att-buffer">+3 classes</div>
                  <div class="text-[9px] text-[#7F8B85]">Bunk Margin Buffer</div>
                </div>
              </div>

              <!-- Subject Health Mini-Bars -->
              <div class="pt-2 border-t border-white/[0.08] space-y-1.5 text-[10px]">
                <div class="flex justify-between items-center text-[#9EA9A3]">
                  <span>Electronics (Critical):</span>
                  <span class="text-red-400 font-bold font-mono-code">62% ⚠️</span>
                </div>
                <div class="flex justify-between items-center text-[#9EA9A3]">
                  <span>Engg Physics:</span>
                  <span class="text-[#51D6A0] font-bold font-mono-code">82% ✓</span>
                </div>
                <div class="flex justify-between items-center text-[#9EA9A3]">
                  <span>Engg Mathematics:</span>
                  <span class="text-amber-400 font-bold font-mono-code">68%</span>
                </div>
              </div>

              <div class="pt-1 flex items-center justify-between text-[10px] text-[#51D6A0] font-bold group-hover:translate-x-1 transition-transform">
                <span>Manage Attendance Calculations →</span>
              </div>
            </div>
          </div>

          <!-- 2. BOSS FLIGHT / BOSS FIGHT CARD (HERO PRIORITY 2) -->
          <div onclick="switchTab('quiz')" class="liquid-glass-card p-5 group cursor-pointer relative overflow-hidden border-2 hover:border-[#9875FF]/70 transition-all duration-300">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-black uppercase tracking-wider text-[#9875FF] flex items-center gap-1.5 font-mono-code">
                  <span>⚔️</span> 2. BOSS FLIGHT / EXAM
                </span>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#9875FF]/20 text-[#D8CEFF] font-bold font-mono-code">
                  PRIORITY 1
                </span>
              </div>

              <div>
                <h3 class="text-lg sm:text-xl font-black text-white group-hover:text-[#D8CEFF] transition">
                  MT-02 Physics Exam
                </h3>
                <div class="flex items-center gap-2 pt-1 text-xs">
                  <span class="text-red-400 font-bold font-mono-code">12 days to go</span>
                  <span class="text-white/30">·</span>
                  <span class="text-[#7F8B85]">Syllabus covered: <strong class="text-white">51%</strong></span>
                </div>
              </div>

              <!-- Progress Bar -->
              <div class="space-y-1">
                <div class="w-full h-2 rounded-full bg-black/60 overflow-hidden p-[1px] border border-white/[0.08]">
                  <div class="h-full rounded-full bg-gradient-to-r from-[#9875FF] to-[#51D6A0]" style="width: 51%"></div>
                </div>
                <div class="flex justify-between text-[9px] text-[#7F8B85] font-mono-code">
                  <span>Unit 1, 2, 3 Revised</span>
                  <span>Unit 4 &amp; 5 Pending</span>
                </div>
              </div>

              <div class="pt-2 border-t border-white/[0.08] flex items-center justify-between text-[10px] text-[#9875FF] font-bold group-hover:translate-x-1 transition-transform">
                <span>Enter ABES Exam Lab &amp; PYQs →</span>
                <span>🔥</span>
              </div>
            </div>
          </div>

          <!-- 3. NEXT UP CARD (HERO PRIORITY 3) -->
          <div onclick="switchTab('timetable')" class="liquid-glass-card p-5 group cursor-pointer relative overflow-hidden border-2 hover:border-[#48B8FF]/70 transition-all duration-300">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-[11px] font-black uppercase tracking-wider text-[#48B8FF] flex items-center gap-1.5 font-mono-code">
                  <span>⚡</span> 3. NEXT UP
                </span>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#48B8FF]/20 text-[#48B8FF] font-bold font-mono-code animate-pulse">
                  IN 20 MINS
                </span>
              </div>

              <div>
                <h3 class="text-lg sm:text-xl font-black text-white group-hover:text-[#48B8FF] transition">
                  Engineering Physics
                </h3>
                <div class="text-xs text-[#7F8B85] pt-0.5 font-medium">
                  10:00 AM – 11:00 AM · Room 204 · Dr. Verma
                </div>
              </div>

              <div class="p-2.5 rounded-xl bg-black/40 border border-white/[0.06] space-y-1">
                <div class="flex items-center justify-between text-[10px]">
                  <span class="text-[#D6B66C] font-bold">Topic for Today:</span>
                  <span class="text-[#7F8B85] font-mono-code">Unit 3 Quantum</span>
                </div>
                <p class="text-[10px] text-white/90 truncate">Compton Effect derivation &amp; de-Broglie wave packet</p>
              </div>

              <div class="pt-1 flex items-center justify-between text-[10px] text-[#48B8FF] font-bold group-hover:translate-x-1 transition-transform">
                <span>View Full Daily Grind Timetable →</span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- =================================================================
           3D SLIDING FEATURE CAROUSEL (COOL 3D SLIDING POWER FEATURES)
           ================================================================= -->
      <div class="space-y-3 pt-2" id="section-3d-carousel">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <h3 class="text-sm font-black text-white uppercase tracking-wider flex items-center gap-2">
              <span>🚀</span><span>ZYNAX 3D POWER MODULES</span>
            </h3>
            <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] font-mono-code font-bold">INTERACTIVE SLIDER</span>
          </div>
          <!-- Slider Navigation Arrows -->
          <div class="flex items-center gap-2">
            <button onclick="slideCarousel(-1)" class="w-8 h-8 rounded-xl liquid-glass-card flex items-center justify-center text-xs text-white hover:text-[#D6B66C] hover:scale-110 active:scale-95 transition" title="Previous Slide">
              ❮
            </button>
            <button onclick="slideCarousel(1)" class="w-8 h-8 rounded-xl liquid-glass-card flex items-center justify-center text-xs text-white hover:text-[#D6B66C] hover:scale-110 active:scale-95 transition" title="Next Slide">
              ❯
            </button>
          </div>
        </div>

        <!-- 3D Viewport Track -->
        <div class="carousel-3d-viewport">
          <div class="carousel-3d-track" id="power-carousel-track">
            
            <!-- Slide 1: ABES Exam Lab -->
            <div onclick="switchTab('quiz')" class="carousel-3d-card liquid-glass-card p-5 cursor-pointer group hover:scale-[1.02] transition-all">
              <div class="liquid-sheen-overlay"></div>
              <div class="relative z-10 space-y-2.5">
                <div class="w-10 h-10 rounded-xl bg-[#9875FF]/20 border border-[#9875FF]/40 flex items-center justify-center text-lg text-[#9875FF]">⚔️</div>
                <h4 class="font-black text-sm text-white group-hover:text-[#9875FF] transition">ABES Exam Lab &amp; PYQ Vault</h4>
                <p class="text-[11px] text-[#7F8B85] leading-relaxed">4 verified exam papers, OCR processor, 2m/4m/10m question bank, and 90-minute proctored mock simulator.</p>
                <div class="text-[10px] text-[#9875FF] font-bold pt-1">Launch Exam Lab →</div>
              </div>
            </div>

            <!-- Slide 2: Code Arena -->
            <div onclick="switchTab('arena')" class="carousel-3d-card liquid-glass-card p-5 cursor-pointer group hover:scale-[1.02] transition-all">
              <div class="liquid-sheen-overlay"></div>
              <div class="relative z-10 space-y-2.5">
                <div class="w-10 h-10 rounded-xl bg-[#48B8FF]/20 border border-[#48B8FF]/40 flex items-center justify-center text-lg text-[#48B8FF]">👾</div>
                <h4 class="font-black text-sm text-white group-hover:text-[#48B8FF] transition">Topic-Wise Code Arena</h4>
                <p class="text-[11px] text-[#7F8B85] leading-relaxed">LeetCode &amp; CodeChef curated DSA problems with 1-click launcher to local Visual Studio Code.</p>
                <div class="text-[10px] text-[#48B8FF] font-bold pt-1">Open Code Arena →</div>
              </div>
            </div>

            <!-- Slide 3: Unstop Radar -->
            <div onclick="switchTab('unstop')" class="carousel-3d-card liquid-glass-card p-5 cursor-pointer group hover:scale-[1.02] transition-all">
              <div class="liquid-sheen-overlay"></div>
              <div class="relative z-10 space-y-2.5">
                <div class="w-10 h-10 rounded-xl bg-[#51D6A0]/20 border border-[#51D6A0]/40 flex items-center justify-center text-lg text-[#51D6A0]">🚀</div>
                <h4 class="font-black text-sm text-white group-hover:text-[#51D6A0] transition">Unstop Hackathon Radar</h4>
                <p class="text-[11px] text-[#7F8B85] leading-relaxed">Real-time college and national hackathons, technical challenges, internships, and countdown alerts.</p>
                <div class="text-[10px] text-[#51D6A0] font-bold pt-1">Explore Hackathons →</div>
              </div>
            </div>

            <!-- Slide 4: 4-Year AI Companion -->
            <div onclick="switchTab('journey')" class="carousel-3d-card liquid-glass-card p-5 cursor-pointer group hover:scale-[1.02] transition-all">
              <div class="liquid-sheen-overlay"></div>
              <div class="relative z-10 space-y-2.5">
                <div class="w-10 h-10 rounded-xl bg-[#D6B66C]/20 border border-[#D6B66C]/40 flex items-center justify-center text-lg text-[#D6B66C]">🧠</div>
                <h4 class="font-black text-sm text-white group-hover:text-[#D6B66C] transition">4-Year Career Companion</h4>
                <p class="text-[11px] text-[#7F8B85] leading-relaxed">8-semester academic trajectory map, skill progression graph, and placement target milestones.</p>
                <div class="text-[10px] text-[#D6B66C] font-bold pt-1">View 4-Yr Roadmap →</div>
              </div>
            </div>

            <!-- Slide 5: Resume AI -->
            <div onclick="switchTab('resume')" class="carousel-3d-card liquid-glass-card p-5 cursor-pointer group hover:scale-[1.02] transition-all">
              <div class="liquid-sheen-overlay"></div>
              <div class="relative z-10 space-y-2.5">
                <div class="w-10 h-10 rounded-xl bg-cyan-400/20 border border-cyan-400/40 flex items-center justify-center text-lg text-cyan-300">📄</div>
                <h4 class="font-black text-sm text-white group-hover:text-cyan-300 transition">ATS Resume &amp; LinkedIn AI</h4>
                <p class="text-[11px] text-[#7F8B85] leading-relaxed">Instant LaTeX / PDF resume exporter with 94/100 ATS scoring and AI headline generator.</p>
                <div class="text-[10px] text-cyan-300 font-bold pt-1">Build Resume →</div>
              </div>
            </div>

          </div>
        </div>
      </div>
'''

ACHIEVEMENTS_SECTION_HTML = r'''
      <!-- =================================================================
           DEDICATED ACHIEVEMENTS SHOWCASE SECTION
           (Placed at the very bottom of the main webpage)
           ================================================================= -->
      <section id="section-achievements" class="achievements-backdrop p-6 sm:p-10 rounded-3xl border border-[#D6B66C]/40 space-y-8 mt-12 relative overflow-hidden">
        <!-- Floating Ambient Glow Orbs -->
        <div class="absolute -top-20 -left-20 w-80 h-80 bg-[#D6B66C]/15 rounded-full blur-[90px] pointer-events-none"></div>
        <div class="absolute -bottom-20 -right-20 w-80 h-80 bg-[#9875FF]/15 rounded-full blur-[90px] pointer-events-none"></div>

        <!-- Section Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-white/[0.08] relative z-10">
          <div class="flex items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl bg-[#D6B66C]/15 border border-[#D6B66C]/40 flex items-center justify-center text-2xl text-[#D6B66C] shadow-xl">
              🏆
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h2 class="text-xl sm:text-2xl font-black text-white tracking-wide">
                  STUDENT ACHIEVEMENTS SHOWCASE
                </h2>
                <span class="text-[10px] px-2.5 py-0.5 rounded-full bg-[#D6B66C]/25 text-[#D6B66C] font-mono-code font-bold">
                  VERIFIED BADGES
                </span>
              </div>
              <p class="text-xs text-[#8E9A92]">
                Verified milestones, academic achievements, coding ranks, and earned badges across your 4-year campus journey.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-2 self-start sm:self-center">
            <span class="text-xs font-mono-code px-3 py-1 rounded-xl bg-white/[0.04] border border-white/[0.08] text-[#51D6A0]">
              Level 4 Scholar · 1,450 XP
            </span>
          </div>
        </div>

        <!-- Achievement Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 relative z-10">

          <!-- 1. Code Arena Grandmaster -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-[#48B8FF]/20 border border-[#48B8FF]/40 flex items-center justify-center text-xl">
                  👾
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#48B8FF]/20 text-[#48B8FF] font-bold font-mono-code">TOP 5%</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#48B8FF] transition">Code Arena Grandmaster</h4>
              <p class="text-[11px] text-[#7F8B85]">84+ curated LeetCode &amp; CodeChef problems solved across Arrays, Two Pointers, and Binary Search.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Contest Rating:</span>
                <span class="text-white font-bold">1,642</span>
              </div>
            </div>
          </div>

          <!-- 2. Boss Flight Victor -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-[#9875FF]/20 border border-[#9875FF]/40 flex items-center justify-center text-xl">
                  ⚔️
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#9875FF]/20 text-[#D8CEFF] font-bold font-mono-code">88.6% MOCK</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#9875FF] transition">Boss Flight Victor</h4>
              <p class="text-[11px] text-[#7F8B85]">Scored 39/44 (88.6%) on Physics MT-02 Mock Paper 2 in authentic ABES Exam Lab simulator.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Accuracy:</span>
                <span class="text-[#51D6A0] font-bold">High Precision</span>
              </div>
            </div>
          </div>

          <!-- 3. Unbroken Daily Grind Streak -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-orange-500/20 border border-orange-500/40 flex items-center justify-center text-xl">
                  🔥
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-orange-500/20 text-orange-400 font-bold font-mono-code">5 DAYS ACTIVE</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-orange-400 transition">Unbroken Daily Grind</h4>
              <p class="text-[11px] text-[#7F8B85]">Consecutive 5-day active study streak logged across syllabus notes, timetable, and attendance audits.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Next Tier:</span>
                <span class="text-orange-400 font-bold">7-Day Gold Master</span>
              </div>
            </div>
          </div>

          <!-- 4. Attendance Armor Shield -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-[#51D6A0]/20 border border-[#51D6A0]/40 flex items-center justify-center text-xl">
                  🛡️
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-bold font-mono-code">AKTU SAFE</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#51D6A0] transition">Attendance Armor</h4>
              <p class="text-[11px] text-[#7F8B85]">Maintained aggregate 75.5% attendance with +3 classes buffer over the 75% college exam threshold.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Margin:</span>
                <span class="text-[#51D6A0] font-bold">+3 Buffer Safe</span>
              </div>
            </div>
          </div>

          <!-- 5. Hackathon Vanguard -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-[#D6B66C]/20 border border-[#D6B66C]/40 flex items-center justify-center text-xl">
                  🚀
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] font-bold font-mono-code">1ST PLACE</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#D6B66C] transition">Hackathon Vanguard</h4>
              <p class="text-[11px] text-[#7F8B85]">Won 1st Place at ABES Freshers Hackathon with autonomous TinyFish AI Campus Companion prototype.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Domain:</span>
                <span class="text-[#D6B66C] font-bold">Generative AI</span>
              </div>
            </div>
          </div>

          <!-- 6. Academic Honors Target -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-cyan-400/20 border border-cyan-400/40 flex items-center justify-center text-xl">
                  🎓
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-cyan-400/20 text-cyan-300 font-bold font-mono-code">SGPA 8.80</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-cyan-300 transition">Academic Honors Track</h4>
              <p class="text-[11px] text-[#7F8B85]">On track for First Class with Distinction honors in B.Tech CSE (Artificial Intelligence &amp; ML).</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Current SGPA:</span>
                <span class="text-cyan-300 font-bold">8.65 / 10.0</span>
              </div>
            </div>
          </div>

          <!-- 7. ATS Placement Ready -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-xl">
                  📄
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-[#51D6A0] font-bold font-mono-code">94/100 ATS</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#51D6A0] transition">ATS Placement Ready</h4>
              <p class="text-[11px] text-[#7F8B85]">Verified Tier-1 ATS resume compiled with optimized keywords for FAANG &amp; AI Startup roles.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Format:</span>
                <span class="text-[#51D6A0] font-bold">LaTeX Certified</span>
              </div>
            </div>
          </div>

          <!-- 8. AI Voice Intelligence Master -->
          <div class="liquid-glass-card p-5 space-y-3 group hover:scale-[1.03] transition-all">
            <div class="liquid-sheen-overlay"></div>
            <div class="relative z-10 space-y-2">
              <div class="flex items-center justify-between">
                <div class="w-10 h-10 rounded-xl bg-purple-500/20 border border-purple-500/40 flex items-center justify-center text-xl">
                  🎙️
                </div>
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-purple-500/20 text-[#D8CEFF] font-bold font-mono-code">CO-PILOT</span>
              </div>
              <h4 class="font-black text-sm text-white group-hover:text-[#D8CEFF] transition">Voice AI Master</h4>
              <p class="text-[11px] text-[#7F8B85]">Configured with natural female voice synthesis, conversational coaching, and exam speech readers.</p>
              <div class="pt-2 border-t border-white/[0.06] flex justify-between text-[10px] font-mono-code">
                <span class="text-[#7F8B85]">Status:</span>
                <span class="text-[#D8CEFF] font-bold">100% Operational</span>
              </div>
            </div>
          </div>

        </div>

        <!-- Academic Milestones Progress Tracker -->
        <div class="liquid-glass-card p-6 space-y-4 relative z-10">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-black text-white uppercase tracking-wider flex items-center gap-2">
              <span>📊</span><span>4-Year Milestone Progression Bars</span>
            </h3>
            <span class="text-[10px] text-[#D6B66C] font-mono-code">Year 1 · Semester 1</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-5 text-xs">
            <!-- Metric 1: LeetCode Goal -->
            <div class="space-y-1.5">
              <div class="flex justify-between">
                <span class="text-[#8E9A92]">DSA Problems:</span>
                <span class="text-white font-mono-code font-bold">84 / 150 (56%)</span>
              </div>
              <div class="w-full h-2 rounded-full bg-black/60 overflow-hidden p-[1px] border border-white/[0.08]">
                <div class="h-full rounded-full bg-gradient-to-r from-[#48B8FF] to-[#D6B66C]" style="width: 56%"></div>
              </div>
            </div>

            <!-- Metric 2: Semester 1 Timeline -->
            <div class="space-y-1.5">
              <div class="flex justify-between">
                <span class="text-[#8E9A92]">Semester 1 Progress:</span>
                <span class="text-white font-mono-code font-bold">65% Completed</span>
              </div>
              <div class="w-full h-2 rounded-full bg-black/60 overflow-hidden p-[1px] border border-white/[0.08]">
                <div class="h-full rounded-full bg-gradient-to-r from-[#51D6A0] to-[#48B8FF]" style="width: 65%"></div>
              </div>
            </div>

            <!-- Metric 3: PYQ Vault Coverage -->
            <div class="space-y-1.5">
              <div class="flex justify-between">
                <span class="text-[#8E9A92]">AKTU Exam Papers:</span>
                <span class="text-[#51D6A0] font-mono-code font-bold">4 / 4 Analyzed (100%)</span>
              </div>
              <div class="w-full h-2 rounded-full bg-black/60 overflow-hidden p-[1px] border border-white/[0.08]">
                <div class="h-full rounded-full bg-gradient-to-r from-[#51D6A0] to-[#51D6A0]" style="width: 100%"></div>
              </div>
            </div>
          </div>
        </div>

      </section>
'''
