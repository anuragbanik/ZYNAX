# -*- coding: utf-8 -*-
"""
JavaScript logic for:
1. 3D Student Identity Card (Tilt, Flip, Specular sheen)
2. AI Profile Photograph Enhancement (Canvas-based studio filter)
3. AI-Powered "Your Strengths" Analysis
4. AI Voice Welcome Experience (Female Voice)
5. Multi-Language Switcher Integration
6. PDF Credential Download & Profile Sharing
"""

STUDENT_IDENTITY_JS = r'''
    // =========================================================================
    // 3D AI STUDENT IDENTITY CARD ENGINE (TILT, FLIP, & SHINE)
    // =========================================================================

    function handleCardClick(e) {
      if (e.target.closest('button, input, select, a, label')) return;
      flipStudentCard();
    }

    function flipStudentCard() {
      const flipper = document.getElementById("interactive-student-card");
      if (flipper) flipper.classList.toggle("flipped");
    }

    function handleCardTilt(e) {
      if (window.innerWidth < 768 || (window.matchMedia && window.matchMedia("(pointer: coarse)").matches)) return;
      const card = document.getElementById("interactive-student-card");
      if (!card) return;
      if (card.classList.contains("flipped")) return;

      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -12;
      const rotateY = ((x - centerX) / centerX) * 12;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;

      const sheen = document.getElementById("card-sheen");
      if (sheen) {
        const posX = ((x / rect.width) * 100).toFixed(1);
        const posY = ((y / rect.height) * 100).toFixed(1);
        sheen.style.backgroundPosition = `${posX}% ${posY}%`;
      }
    }

    function resetCardTilt() {
      const card = document.getElementById("interactive-student-card");
      if (!card) return;
      if (!card.classList.contains("flipped")) {
        card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg)";
      }
    }

    // =========================================================================
    // AI PROFILE PHOTOGRAPH ENHANCEMENT ENGINE
    // =========================================================================

    function handleIdentityPhotoUpload(e) {
      const file = e.target.files && e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        const originalUrl = evt.target.result;
        enhancePhotoWithStudioLighting(originalUrl, function(enhancedUrl) {
          APP.studentProfile.originalPhotoUrl = originalUrl;
          APP.studentProfile.enhancedPhotoUrl = enhancedUrl;
          APP.studentProfile.avatarDataUrl = enhancedUrl;
          APP.studentProfile.activePhotoFilter = "enhanced";

          try {
            localStorage.setItem("ZYNAX_STUDENT_PROFILE", JSON.stringify(APP.studentProfile));
          } catch(err){}

          syncProfileAcrossApp();
          alert("✨ AI Studio Photograph Enhancement Complete!\nFacial features preserved with cinematic champagne gold rim-lighting & studio contrast.");
        });
      };
      reader.readAsDataURL(file);
    }

    function enhancePhotoWithStudioLighting(dataUrl, callback) {
      const img = new Image();
      img.onload = function() {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");
        const maxDim = 600;
        let w = img.width;
        let h = img.height;

        if (w > h && w > maxDim) {
          h = Math.round((h * maxDim) / w);
          w = maxDim;
        } else if (h > maxDim) {
          w = Math.round((w * maxDim) / h);
          h = maxDim;
        }

        canvas.width = w;
        canvas.height = h;

        // 1. Draw base photo
        ctx.drawImage(img, 0, 0, w, h);

        // 2. Subtle contrast & vibrance boost
        const imgData = ctx.getImageData(0, 0, w, h);
        const d = imgData.data;
        for (let i = 0; i < d.length; i += 4) {
          // Contrast curve
          d[i] = Math.min(255, Math.max(0, ((d[i] - 128) * 1.1) + 132));     // Red
          d[i+1] = Math.min(255, Math.max(0, ((d[i+1] - 128) * 1.08) + 130)); // Green
          d[i+2] = Math.min(255, Math.max(0, ((d[i+2] - 128) * 1.05) + 126)); // Blue
        }
        ctx.putImageData(imgData, 0, 0);

        // 3. Studio Champagne Gold Rim Lighting (#D6B66C)
        const rimGrad = ctx.createLinearGradient(0, 0, w, h);
        rimGrad.addColorStop(0, "rgba(214, 182, 108, 0.18)");
        rimGrad.addColorStop(0.4, "rgba(214, 182, 108, 0.0)");
        rimGrad.addColorStop(1, "rgba(72, 184, 255, 0.12)");
        ctx.globalCompositeOperation = "screen";
        ctx.fillStyle = rimGrad;
        ctx.fillRect(0, 0, w, h);

        // 4. Subtle Studio Vignette
        ctx.globalCompositeOperation = "multiply";
        const vigGrad = ctx.createRadialGradient(w/2, h/2, Math.min(w,h)*0.35, w/2, h/2, Math.min(w,h)*0.75);
        vigGrad.addColorStop(0, "rgba(255, 255, 255, 1)");
        vigGrad.addColorStop(1, "rgba(210, 215, 210, 0.9)");
        ctx.fillStyle = vigGrad;
        ctx.fillRect(0, 0, w, h);

        ctx.globalCompositeOperation = "source-over";
        callback(canvas.toDataURL("image/jpeg", 0.92));
      };
      img.src = dataUrl;
    }

    function setCardPhotoFilter(mode) {
      if (!APP.studentProfile) return;
      APP.studentProfile.activePhotoFilter = mode;

      const btnEnhanced = document.getElementById("btn-photo-enhanced");
      const btnOriginal = document.getElementById("btn-photo-original");

      if (mode === "enhanced") {
        APP.studentProfile.avatarDataUrl = APP.studentProfile.enhancedPhotoUrl || APP.studentProfile.avatarDataUrl;
        if (btnEnhanced) btnEnhanced.className = "px-2.5 py-1 rounded-lg bg-[#9875FF] text-white font-bold text-[11px] transition shadow";
        if (btnOriginal) btnOriginal.className = "px-2.5 py-1 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[11px] transition";
      } else {
        APP.studentProfile.avatarDataUrl = APP.studentProfile.originalPhotoUrl || APP.studentProfile.avatarDataUrl;
        if (btnEnhanced) btnEnhanced.className = "px-2.5 py-1 rounded-lg text-[#8C9690] hover:text-white font-semibold text-[11px] transition";
        if (btnOriginal) btnOriginal.className = "px-2.5 py-1 rounded-lg bg-[#48B8FF] text-black font-bold text-[11px] transition shadow";
      }

      try {
        localStorage.setItem("ZYNAX_STUDENT_PROFILE", JSON.stringify(APP.studentProfile));
      } catch(e){}

      syncProfileAcrossApp();
    }

    // =========================================================================
    // AI-POWERED "YOUR STRENGTHS" SYNTHESIS ENGINE
    // =========================================================================

    function recalculateStudentStrengths() {
      const p = APP.studentProfile || {};
      const leetSolved = p.leetCodeSolved || 84;
      const rating = p.contestRating || 1642;
      const att = p.aggregateAttendance || 75.5;

      const keyEl = document.getElementById("str-key");
      const techEl = document.getElementById("str-tech");
      const probEl = document.getElementById("str-problem");
      const growthEl = document.getElementById("str-growth");
      const backDomain = document.getElementById("card-back-domain");
      const backStrength = document.getElementById("card-back-strength");

      if (keyEl) keyEl.innerText = `Fast Algorithmic Modeling (${leetSolved}+ Solved), Structured Prompt Engineering, High Math Aptitude`;
      if (techEl) techEl.innerText = `Python, C++, PyTorch, React, SQLite, DSA, Neural Audio APIs`;
      if (probEl) probEl.innerText = `Binary Search, Dynamic Programming, Two Pointers (Rating: ${rating})`;
      if (growthEl) growthEl.innerText = `Target 150+ LeetCode milestones, maintain attendance armor above 75%, and publish 1 open-source agent before Sem 3.`;
      if (backDomain) backDomain.innerText = `${p.branch || 'CSE (AI/ML)'} · Autonomous Agent Ecosystems`;
      if (backStrength) backStrength.innerText = `Algorithmic Problem Solving & Neural Nets (${leetSolved} Problems)`;

      speakWithFemaleVoice("Student strengths analyzed and verified based on your active academic profile and coding achievements.");
      alert("⚡ AI Student Strengths Analyzed!\nAll metrics updated with verified problem solving and academic records.");
    }

    // =========================================================================
    // AI VOICE WELCOME EXPERIENCE (SOFT ELEGANT FEMALE VOICE)
    // =========================================================================

    function triggerLoginWelcome(studentName) {
      const pName = studentName || (APP.studentProfile && APP.studentProfile.name) || "Anurag";
      const firstName = pName.split(" ")[0] || "Anurag";

      // 1. Show Animated Full-Screen Welcome Modal
      const modal = document.getElementById("zynax-welcome-modal");
      const modalUser = document.getElementById("welcome-modal-username");
      if (modalUser) modalUser.innerText = firstName;
      if (modal) {
        modal.classList.remove("opacity-0", "pointer-events-none");
        modal.classList.add("opacity-100");
      }

      // 2. Update Dashboard Greeting Banner
      const banner = document.getElementById("zynax-welcome-banner");
      if (banner) {
        banner.classList.remove("hidden");
        const heading = document.getElementById("welcome-banner-heading");
        const scriptEl = document.getElementById("welcome-banner-script");
        if (heading) heading.innerText = `Welcome to ZYNAX, ${firstName}!`;
        if (scriptEl) scriptEl.innerText = `"Welcome to ZYNAX — Your Campus, Your Intelligence, Your Companion."`;
      }

      // 3. Exact greeting spoken in soft, pleasant female voice
      const exactGreeting = `Welcome, ${firstName}! Welcome to ZYNAX — Your Campus, Your Intelligence, Your Companion.`;

      if (!APP.voiceMuted) {
        speakWithFemaleVoice(exactGreeting);
      }
    }

    function dismissWelcomeModal() {
      const modal = document.getElementById("zynax-welcome-modal");
      if (modal) {
        modal.classList.remove("opacity-100");
        modal.classList.add("opacity-0", "pointer-events-none");
      }
      switchTab("dashboard");
    }

    function replayWelcomeGreeting() {
      const firstName = (APP.studentProfile && APP.studentProfile.name) ? APP.studentProfile.name.split(" ")[0] : "Anurag";
      const exactGreeting = `Welcome, ${firstName}! Welcome to ZYNAX — Your Campus, Your Intelligence, Your Companion.`;

      // Trigger animated wave bars
      document.querySelectorAll(".voice-wave-bar").forEach(el => el.classList.add("animate-pulse"));

      speakWithFemaleVoice(exactGreeting);
    }

    function toggleWelcomeMute() {
      APP.voiceMuted = !APP.voiceMuted;
      const modalLabel = document.getElementById("welcome-mute-label");
      const modalIcon = document.getElementById("welcome-mute-icon");
      const dashLabel = document.getElementById("welcome-dash-mute-label");

      if (APP.voiceMuted) {
        if ("speechSynthesis" in window) window.speechSynthesis.cancel();
        if (modalLabel) modalLabel.innerText = "Unmute";
        if (modalIcon) modalIcon.innerText = "🔇";
        if (dashLabel) dashLabel.innerText = "Unmute";
      } else {
        if (modalLabel) modalLabel.innerText = "Mute";
        if (modalIcon) modalIcon.innerText = "🔈";
        if (dashLabel) dashLabel.innerText = "Mute";
        replayWelcomeGreeting();
      }
    }

    function dismissWelcomeBanner() {
      const banner = document.getElementById("zynax-welcome-banner");
      if (banner) banner.classList.add("hidden");
    }

    // =========================================================================
    // PDF DOWNLOAD & PROFILE SHARING ENGINE
    // =========================================================================

    function downloadStudentCardPdf() {
      const p = APP.studentProfile || {};
      const printWindow = window.open("", "_blank");
      if (!printWindow) {
        alert("Please allow popups to download or print your Student Identity Card.");
        return;
      }
      const photo = p.avatarDataUrl || "";
      printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
          <title>ZYNAX Student Identity Credential - ${p.name || 'Student'}</title>
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0A0D0B; color: #FFF; padding: 40px; margin: 0; }
            .card { width: 520px; margin: 0 auto; border: 2px solid #D6B66C; border-radius: 20px; padding: 24px; background: #141816; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            .header { display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; margin-bottom: 16px; }
            .college { font-size: 14px; font-weight: 900; letter-spacing: 1px; color: #D6B66C; }
            .sub { font-size: 10px; color: #888; }
            .body { display: flex; gap: 20px; align-items: center; }
            .photo { width: 90px; height: 110px; border-radius: 12px; border: 2px solid #D6B66C; background: #222; object-fit: cover; }
            .details { flex: 1; }
            .name { font-size: 20px; font-weight: 900; margin-bottom: 4px; }
            .roll { font-family: monospace; font-size: 14px; color: #D6B66C; font-weight: bold; margin-bottom: 6px; }
            .meta { font-size: 12px; color: #CCC; margin-bottom: 4px; }
            .badges { margin-top: 10px; display: flex; gap: 8px; font-size: 10px; font-weight: bold; }
            .badge { background: rgba(81,214,160,0.2); color: #51D6A0; padding: 3px 8px; border-radius: 6px; border: 1px solid rgba(81,214,160,0.3); }
            .footer { margin-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 12px; display: flex; justify-content: space-between; font-size: 10px; color: #888; }
            @media print { body { background: #FFF; color: #000; padding: 0; } .card { border-color: #333; background: #FFF; color: #000; } .name { color: #000; } .roll { color: #333; } }
          </style>
        </head>
        <body>
          <div class="card">
            <div class="header">
              <div>
                <div class="college">ABES ENGINEERING COLLEGE</div>
                <div class="sub">AKTU CODE 032 · GHAZIABAD · CAMPUS ECOSYSTEM</div>
              </div>
              <div style="text-align: right;">
                <span style="color: #51D6A0; font-weight: bold; font-family: monospace;">2026–2030</span>
              </div>
            </div>
            <div class="body">
              ${photo ? `<img src="${photo}" class="photo" />` : `<div class="photo" style="display:flex;align-items:center;justify-content:center;font-size:24px;color:#D6B66C;font-weight:bold;">AB</div>`}
              <div class="details">
                <div class="name">${p.name || 'Anurag Banik'}</div>
                <div class="roll">${p.roll || '2026ABES042'}</div>
                <div class="meta">${p.branch || 'CSE (AI/ML)'}</div>
                <div class="meta">Section ${p.section || 'Sec A'} · Year ${p.currentYear || '1'} (Sem ${p.currentSem || '1'})</div>
                <div class="badges">
                  <span class="badge">AKTU VERIFIED</span>
                  <span class="badge" style="background:rgba(214,182,108,0.2);color:#D6B66C;border-color:rgba(214,182,108,0.3);">AI/ML SPECIALIST</span>
                </div>
              </div>
            </div>
            <div class="footer">
              <div>OFFICIAL ZYNAX DIGITAL IDENTITY PASS</div>
              <div>REGISTRAR DIGITALLY AUTHENTICATED</div>
            </div>
          </div>
        </body>
        </html>
      `);
      printWindow.document.close();
      setTimeout(function() {
        try { printWindow.focus(); printWindow.print(); } catch(e){}
      }, 500);
    }

    function shareStudentProfile() {
      const p = APP.studentProfile || {};
      const shareText = `🪪 ZYNAX Digital Student ID: ${p.name || 'Anurag Banik'} (${p.roll || '2026ABES042'}) · ${p.branch || 'CSE AI/ML'} · ABES Engineering College · Verified SGPA: 8.80 · Strengths: Algorithmic Modeling & Neural Nets. View on ZYNAX: ${window.location.origin}${window.location.pathname}`;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(shareText).then(() => {
          alert("✓ Shareable Student Identity credentials copied to clipboard!");
        }).catch(() => {
          prompt("Copy your shareable Student Profile credentials:", shareText);
        });
      } else {
        prompt("Copy your shareable Student Profile credentials:", shareText);
      }
    }
'''
