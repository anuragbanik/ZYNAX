# -*- coding: utf-8 -*-
"""
AI Voice Welcome Experience Module for ZYNAX:
- Natural friendly female voice greeting
- Spoken script: "Welcome, [USER NAME]! Welcome to ZYNAX. Your campus, your intelligence, your 4-year companion."
- Animated waveform visual banner
- Mute/Unmute & Replay controls
- Graceful audio autoplay handling
"""

WELCOME_BANNER_HTML = r'''
      <!-- =================================================================
           AI VOICE WELCOME BANNER (FEMALE VOICE ENGINE)
           ================================================================= -->
      <div id="zynax-welcome-banner" class="hidden ref-card p-4 border border-[#D6B66C]/40 bg-gradient-to-r from-[#171D19] via-[#101412] to-[#17131F] shadow-2xl relative overflow-hidden transition-all duration-500">
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
                  🎙️ AI CAMPUS GREETING
                </span>
                <span class="text-[9px] text-[#51D6A0] font-mono-code font-bold">FEMALE VOICE ACTIVE</span>
              </div>
              <h2 class="text-sm sm:text-base font-black text-white" id="welcome-banner-heading" data-i18n="welcome_banner_title">
                Welcome to ZYNAX, Anurag!
              </h2>
              <p class="text-xs text-[#C4D0C9] italic font-medium" id="welcome-banner-script" data-i18n="welcome_banner_sub">
                "Welcome, Anurag! Welcome to ZYNAX. Your campus, your intelligence, your 4-year companion."
              </p>
            </div>
          </div>

          <!-- Right Controls -->
          <div class="flex items-center gap-2 flex-shrink-0 self-end sm:self-center">
            <button onclick="replayWelcomeGreeting()" class="btn-gold px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-md">
              <span>🔊</span><span data-i18n="btn_replay">Replay Greeting</span>
            </button>
            <button onclick="toggleWelcomeMute()" id="welcome-mute-btn" class="glass-card px-3 py-1.5 rounded-xl text-xs font-semibold text-[#8C9690] hover:text-white transition">
              <span id="welcome-mute-label" data-i18n="btn_mute">Mute</span>
            </button>
            <button onclick="dismissWelcomeBanner()" class="p-1.5 rounded-xl bg-white/[0.04] text-[#8C9690] hover:text-white transition" title="Dismiss Welcome Banner">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
            </button>
          </div>
        </div>
      </div>
'''
