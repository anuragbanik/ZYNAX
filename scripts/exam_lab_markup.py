# -*- coding: utf-8 -*-
"""
Markup for ABES Exam Lab & PYQ Intelligence Ecosystem
Integrates:
1. ABES PYQ Vault (Upload PDF/JPG/PNG, text extraction, OCR, subject organization, metadata editing)
2. Real ABES PYQ Pattern Analysis (Repeated questions, unit distribution, topic ranking, marks breakdown)
3. Marks-Wise Question Bank (2-mark, 4-mark, 10-mark with step-wise solutions & marking schemes)
4. Four Complete Mock Papers for Every Subject (Pattern Practice, Important Qs, Mixed Difficulty, Final Revision)
5. PYQ Source Verification System ([VERIFIED UPLOADED PYQ], [AI-GENERATED], [REPEATED PYQ TOPIC], [AI-SUGGESTED])
6. Exam Preparation Tracker & Personalized ZYNAX AI Exam Coach
7. Optional Voice & Camera Exam Mode with Pre-Test Setup
8. Transparent Examination Integrity System (fullscreen, tab switch detection, autosave, auto-submit on threshold)
9. ZYNAX Exam Arena — ABES Student Leaderboard
"""

EXAM_LAB_HTML = r'''
    <!-- =================================================================
         TAB 7: ZYNAX ABES EXAM LAB + PYQ INTELLIGENCE ECOSYSTEM
         ================================================================= -->
    <section id="tab-quiz" class="tab-content hidden space-y-6">
      <!-- Exam Lab Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-white/[0.08]">
        <div>
          <div class="flex items-center gap-2">
            <h2 class="text-xl font-black text-white flex items-center gap-2">
              <span>⚔️ ABES EXAM LAB</span>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-[#9875FF]/20 text-[#9875FF] font-mono-code font-bold">PYQ INTELLIGENCE</span>
            </h2>
            <span class="text-[9px] px-2 py-0.5 rounded-full bg-[#D6B66C]/20 text-[#F0D28B] font-bold">AKTU Syllabus Aligned</span>
          </div>
          <p class="text-xs text-[#7F8B85]">Authentic previous-year paper vault, pattern analysis, 3-tier question banks, 4 mock papers, and AI exam coach.</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="openPreExamSetupModal('paper1')" class="btn-purple px-4 py-2 rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
            <span>⚔️</span><span>Start Official Mock Exam</span>
          </button>
        </div>
      </div>

      <!-- Sub-Navigation Pills for Exam Lab -->
      <div class="flex items-center gap-1.5 overflow-x-auto py-1 no-scrollbar border-b border-white/[0.06]">
        <button onclick="switchExamLabTab('vault')" id="elab-tab-vault" class="elab-sub-pill active px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition">
          <span>📚</span><span>PYQ Vault</span>
        </button>
        <button onclick="switchExamLabTab('analysis')" id="elab-tab-analysis" class="elab-sub-pill px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition text-[#87928B] hover:text-white">
          <span>📊</span><span>Pattern Analysis</span>
        </button>
        <button onclick="switchExamLabTab('bank')" id="elab-tab-bank" class="elab-sub-pill px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition text-[#87928B] hover:text-white">
          <span>📑</span><span>Question Bank (2m/4m/10m)</span>
        </button>
        <button onclick="switchExamLabTab('mock')" id="elab-tab-mock" class="elab-sub-pill px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition text-[#87928B] hover:text-white">
          <span>📝</span><span>4 Complete Mock Papers</span>
        </button>
        <button onclick="switchExamLabTab('tracker')" id="elab-tab-tracker" class="elab-sub-pill px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition text-[#87928B] hover:text-white">
          <span>📈</span><span>Exam Tracker &amp; AI Coach</span>
        </button>
        <button onclick="switchExamLabTab('leaderboard')" id="elab-tab-leaderboard" class="elab-sub-pill px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition text-[#87928B] hover:text-white">
          <span>🏆</span><span>ABES Leaderboard</span>
        </button>
      </div>

      <!-- ================= 1. ABES PYQ VAULT ================= -->
      <div id="elab-view-vault" class="space-y-5">
        <!-- Subject Selector & Filter -->
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div class="flex items-center gap-1.5 overflow-x-auto">
            <button onclick="setVaultSubject('phys')" id="vsub-phys" class="px-3 py-1 rounded-lg text-xs font-bold bg-[#D6B66C] text-black">Physics (KAS-101T)</button>
            <button onclick="setVaultSubject('math')" id="vsub-math" class="px-3 py-1 rounded-lg text-xs font-semibold glass-card text-[#87928B] hover:text-white">Maths (KAS-103T)</button>
            <button onclick="setVaultSubject('elec')" id="vsub-elec" class="px-3 py-1 rounded-lg text-xs font-semibold glass-card text-[#87928B] hover:text-white">Electronics (KEE-101T)</button>
            <button onclick="setVaultSubject('prog')" id="vsub-prog" class="px-3 py-1 rounded-lg text-xs font-semibold glass-card text-[#87928B] hover:text-white">Python / PPS (KCS-101T)</button>
          </div>
          <span class="text-[11px] text-[#51D6A0] font-mono-code font-bold">4 Verified Papers In Vault</span>
        </div>

        <!-- Upload Dropzone -->
        <div class="p-6 rounded-2xl ref-card border-2 border-dashed border-[#D6B66C]/40 text-center space-y-3 relative overflow-hidden group hover:border-[#D6B66C] transition">
          <input type="file" id="pyq-file-upload" accept=".pdf,image/jpeg,image/png" multiple class="hidden" onchange="handlePyqFiles(event)" />
          <div class="w-12 h-12 rounded-2xl bg-[#D6B66C]/10 text-[#D6B66C] flex items-center justify-center text-2xl mx-auto">📄</div>
          <div>
            <h3 class="text-sm font-black text-white">Upload Subject Previous-Year Question Papers</h3>
            <p class="text-xs text-[#7F8B85] mt-1">Supports PDF, JPG, PNG, and scanned examination papers. AI automatically extracts questions, marks allocation, and exam sessions.</p>
          </div>
          <div class="flex justify-center gap-2">
            <button onclick="document.getElementById('pyq-file-upload').click()" class="btn-gold px-4 py-2 rounded-xl text-xs font-bold">
              Select Files to Upload
            </button>
          </div>
          <!-- Upload Status Indicator -->
          <div id="pyq-upload-progress" class="hidden max-w-sm mx-auto space-y-1.5 pt-2">
            <div class="flex justify-between text-[10px] text-[#D6B66C]">
              <span id="pyq-upload-filename">Processing file...</span>
              <span id="pyq-upload-pct">100%</span>
            </div>
            <div class="w-full h-1.5 bg-white/10 rounded-full overflow-hidden">
              <div id="pyq-upload-bar" class="h-full bg-gradient-to-r from-[#D6B66C] to-[#51D6A0] w-full"></div>
            </div>
          </div>
        </div>

        <!-- Document Library Cards Grid -->
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-bold text-white uppercase tracking-wider">Verified Documents in Vault</h3>
            <span class="text-[10px] text-[#7F8B85]">Traceable to authentic ABES / AKTU examinations</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3" id="pyq-documents-container">
            <!-- Dynamically populated or pre-loaded papers -->
          </div>
        </div>
      </div>

      <!-- ================= 2. REAL ABES PYQ PATTERN ANALYSIS ================= -->
      <div id="elab-view-analysis" class="space-y-5 hidden">
        <!-- Frequency Insights Overview -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
          <div class="ref-card p-3 text-center">
            <span class="text-[9px] font-bold text-[#87928B] uppercase block">REPEATED TOPICS</span>
            <div class="text-xl font-black text-[#51D6A0] my-0.5">8 Topics</div>
            <span class="text-[9px] text-[#51D6A0]">Appeared &gt;= 2x</span>
          </div>
          <div class="ref-card p-3 text-center">
            <span class="text-[9px] font-bold text-[#87928B] uppercase block">HIGHEST WEIGHTAGE</span>
            <div class="text-xl font-black text-[#D6B66C] my-0.5">Unit 3 (26%)</div>
            <span class="text-[9px] text-[#87928B]">Quantum Mechanics</span>
          </div>
          <div class="ref-card p-3 text-center">
            <span class="text-[9px] font-bold text-[#87928B] uppercase block">NUMERICAL SHARE</span>
            <div class="text-xl font-black text-[#48B8FF] my-0.5">32% Marks</div>
            <span class="text-[9px] text-[#48B8FF]">Formula heavy</span>
          </div>
          <div class="ref-card p-3 text-center">
            <span class="text-[9px] font-bold text-[#87928B] uppercase block">TOP REPEATED QUESTION</span>
            <div class="text-xl font-black text-[#9875FF] my-0.5">3 Times</div>
            <span class="text-[9px] text-[#9875FF]">Compton Effect</span>
          </div>
        </div>

        <!-- Repeated Questions Table -->
        <div class="ref-card p-4 space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <h3 class="text-sm font-black text-white flex items-center gap-2">
              <span>🔁 Verified Repeated Questions &amp; Derivations</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-[#9875FF]/20 text-[#9875FF]">Authentic Evidence</span>
            </h3>
            <span class="text-[10px] text-[#7F8B85]">Source verified from uploaded papers</span>
          </div>
          <div class="space-y-2 text-xs">
            <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-red-500/20 text-red-400">Repeated 3x</span>
                  <span class="text-[9px] px-2 py-0.5 rounded bg-white/5 text-[#D6B66C] font-mono-code">10 Marks</span>
                  <span class="text-[9px] text-[#7F8B85]">Unit 1 · Relativistic Mechanics</span>
                </div>
                <strong class="text-white block">Explain Compton Effect and derive expression for Compton Shift &Delta;&lambda; = (h/m₀c)(1 - cos&theta;).</strong>
                <span class="text-[10px] text-[#8F9B94] block">Appeared in: 2024 Pre-University Q2 · 2023 End-Sem Q3b · 2022 MT-02 Q4a</span>
              </div>
              <button onclick="viewQuestionDetails('rep1')" class="btn-gold px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap">View Solution &amp; Scheme</button>
            </div>

            <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-red-500/20 text-red-400">Repeated 3x</span>
                  <span class="text-[9px] px-2 py-0.5 rounded bg-white/5 text-[#D6B66C] font-mono-code">4 Marks</span>
                  <span class="text-[9px] text-[#7F8B85]">Unit 3 · Quantum Mechanics</span>
                </div>
                <strong class="text-white block">Derive Schrödinger's Time-Independent Wave Equation for a free particle in 1D.</strong>
                <span class="text-[10px] text-[#8F9B94] block">Appeared in: 2024 End-Sem Q1e · 2023 PUT Q2c · 2022 End-Sem Q3</span>
              </div>
              <button onclick="viewQuestionDetails('rep2')" class="btn-gold px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap">View Solution &amp; Scheme</button>
            </div>

            <div class="p-3 rounded-xl bg-white/[0.03] border border-white/[0.06] flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-orange-500/20 text-orange-400">Repeated 2x</span>
                  <span class="text-[9px] px-2 py-0.5 rounded bg-white/5 text-[#D6B66C] font-mono-code">2 Marks</span>
                  <span class="text-[9px] text-[#7F8B85]">Unit 4 · Superconductors</span>
                </div>
                <strong class="text-white block">Differentiate between Type-I and Type-II Superconductors based on Meissner effect.</strong>
                <span class="text-[10px] text-[#8F9B94] block">Appeared in: 2024 MT-02 Q1c · 2023 End-Sem Q1b</span>
              </div>
              <button onclick="viewQuestionDetails('rep3')" class="btn-gold px-3 py-1 rounded-lg text-xs font-bold whitespace-nowrap">View Solution &amp; Scheme</button>
            </div>
          </div>
        </div>

        <!-- Unit Distribution & Marks Breakdown -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <!-- Unit Distribution Chart -->
          <div class="ref-card p-4 space-y-3">
            <h3 class="font-bold text-white flex items-center justify-between">
              <span>📊 Unit-Wise Weightage Distribution</span>
              <span class="text-[10px] text-[#51D6A0]">100% Syllabus</span>
            </h3>
            <div class="space-y-2">
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-white">Unit 3: Quantum Mechanics</span>
                  <span class="text-[#51D6A0] font-bold">26% (26 Marks)</span>
                </div>
                <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#51D6A0] w-[26%]"></div></div>
              </div>
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-white">Unit 1: Relativistic Mechanics</span>
                  <span class="text-[#D6B66C] font-bold">22% (22 Marks)</span>
                </div>
                <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#D6B66C] w-[22%]"></div></div>
              </div>
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-white">Unit 2: Electromagnetic Wave Theory</span>
                  <span class="text-[#48B8FF] font-bold">20% (20 Marks)</span>
                </div>
                <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#48B8FF] w-[20%]"></div></div>
              </div>
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-white">Unit 4: Wave Optics &amp; Lasers</span>
                  <span class="text-[#9875FF] font-bold">18% (18 Marks)</span>
                </div>
                <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#9875FF] w-[18%]"></div></div>
              </div>
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-white">Unit 5: Fiber Optics &amp; Superconductors</span>
                  <span class="text-orange-400 font-bold">14% (14 Marks)</span>
                </div>
                <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-orange-400 w-[14%]"></div></div>
              </div>
            </div>
          </div>

          <!-- Question Format Patterns -->
          <div class="ref-card p-4 space-y-3">
            <h3 class="font-bold text-white flex items-center justify-between">
              <span>🎯 ABES Exam Question Patterns</span>
              <span class="text-[10px] text-[#D6B66C]">AKTU Standard</span>
            </h3>
            <div class="space-y-2">
              <div class="p-2.5 rounded-xl bg-white/[0.03] border border-white/[0.06]">
                <strong class="text-white text-xs block">Section A: 2-Mark Short Questions (10 Qs = 20m)</strong>
                <p class="text-[10px] text-[#7F8B85]">Definitions (Meissner effect, Numerical aperture), formula statements (Lorentz contraction, de-Broglie), and 1-line conceptual deductions.</p>
              </div>
              <div class="p-2.5 rounded-xl bg-white/[0.03] border border-white/[0.06]">
                <strong class="text-white text-xs block">Section B: 4-Mark Medium / Short Derivations (5 Qs = 20m)</strong>
                <p class="text-[10px] text-[#7F8B85]">Short derivations (Poynting theorem, phase vs group velocity) and direct numerical problems with SI units.</p>
              </div>
              <div class="p-2.5 rounded-xl bg-white/[0.03] border border-white/[0.06]">
                <strong class="text-white text-xs block">Section C: 10-Mark Comprehensive Theory (5 Qs = 50m)</strong>
                <p class="text-[10px] text-[#7F8B85]">Full theoretical derivations with labeled ray/field diagrams, physical significance, and multi-part numerical extensions.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= 3. MARKS-WISE QUESTION BANK ================= -->
      <div id="elab-view-bank" class="space-y-4 hidden">
        <!-- Tier Switcher -->
        <div class="flex items-center gap-2 border-b border-white/[0.08] pb-2">
          <button onclick="setBankTier('2m')" id="bank-btn-2m" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-[#D6B66C] text-black">
            2-Mark Question Bank (Definitions &amp; Formulas)
          </button>
          <button onclick="setBankTier('4m')" id="bank-btn-4m" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold glass-card text-[#87928B] hover:text-white">
            4-Mark Question Bank (Derivations &amp; Numericals)
          </button>
          <button onclick="setBankTier('10m')" id="bank-btn-10m" class="px-3.5 py-1.5 rounded-xl text-xs font-semibold glass-card text-[#87928B] hover:text-white">
            Long-Answer Question Bank (10-Mark Comprehensive)
          </button>
        </div>

        <!-- Question List Container -->
        <div id="qbank-list-container" class="space-y-3">
          <!-- Dynamically populated via JS -->
        </div>
      </div>

      <!-- ================= 4. FOUR COMPLETE MOCK PAPERS ================= -->
      <div id="elab-view-mock" class="space-y-5 hidden">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-black text-white">📝 Four Complete Practice Papers for Engineering Physics</h3>
            <span class="text-xs text-[#7F8B85]">Each paper follows verified ABES sessional &amp; end-semester paper structures.</span>
          </div>
          <button onclick="openPaperCustomizer()" class="glass-card px-3 py-1.5 rounded-xl text-xs font-bold text-[#D6B66C]">
            ⚙️ Customize &amp; Regenerate
          </button>
        </div>

        <!-- 4 Default Paper Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs" id="mock-papers-grid">
          <!-- Dynamically rendered via renderMockPapers() -->
        </div>
      </div>

      <!-- ================= 5. EXAM PREPARATION TRACKER & AI COACH ================= -->
      <div id="elab-view-tracker" class="space-y-5 hidden">
        <!-- Progress Summary -->
        <div class="ref-card p-5 space-y-4">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
            <div>
              <span class="text-[10px] font-mono-code text-[#51D6A0] uppercase font-bold">PHYSICS (KAS-101T) STATUS</span>
              <h3 class="text-lg font-black text-white">Subject Examination Readiness: 68%</h3>
              <p class="text-xs text-[#7F8B85]">Papers Generated: 4/4 · Papers Attempted: 2/4 · MT-02 Physics Exam in 12 days</p>
            </div>
            <span class="text-sm font-black text-[#D6B66C] px-3 py-1 rounded-xl bg-[#D6B66C]/10 border border-[#D6B66C]/30">On Track for SGPA 8.8+</span>
          </div>

          <!-- Weak & Strong Units -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs pt-2">
            <div class="p-3 rounded-xl bg-red-500/10 border border-red-500/20 space-y-1">
              <strong class="text-red-400 text-xs block">⚠️ Weak Units (Identified from actual attempts)</strong>
              <p class="text-[11px] text-[#E0E7E4]">Unit 3 (Quantum Mechanics) — Numerical solutions for de-Broglie wavelength &amp; particle-in-a-box had an accuracy of 58%.</p>
            </div>
            <div class="p-3 rounded-xl bg-[#51D6A0]/10 border border-[#51D6A0]/20 space-y-1">
              <strong class="text-[#51D6A0] text-xs block">✓ Strong Units (Verified high performance)</strong>
              <p class="text-[11px] text-[#E0E7E4]">Unit 1 (Relativistic Mechanics) — Compton effect &amp; Lorentz transformations scored 92% accuracy.</p>
            </div>
          </div>
        </div>

        <!-- AI Exam Coach Chat & Quick Queries -->
        <div class="ref-card p-5 space-y-4">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <h3 class="text-sm font-black text-white flex items-center gap-2">
              <span>🤖 Personalized ZYNAX AI Exam Coach</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-[#9875FF]/20 text-[#9875FF]">Connected with 4-Year Memory</span>
            </h3>
            <span class="text-[10px] text-[#7F8B85]">Roll: 2026ABES042</span>
          </div>

          <!-- 8 Quick Student Query Buttons -->
          <div class="space-y-1.5">
            <span class="text-[10px] font-bold text-[#F0D28B] uppercase block">Quick Student Queries</span>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2 text-[10px]">
              <button onclick="askCoach('Which Physics PYQs should I revise?')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                🔍 <em>Which Physics PYQs should I revise?</em>
              </button>
              <button onclick="askCoach('Show my repeated 2-mark questions.')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                🔁 <em>Show my repeated 2-mark questions.</em>
              </button>
              <button onclick="askCoach('Which units am I weak in?')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                ⚠️ <em>Which units am I weak in?</em>
              </button>
              <button onclick="askCoach('Compare my last two mock tests.')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                📊 <em>Compare my last two mock tests.</em>
              </button>
              <button onclick="askCoach('Prepare a revision plan before my examination.')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                📅 <em>Prepare a revision plan before exam.</em>
              </button>
              <button onclick="askCoach('Generate another 4-mark practice set.')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                🎯 <em>Generate another 4-mark practice set.</em>
              </button>
              <button onclick="askCoach('Which mock paper should I attempt next?')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                📝 <em>Which mock paper should I attempt next?</em>
              </button>
              <button onclick="askCoach('Give me a final practice paper based on uploaded PYQs.')" class="p-2 rounded-xl glass-card text-left text-white hover:border-[#D6B66C] transition">
                🏁 <em>Final practice paper from PYQs.</em>
              </button>
            </div>
          </div>

          <!-- Coach Response Box -->
          <div id="coach-response-box" class="p-4 rounded-xl bg-black/50 border border-[#9875FF]/30 text-xs text-white leading-relaxed space-y-2">
            <div class="flex items-center gap-2 text-[#9875FF] font-bold">
              <span>🤖 AI Exam Coach:</span>
              <span class="text-[10px] text-[#8F9B94]">Based on your actual test history &amp; uploaded papers</span>
            </div>
            <p id="coach-response-text">
              Yo Anurag! For Engineering Physics MT-02, prioritize <strong>Unit 3 Quantum Mechanics</strong> where your numerical accuracy is currently 58%. The Compton Shift derivation appeared 3x in recent papers — review that first! Click any query above for tailored guidance.
            </p>
          </div>
        </div>
      </div>

      <!-- ================= 6. ZYNAX EXAM ARENA — ABES LEADERBOARD ================= -->
      <div id="elab-view-leaderboard" class="space-y-5 hidden">
        <!-- Leaderboard Header & Filters -->
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
          <div>
            <h3 class="text-sm font-black text-white flex items-center gap-2">
              <span>🏆 ZYNAX EXAM ARENA — ABES LEADERBOARD</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-[#D6B66C]/20 text-[#D6B66C]">Verified Students</span>
            </h3>
            <span class="text-xs text-[#7F8B85]">Subject-wise and overall examination performance rankings.</span>
          </div>
          <!-- Categories Filter -->
          <div class="flex items-center gap-1 overflow-x-auto text-xs">
            <button onclick="filterLeaderboard('daily')" id="lb-btn-daily" class="px-3 py-1 rounded-lg font-bold bg-[#D6B66C] text-black">Daily</button>
            <button onclick="filterLeaderboard('weekly')" id="lb-btn-weekly" class="px-3 py-1 rounded-lg font-semibold glass-card text-[#87928B] hover:text-white">Weekly</button>
            <button onclick="filterLeaderboard('physics')" id="lb-btn-physics" class="px-3 py-1 rounded-lg font-semibold glass-card text-[#87928B] hover:text-white">Physics</button>
            <button onclick="filterLeaderboard('overall')" id="lb-btn-overall" class="px-3 py-1 rounded-lg font-semibold glass-card text-[#87928B] hover:text-white">Overall</button>
          </div>
        </div>

        <!-- Top 3 Podium (Exact Specification) -->
        <div class="grid grid-cols-3 gap-2 sm:gap-4 max-w-xl mx-auto pt-6 pb-2 text-center items-end">
          <!-- 2nd Place Silver -->
          <div class="ref-card p-3 space-y-1 border-t-4 border-slate-300">
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-slate-300/20 text-slate-200 border border-slate-300 flex items-center justify-center font-bold text-sm mx-auto">
              PV
            </div>
            <strong class="text-white text-xs block truncate">Priya Verma</strong>
            <span class="text-[9px] text-[#7F8B85] block">CSE Sec B</span>
            <div class="text-xs font-mono-code font-bold text-slate-300">🥈 95.0%</div>
            <span class="text-[8px] text-[#8F9B94] block">14 Papers</span>
          </div>

          <!-- 1st Place Gold (Tall) -->
          <div class="ref-card p-4 space-y-1.5 border-t-4 border-[#D6B66C] shadow-[0_0_30px_rgba(214,182,108,0.2)] bg-gradient-to-b from-[#1E1911] to-[#121614]">
            <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-[#D6B66C]/20 text-[#D6B66C] border-2 border-[#D6B66C] flex items-center justify-center font-black text-base mx-auto">
              AS
            </div>
            <strong class="text-[#F0D28B] text-xs sm:text-sm block truncate font-black">Aditya Sharma</strong>
            <span class="text-[9px] text-[#D6B66C] block">CSE AI/ML Sec A</span>
            <div class="text-sm font-mono-code font-black text-[#D6B66C]">🥇 97.5%</div>
            <span class="text-[8px] text-[#8F9B94] block">16 Papers · Master</span>
          </div>

          <!-- 3rd Place Bronze -->
          <div class="ref-card p-3 space-y-1 border-t-4 border-amber-600">
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-amber-600/20 text-amber-500 border border-amber-600 flex items-center justify-center font-bold text-sm mx-auto">
              RG
            </div>
            <strong class="text-white text-xs block truncate">Rohit Gupta</strong>
            <span class="text-[9px] text-[#7F8B85] block">IT Sec A</span>
            <div class="text-xs font-mono-code font-bold text-amber-500">🥉 93.2%</div>
            <span class="text-[8px] text-[#8F9B94] block">13 Papers</span>
          </div>
        </div>

        <!-- Personal Ranking Card (Current User: Anurag Banik) -->
        <div class="p-3.5 rounded-2xl bg-gradient-to-r from-[#181D1A] via-[#141A17] to-[#181D1A] border border-[#51D6A0]/40 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
          <div class="flex items-center gap-3">
            <div id="lb-user-avatar" class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#51D6A0] to-[#9875FF] flex items-center justify-center text-xs font-black text-white border border-white/20 overflow-hidden">
              <span id="lb-user-initials">AB</span>
            </div>
            <div>
              <div class="flex items-center gap-2">
                <strong class="text-white text-sm" id="lb-user-name">Anurag Banik</strong>
                <span class="text-[9px] px-2 py-0.2 rounded-full bg-[#51D6A0]/20 text-[#51D6A0] font-bold">You (Rank #4)</span>
              </div>
              <span class="text-[10px] text-[#8F9B94]" id="lb-user-section">CSE (AI/ML) Sec A · ABES EC</span>
            </div>
          </div>
          <div class="flex items-center gap-4">
            <div class="text-right">
              <span class="text-[9px] text-[#717D77] block uppercase">Physics Avg</span>
              <span class="text-sm font-mono-code font-bold text-[#51D6A0]" id="lb-user-score">91.8%</span>
            </div>
            <div class="text-right">
              <span class="text-[9px] text-[#717D77] block uppercase">Completed</span>
              <span class="text-sm font-mono-code font-bold text-white" id="lb-user-papers">10 Papers</span>
            </div>
            <button onclick="toggleLeaderboardVisibility()" id="lb-optout-btn" class="px-3 py-1.5 rounded-xl glass-card text-[10px] text-[#D6B66C] font-semibold">
              Public: Active
            </button>
          </div>
        </div>

        <!-- Full Leaderboard Table -->
        <div class="ref-card overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <thead class="bg-white/[0.03] text-[#7F8B85] uppercase text-[10px] border-b border-white/[0.08]">
                <tr>
                  <th class="py-2.5 px-3">Rank</th>
                  <th class="py-2.5 px-3">Student</th>
                  <th class="py-2.5 px-3">Section</th>
                  <th class="py-2.5 px-3">Subject</th>
                  <th class="py-2.5 px-3 text-right">Score</th>
                  <th class="py-2.5 px-3 text-right">Accuracy</th>
                  <th class="py-2.5 px-3 text-right">Papers</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-white/[0.04]" id="leaderboard-table-body">
                <!-- Dynamically populated via renderLeaderboardTable() -->
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- ================= 7. PRE-TEST SETUP MODAL (VOICE & CAMERA OPTIONS) ================= -->
      <div id="pre-exam-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="ref-card max-w-lg w-full p-6 space-y-5 border border-[#9875FF]/40 shadow-2xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <div>
              <h3 class="text-sm font-black text-white flex items-center gap-2">
                <span>🛡️ Pre-Examination Setup &amp; Rules</span>
              </h3>
              <span class="text-[10px] text-[#7F8B85]" id="pre-exam-paper-name">Engineering Physics · MT-02 Simulation</span>
            </div>
            <button onclick="closePreExamModal()" class="text-white/60 hover:text-white text-lg font-bold">✕</button>
          </div>

          <div class="space-y-3 text-xs">
            <!-- Rules Explanation -->
            <div class="p-3 rounded-xl bg-white/[0.03] space-y-1.5 border border-white/[0.06]">
              <strong class="text-white block font-bold">📋 Transparent Examination Integrity Policy</strong>
              <ul class="text-[10px] text-[#8F9B94] space-y-1 list-disc pl-4">
                <li>Exam runs in secure full-screen mode.</li>
                <li>Switching browser tabs or minimizing the window logs an integrity warning.</li>
                <li>Maximum 3 warnings allowed before answers are secured and auto-submitted.</li>
                <li>All answers are continuously autosaved locally every 3 seconds.</li>
              </ul>
            </div>

            <!-- Permission 1: Voice Assistant -->
            <div class="p-3 rounded-xl ref-card flex items-center justify-between">
              <div>
                <strong class="text-white text-xs block">1. Voice-Based Accessibility Assistance</strong>
                <span class="text-[10px] text-[#7F8B85] block">Reads questions aloud and announces remaining time milestones. Never reveals answers.</span>
              </div>
              <input type="checkbox" id="setup-opt-voice" checked class="accent-[#9875FF] w-4 h-4 cursor-pointer" />
            </div>

            <!-- Permission 2: Camera Monitoring -->
            <div class="p-3 rounded-xl ref-card flex items-center justify-between">
              <div>
                <strong class="text-white text-xs block">2. Optional Camera-Based Examination Monitoring</strong>
                <span class="text-[10px] text-[#7F8B85] block">Displays a visible local camera proctor preview in the corner. Video is NEVER recorded or uploaded. You may keep camera OFF without penalty.</span>
              </div>
              <input type="checkbox" id="setup-opt-camera" class="accent-[#51D6A0] w-4 h-4 cursor-pointer" />
            </div>
          </div>

          <div class="flex justify-between gap-3 pt-2">
            <button onclick="closePreExamModal()" class="glass-card px-4 py-2 rounded-xl text-xs font-bold text-white flex-1">Cancel</button>
            <button onclick="launchExamSession()" class="btn-emerald px-5 py-2.5 rounded-xl text-xs font-bold flex-1 shadow-lg flex items-center justify-center gap-1.5">
              <span>🚀</span><span>Enter Fullscreen &amp; Start</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ================= 8. ACTIVE EXAM RUNNER CONTAINER ================= -->
      <div id="active-exam-container" class="hidden ref-card border-2 border-[#9875FF]/60 p-5 space-y-5 relative">
        <!-- Floating Local Proctor Camera Feed -->
        <div id="proctor-cam-box" class="hidden absolute top-4 right-4 z-20 w-32 h-24 rounded-xl overflow-hidden bg-black border-2 border-[#51D6A0] shadow-xl">
          <video id="proctor-video" autoplay playsinline class="w-full h-full object-cover"></video>
          <div class="absolute bottom-1 left-1 px-1.5 py-0.2 rounded bg-black/70 text-[8px] font-bold text-[#51D6A0] flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-[#51D6A0] animate-pulse"></span> Proctor Active
          </div>
          <button onclick="turnOffExamCamera()" class="absolute top-1 right-1 text-[9px] bg-red-500/80 text-white rounded px-1" title="Disable Camera">✕</button>
        </div>

        <!-- Exam Header -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pb-3 border-b border-white/[0.08]">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-[10px] px-2 py-0.5 rounded bg-red-500/20 text-red-400 font-bold uppercase tracking-wider">LIVE EXAM IN PROGRESS</span>
              <span class="text-[10px] text-[#51D6A0] font-mono-code" id="exam-autosave-indicator">✓ Autosaved</span>
            </div>
            <h3 class="text-base font-black text-white mt-1" id="active-exam-title">Engineering Physics · MT-02 Simulation</h3>
          </div>
          <!-- Live Timer -->
          <div class="text-right flex items-center gap-3">
            <div class="text-right">
              <span class="text-2xl font-mono-code font-black text-red-400" id="exam-timer-display">90:00</span>
              <span class="text-[9px] text-[#7F8B85] block">Time Remaining</span>
            </div>
            <button onclick="readCurrentQuestionVoice()" class="p-2 rounded-xl glass-card text-[#9875FF] hover:bg-[#9875FF]/20" title="Read Question Aloud">
              🔊
            </button>
          </div>
        </div>

        <!-- Warning Banner for Integrity -->
        <div id="exam-integrity-banner" class="hidden p-3 rounded-xl bg-red-500/15 border border-red-500/40 text-xs text-red-400 flex items-center justify-between">
          <span id="exam-integrity-msg">⚠️ Integrity Warning 1/3: Focus lost or tab switch detected.</span>
          <span class="text-[10px] text-white">Threshold: 3</span>
        </div>

        <!-- Question Body Area -->
        <div class="p-4 rounded-xl glass-card space-y-3">
          <div class="flex items-center justify-between text-xs">
            <span class="text-[#D6B66C] font-mono-code font-bold" id="exam-q-num">Question 1 of 10</span>
            <div class="flex items-center gap-2">
              <span class="text-[10px] px-2 py-0.5 rounded bg-[#9875FF]/20 text-[#9875FF] font-bold" id="exam-q-marks">[4 Marks]</span>
              <span class="text-[10px] text-[#51D6A0]" id="exam-q-source">[VERIFIED UPLOADED PYQ]</span>
            </div>
          </div>
          <h4 class="text-sm font-bold text-white leading-relaxed" id="exam-q-text">Loading question...</h4>

          <!-- Question Options / Answer Textarea -->
          <div id="exam-interactive-answer-area" class="space-y-2 pt-2">
            <!-- Rendered options or textarea -->
          </div>
        </div>

        <!-- Exam Controls -->
        <div class="flex justify-between items-center pt-2 flex-wrap gap-2">
          <button onclick="prevExamQ()" class="glass-card px-4 py-2 rounded-xl text-xs font-bold text-white">← Previous</button>
          <div class="flex items-center gap-2">
            <button onclick="nextExamQ()" class="btn-purple px-4 py-2 rounded-xl text-xs font-bold">Next Question →</button>
            <button onclick="submitExamNow(false)" class="btn-emerald px-5 py-2 rounded-xl text-xs font-bold shadow-lg">Submit Final Answers</button>
          </div>
        </div>
      </div>

      <!-- ================= 9. EXAM SCORECARD & INTEGRITY REPORT MODAL ================= -->
      <div id="exam-scorecard-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
        <div class="ref-card max-w-lg w-full p-6 space-y-4 border border-[#51D6A0]/40 shadow-2xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <h3 class="text-sm font-black text-white flex items-center gap-2">
              <span>🎯 Examination Evaluation &amp; Report</span>
            </h3>
            <button onclick="closeScorecardModal()" class="text-white/60 hover:text-white text-lg font-bold">✕</button>
          </div>

          <div class="text-center py-2 space-y-1">
            <span class="text-3xl font-mono-code font-black text-[#51D6A0]" id="scorecard-pct">85%</span>
            <p class="text-xs text-[#8F9B94]" id="scorecard-marks">Score: 36 / 42 Marks</p>
          </div>

          <div class="space-y-2 text-xs">
            <div class="p-3 rounded-xl bg-white/[0.03] space-y-1">
              <strong class="text-white block font-bold">Performance Feedback:</strong>
              <p class="text-[11px] text-[#A0ABA4]" id="scorecard-feedback">Outstanding command over Relativistic Mechanics derivations! Numerical accuracy in Quantum Mechanics needs 1 more revision session.</p>
            </div>
            <!-- Integrity Audit Log -->
            <div class="p-3 rounded-xl bg-white/[0.03] space-y-1">
              <strong class="text-white block font-bold">Integrity Events Audit:</strong>
              <div id="scorecard-integrity-log" class="text-[10px] text-[#7F8B85] space-y-0.5">
                <span>✓ 0 critical violations detected. Exam verified.</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex justify-end">
            <button onclick="closeScorecardModal()" class="btn-gold px-5 py-2 rounded-xl text-xs font-bold">Close &amp; View Updated Leaderboard</button>
          </div>
        </div>
      </div>

    </section>
'''
