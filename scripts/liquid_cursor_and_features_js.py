# -*- coding: utf-8 -*-
"""
Interactive Engine for:
1. Smooth Cursor Sensor (Desktop Lerp tracking, magnetic hover, touch-disabled)
2. 3D Feature Sliding Carousel
3. Liquid Glass Student Authentication & Validation Suite
4. Scroll Reveal Animations
"""

LIQUID_FEATURES_JS = r'''
    // =========================================================================
    // 1. SMOOTH LIQUID CURSOR SENSOR ENGINE (DESKTOP ONLY)
    // =========================================================================

    (function initLiquidCursor() {
      // Disable on touch devices
      if (window.matchMedia("(pointer: coarse)").matches || "ontouchstart" in window) {
        return;
      }

      const dot = document.createElement("div");
      dot.id = "liquid-cursor-dot";
      const glow = document.createElement("div");
      glow.id = "liquid-cursor-glow";
      document.body.appendChild(dot);
      document.body.appendChild(glow);

      let mouseX = -100, mouseY = -100;
      let glowX = -100, glowY = -100;
      let isVisible = false;

      window.addEventListener("mousemove", (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        if (!isVisible) {
          isVisible = true;
          dot.style.opacity = "1";
          glow.style.opacity = "1";
        }
        dot.style.transform = `translate(${mouseX}px, ${mouseY}px) translate(-50%, -50%)`;
      });

      window.addEventListener("mouseleave", () => {
        isVisible = false;
        dot.style.opacity = "0";
        glow.style.opacity = "0";
      });

      // Smooth Lerp loop for trailing glow ring
      function animateCursorGlow() {
        if (isVisible) {
          glowX += (mouseX - glowX) * 0.18;
          glowY += (mouseY - glowY) * 0.18;
          glow.style.transform = `translate(${glowX.toFixed(2)}px, ${glowY.toFixed(2)}px) translate(-50%, -50%)`;
        }
        requestAnimationFrame(animateCursorGlow);
      }
      animateCursorGlow();

      // Magnetic hover feedback on interactive elements
      document.addEventListener("mouseover", (e) => {
        const target = e.target.closest("button, a, .nav-tab-pill, .carousel-3d-card, .id-card-flipper, input, select");
        if (target) {
          glow.classList.add("cursor-hover");
        }
      });
      document.addEventListener("mouseout", (e) => {
        const target = e.target.closest("button, a, .nav-tab-pill, .carousel-3d-card, .id-card-flipper, input, select");
        if (target) {
          glow.classList.remove("cursor-hover");
        }
      });
    })();

    function toggleMobileMenu() {
      const drawer = document.getElementById("mobile-menu-drawer");
      if (!drawer) return;
      drawer.classList.toggle("hidden");
    }

    // =========================================================================
    // 2. 3D FEATURE SLIDING CAROUSEL ENGINE
    // =========================================================================

    let currentCarouselIndex = 0;
    const totalCarouselSlides = 5;

    function slideCarousel(direction) {
      const track = document.getElementById("power-carousel-track");
      if (!track) return;

      currentCarouselIndex += direction;
      if (currentCarouselIndex < 0) {
        currentCarouselIndex = totalCarouselSlides - 1;
      } else if (currentCarouselIndex >= totalCarouselSlides) {
        currentCarouselIndex = 0;
      }

      const firstCard = track.querySelector(".carousel-3d-card");
      if (firstCard && firstCard.offsetWidth > 0) {
        const cardWidth = firstCard.offsetWidth;
        const gap = 20;
        const shiftPx = currentCarouselIndex * (cardWidth + gap);
        track.style.transform = `translateX(-${shiftPx}px)`;
      } else {
        const isMobile = window.innerWidth <= 640;
        const isTablet = window.innerWidth <= 1024;
        const slideWidthPercent = isMobile ? 100 : (isTablet ? 50 : 33.333);
        const offset = currentCarouselIndex * slideWidthPercent;
        track.style.transform = `translateX(-${offset}%)`;
      }

      // Apply 3D perspective depth to active cards
      const cards = track.querySelectorAll(".carousel-3d-card");
      cards.forEach((card, idx) => {
        if (idx === currentCarouselIndex) {
          card.style.transform = "scale(1.03) translateZ(15px)";
          card.style.opacity = "1";
        } else {
          card.style.transform = "scale(0.98) translateZ(0px)";
          card.style.opacity = "0.85";
        }
      });
    }

    // Auto-advance carousel every 6 seconds if not hovered
    let carouselInterval = setInterval(() => {
      slideCarousel(1);
    }, 6000);

    const carouselViewport = document.querySelector(".carousel-3d-viewport");
    if (carouselViewport) {
      carouselViewport.addEventListener("mouseenter", () => clearInterval(carouselInterval));
      carouselViewport.addEventListener("mouseleave", () => {
        clearInterval(carouselInterval);
        carouselInterval = setInterval(() => slideCarousel(1), 6000);
      });
    }

    // =========================================================================
    // 3. STUDENT LOGIN & ACCOUNT SUITE (AUTHENTICATION & VALIDATION)
    // =========================================================================

    function setAuthMode(mode) {
      const tabSignIn = document.getElementById("auth-tab-signin");
      const tabRegister = document.getElementById("auth-tab-register");
      const formSignIn = document.getElementById("form-signin");
      const formRegister = document.getElementById("form-register");
      const heading = document.getElementById("auth-heading-text");
      const sub = document.getElementById("auth-sub-text");
      const alertBox = document.getElementById("auth-alert-box");

      if (alertBox) alertBox.classList.add("hidden");

      if (mode === "signin") {
        if (tabSignIn) {
          tabSignIn.className = "flex-1 py-2.5 rounded-xl text-xs font-bold text-black bg-[#D6B66C] shadow-lg transition-all";
        }
        if (tabRegister) {
          tabRegister.className = "flex-1 py-2.5 rounded-xl text-xs font-semibold text-[#87928B] hover:text-white transition-all";
        }
        if (formSignIn) formSignIn.classList.remove("hidden");
        if (formRegister) formRegister.classList.add("hidden");
        if (heading) heading.innerText = "Student Sign In";
        if (sub) sub.innerText = "Enter your student credentials to access your ZYNAX companion.";
      } else {
        if (tabSignIn) {
          tabSignIn.className = "flex-1 py-2.5 rounded-xl text-xs font-semibold text-[#87928B] hover:text-white transition-all";
        }
        if (tabRegister) {
          tabRegister.className = "flex-1 py-2.5 rounded-xl text-xs font-bold text-black bg-[#51D6A0] shadow-lg transition-all";
        }
        if (formSignIn) formSignIn.classList.add("hidden");
        if (formRegister) formRegister.classList.remove("hidden");
        if (heading) heading.innerText = "Create Student Account";
        if (sub) sub.innerText = "Register your individual student identity on ZYNAX.";
      }
    }

    function togglePasswordVisibility(inputId, btn) {
      const input = document.getElementById(inputId);
      if (!input) return;
      if (input.type === "password") {
        input.type = "text";
        if (btn) btn.innerText = "🙈";
      } else {
        input.type = "password";
        if (btn) btn.innerText = "👁️";
      }
    }

    function showAuthAlert(msg, isSuccess) {
      const box = document.getElementById("auth-alert-box");
      if (!box) return;
      box.classList.remove("hidden");
      if (isSuccess) {
        box.className = "p-3 rounded-xl border border-[#51D6A0]/40 bg-[#51D6A0]/10 text-[#51D6A0] text-xs font-medium";
        box.innerHTML = `<span>✓ ${msg}</span>`;
      } else {
        box.className = "p-3 rounded-xl border border-red-500/40 bg-red-500/10 text-red-400 text-xs font-medium";
        box.innerHTML = `<span>⚠️ ${msg}</span>`;
      }
    }

    // ==========================================
    // MULTI-USER ACCOUNT DATABASE & SESSION ENGINE
    // ==========================================
    function getRegisteredAccounts() {
      try {
        const raw = localStorage.getItem("ZYNAX_ACCOUNTS_DB");
        if (!raw) return {};
        const parsed = JSON.parse(raw);
        return (typeof parsed === "object" && parsed !== null) ? parsed : {};
      } catch(err) {
        return {};
      }
    }

    function saveAccountToDb(account) {
      if (!account || !account.roll) return;
      try {
        const db = getRegisteredAccounts();
        const primaryKey = String(account.roll).trim().toLowerCase();
        db[primaryKey] = account;
        if (account.email) {
          db[String(account.email).trim().toLowerCase()] = primaryKey; // alias pointer
        }
        localStorage.setItem("ZYNAX_ACCOUNTS_DB", JSON.stringify(db));
      } catch(err){}
    }

    function renderSavedAccountsList() {
      const container = document.getElementById("saved-accounts-list");
      const section = document.getElementById("saved-accounts-section");
      if (!container || !section) return;

      const db = getRegisteredAccounts();
      const uniqueAccounts = [];
      const seen = new Set();

      for (const key of Object.keys(db)) {
        const item = db[key];
        if (typeof item === "object" && item !== null && item.roll) {
          const rollKey = String(item.roll).toLowerCase();
          if (!seen.has(rollKey)) {
            seen.add(rollKey);
            uniqueAccounts.push(item);
          }
        }
      }

      if (uniqueAccounts.length === 0) {
        section.classList.add("hidden");
        container.innerHTML = "";
        return;
      }

      section.classList.remove("hidden");
      container.innerHTML = uniqueAccounts.map(acc => {
        const initials = ((acc.name || "ST").trim().split(" ").map(w => w[0]).slice(0, 2).join("")).toUpperCase();
        const safeName = (acc.name || "Student").replace(/"/g, "&quot;");
        const safeRoll = (acc.roll || "").replace(/"/g, "&quot;");
        const safeCol = (acc.college || acc.branch || "Student Workspace").replace(/"/g, "&quot;");
        return `
          <div class="p-3 rounded-xl bg-white/[0.03] hover:bg-white/[0.07] border border-white/[0.08] hover:border-[#D6B66C]/40 transition flex items-center justify-between gap-3 group cursor-pointer" onclick="quickSelectAccount('${safeRoll}')">
            <div class="flex items-center gap-2.5 min-w-0">
              <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-[#D6B66C]/20 to-[#51D6A0]/20 border border-white/10 flex items-center justify-center text-xs font-bold text-white shrink-0">
                ${initials}
              </div>
              <div class="min-w-0">
                <div class="text-xs font-bold text-white truncate">${safeName}</div>
                <div class="text-[10px] text-[#7F8B85] font-mono-code truncate">${safeRoll} · ${safeCol}</div>
              </div>
            </div>
            <div class="flex items-center gap-1.5 shrink-0">
              <span class="text-[10px] text-[#D6B66C] font-semibold opacity-0 group-hover:opacity-100 transition">Select →</span>
              <button type="button" onclick="removeSavedAccount('${safeRoll}', event)" class="p-1 rounded text-[#7F8B85] hover:text-red-400 hover:bg-red-500/10 text-xs transition" title="Remove account from device">✕</button>
            </div>
          </div>
        `;
      }).join("");
    }

    function quickSelectAccount(roll) {
      const uField = document.getElementById("signin-username");
      const pField = document.getElementById("signin-password");
      if (uField) {
        uField.value = roll;
      }
      setAuthMode("signin");
      if (pField) pField.focus();
    }

    function removeSavedAccount(roll, e) {
      if (e) e.stopPropagation();
      try {
        const db = getRegisteredAccounts();
        const primaryKey = String(roll).trim().toLowerCase();
        let emailKey = null;
        if (db[primaryKey] && db[primaryKey].email) {
          emailKey = String(db[primaryKey].email).trim().toLowerCase();
        }
        delete db[primaryKey];
        if (emailKey && db[emailKey] === primaryKey) {
          delete db[emailKey];
        }
        localStorage.setItem("ZYNAX_ACCOUNTS_DB", JSON.stringify(db));

        // If active user was removed, reset active session
        const active = localStorage.getItem("ZYNAX_ACTIVE_USER_ID");
        if (active && (active.toLowerCase() === primaryKey || active.toLowerCase() === emailKey)) {
          localStorage.removeItem("ZYNAX_ACTIVE_USER_ID");
          sessionStorage.removeItem("ZYNAX_ACTIVE_USER_ID");
        }
        renderSavedAccountsList();
        showAuthAlert("Account removed from this device.", true);
      } catch(err){}
    }

    function handleSignInSubmit(e) {
      e.preventDefault();
      const usernameInput = (document.getElementById("signin-username") || {}).value || "";
      const passwordInput = (document.getElementById("signin-password") || {}).value || "";
      const remember = (document.getElementById("signin-remember") || {}).checked;

      const lookup = usernameInput.trim().toLowerCase();
      if (!lookup || !passwordInput) {
        showAuthAlert("Please enter both your Student Roll/Email and Password.", false);
        return;
      }

      const db = getRegisteredAccounts();
      let account = null;

      if (db[lookup]) {
        if (typeof db[lookup] === "string") {
          account = db[db[lookup]]; // resolved alias
        } else {
          account = db[lookup];
        }
      } else {
        // Also search across all accounts by roll, email, or name
        for (const k of Object.keys(db)) {
          const item = db[k];
          if (typeof item === "object" && item !== null) {
            if (
              (item.roll && item.roll.toLowerCase() === lookup) ||
              (item.email && item.email.toLowerCase() === lookup) ||
              (item.name && item.name.toLowerCase() === lookup)
            ) {
              account = item;
              break;
            }
          }
        }
      }

      if (!account) {
        showAuthAlert(`No account found matching "${usernameInput}". Please click "Create Account" below to register your individual details.`, false);
        return;
      }

      // Check password if set during registration
      if (account.password && account.password !== passwordInput) {
        showAuthAlert("Incorrect password for this student account. Please re-enter or click 'Forgot Password'.", false);
        return;
      }

      // Activate session
      const studentName = account.name || "Student";
      APP.isAuthenticated = true;
      Object.assign(APP.studentProfile, account.profile || account);

      try {
        if (remember) {
          localStorage.setItem("ZYNAX_ACTIVE_USER_ID", account.roll || account.email || lookup);
          localStorage.setItem("ZYNAX_REMEMBERED_USER", lookup);
        } else {
          sessionStorage.setItem("ZYNAX_ACTIVE_USER_ID", account.roll || account.email || lookup);
          localStorage.removeItem("ZYNAX_ACTIVE_USER_ID");
        }
      } catch(err){}

      syncProfileAcrossApp();
      showAuthAlert(`Authentication successful! Welcome back, ${studentName}.`, true);

      setTimeout(() => {
        switchTab("dashboard");
        triggerLoginWelcome(studentName);
      }, 650);
    }

    function handleRegisterSubmit(e) {
      e.preventDefault();
      const name = ((document.getElementById("reg-name") || {}).value || "").trim();
      const college = ((document.getElementById("reg-college") || {}).value || "").trim();
      const roll = ((document.getElementById("reg-roll") || {}).value || "").trim();
      const email = ((document.getElementById("reg-email") || {}).value || "").trim();
      const branch = ((document.getElementById("reg-branch") || {}).value || "").trim();
      const section = ((document.getElementById("reg-section") || {}).value || "").trim();
      const phone = ((document.getElementById("reg-phone") || {}).value || "").trim();
      const pass = (document.getElementById("reg-password") || {}).value || "";
      const passConfirm = (document.getElementById("reg-password-confirm") || {}).value || "";

      if (!name || !roll || !email) {
        showAuthAlert("Please fill in your Full Name, Roll Number, and Email.", false);
        return;
      }

      if (pass.length < 6) {
        showAuthAlert("Password must be at least 6 characters long.", false);
        return;
      }

      if (pass !== passConfirm) {
        showAuthAlert("Passwords do not match. Please re-enter carefully.", false);
        return;
      }

      const db = getRegisteredAccounts();
      const rollLookup = roll.toLowerCase();
      const emailLookup = email.toLowerCase();

      if (db[rollLookup] || db[emailLookup]) {
        showAuthAlert(`An account with Roll "${roll}" or Email "${email}" already exists. Please Sign In.`, false);
        setAuthMode("signin");
        const uField = document.getElementById("signin-username");
        if (uField) uField.value = roll;
        return;
      }

      // Construct clean profile purely from student's inputs
      const newProfile = {
        name: name,
        college: college,
        roll: roll,
        email: email,
        branch: branch,
        section: section,
        phone: phone,
        currentYear: 1,
        currentSem: 1,
        github: "",
        linkedin: "",
        targetSgpa: "",
        libraryId: "",
        photoUrl: "",
        enhancedPhotoUrl: "",
        keyStrengths: "",
        technicalStrengths: "",
        creativeAbilities: "",
        problemSolving: "",
        leadership: "",
        communication: "",
        growthGoals: ""
      };

      const newAccount = {
        name: name,
        college: college,
        roll: roll,
        email: email,
        branch: branch,
        section: section,
        phone: phone,
        password: pass,
        createdAt: new Date().toISOString(),
        profile: newProfile
      };

      saveAccountToDb(newAccount);

      // Activate session
      APP.isAuthenticated = true;
      Object.assign(APP.studentProfile, newProfile);
      try {
        localStorage.setItem("ZYNAX_ACTIVE_USER_ID", roll);
        localStorage.setItem("ZYNAX_REMEMBERED_USER", roll);
      } catch(err){}

      syncProfileAcrossApp();
      renderSavedAccountsList();

      showAuthAlert(`Account successfully created for ${name}! Entering your individual workspace...`, true);

      setTimeout(() => {
        switchTab("dashboard");
        triggerLoginWelcome(name);
      }, 750);
    }

    function handleGuestSignIn() {
      const guestProfile = {
        name: "Guest Student",
        college: "ZYNAX Interactive Preview",
        roll: "GUEST-001",
        email: "guest@zynax.ai",
        branch: "General Engineering",
        section: "Demo Section",
        phone: "",
        currentYear: 1,
        currentSem: 1,
        github: "",
        linkedin: "",
        targetSgpa: "9.0",
        libraryId: "LIB-GUEST",
        photoUrl: "",
        enhancedPhotoUrl: "",
        keyStrengths: "",
        technicalStrengths: "",
        creativeAbilities: "",
        problemSolving: "",
        leadership: "",
        communication: "",
        growthGoals: ""
      };

      APP.isAuthenticated = true;
      Object.assign(APP.studentProfile, guestProfile);
      try {
        sessionStorage.setItem("ZYNAX_ACTIVE_USER_ID", "GUEST-001");
      } catch(err){}

      syncProfileAcrossApp();
      showAuthAlert("Entering as Guest Student...", true);
      setTimeout(() => {
        switchTab("dashboard");
        triggerLoginWelcome("Guest Student");
      }, 400);
    }

    // Support direct navigation to Achievements section via switchTab
    if (typeof window.switchTab === "function") {
      const _baseSwitchTab = window.switchTab;
      window.switchTab = function(tabId) {
        if (tabId === "achievements") {
          _baseSwitchTab("dashboard");
          setTimeout(() => {
            const el = document.getElementById("section-achievements");
            if (el) el.scrollIntoView({ behavior: "smooth" });
          }, 120);
          return;
        }
        _baseSwitchTab(tabId);
      };
    }

    function toggleLegacyOtpBox() {
      const container = document.getElementById("legacy-otp-container");
      const arrow = document.getElementById("legacy-otp-arrow");
      if (!container) return;
      const isHidden = container.classList.contains("hidden");
      container.classList.toggle("hidden");
      if (arrow) arrow.innerText = isHidden ? "▲" : "▼";
    }

    function openForgotPasswordModal() {
      const m = document.getElementById("modal-forgot-password");
      if (m) m.classList.remove("hidden");
    }

    function closeForgotPasswordModal() {
      const m = document.getElementById("modal-forgot-password");
      if (m) m.classList.add("hidden");
    }

    function submitForgotPassword() {
      const email = (document.getElementById("forgot-email") || {}).value;
      if (!email || !email.includes("@")) {
        alert("Please enter a valid ABES college email.");
        return;
      }
      alert(`🔑 Password reset link and security verification token dispatched to: ${email}\nFollow the link to securely update your credentials.`);
      closeForgotPasswordModal();
    }

    function handleAuthTilt(e) {
      const card = document.getElementById("auth-main-card");
      if (!card || window.innerWidth < 768) return;

      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      const rotateX = ((y - centerY) / centerY) * -5;
      const rotateY = ((x - centerX) / centerX) * 5;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) scale(1.005)`;
    }

    function resetAuthTilt() {
      const card = document.getElementById("auth-main-card");
      if (!card) return;
      card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)";
    }

    // =========================================================================
    // 4. SCROLL REVEAL OBSERVER
    // =========================================================================

    if ("IntersectionObserver" in window) {
      const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
          }
        });
      }, { threshold: 0.1 });

      window.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll(".scroll-reveal, #section-achievements, #primary-triad-section, #section-3d-carousel").forEach((el) => {
          el.classList.add("scroll-reveal");
          revealObserver.observe(el);
        });
      });
    }
'''
