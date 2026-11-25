# -*- coding: utf-8 -*-
"""
Premium Liquid Glass Student Authentication & Account Suite
Features:
- Dual-mode switch: "Sign In" vs. "Create Account"
- Liquid glass container with 3D tilt interaction & glowing metallic gold border
- Student Username/Email, Password, Confirm Password
- Show/Hide Password toggle with eye icon
- "Remember Me" session persistence
- "Forgot Password" security reset modal with simulated OTP verification
- Client-side cryptographic hash / secure localStorage credential store
- Seamless sync with APP.studentProfile without altering backend APIs
"""

AUTH_SYSTEM_HTML = r'''
    <!-- =================================================================
         PREMIUM LIQUID GLASS STUDENT AUTHENTICATION & ACCOUNT SUITE
         ================================================================= -->
    <section id="tab-auth" class="tab-content hidden space-y-8 py-4">
      
      <!-- Top Hero Welcome Banner -->
      <div class="liquid-glass-card p-6 sm:p-8 relative overflow-hidden">
        <div class="liquid-sheen-overlay"></div>
        <div class="flex flex-col lg:flex-row items-center justify-between gap-8 relative z-10">
          <div class="space-y-3 text-center lg:text-left max-w-xl">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#D6B66C]/15 border border-[#D6B66C]/30 text-xs font-mono-code font-bold text-[#D6B66C]">
              <span>🛡️</span><span>AKTU SECURE IDENTITY PASS · ZYNAX 3.5</span>
            </div>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight text-white">
              STUDENT ACCOUNT &amp;<br/>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#D6B66C] via-[#F0D28B] to-[#51D6A0]">
                CAMPUS CREDENTIALS
              </span>
            </h1>
            <p class="text-xs sm:text-sm text-[#87928B] leading-relaxed">
              Sign in to sync your verified attendance armor, daily timetable alerts, LeetCode arena streaks, and 4-Year career milestones. All credentials are encrypted locally in compliance with campus data privacy.
            </p>
            <div class="pt-2 flex flex-wrap gap-2.5 justify-center lg:justify-start">
              <button onclick="switchTab('dashboard')" class="btn-gold px-5 py-2.5 rounded-xl text-xs font-bold shadow-lg flex items-center gap-1.5">
                <span>⚡</span><span>Open Main Dashboard</span>
              </button>
              <button onclick="switchTab('settings')" class="glass-card px-4 py-2.5 rounded-xl text-xs font-bold text-[#D6B66C] flex items-center gap-1.5">
                <span>⚙️</span><span>Profile Settings</span>
              </button>
            </div>
          </div>

          <!-- 3D Floating ZYNAX Core Emblem -->
          <div class="flex flex-col items-center gap-3 flex-shrink-0">
            <div class="w-24 h-24 rounded-3xl p-[2.5px] bg-gradient-to-tr from-[#D6B66C] via-[#9875FF] to-[#48B8FF] shadow-2xl shadow-[#D6B66C]/25 hover:rotate-6 transition-transform duration-500">
              <div class="w-full h-full rounded-[22px] bg-[#0A0D0B] flex items-center justify-center font-black text-4xl text-transparent bg-clip-text bg-gradient-to-tr from-[#D6B66C] to-[#51D6A0]">
                Z
              </div>
            </div>
            <span class="text-[10px] text-[#D6B66C] font-mono-code tracking-widest uppercase font-bold">
              AKTU VERIFIED SYSTEM
            </span>
          </div>
        </div>
      </div>

      <!-- Main Liquid Glass Authentication Card -->
      <div class="max-w-xl mx-auto liquid-glass-card p-6 sm:p-9 space-y-6 relative" id="auth-main-card" onmousemove="handleAuthTilt(event)" onmouseleave="resetAuthTilt()">
        <div class="liquid-sheen-overlay"></div>

        <div class="relative z-10 space-y-5">
          <!-- Mode Switcher Tabs: Sign In vs Create Account -->
          <div class="flex p-1.5 rounded-2xl bg-black/50 border border-white/[0.08] relative">
            <button onclick="setAuthMode('signin')" id="auth-tab-signin" class="flex-1 py-2.5 rounded-xl text-xs font-bold text-black bg-[#D6B66C] shadow-lg transition-all">
              Sign In
            </button>
            <button onclick="setAuthMode('register')" id="auth-tab-register" class="flex-1 py-2.5 rounded-xl text-xs font-semibold text-[#87928B] hover:text-white transition-all">
              Create Account
            </button>
          </div>

          <!-- Form Header -->
          <div class="text-center space-y-1">
            <h2 class="text-2xl font-black text-white" id="auth-heading-text">Student Sign In</h2>
            <p class="text-xs text-[#7F8B85]" id="auth-sub-text">Enter your student credentials to access your ZYNAX companion.</p>
          </div>

          <!-- Alert / Validation Banner -->
          <div id="auth-alert-box" class="hidden p-3 rounded-xl border text-xs font-medium transition-all"></div>

          <!-- SIGN IN FORM VIEW -->
          <form id="form-signin" onsubmit="handleSignInSubmit(event)" class="space-y-4">
            <div>
              <label class="text-xs text-[#8E9A92] font-semibold block mb-1.5">Student Username or College Email</label>
              <div class="relative">
                <input type="text" id="signin-username" value="anurag.banik@abes.ac.in" required placeholder="e.g. 2026ABES042 or student@abes.ac.in" class="w-full px-4 py-3 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white placeholder-[#5C6660] focus:outline-none focus:border-[#D6B66C] transition" />
                <span class="absolute right-3.5 top-3 text-xs text-[#7F8B85]">👤</span>
              </div>
            </div>

            <div>
              <label class="text-xs text-[#8E9A92] font-semibold block mb-1.5">Student Password</label>
              <div class="relative">
                <input type="password" id="signin-password" value="Zynax2026!#" required placeholder="Enter your password" class="w-full px-4 py-3 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white placeholder-[#5C6660] focus:outline-none focus:border-[#D6B66C] transition pr-10" />
                <button type="button" onclick="togglePasswordVisibility('signin-password', this)" class="absolute right-3 top-3 text-xs text-[#7F8B85] hover:text-white transition" title="Show/Hide Password">
                  👁️
                </button>
              </div>
            </div>

            <!-- Remember Me & Forgot Password -->
            <div class="flex items-center justify-between text-xs pt-1">
              <label class="flex items-center gap-2 cursor-pointer select-none">
                <input type="checkbox" id="signin-remember" checked class="w-4 h-4 accent-[#D6B66C] rounded" />
                <span class="text-[#8E9A92]">Remember Me</span>
              </label>
              <button type="button" onclick="openForgotPasswordModal()" class="text-[#D6B66C] hover:underline font-bold">
                Forgot Password?
              </button>
            </div>

            <button type="submit" class="w-full btn-gold py-3 rounded-xl text-xs font-bold shadow-lg shadow-[#D6B66C]/20 hover:scale-[1.01] active:scale-95 transition flex items-center justify-center gap-2">
              <span>Sign In to ZYNAX</span>
              <span>→</span>
            </button>
          </form>

          <!-- CREATE ACCOUNT (REGISTER) FORM VIEW -->
          <form id="form-register" onsubmit="handleRegisterSubmit(event)" class="hidden space-y-4">
            <div>
              <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Student Full Name</label>
              <input type="text" id="reg-name" required placeholder="e.g. Anurag Banik" class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition" />
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label class="text-xs text-[#8E9A92] font-semibold block mb-1">College Email</label>
                <input type="email" id="reg-email" required placeholder="name@abes.ac.in" class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition" />
              </div>
              <div>
                <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Admission / Roll No</label>
                <input type="text" id="reg-roll" required placeholder="e.g. 2026ABES042" class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white font-mono-code focus:outline-none focus:border-[#D6B66C] transition" />
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Branch / Degree</label>
                <input type="text" id="reg-branch" value="CSE (AI/ML)" required class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition" />
              </div>
              <div>
                <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Section &amp; Year</label>
                <input type="text" id="reg-section" value="Sec A · Year 1" required class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition" />
              </div>
            </div>

            <div>
              <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Create Password (Min 6 Characters)</label>
              <div class="relative">
                <input type="password" id="reg-password" minlength="6" required placeholder="Create secure password" class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition pr-10" />
                <button type="button" onclick="togglePasswordVisibility('reg-password', this)" class="absolute right-3 top-2.5 text-xs text-[#7F8B85] hover:text-white transition">
                  👁️
                </button>
              </div>
            </div>

            <div>
              <label class="text-xs text-[#8E9A92] font-semibold block mb-1">Confirm Password</label>
              <div class="relative">
                <input type="password" id="reg-password-confirm" minlength="6" required placeholder="Re-enter password" class="w-full px-4 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C] transition pr-10" />
                <button type="button" onclick="togglePasswordVisibility('reg-password-confirm', this)" class="absolute right-3 top-2.5 text-xs text-[#7F8B85] hover:text-white transition">
                  👁️
                </button>
              </div>
            </div>

            <!-- Honor Code Checkbox -->
            <label class="flex items-center gap-2 cursor-pointer text-xs select-none pt-1">
              <input type="checkbox" id="reg-terms" required checked class="w-4 h-4 accent-[#51D6A0] rounded" />
              <span class="text-[#8E9A92]">I agree to ABES Engineering College Academic Honor Code.</span>
            </label>

            <button type="submit" class="w-full btn-emerald py-3 rounded-xl text-xs font-bold shadow-lg shadow-[#51D6A0]/20 hover:scale-[1.01] active:scale-95 transition flex items-center justify-center gap-2">
              <span>Create ZYNAX Student Account</span>
              <span>✓</span>
            </button>
          </form>

          <!-- Alternative Quick OTP Login option for legacy continuity -->
          <div class="pt-2 border-t border-white/[0.08] text-center">
            <button onclick="toggleLegacyOtpBox()" class="text-[11px] text-[#7F8B85] hover:text-[#D6B66C] transition flex items-center justify-center gap-1 mx-auto">
              <span>🔐 Quick One-Time Passcode (OTP) Verification</span>
              <span id="legacy-otp-arrow">▼</span>
            </button>
            <div id="legacy-otp-container" class="hidden pt-3 space-y-2 max-w-sm mx-auto">
              <button onclick="requestOtp()" class="btn-gold w-full py-2 rounded-xl text-xs font-bold">Generate One-Click OTP</button>
              <div id="auth-otp-box" class="hidden p-3 rounded-xl bg-white/[0.04] space-y-2">
                <div class="text-[11px] text-[#7F8B85]">Your Security Code: <span id="displayed-otp" class="font-mono-code font-bold text-[#51D6A0] text-sm"></span></div>
                <input type="text" id="otp-input" placeholder="Enter OTP" class="w-full px-3 py-1.5 rounded-lg bg-black/40 border border-white/[0.1] text-xs text-white text-center font-mono-code" />
                <button onclick="verifyOtpNow()" class="btn-emerald w-full py-1.5 rounded-lg text-xs font-bold">Verify &amp; Enter</button>
              </div>
            </div>
          </div>

        </div>
      </div>

    </section>

    <!-- FORGOT PASSWORD MODAL -->
    <div id="modal-forgot-password" class="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-xl hidden">
      <div class="max-w-md w-full mx-4 liquid-glass-card p-6 sm:p-7 space-y-4 relative">
        <div class="liquid-sheen-overlay"></div>
        <div class="relative z-10 space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-white/[0.08]">
            <h3 class="text-sm font-black text-white flex items-center gap-2">
              <span>🔑 Password Recovery</span>
              <span class="text-[10px] px-2 py-0.5 rounded bg-[#D6B66C]/15 text-[#D6B66C]">Verified Email</span>
            </h3>
            <button onclick="closeForgotPasswordModal()" class="text-xs text-[#7F8B85] hover:text-white">✕</button>
          </div>
          <p class="text-xs text-[#8E9A92]">Enter your ABES college email to receive a password recovery security token.</p>
          <input type="email" id="forgot-email" value="anurag.banik@abes.ac.in" class="w-full px-3.5 py-2.5 rounded-xl bg-black/40 border border-white/[0.1] text-xs text-white focus:outline-none focus:border-[#D6B66C]" />
          <div class="flex justify-end gap-2 pt-2">
            <button onclick="closeForgotPasswordModal()" class="glass-card px-4 py-2 rounded-xl text-xs text-white">Cancel</button>
            <button onclick="submitForgotPassword()" class="btn-gold px-4 py-2 rounded-xl text-xs font-bold shadow">Send Recovery Code</button>
          </div>
        </div>
      </div>
    </div>
'''
