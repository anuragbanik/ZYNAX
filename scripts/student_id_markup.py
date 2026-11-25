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
                        <div class="text-[11px] font-black tracking-wider text-white uppercase" id="card-college-name">CAMPUS DIGITAL IDENTITY</div>
                        <div class="text-[8px] text-[#7F8B85] font-mono-code" id="card-college-sub">VERIFIED STUDENT ID · SMART PASS</div>
                      </div>
                    </div>
                    <div class="text-right">
                      <span class="text-[9px] px-1.5 py-0.5 rounded bg-[#51D6A0]/15 text-[#51D6A0] font-mono-code font-bold" id="card-year-badge">ACTIVE</span>
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
                          <span id="card-photo-fallback" class="font-black text-2xl text-[#D6B66C]">ST</span>
                        </div>
                      </div>
                      <div id="card-photo-badge" class="absolute -bottom-1 -right-1 px-1.5 py-0.5 rounded bg-[#9875FF] text-[8px] font-bold text-white shadow">
                        ENHANCED
                      </div>
                    </div>

                    <!-- Details -->
                    <div class="space-y-1 flex-1 min-w-0">
                      <div class="flex items-center justify-between">
                        <h3 class="text-base font-black text-white truncate" id="card-display-name">Student Name</h3>
                        <div class="id-chip-gold flex-shrink-0" title="Smart NFC Microchip"></div>
                      </div>
                      <div class="text-[11px] font-mono-code text-[#D6B66C] font-bold tracking-wide" id="card-display-roll">
                        Roll No Pending
                      </div>
                      <div class="text-[10px] text-[#C4D0C9] truncate font-medium" id="card-display-branch">
                        Program / Department
                      </div>
                      <div class="text-[9px] text-[#7F8B85] flex items-center gap-2">
                        <span id="card-display-sec">Section &amp; Year</span>
                      </div>
                      <div class="flex items-center gap-1.5 pt-1">
                        <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F5F5F5] font-mono-code" id="card-tag-badge">STUDENT</span>
                        <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/15 text-[#51D6A0] font-mono-code" id="card-sgpa-badge">ACADEMIC PASS</span>
                      </div>
                    </div>
                  </div>

                  <!-- Footer: Barcode & Digital Signature -->
                  <div class="pt-2 border-t border-white/[0.08] flex items-center justify-between">
                    <div class="space-y-0.5">
                      <div class="w-36 h-4 barcode-lines rounded-sm"></div>
                      <div class="text-[7px] text-[#7F8B85] font-mono-code tracking-widest" id="card-barcode-str">ZYNAX-PASS-VERIFIED</div>
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
                    <div class="flex items-center gap-1.5">
                      <span class="text-xs">🪪</span>
                      <span class="text-[10px] font-black uppercase text-[#D6B66C] tracking-wider">STUDENT PROFILE &amp; CONTACT PASS</span>
                    </div>
                    <span class="text-[8px] px-2 py-0.5 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code font-bold">
                      VERIFIED RECORD
                    </span>
                  </div>

                  <!-- Middle: Comprehensive Contact, Links, and Academic Info -->
                  <div class="grid grid-cols-2 gap-3 py-1.5 text-[9px]">
                    <!-- Left Column: Academic & Contact -->
                    <div class="space-y-1">
                      <span class="text-[#7F8B85] block font-bold">STUDENT CONTACT:</span>
                      <p class="text-white font-mono-code truncate" id="card-back-email">Not provided</p>
                      <p class="text-[#D6B66C] font-mono-code" id="card-back-phone">Not provided</p>
                      
                      <span class="text-[#7F8B85] block font-bold pt-1">CAMPUS RESIDENCE:</span>
                      <p class="text-white truncate" id="card-back-residence">Campus / Local Residency</p>

                      <span class="text-[#7F8B85] block font-bold pt-1">BLOOD GROUP &amp; MEDICAL:</span>
                      <p class="text-[#51D6A0] font-mono-code" id="card-back-blood">Not recorded</p>
                    </div>

                    <!-- Right Column: Student Links & Credentials -->
                    <div class="space-y-1">
                      <span class="text-[#7F8B85] block font-bold">VERIFIED LINKS &amp; SOCIAL:</span>
                      <a id="card-back-github" href="#" target="_blank" class="text-[#48B8FF] font-mono-code hover:underline block truncate">
                        🔗 Add GitHub in Profile
                      </a>
                      <p class="text-white/80 font-mono-code truncate" id="card-back-linkedin">💼 Add LinkedIn in Profile</p>

                      <span class="text-[#7F8B85] block font-bold pt-1">ACADEMIC STANDING:</span>
                      <p class="text-[#D6B66C] font-mono-code" id="card-back-sgpa">Target SGPA: Not set</p>
                      <p class="text-white/80 font-mono-code" id="card-back-lib">Library ID: Not set</p>
                    </div>
                  </div>

                  <!-- QR Code & Official Stamp -->
                  <div class="pt-2 border-t border-white/[0.08] flex items-center justify-between">
                    <div class="flex items-center gap-2">
                      <div class="w-9 h-9 rounded bg-white p-0.5 flex items-center justify-center">
                        <svg class="w-full h-full text-black" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M2 2h8v8H2V2zm2 2v4h4V4H4zm10-2h8v8h-8V2zm2 2v4h4V4h-4zM2 14h8v8H2v-8zm2 2v4h4v-4H4zm14 0h4v4h-4v-4zm-4 4h4v4h-4v-4zm4-4v-4h-4v4h4zm-4-4h4V6h-4v4z"/>
                        </svg>
                      </div>
                      <div class="text-[7.5px] text-[#7F8B85] leading-tight font-mono-code">
                        <div>DIGITAL HASH</div>
                        <div class="text-white/80" id="card-back-hash">SHA-256 · VERIFIED</div>
                      </div>
                    </div>
                    <div class="text-right">
                      <div class="text-[9px] font-black text-[#D6B66C]">CAMPUS REGISTRAR</div>
                      <div class="text-[7px] text-[#7F8B85]">DIGITALLY SIGNED PASS</div>
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
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code">STUDENT INPUT</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-key">Not added yet. Click &quot;Edit Skills&quot; to add your strengths.</p>
                </div>

                <!-- 2. Technical Strengths -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#48B8FF] font-bold text-[11px] flex items-center gap-1"><span>💻</span> Technical Strengths</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F0D28B] font-mono-code">INDIVIDUAL</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-tech">Not added yet. Add languages and frameworks.</p>
                </div>

                <!-- 3. Creative Abilities -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#9875FF] font-bold text-[11px] flex items-center gap-1"><span>🎨</span> Creative Abilities</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#9875FF]/20 text-[#9875FF] font-mono-code">STUDENT INPUT</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-creative">Not added yet. Add design and creative tools.</p>
                </div>

                <!-- 4. Problem-Solving -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-[#51D6A0] font-bold text-[11px] flex items-center gap-1"><span>🧩</span> Problem Solving</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-[#51D6A0]/20 text-[#51D6A0] font-mono-code">INDIVIDUAL</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-problem">Not added yet. Add topics and algorithms practiced.</p>
                </div>

                <!-- 5. Leadership Potential -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-orange-400 font-bold text-[11px] flex items-center gap-1"><span>👑</span> Leadership &amp; Team</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-white/[0.06] text-[#F0D28B] font-mono-code">STUDENT INPUT</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-leadership">Not added yet. Add clubs, initiatives, or roles.</p>
                </div>

                <!-- 6. Communication -->
                <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] space-y-1">
                  <div class="flex items-center justify-between">
                    <span class="text-cyan-300 font-bold text-[11px] flex items-center gap-1"><span>🗣️</span> Communication</span>
                    <span class="text-[8px] px-1.5 py-0.2 rounded bg-cyan-400/20 text-cyan-300 font-mono-code">STUDENT INPUT</span>
                  </div>
                  <p class="text-[11px] text-[#A6B2AC]" id="str-comm">Not added yet. Add presentation or writing skills.</p>
                </div>
              </div>

              <!-- Growth Opportunities Section -->
              <div class="p-3 rounded-xl bg-[#F0D28B]/10 border border-[#F0D28B]/25 text-xs space-y-1">
                <div class="flex items-center justify-between">
                  <strong class="text-[#F0D28B] flex items-center gap-1.5 font-bold">
                    <span>🚀</span><span>Growth &amp; Career Opportunities</span>
                  </strong>
                  <span class="text-[9px] text-[#7F8B85] font-mono-code">PERSONAL ROADMAP</span>
                </div>
                <p class="text-[11px] text-[#E8DEC0]" id="str-growth">
                  Add your target semester goals, projects, and career milestones in Settings to personalize your AI companion.
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
