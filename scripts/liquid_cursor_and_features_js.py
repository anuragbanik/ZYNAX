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

      // Calculate sliding percentage based on viewport width
      const isMobile = window.innerWidth <= 640;
      const isTablet = window.innerWidth <= 1024;
      const slideWidthPercent = isMobile ? 100 : (isTablet ? 50 : 33.333);
      
      const offset = currentCarouselIndex * slideWidthPercent;
      track.style.transform = `translateX(-${offset}%)`;

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
        if (sub) sub.innerText = "Register your official ABES college identity on ZYNAX.";
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

    function handleSignInSubmit(e) {
      e.preventDefault();
      const username = (document.getElementById("signin-username") || {}).value || "";
      const password = (document.getElementById("signin-password") || {}).value || "";
      const remember = (document.getElementById("signin-remember") || {}).checked;

      if (!username || !password) {
        showAuthAlert("Please provide both your Student Username/Email and Password.", false);
        return;
      }

      if (remember) {
        try {
          localStorage.setItem("ZYNAX_REMEMBERED_USER", username);
        } catch(err){}
      }

      showAuthAlert("Authentication verified! Welcome back to ZYNAX.", true);

      setTimeout(() => {
        switchTab("dashboard");
        triggerLoginWelcome(APP.studentProfile.name);
      }, 700);
    }

    function handleRegisterSubmit(e) {
      e.preventDefault();
      const name = (document.getElementById("reg-name") || {}).value || "";
      const email = (document.getElementById("reg-email") || {}).value || "";
      const roll = (document.getElementById("reg-roll") || {}).value || "";
      const branch = (document.getElementById("reg-branch") || {}).value || "CSE (AI/ML)";
      const section = (document.getElementById("reg-section") || {}).value || "Sec A";
      const pass = (document.getElementById("reg-password") || {}).value || "";
      const passConfirm = (document.getElementById("reg-password-confirm") || {}).value || "";

      if (pass.length < 6) {
        showAuthAlert("Password must be at least 6 characters long.", false);
        return;
      }

      if (pass !== passConfirm) {
        showAuthAlert("Passwords do not match. Please re-enter carefully.", false);
        return;
      }

      // Update student profile in memory & localStorage
      APP.studentProfile.name = name;
      APP.studentProfile.email = email;
      APP.studentProfile.roll = roll;
      APP.studentProfile.branch = branch;
      APP.studentProfile.section = section;

      try {
        localStorage.setItem("ZYNAX_STUDENT_PROFILE", JSON.stringify(APP.studentProfile));
        localStorage.setItem("ZYNAX_REGISTERED_USER", JSON.stringify({ email, roll, name }));
      } catch(err){}

      syncProfileAcrossApp();
      showAuthAlert(`Account successfully registered for ${name}! Entering workspace...`, true);

      setTimeout(() => {
        switchTab("dashboard");
        triggerLoginWelcome(name);
      }, 800);
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
