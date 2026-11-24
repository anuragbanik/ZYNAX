# -*- coding: utf-8 -*-
"""
Markup & Styling for 3D AI Student Identity Card & "My Campus Identity"
Features:
- True CSS 3D perspective flip card (Front & Back)
- Holographic champagne gold metallic border (#D6B66C)
- Specular holographic sheen overlay
- Original Photo vs. AI Studio Enhanced Photo toggle
- AKTU verified chip, Barcode, and QR Code
- AI-Powered "Your Strengths" engine (Key, Technical, Creative, Problem-Solving, Leadership, Growth)
- PDF Profile Download and Shareable Profile actions
"""

STUDENT_ID_STYLES = r'''
<style>
/* 3D Student Identity Card Styles */
.id-card-scene {
  perspective: 1200px;
}
.id-card-flipper {
  position: relative;
  width: 100%;
  max-width: 520px;
  height: 310px;
  transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transform-style: preserve-3d;
  cursor: pointer;
  margin: 0 auto;
}
.id-card-flipper.flipped {
  transform: rotateY(180deg);
}
.id-card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 20px rgba(214, 182, 108, 0.15);
  border: 1.5px solid rgba(214, 182, 108, 0.35);
  background: linear-gradient(135deg, #141816 0%, #0d100e 100%);
  display: flex;
  flex-direction: column;
}
.id-card-back {
  transform: rotateY(180deg);
  background: linear-gradient(135deg, #0e1210 0%, #171d19 100%);
}
.id-card-holo-sheen {
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg, transparent 20%, rgba(214, 182, 108, 0.12) 38%, rgba(72, 184, 255, 0.12) 50%, rgba(152, 117, 255, 0.12) 62%, transparent 80%);
  background-size: 200% 200%;
  pointer-events: none;
  mix-blend-mode: overlay;
  transition: background-position 0.5s ease;
  z-index: 5;
}
.id-chip-gold {
  background: linear-gradient(135deg, #F0D28B 0%, #D6B66C 50%, #9B7832 100%);
  border: 1px solid rgba(255,255,255,0.4);
  position: relative;
  border-radius: 6px;
  width: 40px;
  height: 30px;
  box-shadow: inset 0 1px 2px rgba(255,255,255,0.5), 0 2px 4px rgba(0,0,0,0.4);
}
.id-chip-gold::before {
  content: '';
  position: absolute;
  top: 9px;
  left: 0;
  right: 0;
  height: 1px;
  background: rgba(0,0,0,0.3);
}
.id-chip-gold::after {
  content: '';
  position: absolute;
  top: 19px;
  left: 0;
  right: 0;
  height: 1px;
  background: rgba(0,0,0,0.3);
}
.barcode-lines {
  background: repeating-linear-gradient(90deg, #F5F5F5 0px, #F5F5F5 2px, transparent 2px, transparent 4px, #F5F5F5 4px, #F5F5F5 5px, transparent 5px, transparent 8px);
}
</style>
'''

STUDENT_ID_HTML = r'''
      <!-- =================================================================
           MY CAMPUS IDENTITY — 3D AI STUDENT IDENTITY CARD & STRENGTHS ENGINE
           ================================================================= -->
      <div class="ref-card space-y-6 relative overflow-hidden" id="section-campus-identity">
        <!-- Top Section Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-white/[0.08]">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-2xl bg-[#D6B66C]/10 border border-[#D6B66C]/30 flex items-center justify-center text-lg text-[#D6B66C] shadow-lg">
              🪪
            </div>
            <div>
              <div class="flex items-center gap-2">
                <h2 class="text-lg font-black text-white tracking-wide" data-i18n="campus_id_title">MY CAMPUS IDENTITY</h2>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] font-mono-code font-bold">3D AI SMART ID</span>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code font-bold">AKTU VERIFIED</span>
              </div>
              <p class="text-xs text-[#7F8B85]" data-i18n="campus_id_subtitle">Interactive 3D digital credentials with AI-powered strength analysis &amp; photo studio enhancement.</p>
            </div>
          </div>
          <!-- Action Buttons -->
          <div class="flex items-center gap-2 flex-wrap">
            <button onclick="flipStudentCard()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-[#D6B66C] hover:bg-[#D6B66C]/20 transition flex items-center gap-1.5" title="Flip Card to view Academic Backside">
              <span>🔄</span><span data-i18n="flip_card_btn">Flip Card</span>
            </button>
            <button onclick="downloadStudentCardPdf()" class="btn-gold px-3.5 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 shadow-md">
              <span>📄</span><span data-i18n="download_pdf_btn">Download ID (PDF)</span>
            </button>
            <button onclick="shareStudentProfile()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-white hover:text-[#51D6A0] transition flex items-center gap-1.5" title="Copy shareable link">
              <span>🔗</span><span data-i18n="share_profile_btn">Share Profile</span>
            </button>
          </div>
        </div>

        <!-- 3D Card Display + Interactive Studio Column Layout -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          <!-- Left: 3D Interactive Card Scene -->
          <div class="lg:col-span-6 flex flex-col items-center space-y-4">
            
            <div class="id-card-scene w-full">
              <div class="id-card-flipper" id="interactive-student-card" onclick="handleCardClick(event)" onmousemove="handleCardTilt(event)" onmouseleave="resetCardTilt()">
                <!-- Holographic Sheen Overlay -->
                <div class="id-card-holo-sheen" id="card-sheen"></div>

                <!-- ================= FRONT FACE ================= -->
                <div class="id-card-face id-card-front p-5 justify-between">
                  <!-- Header: College Info -->
                  <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
                    <div class="flex items-center gap-2.5">
                      <div class="w-8 h-8 rounded-lg bg-[#0A0D0B] border border-[#D6B66C]/50 flex items-center justify-center font-black text-xs text-[#D6B66C]">
                        Z
                      </div>
                      <div>
                        <div class="text-[11px] font-black tracking-wider text-white uppercase">ABES ENGINEERING COLLEGE</div>
                        <div class="text-[8px] text-[#7F8B85] font-mono-code">AKTU CODE 032 · GHAZIABAD · CAMPUS ECOSYSTEM</div>
                      </div>
                    </div>
                    <div class="text-right">
                      <span class="text-[9px] px-1.5 py-0.5 rounded bg-[#51D6A0]/15 text-[#51D6A0] font-mono-code font-bold">2026–2030</span>
                      <div class="text-[8px] text-[#7F8B85]">SMART PASS</div>
                    </div>
                  </div>

                  <!-- Middle: Student Photo + Main Info -->
                  <div class="flex items-center gap-4 py-2">
                    <!-- Photo with AI Enhanced / Original toggle indicator -->
                    <div class="relative group flex-shrink-0">
                      <div class="w-20 h-24 rounded-xl p-[2px] bg-gradient-to-b from-[#D6B66C] via-[#9875FF] to-[#48B8FF] shadow-lg overflow-hidden">
                        <div class="w-full h-full rounded-[10px] bg-[#101412] flex items-center justify-center overflow-hidden relative">
                          <img id="card-photo-img" src="" alt="Student Photo" class="w-full h-full object-cover hidden" />
                          <span id="card-photo-fallback" class="font-black text-2xl text-[#D6B66C]">AB</span>
                        </div>
                      </div>
                      <div id="card-photo-badge" class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded bg-[#9875FF] text-[8px] font-bold text-white shadow">
                        ENHANCED
                      </div>
                    </div>

                    <!-- Details -->
                    <div class="space-y-1 flex-1 min-w-0">
                      <div class="flex items-center justify-between">
                        <h3 class="text-base font-black text-white truncate" id="card-display-name">Anurag Banik</h3>
                        <div class="id-chip-gold flex-shrink-0" title="Smart NFC Microchip"></div>
                      </div>
                      <div class="text-[11px] font-mono-code text-[#D6B66C] font-bold tracking-wide" id="card-display-roll">
                        2026ABES042
                      </div>
                      <div class="text-[10px] text-[#C4D0C9] truncate font-medium" id="card-display-branch">
                        CSE (AI &amp; Machine Learning)
                      </div>
                      <div class="text-[9px] text-[#7F8B85] flex items-center gap-2">
                        <span id="card-display-sec">Sec A · 1st Year</span>
                        <span>·</span>
                        <span class="text-[#51D6A0]">Sem 1</span>
                      </div>
                      <div class="flex items-center gap-1.5 pt-1">
                        <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F5F5F5] font-mono-code">AI SPECIALIST</span>
                        <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/15 text-[#51D6A0] font-mono-code">SGPA 8.80</span>
                      </div>
                    </div>
                  </div>

                  <!-- Footer: Barcode & Digital Signature -->
                  <div class="pt-2 border-t border-white/[0.08] flex items-center justify-between">
                    <div class="space-y-0.5">
                      <div class="w-36 h-4 barcode-lines rounded-sm"></div>
                      <div class="text-[7px] text-[#7F8B85] font-mono-code tracking-widest">AKTU-ABES-2026-984210</div>
                    </div>
                    <div class="flex items-center gap-2 text-right">
                      <div class="text-[8px] text-[#8C9690] font-mono-code">
                        <span>TAP TO FLIP</span> 🔄
                      </div>
                    </div>
                  </div>
                </div>

                <!-- ================= BACK FACE ================= -->
                <div class="id-card-face id-card-back p-5 justify-between">
                  <!-- Header -->
                  <div class="flex items-center justify-between pb-1.5 border-b border-white/[0.08]">
                    <span class="text-[10px] font-black uppercase text-[#D6B66C] tracking-wider">ACADEMIC &amp; AI VERIFICATION</span>
                    <span class="text-[8px] text-[#51D6A0] font-mono-code">REGISTRAR AUTHENTICATED</span>
                  </div>

                  <!-- Middle: Strengths & Academic Highlights -->
                  <div class="grid grid-cols-2 gap-3 py-1 text-[9px]">
                    <div class="space-y-1">
                      <span class="text-[#7F8B85] block font-bold">CORE DOMAIN:</span>
                      <p class="text-white font-medium" id="card-back-domain">Artificial Intelligence &amp; Autonomous Agents</p>
                      
                      <span class="text-[#7F8B85] block font-bold pt-1">LIBRARY ID:</span>
                      <p class="text-[#D6B66C] font-mono-code">LIB-2026-ABES-042</p>

                      <span class="text-[#7F8B85] block font-bold pt-1">BLOOD GROUP:</span>
                      <p class="text-white">B+ Positive (Verified)</p>
                    </div>

                    <div class="space-y-1">
                      <span class="text-[#7F8B85] block font-bold">TOP STRENGTH:</span>
                      <p class="text-[#51D6A0] font-medium" id="card-back-strength">Algorithmic Problem Solving &amp; Neural Nets</p>

                      <span class="text-[#7F8B85] block font-bold pt-1">CAMPUS PORTAL:</span>
                      <p class="text-[#48B8FF] font-mono-code truncate">zynax.abes.ac.in</p>

                      <span class="text-[#7F8B85] block font-bold pt-1">EMERGENCY LINE:</span>
                      <p class="text-white font-mono-code">+91 98765 43210</p>
                    </div>
                  </div>

                  <!-- QR Code & Official Stamp -->
                  <div class="pt-2 border-t border-white/[0.08] flex items-center justify-between">
                    <div class="flex items-center gap-2">
                      <div class="w-9 h-9 rounded bg-white p-0.5 flex items-center justify-center">
                        <!-- Mini SVG QR Code representation -->
                        <svg class="w-full h-full text-black" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M2 2h8v8H2V2zm2 2v4h4V4H4zm10-2h8v8h-8V2zm2 2v4h4V4h-4zM2 14h8v8H2v-8zm2 2v4h4v-4H4zm14 0h4v4h-4v-4zm-4 4h4v4h-4v-4zm4-4v-4h-4v4h4zm-4-4h4V6h-4v4z"/>
                        </svg>
                      </div>
                      <div class="text-[7.5px] text-[#7F8B85] leading-tight font-mono-code">
                        <div>SCAN TO VERIFY</div>
                        <div>HASH: 7F4A...B902</div>
                      </div>
                    </div>
                    <div class="text-right">
                      <div class="text-[9px] font-black text-[#D6B66C]">ABES EC DEAN</div>
                      <div class="text-[7px] text-[#7F8B85]">DIGITALLY SIGNED</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Card Controls & Studio Photo Enhancer Toggles -->
            <div class="flex flex-wrap items-center justify-center gap-2 pt-1 w-full max-w-[520px]">
              <!-- Toggle Original vs AI Enhanced -->
              <div class="flex items-center gap-1 p-1 rounded-xl bg-white/[0.04] border border-white/[0.08] text-xs">
                <button onclick="setCardPhotoFilter('enhanced')" id="btn-photo-enhanced" class="px-2.5 py-1 rounded-lg bg-[#9875FF] text-white font-bold text-[11px] transition shadow">
                  ✨ AI Studio Enhanced
                </button>
                <button onclick="setCardPhotoFilter('original')" id="btn-photo-original" class="px-2.5 py-1 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[11px] transition">
                  Original Photo
                </button>
              </div>

              <!-- Photo Upload Input -->
              <input type="file" id="id-photo-upload-input" accept="image/jpeg,image/png,image/webp" class="hidden" onchange="handleIdentityPhotoUpload(event)" />
              <button onclick="document.getElementById('id-photo-upload-input').click()" class="btn-gold px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5">
                <span>📷</span><span data-i18n="upload_new_photo">Upload Photo</span>
              </button>

              <button onclick="recalculateStudentStrengths()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-[#51D6A0] hover:bg-[#51D6A0]/15 flex items-center gap-1.5">
                <span>⚡</span><span data-i18n="reanalyze_ai">Re-analyze Strengths</span>
              </button>
            </div>
          </div>

          <!-- Right: AI-POWERED "YOUR STRENGTHS" ANALYSIS -->
          <div class="lg:col-span-6 space-y-4">
            <div class="p-4 rounded-2xl bg-white/[0.02] border border-white/[0.08] space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <span class="text-base">🧠</span>
                  <h3 class="text-sm font-black text-white uppercase tracking-wide" data-i18n="your_strengths_title">Your Strengths &amp; AI Analysis</h3>
                </div>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-[#9875FF]/20 text-[#9875FF] font-mono-code font-bold">ANALYZED FROM STUDENT PROFILE</span>
              </div>
              <p class="text-xs text-[#7F8B85]" data-i18n="strengths_desc">
                AI evaluates voluntary student inputs (skills, solved problems, hackathon projects, academic records) to reveal verified abilities and growth pathways.
              </p>

              <!-- Strengths Grid -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs pt-1" id="strengths-badges-container">
                <!-- 1. Key Strengths -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#D6B66C] font-bold text-[11px] flex items-center gap-1"><span>⚡</span> Key Strengths</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code">AI RATED 9.4</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-key">Fast Algorithmic Modeling, Structured Logic, Prompt Engineering</p>
                </div>

                <!-- 2. Technical Strengths -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#48B8FF] font-bold text-[11px] flex items-center gap-1"><span>💻</span> Technical Strengths</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F0D28B] font-mono-code">VERIFIED</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-tech">Python, C++, PyTorch, React, SQLite, DSA</p>
                </div>

                <!-- 3. Creative Abilities -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#9875FF] font-bold text-[11px] flex items-center gap-1"><span>🎨</span> Creative Abilities</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#9875FF]/20 text-[#9875FF] font-mono-code">AI GENERATED</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-creative">Futuristic UI/UX Prototyping, Clean Design Systems</p>
                </div>

                <!-- 4. Problem-Solving -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#51D6A0] font-bold text-[11px] flex items-center gap-1"><span>🧩</span> Problem Solving</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code">HIGH ACCURACY</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-problem">Dynamic Programming, Binary Trees, Sliding Window</p>
                </div>

                <!-- 5. Leadership Potential -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-orange-400 font-bold text-[11px] flex items-center gap-1"><span>👑</span> Leadership &amp; Team</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F0D28B] font-mono-code">CAMPUS LEAD</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-leadership">Hackathon Project Coordination, Code Review Guidance</p>
                </div>

                <!-- 6. Communication -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-cyan-300 font-bold text-[11px] flex items-center gap-1"><span>🗣️</span> Communication</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-cyan-400/20 text-cyan-300 font-mono-code">TRILINGUAL</span>
                  </div>
                  <p class="text-[11px] text-white font-medium" id="str-comm">Fluent Technical English, Hindi, &amp; Bengali Communication</p>
                </div>
              </div>

              <!-- Growth Opportunities Section -->
              <div class="p-3 rounded-xl bg-[#F0D28B]/10 border border-[#F0D28B]/25 text-xs space-y-1">
                <div class="flex items-center justify-between">
                  <strong class="text-[#F0D28B] flex items-center gap-1.5 font-bold">
                    <span>🚀</span><span>Growth &amp; Career Opportunities</span>
                  </strong>
                  <span class="text-[9px] text-[#7F8B85] font-mono-code">4-YEAR ROADMAP</span>
                </div>
                <p class="text-[11px] text-[#E8DEC0]" id="str-growth">
                  Target 150+ LeetCode DSA milestone before Sem 3, publish 1 open-source AI agent, and target 8.80+ SGPA for Tier-1 placements.
                </p>
              </div>

              <div class="flex items-center justify-between pt-1 text-[10px] text-[#7F8B85]">
                <span>✓ Verified credentials pulled from student database</span>
                <button onclick="switchTab('settings'); switchSettingsCategory('profile');" class="text-[#D6B66C] hover:underline font-bold">
                  Edit Skills in Profile →
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>
'''
