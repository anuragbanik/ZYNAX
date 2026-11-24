# -*- coding: utf-8 -*-
"""
Premium English-Only Welcome Experience & Female Voice Greeting for ZYNAX
Features:
- Full-screen animated welcome screen on login
- Elegant floating 3D ZYNAX logo
- Smooth fade-in typography:
  "Welcome, [Username]!
   Welcome to ZYNAX — Your Campus, Your Intelligence, Your Companion."
- Subtle audio waveform visualizer while soft female voice is speaking
- Speaker mute/unmute option & replay greeting functionality
- Smooth animated transition into the dashboard
"""

WELCOME_OVERLAY_HTML = r'''
<!-- =================================================================
     PREMIUM ANIMATED WELCOME SCREEN OVERLAY (FEMALE VOICE EXPERIENCE)
     ================================================================= -->
<div id="zynax-welcome-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-[#090B0A]/90 backdrop-blur-2xl transition-all duration-700 opacity-0 pointer-events-none">
  <!-- Ambient Gold & Purple Glow Orbs -->
  <div class="absolute top-1/4 left-1/3 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#D6B66C]/10 rounded-full blur-[100px] pointer-events-none"></div>
  <div class="absolute bottom-1/4 right-1/3 translate-x-1/2 translate-y-1/2 w-96 h-96 bg-[#9875FF]/10 rounded-full blur-[100px] pointer-events-none"></div>

  <!-- Central Welcome Modal Card -->
  <div class="relative z-10 max-w-xl w-full mx-4 p-8 sm:p-10 rounded-3xl bg-gradient-to-b from-[#161C19]/90 to-[#0F1311]/90 border border-[#D6B66C]/40 shadow-2xl shadow-black/80 text-center space-y-6">
    
    <!-- Floating ZYNAX 3D Logo -->
    <div class="flex justify-center">
      <div class="relative group">
        <div class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-[#D6B66C] via-[#F0D28B] to-[#51D6A0] p-[2.5px] shadow-xl shadow-[#D6B66C]/20 animate-bounce duration-1000">
          <div class="w-full h-full rounded-[14px] bg-[#0A0D0B] flex items-center justify-center font-black text-3xl text-transparent bg-clip-text bg-gradient-to-tr from-[#D6B66C] to-[#51D6A0]">
            Z
          </div>
        </div>
        <div class="absolute -bottom-2 -right-2 px-2 py-0.5 rounded-full bg-[#9875FF] text-[9px] font-mono-code font-bold text-white shadow">
          AI OS
        </div>
      </div>
    </div>

    <!-- Soft Fade-In Typography -->
    <div class="space-y-3">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D6B66C]/15 border border-[#D6B66C]/30 text-[#D6B66C] text-xs font-mono-code font-bold tracking-wider uppercase">
        <span>✨</span><span>CAMPUS INTELLIGENCE</span>
      </div>
      
      <h1 class="text-3xl sm:text-4xl font-black text-white tracking-tight">
        <span>Welcome, </span>
        <span id="welcome-modal-username" class="text-transparent bg-clip-text bg-gradient-to-r from-[#D6B66C] via-[#F0D28B] to-[#51D6A0]">
          Anurag
        </span>!
      </h1>

      <p class="text-base sm:text-lg text-[#C4D0C9] font-medium leading-relaxed max-w-md mx-auto">
        Welcome to ZYNAX — <span class="text-white font-semibold">Your Campus, Your Intelligence, Your Companion.</span>
      </p>
    </div>

    <!-- Subtle Audio Waveform Visualizer (Active while speaking) -->
    <div class="flex items-center justify-center gap-1.5 py-2">
      <span class="w-1.5 h-4 bg-[#D6B66C] rounded-full voice-wave-bar"></span>
      <span class="w-1.5 h-8 bg-[#9875FF] rounded-full voice-wave-bar"></span>
      <span class="w-1.5 h-12 bg-[#48B8FF] rounded-full voice-wave-bar"></span>
      <span class="w-1.5 h-7 bg-[#51D6A0] rounded-full voice-wave-bar"></span>
      <span class="w-1.5 h-3 bg-[#D6B66C] rounded-full voice-wave-bar"></span>
    </div>

    <!-- Controls & Transition Actions -->
    <div class="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
      <!-- Enter Dashboard Button -->
      <button onclick="dismissWelcomeModal()" class="w-full sm:w-auto btn-gold px-7 py-3 rounded-2xl text-sm font-bold shadow-xl shadow-[#D6B66C]/20 hover:scale-105 active:scale-95 transition flex items-center justify-center gap-2">
        <span>Enter Dashboard</span>
        <span>→</span>
      </button>

      <!-- Replay Greeting Button -->
      <button onclick="replayWelcomeGreeting()" class="w-full sm:w-auto glass-card px-4 py-3 rounded-2xl text-xs font-bold text-[#D6B66C] hover:bg-[#D6B66C]/10 transition flex items-center justify-center gap-1.5" title="Replay English Female Voice Greeting">
        <span>🔊</span><span>Replay Voice</span>
      </button>

      <!-- Mute/Unmute Button -->
      <button onclick="toggleWelcomeMute()" id="welcome-mute-btn" class="w-full sm:w-auto glass-card px-4 py-3 rounded-2xl text-xs font-semibold text-[#8C9690] hover:text-white transition flex items-center justify-center gap-1.5" title="Toggle Audio">
        <span id="welcome-mute-icon">🔈</span>
        <span id="welcome-mute-label">Mute</span>
      </button>
    </div>

    <div class="text-[11px] text-[#7F8B85] font-mono-code pt-1">
      Soft Natural Female Voice · English Edition · Press Escape or Enter to proceed
    </div>
  </div>
</div>
'''

WELCOME_BANNER_HTML = r'''
      <!-- =================================================================
           DASHBOARD AI VOICE COMPANION BADGE (REPLAY & VOICE CONTROLS)
           ================================================================= -->
      <div id="zynax-welcome-banner" class="ref-card p-4 border border-[#D6B66C]/40 bg-gradient-to-r from-[#171D19] via-[#101412] to-[#17131F] shadow-2xl relative overflow-hidden transition-all duration-500">
        <!-- Background Ambient Glow -->
        <div class="absolute -top-12 -right-12 w-48 h-48 bg-[#D6B66C]/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-12 -left-12 w-48 h-48 bg-[#9875FF]/10 rounded-full blur-3xl pointer-events-none"></div>

        <div class="relative z-10 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <!-- Left: Waveform + Message -->
          <div class="flex items-center gap-3.5">
            <!-- Animated Sound Wave Visualizer -->
            <div class="w-12 h-12 rounded-2xl bg-[#9875FF]/15 border border-[#9875FF]/30 flex items-center justify-center gap-1 flex-shrink-0 shadow-lg cursor-pointer hover:scale-105 transition" onclick="replayWelcomeGreeting()" title="Replay Welcome Voice Greeting">
              <span class="w-1 h-3 bg-[#D6B66C] rounded-full voice-wave-bar"></span>
              <span class="w-1 h-6 bg-[#9875FF] rounded-full voice-wave-bar"></span>
              <span class="w-1 h-8 bg-[#48B8FF] rounded-full voice-wave-bar"></span>
              <span class="w-1 h-5 bg-[#51D6A0] rounded-full voice-wave-bar"></span>
              <span class="w-1 h-2 bg-[#D6B66C] rounded-full voice-wave-bar"></span>
            </div>

            <!-- Welcome Text Display -->
            <div class="space-y-0.5">
              <div class="flex items-center gap-2">
                <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#9875FF]/20 text-[#D8CEFF] font-mono-code font-bold uppercase tracking-wider">
                  🎙️ AI CAMPUS COMPANION
                </span>
                <span class="text-[9px] text-[#51D6A0] font-mono-code font-bold">ENGLISH FEMALE VOICE</span>
              </div>
              <h2 class="text-sm sm:text-base font-black text-white" id="welcome-banner-heading">
                Welcome to ZYNAX, Anurag!
              </h2>
              <p class="text-xs text-[#C4D0C9] italic font-medium" id="welcome-banner-script">
                "Welcome to ZYNAX — Your Campus, Your Intelligence, Your Companion."
              </p>
            </div>
          </div>

          <!-- Right Controls -->
          <div class="flex items-center gap-2 flex-shrink-0 self-end sm:self-center">
            <button onclick="replayWelcomeGreeting()" class="btn-gold px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-md">
              <span>🔊</span><span>Replay Greeting</span>
            </button>
            <button onclick="toggleWelcomeMute()" id="welcome-dash-mute-btn" class="glass-card px-3 py-1.5 rounded-xl text-xs font-semibold text-[#8C9690] hover:text-white transition">
              <span id="welcome-dash-mute-label">Mute</span>
            </button>
          </div>
        </div>
      </div>
'''
