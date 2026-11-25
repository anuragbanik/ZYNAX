# -*- coding: utf-8 -*-
"""
Liquid Glass Visual Design System & 3D Interactive CSS
Features:
- Apple-inspired Liquid Glass aesthetics (frosted glass, specular highlights, dynamic blur)
- Floating Liquid Glass navigation menu bar
- Smooth cursor sensor & magnetic hover styles
- 3D tilt, zoom-in, depth shadows, and card flip styling
- 3D horizontal sliding carousel
- Achievements showcase styling with gold shimmer & particle effects
"""

LIQUID_GLASS_STYLES = r'''
<style>
/* =========================================================================
   APPLE LIQUID GLASS & 3D DESIGN SYSTEM
   ========================================================================= */

:root {
  --liquid-glass-bg: rgba(16, 21, 18, 0.75);
  --liquid-glass-border: rgba(214, 182, 108, 0.28);
  --liquid-glass-glow: rgba(214, 182, 108, 0.18);
  --liquid-glass-sheen: linear-gradient(135deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.02) 60%, rgba(214, 182, 108, 0.08) 100%);
  --liquid-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.8), 0 0 30px rgba(214, 182, 108, 0.1);
}

/* Liquid Glass Cards */
.liquid-glass-card {
  background: var(--liquid-glass-bg);
  backdrop-filter: blur(28px) saturate(190%);
  -webkit-backdrop-filter: blur(28px) saturate(190%);
  border: 1.5px solid var(--liquid-glass-border);
  box-shadow: var(--liquid-shadow);
  border-radius: 24px;
  position: relative;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.3s ease;
}
.liquid-glass-card:hover {
  border-color: rgba(214, 182, 108, 0.55);
  box-shadow: 0 25px 60px -10px rgba(0, 0, 0, 0.9), 0 0 35px rgba(214, 182, 108, 0.22);
}

/* Specular Light Reflection Sheen */
.liquid-sheen-overlay {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: var(--liquid-glass-sheen);
  pointer-events: none;
  z-index: 2;
}

/* Floating Liquid Glass Navigation Menu */
.floating-liquid-nav {
  position: sticky;
  top: 12px;
  z-index: 50;
  margin: 0 auto;
  max-width: 96%;
  background: rgba(12, 16, 14, 0.82);
  backdrop-filter: blur(32px) saturate(200%);
  -webkit-backdrop-filter: blur(32px) saturate(200%);
  border: 1.5px solid rgba(214, 182, 108, 0.3);
  border-radius: 22px;
  box-shadow: 0 16px 40px -8px rgba(0, 0, 0, 0.85), 0 0 25px rgba(214, 182, 108, 0.12);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Smooth Cursor Sensor Styles (Desktop Only) */
#liquid-cursor-dot {
  position: fixed;
  top: 0;
  left: 0;
  width: 8px;
  height: 8px;
  background-color: #D6B66C;
  border-radius: 50%;
  pointer-events: none;
  z-index: 99999;
  transform: translate(-50%, -50%);
  transition: width 0.2s ease, height 0.2s ease, background-color 0.2s ease;
  will-change: transform;
}
#liquid-cursor-glow {
  position: fixed;
  top: 0;
  left: 0;
  width: 36px;
  height: 36px;
  border: 1.5px solid rgba(214, 182, 108, 0.5);
  background: radial-gradient(circle, rgba(214, 182, 108, 0.2) 0%, transparent 75%);
  border-radius: 50%;
  pointer-events: none;
  z-index: 99998;
  transform: translate(-50%, -50%);
  transition: width 0.3s ease, height 0.3s ease, border-color 0.3s ease, background 0.3s ease;
  will-change: transform;
}
#liquid-cursor-glow.cursor-hover {
  width: 58px;
  height: 58px;
  border-color: rgba(72, 184, 255, 0.7);
  background: radial-gradient(circle, rgba(72, 184, 255, 0.22) 0%, transparent 80%);
}

@media (pointer: coarse), (hover: none) {
  #liquid-cursor-dot, #liquid-cursor-glow {
    display: none !important;
  }
}

/* 3D Carousel Styles */
.carousel-3d-viewport {
  perspective: 1200px;
  overflow: hidden;
  position: relative;
  width: 100%;
  padding: 10px 0;
}
.carousel-3d-track {
  display: flex;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
  gap: 20px;
}
.carousel-3d-card {
  flex: 0 0 calc(33.333% - 14px);
  min-width: 280px;
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
  transform-style: preserve-3d;
}
@media (max-width: 1024px) {
  .carousel-3d-card {
    flex: 0 0 calc(50% - 10px);
  }
}
@media (max-width: 640px) {
  .carousel-3d-card {
    flex: 0 0 100%;
  }
}

/* Achievements Section Glow */
.achievements-backdrop {
  background: radial-gradient(ellipse at bottom, rgba(214, 182, 108, 0.12) 0%, rgba(152, 117, 255, 0.08) 35%, rgba(7, 9, 8, 0.95) 75%);
  position: relative;
  overflow: hidden;
}

/* Gold Shimmer Badge Effect */
@keyframes goldShimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.gold-shimmer-badge {
  background: linear-gradient(90deg, rgba(214,182,108,0.1) 0%, rgba(240,210,139,0.3) 50%, rgba(214,182,108,0.1) 100%);
  background-size: 200% 100%;
  animation: goldShimmer 3s infinite linear;
}

/* Scroll Reveal Utility Classes */
.scroll-reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.scroll-reveal.revealed {
  opacity: 1;
  transform: translateY(0);
}
</style>
'''
