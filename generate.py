import base64
import os

assets_dir = os.path.join('website', 'assets')

with open(os.path.join(assets_dir, 'savkar_logo_circle.png'), 'rb') as f:
    logo_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open(os.path.join(assets_dir, 'real_dollar.png'), 'rb') as f:
    dollar_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

with open(os.path.join(assets_dir, 'real_dollar_cursor.png'), 'rb') as f:
    cursor_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('ascii')

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAVKAR MEDIA — Radical Digital Growth, Web & Custom Software</title>
    <meta name="description" content="Savkar Media — Digital Marketing Agency in Bengaluru. Fueling business growth with powerful content, viral reels, web development & custom software.">
    <link rel="icon" type="image/png" href="___LOGO_B64___">

    <!-- Fonts: Syne + Space Mono + Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@600;700;800;900&display=swap" rel="stylesheet">

    <!-- Libraries: Three.js + GSAP + Lenis -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>

    <style>
        /* ===================================================
           RESET & REAL DOLLAR BILL CURSOR
        =================================================== */
        *, *::before, *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            cursor: url('___CURSOR_B64___') 16 16, auto !important;
        }

        :root {
            --bg-black: #060608;
            --bg-surface: #0c0c10;
            --bg-card: #121218;
            --bg-card-hover: #181822;
            --text-primary: #f6f6f8;
            --text-secondary: #9292a0;
            --accent-lime: #a8ff53;
            --accent-emerald: #00d665;
            --accent-glow: rgba(168, 255, 83, 0.45);
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(168, 255, 83, 0.5);
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
        }

        html, body {
            width: 100%;
            min-height: 100%;
            background-color: var(--bg-black);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            overflow-x: clip;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* Lenis Smooth Scroll Setup */
        html.lenis, html.lenis body {
            height: auto;
        }
        .lenis.lenis-smooth {
            scroll-behavior: auto !important;
        }

        /* ===================================================
           3D FULL ZOOM DOLLAR BILL VORTEX PORTAL
        =================================================== */
        #cash-zoom-portal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 99000;
            perspective: 1200px;
            overflow: hidden;
            opacity: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .zoom-dollar-bill {
            position: absolute;
            width: 360px;
            height: 510px;
            transform-style: preserve-3d;
            will-change: transform, opacity;
        }

        .zoom-dollar-bill img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            filter: drop-shadow(0 20px 40px rgba(0, 0, 0, 0.85));
        }

        /* ===================================================
           DOLLAR BILL CASCADE CANVAS (CASH RAIN)
        =================================================== */
        #cash-rain-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 98000;
            transition: opacity 0.5s var(--ease-out);
        }

        /* ===================================================
           LANDING SCREEN: THREE.JS LIQUID FLUID LOGO
        =================================================== */
        #liquid-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 90000;
            background-color: #000000;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            padding: 2.5rem 3.5rem;
            box-sizing: border-box;
            transition: opacity 1.1s var(--ease-out), visibility 1.1s;
        }

        #liquid-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
            z-index: 1;
        }

        .intro-top-bar {
            position: relative;
            z-index: 10;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.75);
            pointer-events: none;
        }

        .intro-brand-name {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            font-weight: 700;
            color: #ffffff;
        }

        .intro-brand-name img {
            width: 24px;
            height: 24px;
            border-radius: 50%;
        }

        .intro-bottom-bar {
            position: relative;
            z-index: 10;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.2rem;
            pointer-events: none;
        }

        .enter-experience-btn {
            pointer-events: auto;
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: #ffffff;
            background: rgba(168, 255, 83, 0.08);
            border: 1px solid var(--accent-lime);
            padding: 15px 36px;
            border-radius: 40px;
            display: flex;
            align-items: center;
            gap: 0.9rem;
            backdrop-filter: blur(12px);
            box-shadow: 0 0 30px var(--accent-glow);
            transition: all 0.35s var(--ease-out);
            outline: none;
        }

        .enter-experience-btn:hover {
            background: var(--accent-lime);
            color: #000000;
            transform: translateY(-2px) scale(1.04);
            box-shadow: 0 0 50px var(--accent-lime);
        }

        .intro-instruction {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.45);
        }

        /* ===================================================
           STICKY NAVIGATION BAR
        =================================================== */
        .site-nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1.2rem 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 80000;
            background: rgba(6, 6, 8, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            box-sizing: border-box;
            transition: transform 0.4s var(--ease-out);
        }

        .site-brand {
            display: flex;
            align-items: center;
            gap: 1rem;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.15rem;
            letter-spacing: 0.05em;
            color: #ffffff;
            text-decoration: none;
        }

        .brand-logo-badge {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            object-fit: cover;
            filter: drop-shadow(0 0 10px var(--accent-glow));
            transition: transform 0.4s var(--ease-out);
        }

        .site-brand:hover .brand-logo-badge {
            transform: rotate(180deg) scale(1.1);
        }

        .site-nav-menu {
            display: flex;
            gap: 2rem;
            list-style: none;
            align-items: center;
        }

        .site-nav-menu a {
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--text-secondary);
            text-decoration: none;
            transition: color 0.25s;
        }

        .site-nav-menu a:hover {
            color: var(--accent-lime);
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        /* ==========================================
           FLOATING STICKY WHATSAPP BUTTON (BOTTOM-RIGHT)
        ========================================== */
        .floating-whatsapp-btn {
            position: fixed;
            bottom: 28px;
            right: 28px;
            z-index: 85000;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45), 0 3px 8px rgba(0, 0, 0, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease;
            -webkit-tap-highlight-color: transparent;
        }

        .floating-whatsapp-btn:hover {
            transform: scale(1.1) translateY(-3px);
            box-shadow: 0 12px 32px rgba(37, 211, 102, 0.65), 0 4px 12px rgba(0, 0, 0, 0.4);
        }

        .floating-whatsapp-btn:active {
            transform: scale(0.96) translateY(0);
        }

        /* Pulsing green ring */
        .floating-whatsapp-btn::before {
            content: '';
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            border-radius: 50%;
            border: 2px solid #25D366;
            opacity: 0.8;
            animation: floating-wa-pulse 2.2s infinite ease-out;
            pointer-events: none;
        }

        @keyframes floating-wa-pulse {
            0% {
                transform: scale(0.95);
                opacity: 0.85;
            }
            70% {
                transform: scale(1.35);
                opacity: 0;
            }
            100% {
                transform: scale(1.4);
                opacity: 0;
            }
        }

        .floating-wa-icon {
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease;
        }

        .floating-whatsapp-btn:hover .floating-wa-icon {
            transform: rotate(6deg) scale(1.05);
        }

        .floating-wa-icon svg {
            width: 100%;
            height: 100%;
            fill: #ffffff;
            filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.25));
        }

        /* Desktop hover tooltip */
        .floating-wa-tooltip {
            position: absolute;
            right: 74px;
            background: rgba(10, 10, 14, 0.95);
            color: #ffffff;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.78rem;
            letter-spacing: 0.05em;
            padding: 8px 16px;
            border-radius: 20px;
            border: 1px solid rgba(37, 211, 102, 0.4);
            white-space: nowrap;
            opacity: 0;
            visibility: hidden;
            transform: translateX(10px);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            pointer-events: none;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.55);
        }

        .floating-wa-tooltip::after {
            content: '';
            position: absolute;
            right: -5px;
            top: 50%;
            transform: translateY(-50%) rotate(45deg);
            width: 8px;
            height: 8px;
            background: rgba(10, 10, 14, 0.95);
            border-top: 1px solid rgba(37, 211, 102, 0.4);
            border-right: 1px solid rgba(37, 211, 102, 0.4);
        }

        .floating-whatsapp-btn:hover .floating-wa-tooltip {
            opacity: 1;
            visibility: visible;
            transform: translateX(0);
        }

        @media (max-width: 768px) {
            .floating-whatsapp-btn {
                bottom: 20px;
                right: 20px;
                width: 54px;
                height: 54px;
            }
            .floating-wa-icon {
                width: 28px;
                height: 28px;
            }
            .floating-wa-tooltip {
                display: none;
            }
        }

        /* CASH RAIN TOGGLE SWITCH BUTTON */
        .cash-toggle-btn {
            font-family: 'Space Mono', monospace;
            font-size: 0.66rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            background: rgba(168, 255, 83, 0.12);
            border: 1.5px solid var(--accent-lime);
            color: #ffffff;
            padding: 6px 14px;
            border-radius: 30px;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            transition: all 0.3s var(--ease-out);
            outline: none;
            user-select: none;
            box-shadow: 0 0 16px var(--accent-glow);
        }

        .cash-toggle-btn:hover {
            transform: translateY(-1px) scale(1.02);
            box-shadow: 0 0 25px var(--accent-glow);
        }

        .cash-toggle-icon {
            font-size: 0.82rem;
            line-height: 1;
        }

        .cash-toggle-text {
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 0.1em;
        }

        .cash-toggle-badge {
            font-size: 0.6rem;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 10px;
            background: var(--accent-lime);
            color: #000000;
            letter-spacing: 0.1em;
            transition: all 0.25s;
        }

        .cash-toggle-switch {
            width: 26px;
            height: 14px;
            background: rgba(168, 255, 83, 0.35);
            border-radius: 10px;
            position: relative;
            transition: background 0.25s;
            display: inline-block;
        }

        .cash-toggle-knob {
            position: absolute;
            top: 1px;
            left: 13px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent-lime);
            box-shadow: 0 0 8px var(--accent-lime);
            transition: left 0.25s cubic-bezier(0.16, 1, 0.3, 1), background 0.25s;
        }

        /* OFF State (Default on Home Page) */
        .cash-toggle-btn.off {
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(255, 255, 255, 0.18);
            box-shadow: none;
            color: rgba(255, 255, 255, 0.5);
        }

        .cash-toggle-btn.off .cash-toggle-text {
            color: rgba(255, 255, 255, 0.55);
        }

        .cash-toggle-btn.off .cash-toggle-badge {
            background: rgba(255, 255, 255, 0.15);
            color: rgba(255, 255, 255, 0.6);
        }

        .cash-toggle-btn.off .cash-toggle-switch {
            background: rgba(255, 255, 255, 0.12);
        }

        .cash-toggle-btn.off .cash-toggle-knob {
            left: 2px;
            background: rgba(255, 255, 255, 0.4);
            box-shadow: none;
        }

        /* ===================================================
           HERO SECTION: RADICAL DIGITAL GROWTH
        =================================================== */
        .hero-statement-section {
            min-height: 100vh;
            width: 100%;
            background-color: var(--bg-black);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 8.5rem 3rem 4rem;
            position: relative;
            box-sizing: border-box;
            overflow: hidden;
        }

        .hero-logo-badge-center {
            width: 135px;
            height: 135px;
            border-radius: 50%;
            margin-bottom: 1.8rem;
            filter: drop-shadow(0 0 35px var(--accent-glow));
            transition: transform 0.5s var(--ease-out);
            position: relative;
        }

        .hero-logo-badge-center img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
        }

        .hero-logo-badge-center:hover {
            transform: scale(1.08) rotate(8deg);
        }

        .hero-meta-top {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--accent-lime);
            margin-bottom: 1.8rem;
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }

        .hero-meta-top::before, .hero-meta-top::after {
            content: '';
            width: 30px;
            height: 1px;
            background: rgba(168, 255, 83, 0.4);
        }

        .hero-giant-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(3.6rem, 10.5vw, 10.5rem);
            font-weight: 900;
            line-height: 0.9;
            letter-spacing: -0.05em;
            color: #ffffff;
            margin-bottom: 2.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .hero-giant-title .word-row {
            display: block;
            overflow: hidden;
        }

        .hero-giant-title .word-inner {
            display: inline-block;
            transform: translateY(0%);
            transition: transform 1.2s var(--ease-out);
        }

        .hero-giant-title .outline-row {
            color: transparent;
            -webkit-text-stroke: 1.5px var(--accent-lime);
            text-stroke: 1.5px var(--accent-lime);
            text-shadow: 0 0 35px var(--accent-glow);
        }

        /* Tagline from brochure */
        .hero-tagline-quote {
            max-width: 780px;
            font-size: 1.15rem;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.85);
            margin-bottom: 2.2rem;
            font-weight: 400;
        }

        .hero-tagline-quote strong {
            color: var(--accent-lime);
            font-weight: 600;
        }

        .hero-slogan-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            padding: 8px 20px;
            background: rgba(168, 255, 83, 0.08);
            border: 1px solid rgba(168, 255, 83, 0.3);
            border-radius: 30px;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.15em;
            color: var(--accent-lime);
            text-transform: uppercase;
            margin-bottom: 3.5rem;
        }

        .hero-bottom-grid {
            width: 100%;
            max-width: 1400px;
            display: grid;
            grid-template-columns: 1fr auto 1fr;
            align-items: flex-end;
            font-family: 'Space Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.12em;
            color: var(--text-secondary);
            border-top: 1px solid var(--border);
            padding-top: 2rem;
        }

        .hero-bottom-left {
            text-align: left;
            line-height: 1.8;
        }

        .hero-bottom-center {
            display: flex;
            justify-content: center;
        }

        .scroll-down-pill {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.6rem;
            color: var(--text-primary);
        }

        .scroll-down-pill span {
            font-size: 0.65rem;
            letter-spacing: 0.25em;
        }

        .scroll-down-line {
            width: 1px;
            height: 35px;
            background: linear-gradient(180deg, var(--accent-lime) 0%, transparent 100%);
            animation: scrollPulse 2s infinite ease-in-out;
        }

        @keyframes scrollPulse {
            0%, 100% { transform: scaleY(0.4); opacity: 0.3; }
            50% { transform: scaleY(1); opacity: 1; }
        }

        .hero-bottom-right {
            text-align: right;
            line-height: 1.8;
        }

        /* ===================================================
           SELECTED WORK: AUTO MOVEMENT SLIDER
        =================================================== */
        .work-section {
            width: 100%;
            padding: 7rem 0 7rem;
            background-color: var(--bg-black);
            position: relative;
            box-sizing: border-box;
            overflow: hidden;
            border-top: 1px solid var(--border);
        }

        .section-header-row {
            max-width: 1400px;
            margin: 0 auto 3.5rem;
            padding: 0 3.5rem;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }

        .section-tagline {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--accent-lime);
            display: block;
            margin-bottom: 0.8rem;
        }

        .section-headline {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2rem, 4vw, 3.2rem);
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.03em;
        }

        .slider-controls {
            display: flex;
            gap: 0.8rem;
        }

        .slider-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            outline: none;
        }

        .slider-btn:hover {
            border-color: var(--accent-lime);
            background: var(--accent-lime);
            color: #000000;
            transform: scale(1.08);
        }

        .auto-slider-container {
            width: 100%;
            overflow: hidden;
            position: relative;
            padding: 1.8rem 0;
            cursor: default;
        }

        .auto-slider-track {
            display: flex;
            gap: 1.5rem;
            width: max-content;
            animation: marqueeSlide 40s linear infinite;
            will-change: transform;
            transform: translateZ(0);
        }

        .auto-slider-track:hover {
            animation-play-state: paused;
        }

        @keyframes marqueeSlide {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(-280px * 9 - 1.5rem * 9)); }
        }

        .work-card {
            width: 280px;
            aspect-ratio: 9/16;
            flex-shrink: 0;
            background: #08090d;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            transition: transform 0.4s var(--ease-out), border-color 0.3s, box-shadow 0.3s;
        }

        .work-card:hover {
            transform: translateY(-8px) scale(1.02);
            border-color: var(--accent-lime);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85), 0 0 30px rgba(168, 255, 83, 0.25);
        }

        .work-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            background: #06070a;
            border-radius: 17px;
        }

        .work-sound-badge {
            position: absolute;
            bottom: 14px;
            right: 14px;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(10, 10, 15, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.25s ease;
            z-index: 5;
            padding: 0;
        }

        .work-card:hover .work-sound-badge {
            border-color: var(--accent-lime);
            background: rgba(10, 10, 15, 0.95);
            color: var(--accent-lime);
            transform: scale(1.08);
        }

        /* ===================================================
           ABOUT US & BRAND PHILOSOPHY SECTION
        =================================================== */
        .about-section {
            width: 100%;
            padding: 5.5rem 3.5rem 2.5rem;
            background-color: var(--bg-surface);
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            box-sizing: border-box;
            overflow: hidden;
        }

        .about-grid {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 0.85fr 1.15fr;
            column-gap: 4.5rem;
            row-gap: 0;
        }

        .about-sticky-col {
            position: relative;
            top: 0;
            height: fit-content;
            margin-top: -0.5rem;
        }

        .about-title {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2.2rem, 4vw, 3.6rem);
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -0.03em;
            color: #ffffff;
            margin-bottom: 2rem;
        }

        .about-quote-box {
            padding: 1.8rem;
            background: rgba(168, 255, 83, 0.05);
            border-left: 3px solid var(--accent-lime);
            border-radius: 0 8px 8px 0;
            margin-bottom: 0;
        }

        .about-quote-box p {
            font-family: 'Syne', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.4;
        }

        .about-stats-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
        }

        .stat-number {
            font-family: 'Syne', sans-serif;
            font-size: 2.4rem;
            font-weight: 900;
            color: var(--accent-lime);
            line-height: 1;
            margin-bottom: 0.4rem;
        }

        .stat-desc {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.1em;
            color: var(--text-secondary);
            text-transform: uppercase;
        }

        .about-content-col {
            display: flex;
            flex-direction: column;
            gap: 1.25rem;
        }

        .about-headline {
            font-family: 'Syne', sans-serif;
            font-size: clamp(1.6rem, 2.8vw, 2.4rem);
            font-weight: 700;
            line-height: 1.3;
            letter-spacing: -0.02em;
            color: #ffffff;
        }

        .about-body-text {
            font-size: 1.05rem;
            line-height: 1.85;
            color: var(--text-secondary);
            font-weight: 300;
        }

        /* ===================================================
           RIBBON TYPE COMPONENT (REACT BITS PRO)
           Full Screen-Fit 3D Satin Ribbon with Continuous Auto-Running Typography
        =================================================== */
        .about-ribbon-full-row {
            grid-column: 1 / -1;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            margin-top: 2rem;
        }

        .ribbon-type-wrapper {
            position: relative;
            width: 100%;
            margin-top: 0;
            background: transparent;
            border: none;
            box-shadow: none;
            padding: 0;
            overflow: hidden;
        }

        .ribbon-type-canvas-container {
            width: 100%;
            height: 165px;
            position: relative;
            background: transparent;
            overflow: hidden;
            cursor: grab;
            touch-action: none;
        }

        .ribbon-type-canvas-container:active {
            cursor: grabbing;
        }

        #ribbon-type-canvas {
            width: 100%;
            height: 100%;
            display: block;
        }

        /* ===================================================
           OUR SERVICES / WHAT WE OFFER SECTION
           (BounceCards Physics Engine from React Bits)
        =================================================== */
        .services-section {
            width: 100%;
            padding: 8rem 3.5rem;
            background-color: var(--bg-black);
            box-sizing: border-box;
            border-bottom: 1px solid var(--border);
            overflow: hidden;
            position: relative;
        }

        .services-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .services-header-wrap {
            margin-bottom: 3.5rem;
            max-width: 800px;
        }

        /* BounceCards Interactive Container */
        .bounce-cards-stage-wrap {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .bounce-cards {
            position: relative;
            touch-action: none;
            -webkit-tap-highlight-color: transparent;
            width: 100%;
            max-width: 1400px;
            height: 560px;
            perspective: 1200px;
            user-select: none;
        }

        /* Service Cards with BounceCards spring physics */
        .bounce-cards__card.service-card {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 350px;
            min-height: 480px;
            max-height: 510px;
            background: var(--bg-card); /* EXACT ORIGINAL COLOR */
            border: 1px solid var(--border); /* EXACT ORIGINAL BORDER */
            border-radius: 16px;
            padding: 2.2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.65), 0 1px 3px rgba(255, 255, 255, 0.05);
            transform: translate(-50%, -50%) scale(0);
            transition: box-shadow 0.3s ease, border-color 0.3s ease;
            will-change: transform;
            box-sizing: border-box;
        }

        .bounce-cards__card.service-card:hover,
        .bounce-cards__card.service-card[data-active] {
            border-color: var(--accent-lime);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(160, 255, 100, 0.28);
        }

        .bounce-cards__card.service-card:focus-visible {
            outline: 2px solid var(--accent-lime);
            outline-offset: 3px;
        }

        .service-top-row {
            display: flex;
            justify-content: flex-end;
            align-items: center;
            margin-bottom: 1.2rem;
        }

        .service-icon-box {
            display: none;
        }

        .service-num {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            color: var(--accent-lime);
            letter-spacing: 0.15em;
        }

        .service-title {
            font-family: 'Syne', sans-serif;
            font-size: 1.45rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.8rem;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }

        .service-desc {
            font-size: 0.9rem;
            line-height: 1.65;
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            font-weight: 300;
        }

        .service-features-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            border-top: 1px solid var(--border);
            padding-top: 1.2rem;
            margin: 0;
        }

        .service-features-list li {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: rgba(255, 255, 255, 0.85);
            display: flex;
            align-items: center;
            gap: 0.7rem;
            letter-spacing: 0.04em;
            line-height: 1.35;
        }

        .service-features-list li::before {
            content: '';
            display: inline-block;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent-lime);
            box-shadow: 0 0 8px rgba(168, 255, 83, 0.7);
            flex-shrink: 0;
        }

        /* BounceCards Dock & Indicator Bar */
        .bounce-cards-dock {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            max-width: 1200px;
            margin-top: 2rem;
            padding: 0 0.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .bounce-cards-hint {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-secondary);
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .bounce-pulse-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-lime);
            animation: pulse-glow 2s infinite;
        }

        .bounce-pills-list {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .bounce-pill-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: rgba(255, 255, 255, 0.75);
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 6px 14px;
            border-radius: 100px;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        .bounce-pill-btn:hover {
            border-color: var(--accent-lime);
            color: var(--accent-lime);
            background: rgba(160, 255, 100, 0.1);
        }

        .bounce-pill-btn.active {
            background: var(--accent-lime);
            color: #000000;
            border-color: var(--accent-lime);
            box-shadow: 0 0 16px rgba(160, 255, 100, 0.4);
        }

        .bounce-nav-arrows {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .bounce-arrow-btn {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.05);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.2s;
        }

        .bounce-arrow-btn:hover {
            border-color: var(--accent-lime);
            color: var(--accent-lime);
            background: rgba(160, 255, 100, 0.1);
            transform: scale(1.08);
        }

        /* Services Component Responsive Modes:
           Desktop (> 868px): Interactive BounceCards Physics Stage
           Mobile (<= 868px): Touch Swipe Media Stack (scd-20)
        ============================================================ */
        .services-mobile-deck {
            display: none !important;
        }

        @media (min-width: 869px) {
            .bounce-cards-stage-wrap {
                display: flex !important;
            }
            .services-mobile-deck {
                display: none !important;
            }
        }

        @media (max-width: 992px) {
            .bounce-cards {
                height: 530px;
            }
            .bounce-cards__card.service-card {
                width: 300px;
                min-height: 440px;
                padding: 1.8rem;
            }
            .service-title {
                font-size: 1.3rem;
            }
            .service-desc {
                font-size: 0.85rem;
            }
        }

        @media (max-width: 868px) {
            /* Switch from BounceCards stage to Touch Swipe Stack on mobile */
            .bounce-cards-stage-wrap {
                display: none !important;
            }

            .services-mobile-deck.scd-20 {
                display: flex !important;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 20px;
                width: 100%;
                padding: 15px 0 25px;
                position: relative;
                box-sizing: border-box;
            }

            .scd-20__deck {
                position: relative;
                width: min(330px, calc(100vw - 36px));
                max-width: 100%;
                height: 480px;
                margin: 0 auto 18px;
                perspective: 1000px;
            }

            .scd-20__card {
                position: absolute;
                inset: 0;
                border-radius: 20px;
                overflow: hidden;
                background: var(--bg-card);
                border: 1px solid var(--border);
                box-shadow: 0 20px 45px -18px rgba(0, 0, 0, 0.95), 0 0 25px rgba(0, 214, 101, 0.05);
                transform: translate3d(0, calc(min(var(--d, 0), 3) * 10px), 0) scale(calc(1 - min(var(--d, 0), 3) * 0.04));
                z-index: calc(10 - var(--d, 0));
                transition: transform 0.45s cubic-bezier(0.3, 0.9, 0.3, 1), opacity 0.45s cubic-bezier(0.3, 0.9, 0.3, 1), border-color 0.3s ease;
                touch-action: none;
                cursor: grab;
                user-select: none;
                -webkit-user-select: none;
                will-change: transform;
                box-sizing: border-box;
                padding: 1.5rem 1.35rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }

            .scd-20__card[style*="--d: 0"],
            .scd-20__card[style*="--d:0"] {
                border-color: rgba(168, 255, 83, 0.4);
                box-shadow: 0 24px 50px -18px rgba(0, 0, 0, 0.95), 0 0 30px rgba(168, 255, 83, 0.14);
            }

            .scd-20__card.scd-20__drag {
                transition: none !important;
                cursor: grabbing;
                box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.98), 0 0 35px rgba(168, 255, 83, 0.28);
            }

            .scd-20__card.scd-20__fly {
                opacity: 0 !important;
                pointer-events: none;
            }

            .scd-20__card .service-top-row {
                display: flex;
                justify-content: flex-end;
                align-items: center;
                margin-bottom: 0.9rem;
            }

            .scd-20__card .service-icon-box {
                display: none;
            }

            .scd-20__card .service-num {
                font-family: 'Space Mono', monospace;
                font-size: 0.72rem;
                color: var(--accent-lime);
                letter-spacing: 0.15em;
            }

            .scd-20__card .service-title {
                font-family: 'Syne', sans-serif;
                font-size: 1.3rem;
                font-weight: 800;
                color: #ffffff;
                margin-bottom: 0.6rem;
                letter-spacing: -0.02em;
                line-height: 1.25;
            }

            .scd-20__card .service-desc {
                font-size: 0.84rem;
                line-height: 1.6;
                color: var(--text-secondary);
                margin-bottom: 1rem;
                font-weight: 300;
            }

            .scd-20__card .service-features-list {
                list-style: none;
                display: flex;
                flex-direction: column;
                gap: 0.55rem;
                border-top: 1px solid var(--border);
                padding-top: 1rem;
                margin: 0;
            }

            .scd-20__card .service-features-list li {
                font-family: 'Space Mono', monospace;
                font-size: 0.68rem;
                color: rgba(255, 255, 255, 0.88);
                display: flex;
                align-items: center;
                gap: 0.6rem;
                letter-spacing: 0.03em;
                line-height: 1.35;
            }

            .scd-20__card .service-features-list li::before {
                content: '';
                display: inline-block;
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: var(--accent-lime);
                box-shadow: 0 0 8px rgba(168, 255, 83, 0.7);
                flex-shrink: 0;
            }

            .scd-20__ctl {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 10px;
                width: min(330px, calc(100vw - 36px));
                max-width: 100%;
                margin: 0 auto;
            }

            .scd-20__ctl button {
                width: 44px;
                height: 44px;
                flex-shrink: 0;
                border-radius: 50%;
                border: 1px solid rgba(255, 255, 255, 0.14);
                background: #151722;
                color: #ffffff;
                font-size: 24px;
                line-height: 1;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
                -webkit-tap-highlight-color: transparent;
            }

            .scd-20__ctl button:hover,
            .scd-20__ctl button:active {
                background: rgba(168, 255, 83, 0.12);
                border-color: var(--accent-lime);
                color: var(--accent-lime);
                transform: scale(1.06);
            }

            .scd-20__ctl button:focus-visible {
                outline: 2px solid var(--accent-lime);
                outline-offset: 2px;
            }

            .scd-20__ctl p {
                color: #ffffff;
                font-family: 'Space Mono', monospace;
                font-size: 0.72rem;
                letter-spacing: 0.03em;
                flex: 1;
                text-align: center;
                padding: 8px 10px;
                border-radius: 20px;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }

            .scd-20__hint {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 6px;
                font-family: 'Space Mono', monospace;
                font-size: 0.65rem;
                color: var(--text-secondary);
                letter-spacing: 0.12em;
                text-transform: uppercase;
                opacity: 0.75;
                margin-top: -6px;
            }

            .scd-20__hint .pulse-dot {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: var(--accent-lime);
                animation: pulseGlow 2s infinite ease-in-out;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            .scd-20__card {
                transition: transform .2s, opacity .2s;
            }
        }


        /* ===================================================
           PRICE PACKAGES: SHADER CARD COMPONENT (REACT BITS PRO)
           3D Interactive WebGL Flame Shader with Pointer Wind Reaction
        =================================================== */
        .pricing-section {
            width: 100%;
            padding: 8rem 3.5rem;
            background-color: var(--bg-surface);
            box-sizing: border-box;
            border-bottom: 1px solid var(--border);
            position: relative;
            overflow: visible;
        }

        .pricing-container {
            max-width: 1400px;
            margin: 0 auto;
            position: relative;
            z-index: 2;
        }

        .pricing-header-wrap {
            text-align: center;
            max-width: 750px;
            margin: 0 auto 5rem;
        }

        .pricing-scroll-pin-wrapper {
            display: contents;
        }

        .pricing-sticky-viewport {
            display: contents;
        }

        .pricing-mobile-progress {
            display: none !important;
        }

        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2.2rem;
            align-items: stretch;
            perspective: 1200px;
        }

        /* Shader Card Container */
        .pricing-card.shader-card {
            background: rgba(12, 14, 20, 0.82);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 18px;
            padding: 2.8rem 2.2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: visible; /* Allows badge to float freely above top border */
            transform-style: preserve-3d;
            transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1),
                        border-color 0.4s ease,
                        box-shadow 0.4s ease;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
            will-change: transform;
        }

        .shader-card-dark-layer {
            position: absolute;
            inset: 0;
            border-radius: 18px;
            background: radial-gradient(circle at 50% 45%, rgba(10, 12, 18, 0.65) 0%, rgba(6, 8, 12, 0.88) 100%);
            z-index: 2;
            pointer-events: none;
        }

        .pricing-card.shader-card:hover {
            border-color: rgba(160, 255, 100, 0.5);
            box-shadow: 0 30px 70px rgba(0, 0, 0, 0.95), 0 0 45px rgba(160, 255, 100, 0.25);
        }

        /* Shader canvas wrapper sitting directly in the background */
        .shader-card-canvas-wrap {
            position: absolute;
            inset: 0;
            overflow: hidden;
            border-radius: 18px;
            pointer-events: none;
            z-index: 1;
        }

        .shader-card-canvas {
            width: 100%;
            height: 100%;
            display: block;
            opacity: 0.82;
            transition: opacity 0.5s ease;
            filter: blur(3px) contrast(1.25);
            mix-blend-mode: screen;
        }

        .pricing-card.shader-card:hover .shader-card-canvas {
            opacity: 1;
            filter: blur(2px) contrast(1.35);
        }

        /* Ambient luminous glow on card frame */
        .shader-card-glow {
            position: absolute;
            inset: -2px;
            border-radius: 20px;
            pointer-events: none;
            z-index: 0;
            opacity: 0;
            transition: opacity 0.4s ease;
            background: radial-gradient(circle at var(--mouse-x, 50%) var(--mouse-y, 50%), var(--card-glow-color, rgba(160, 255, 100, 0.35)), transparent 70%);
        }

        .pricing-card.shader-card:hover .shader-card-glow {
            opacity: 1;
        }

        /* Highlighted Growth Package (Popular Choice) */
        .pricing-card.shader-card.featured {
            border: 2px solid var(--accent-lime);
            box-shadow: 0 0 50px rgba(160, 255, 100, 0.25), 0 25px 60px rgba(0, 0, 0, 0.9);
            transform: scale(1.03);
        }

        .pricing-card.shader-card.featured:hover {
            border-color: #c8ff00;
            box-shadow: 0 0 70px rgba(160, 255, 100, 0.45), 0 30px 80px rgba(0, 0, 0, 0.95);
        }

        .pricing-badge {
            position: absolute;
            top: -14px;
            left: 50%;
            transform: translateX(-50%) translateZ(30px);
            background: var(--accent-lime);
            color: #000000;
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            padding: 5px 18px;
            border-radius: 20px;
            text-transform: uppercase;
            box-shadow: 0 0 20px rgba(160, 255, 100, 0.6);
            z-index: 10;
        }

        /* Card Content Layer - elevated in 3D */
        .shader-card-content {
            position: relative;
            z-index: 3;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transform: translateZ(20px);
            pointer-events: auto;
        }

        .pricing-tier-name {
            font-family: 'Syne', sans-serif;
            font-size: 1.6rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }

        .pricing-tier-desc {
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            line-height: 1.5;
        }

        .pricing-price-wrap {
            display: flex;
            align-items: baseline;
            gap: 0.3rem;
            margin-bottom: 2.2rem;
            padding-bottom: 1.8rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .pricing-currency {
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 900;
            color: var(--accent-lime);
        }

        .pricing-amount {
            font-family: 'Syne', sans-serif;
            font-size: 3.2rem;
            font-weight: 900;
            color: #ffffff;
            line-height: 1;
        }

        .pricing-period {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: var(--text-secondary);
            margin-left: 0.4rem;
        }

        .pricing-checklist {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 1.1rem;
            margin-bottom: 2.8rem;
            padding: 0;
        }

        .pricing-checklist li {
            font-size: 0.92rem;
            color: rgba(255, 255, 255, 0.88);
            display: flex;
            align-items: flex-start;
            gap: 0.8rem;
            line-height: 1.4;
        }

        .pricing-check-icon {
            color: var(--accent-lime);
            font-weight: 700;
            font-size: 1rem;
            flex-shrink: 0;
        }

        .pricing-cta-btn {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            font-weight: 700;
            padding: 14px 24px;
            border-radius: 30px;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.8rem;
            transition: all 0.3s;
            text-align: center;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--accent-lime);
            color: var(--accent-lime);
            transform: translateZ(25px);
        }

        .pricing-card.featured .pricing-cta-btn {
            background: var(--accent-lime);
            color: #000000;
            box-shadow: 0 0 25px var(--accent-glow);
        }

        .pricing-cta-btn:hover {
            background: var(--accent-lime);
            color: #000000;
            box-shadow: 0 0 35px var(--accent-glow);
            transform: translateZ(35px) scale(1.02);
        }


        /* ===================================================
           CUSTOM TECH CALLOUT BANNER (WEB, 3D & SOFTWARE)
        =================================================== */
        .pricing-custom-callout {
            margin-top: 4.5rem;
            background: radial-gradient(ellipse at 50% -20%, rgba(26, 32, 46, 0.9) 0%, rgba(12, 14, 20, 0.97) 70%, rgba(8, 10, 14, 0.99) 100%);
            border: 1px solid rgba(168, 255, 83, 0.35);
            border-radius: 22px;
            padding: 3.2rem 3rem;
            display: flex;
            flex-direction: column;
            gap: 2.2rem;
            box-shadow: 0 25px 65px rgba(0, 0, 0, 0.85), 0 0 35px rgba(168, 255, 83, 0.08);
            position: relative;
            overflow: hidden;
        }

        .pricing-custom-callout::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent 0%, var(--accent-lime) 50%, transparent 100%);
            opacity: 0.9;
        }

        .callout-top-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 2.5rem;
            width: 100%;
        }

        .callout-header-content {
            flex: 1;
            max-width: 680px;
        }

        .callout-header-cta-wrap {
            flex-shrink: 0;
            width: 360px;
        }

        .clients-showcase-btn {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            background: linear-gradient(145deg, rgba(20, 26, 38, 0.9) 0%, rgba(12, 15, 22, 0.98) 100%);
            border: 1.5px solid rgba(168, 255, 83, 0.45);
            border-radius: 18px;
            padding: 1.35rem 1.6rem;
            text-decoration: none;
            color: #ffffff;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(168, 255, 83, 0.05);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }

        .clients-showcase-btn:hover {
            transform: translateY(-4px) scale(1.02);
            border-color: var(--accent-lime);
            box-shadow: 0 20px 45px rgba(168, 255, 83, 0.25), 0 0 25px rgba(168, 255, 83, 0.18);
        }

        .showcase-btn-top {
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .showcase-live-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-lime);
            box-shadow: 0 0 10px var(--accent-lime);
            animation: pulse-dot 2s infinite ease-in-out;
        }

        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.85); }
        }

        .showcase-pill-tag {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.14em;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            border: 1px solid rgba(168, 255, 83, 0.3);
            padding: 3px 10px;
            border-radius: 20px;
            font-weight: 700;
        }

        .showcase-arrow {
            margin-left: auto;
            color: var(--accent-lime);
            font-size: 1.15rem;
            font-weight: 700;
            transition: transform 0.25s ease;
        }

        .clients-showcase-btn:hover .showcase-arrow {
            transform: translate(3px, -3px);
        }

        .showcase-btn-title {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            line-height: 1.25;
            letter-spacing: 0.01em;
            color: #ffffff;
            transition: color 0.25s ease;
        }

        .clients-showcase-btn:hover .showcase-btn-title {
            color: var(--accent-lime);
        }

        .showcase-btn-sub {
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            color: var(--text-secondary);
            line-height: 1.45;
        }

        .showcase-btn-action {
            display: inline-flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.5rem;
            margin-top: 0.2rem;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            background: var(--accent-lime);
            color: #000000;
            padding: 8px 16px;
            border-radius: 30px;
            transition: all 0.25s ease;
        }

        .clients-showcase-btn:hover .showcase-btn-action {
            background: #ffffff;
            box-shadow: 0 0 16px rgba(255, 255, 255, 0.4);
        }

        .callout-eyebrow {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.22em;
            color: var(--accent-lime);
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 0.8rem;
            font-weight: 700;
        }

        .callout-header-content h4 {
            font-family: 'Syne', sans-serif;
            font-size: clamp(1.45rem, 2.6vw, 2.2rem);
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.8rem;
            line-height: 1.25;
            letter-spacing: -0.02em;
        }

        .callout-header-content p {
            font-size: 0.96rem;
            color: var(--text-secondary);
            line-height: 1.65;
        }

        /* 3-Column Offerings Grid within the Box */
        .callout-offerings-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.6rem;
            align-items: stretch;
            margin-top: 0.5rem;
        }

        .callout-subcard {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.09);
            border-radius: 16px;
            padding: 2rem 1.8rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 1.8rem;
            transition: transform 0.3s var(--ease-out), border-color 0.3s ease, background 0.3s ease, box-shadow 0.3s ease;
            position: relative;
        }

        .callout-subcard:hover {
            transform: translateY(-5px);
            border-color: rgba(168, 255, 83, 0.65);
            background: rgba(255, 255, 255, 0.05);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.65), 0 0 25px rgba(168, 255, 83, 0.12);
        }

        .callout-subcard.highlighted {
            background: rgba(168, 255, 83, 0.04);
            border: 1.5px solid rgba(168, 255, 83, 0.45);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 22px rgba(168, 255, 83, 0.08);
        }

        .callout-subcard.highlighted:hover {
            border-color: var(--accent-lime);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.75), 0 0 35px rgba(168, 255, 83, 0.25);
        }

        /* Default: hide mobile callout slider controls on desktop */
        .callout-mobile-nav,
        .callout-mobile-bottom-ctl {
            display: none;
        }

        .subcard-top {
            display: flex;
            flex-direction: column;
            gap: 0.65rem;
        }

        .subcard-pill {
            font-family: 'Space Mono', monospace;
            font-size: 0.64rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            border: 1px solid rgba(168, 255, 83, 0.25);
            padding: 3px 10px;
            border-radius: 12px;
            width: fit-content;
        }

        .subcard-title {
            font-family: 'Syne', sans-serif;
            font-size: 1.4rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.02em;
        }

        .subcard-desc {
            font-size: 0.86rem;
            color: var(--text-secondary);
            line-height: 1.55;
        }

        .subcard-bottom {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            padding-top: 1.4rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }

        .subcard-price-row {
            display: flex;
            align-items: baseline;
            gap: 0.4rem;
        }

        .subcard-price-val {
            font-family: 'Syne', sans-serif;
            font-size: 2.2rem;
            font-weight: 900;
            color: var(--accent-lime);
            line-height: 1;
        }

        .subcard-price-sub {
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            color: var(--text-secondary);
            letter-spacing: 0.05em;
        }

        .subcard-btn {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 12px 18px;
            border-radius: 30px;
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: all 0.25s ease;
        }

        .subcard-btn.btn-lime {
            background: var(--accent-lime);
            color: #000000;
            border: 1px solid var(--accent-lime);
        }

        .subcard-btn.btn-lime:hover {
            background: #bbf86e;
            transform: translateY(-2px);
            box-shadow: 0 0 20px rgba(168, 255, 83, 0.5);
        }

        .subcard-btn.btn-outline {
            background: rgba(168, 255, 83, 0.08);
            border: 1px solid rgba(168, 255, 83, 0.4);
            color: var(--accent-lime);
        }

        .subcard-btn.btn-outline:hover {
            background: var(--accent-lime);
            color: #000000;
            transform: translateY(-2px);
            box-shadow: 0 0 20px rgba(168, 255, 83, 0.45);
        }

        @media (max-width: 992px) {
            .pricing-custom-callout {
                padding: 2.2rem 1.6rem;
            }
        }

        /* ===================================================
           ELASTIC REEL COMPONENT - REACT BITS PRO
           Why Choose Us: 8 Slices Dock with Fisheye Swell
        =================================================== */
        .why-section {
            width: 100%;
            padding: 8rem 3.5rem;
            background-color: var(--bg-black);
            box-sizing: border-box;
            border-bottom: 1px solid var(--border);
            overflow: hidden;
            position: relative;
        }

        .why-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .elastic-reel-wrap {
            position: relative;
            width: 100%;
            margin-top: 1.5rem;
        }

        .elastic-reel {
            display: flex;
            align-items: stretch;
            height: 520px;
            width: 100%;
            gap: 12px;
            border-radius: 24px;
            overflow: hidden;
            background: rgba(12, 14, 20, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.85), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            padding: 12px;
            box-sizing: border-box;
            position: relative;
        }

        .elastic-slice {
            position: relative;
            flex: 1 1 0%;
            min-width: 68px;
            border-radius: 18px;
            overflow: hidden;
            cursor: pointer;
            transition: flex 0.65s cubic-bezier(0.34, 1.56, 0.64, 1),
                        transform 0.4s ease,
                        box-shadow 0.4s ease,
                        border-color 0.4s ease;
            user-select: none;
            background-color: #12151e;
            border: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            will-change: flex;
        }

        .elastic-slice:hover {
            border-color: rgba(160, 255, 100, 0.4);
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.7);
        }

        .elastic-slice.is-active {
            flex: 5.5 1 0%;
            border-color: var(--accent-lime);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9), 0 0 35px rgba(160, 255, 100, 0.25);
            cursor: default;
        }

        .elastic-slice.is-neighbor {
            flex: 1.6 1 0%;
        }

        .elastic-slice-bg {
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center;
            transform: scale(1.02);
            transition: transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.6s ease;
            filter: brightness(0.48) contrast(1.15) saturate(0.85);
        }

        .elastic-slice:hover .elastic-slice-bg,
        .elastic-slice.is-active .elastic-slice-bg {
            filter: brightness(0.72) contrast(1.1) saturate(1.15);
            transform: scale(1.08);
        }

        .elastic-slice-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(8,10,14,0.1) 0%, rgba(8,10,14,0.65) 45%, rgba(6,7,10,0.96) 100%);
            transition: opacity 0.5s ease;
        }

        .elastic-slice.is-active .elastic-slice-overlay {
            background: linear-gradient(180deg, rgba(8,10,14,0.15) 0%, rgba(8,10,14,0.7) 45%, rgba(6,7,10,0.98) 100%);
        }

        /* Collapsed Teaser view: shown when slice is resting or narrow */
        .elastic-slice-collapsed {
            position: absolute;
            inset: 0;
            padding: 24px 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            z-index: 2;
            pointer-events: none;
            transition: opacity 0.35s ease, transform 0.4s ease;
        }

        .elastic-slice.is-active .elastic-slice-collapsed {
            opacity: 0;
            transform: translateY(14px);
            pointer-events: none;
        }

        .elastic-col-num {
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--accent-lime);
            letter-spacing: 0.12em;
            background: rgba(0, 0, 0, 0.7);
            padding: 6px 9px;
            border-radius: 8px;
            border: 1px solid rgba(160, 255, 100, 0.35);
        }

        .elastic-col-title-vertical {
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            font-family: 'Syne', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: rgba(255, 255, 255, 0.85);
            white-space: nowrap;
            margin: auto 0;
            text-shadow: 0 2px 10px rgba(0,0,0,0.9);
        }

        .elastic-col-indicator {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transition: background 0.3s, transform 0.3s;
        }

        .elastic-slice:hover .elastic-col-indicator {
            background: var(--accent-lime);
            box-shadow: 0 0 10px var(--accent-lime);
            transform: scale(1.4);
        }

        /* Expanded content view */
        .elastic-slice-expanded {
            position: relative;
            z-index: 3;
            padding: 36px 40px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            opacity: 0;
            transform: translateY(22px);
            pointer-events: none;
            transition: opacity 0.45s 0.1s ease, transform 0.45s 0.1s cubic-bezier(0.34, 1.56, 0.64, 1);
            max-width: 600px;
        }

        .elastic-slice.is-active .elastic-slice-expanded {
            opacity: 1;
            transform: translateY(0);
            pointer-events: auto;
        }

        .elastic-exp-badge-row {
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .elastic-exp-num {
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--accent-lime);
            letter-spacing: 0.15em;
            background: rgba(160, 255, 100, 0.12);
            border: 1px solid var(--accent-lime);
            padding: 5px 12px;
            border-radius: 100px;
        }

        .elastic-exp-tag {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: rgba(255, 255, 255, 0.7);
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .elastic-exp-title {
            font-family: 'Syne', sans-serif;
            font-size: 2.1rem;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.15;
            letter-spacing: -0.02em;
            margin: 0;
            text-shadow: 0 4px 18px rgba(0, 0, 0, 0.8);
        }

        .elastic-exp-desc {
            font-size: 0.95rem;
            line-height: 1.7;
            color: rgba(255, 255, 255, 0.85);
            margin: 0;
            max-width: 500px;
        }

        .elastic-exp-footer {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-top: 8px;
        }

        .elastic-cta-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 22px;
            background: var(--accent-lime);
            color: #000;
            font-family: 'Space Mono', monospace;
            font-size: 0.78rem;
            font-weight: 700;
            border-radius: 100px;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .elastic-cta-pill:hover {
            transform: scale(1.05);
            box-shadow: 0 0 24px rgba(160, 255, 100, 0.55);
        }

        /* Reel Controls & Dock Dots */
        .elastic-dock-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 1.8rem;
            padding: 0 0.5rem;
        }

        .elastic-dock-hint {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            color: var(--text-secondary);
            letter-spacing: 0.08em;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .elastic-dock-hint span.pulse-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-lime);
            animation: pulse-glow 2s infinite;
        }

        .elastic-dots-list {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .elastic-dot-btn {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.1);
            cursor: pointer;
            padding: 0;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .elastic-dot-btn:hover {
            background: rgba(160, 255, 100, 0.5);
            border-color: var(--accent-lime);
            transform: scale(1.25);
        }

        .elastic-dot-btn.active {
            width: 28px;
            border-radius: 100px;
            background: var(--accent-lime);
            border-color: var(--accent-lime);
            box-shadow: 0 0 14px rgba(160, 255, 100, 0.45);
        }

        .elastic-nav-arrows {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .elastic-arrow-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.05);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.1rem;
            transition: all 0.2s;
        }

        .elastic-arrow-btn:hover {
            border-color: var(--accent-lime);
            color: var(--accent-lime);
            background: rgba(160, 255, 100, 0.1);
            transform: scale(1.08);
        }

        @keyframes pulse-glow {
            0%, 100% { opacity: 0.4; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.2); }
        }

        /* Mobile & Tablet Responsiveness */
        @media (max-width: 992px) {
            .elastic-reel {
                height: 480px;
                gap: 8px;
                padding: 8px;
            }
            .elastic-slice {
                min-width: 52px;
            }
            .elastic-slice-expanded {
                padding: 26px 22px;
            }
            .elastic-exp-title {
                font-size: 1.6rem;
            }
            .elastic-exp-desc {
                font-size: 0.88rem;
            }
        }

        @media (max-width: 768px) {
            .elastic-reel {
                flex-direction: column;
                height: auto;
                gap: 10px;
                padding: 0;
                background: transparent;
                border: none;
                box-shadow: none;
            }
            .elastic-slice {
                min-height: 84px;
                height: 84px;
                flex: none;
                width: 100%;
                border-radius: 14px;
                transition: height 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            }
            .elastic-slice.is-active {
                height: 360px;
                flex: none;
            }
            .elastic-slice-collapsed {
                flex-direction: row;
                padding: 18px 22px;
                align-items: center;
            }
            .elastic-col-title-vertical {
                writing-mode: horizontal-tb;
                transform: none;
                font-size: 1.05rem;
                margin: 0;
            }
            .elastic-slice-expanded {
                padding: 26px 22px;
                gap: 12px;
            }
            .elastic-exp-title {
                font-size: 1.45rem;
            }
            .elastic-dock-bar {
                flex-direction: column;
                gap: 14px;
                align-items: center;
            }
        }
        /* ===================================================
           INSTAGRAM DIRECT FROM @SAVKAR_MEDIA
        =================================================== */
        .instagram-direct-section {
            width: 100%;
            padding: 8rem 3.5rem;
            background-color: var(--bg-surface);
            box-sizing: border-box;
            border-bottom: 1px solid var(--border);
        }

        .insta-header-wrap {
            max-width: 1400px;
            margin: 0 auto 3.5rem;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            padding-bottom: 2rem;
            border-bottom: 1px solid var(--border);
        }

        .insta-profile-bar {
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }

        .insta-avatar-big {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            filter: drop-shadow(0 0 20px var(--accent-glow));
            object-fit: cover;
        }

        .insta-title {
            font-family: 'Syne', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            color: #ffffff;
        }

        .insta-btn-link {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            padding: 12px 28px;
            border-radius: 30px;
            background: transparent;
            border: 1px solid var(--accent-lime);
            color: var(--accent-lime);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.8rem;
            transition: all 0.3s;
        }

        .insta-btn-link:hover {
            background: var(--accent-lime);
            color: #000000;
            box-shadow: 0 0 30px var(--accent-glow);
        }

        .insta-live-badge {
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            color: var(--accent-lime);
            letter-spacing: 0.1em;
            background: rgba(168, 255, 83, 0.1);
            border: 1px solid rgba(168, 255, 83, 0.25);
            padding: 3px 9px;
            border-radius: 20px;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        .insta-subtitle {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-top: 0.4rem;
            line-height: 1.5;
        }

        .insta-reels-grid {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.8rem;
        }

        .reel-tile {
            aspect-ratio: 9/16;
            background: #08080c;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            user-select: none;
            transition: transform 0.35s cubic-bezier(0.2, 0.9, 0.3, 1), border-color 0.3s, box-shadow 0.3s;
            will-change: transform;
        }

        .reel-tile:hover {
            transform: translateY(-6px) scale(1.015);
            border-color: rgba(168, 255, 83, 0.45);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8), 0 0 25px rgba(168, 255, 83, 0.18);
        }

        .reel-tile.is-playing {
            border-color: var(--accent-lime);
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.85), 0 0 35px rgba(168, 255, 83, 0.3);
        }

        .reel-video {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            background: #0d0e14;
            pointer-events: none;
        }

        .reel-overlay {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 1.35rem;
            box-sizing: border-box;
            background: linear-gradient(180deg, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.05) 40%, rgba(0,0,0,0.85) 100%);
            transition: background 0.3s ease;
            z-index: 2;
        }

        .reel-tile.is-playing .reel-overlay {
            background: linear-gradient(180deg, rgba(0,0,0,0.45) 0%, rgba(0,0,0,0) 45%, rgba(0,0,0,0.85) 100%);
        }

        .reel-top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            z-index: 3;
        }

        .reel-tag {
            font-family: 'Space Mono', monospace;
            font-size: 0.62rem;
            letter-spacing: 0.14em;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            border: 1px solid rgba(168, 255, 83, 0.25);
            padding: 4px 10px;
            border-radius: 20px;
            backdrop-filter: blur(6px);
            font-weight: 700;
        }

        .reel-top-actions {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .reel-action-btn {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.25s ease;
            padding: 0;
        }

        .reel-action-btn:hover {
            background: var(--accent-lime);
            color: #000000;
            border-color: var(--accent-lime);
            transform: scale(1.1);
        }

        .reel-sound-btn.is-unmuted {
            background: var(--accent-lime);
            color: #000000;
            border-color: var(--accent-lime);
            box-shadow: 0 0 12px rgba(168, 255, 83, 0.45);
        }

        .reel-center-play {
            width: 58px;
            height: 58px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.55);
            backdrop-filter: blur(10px);
            border: 1.5px solid rgba(255, 255, 255, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #ffffff;
            font-size: 1.25rem;
            align-self: center;
            transition: all 0.3s cubic-bezier(0.2, 0.9, 0.3, 1);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
            z-index: 3;
        }

        .reel-tile:hover .reel-center-play {
            background: var(--accent-lime);
            color: #000000;
            border-color: var(--accent-lime);
            transform: scale(1.12);
            box-shadow: 0 0 25px var(--accent-glow);
        }

        .reel-tile.is-playing .reel-center-play {
            opacity: 0;
            transform: scale(0.7);
            pointer-events: none;
        }

        .reel-tile.is-playing:hover .reel-center-play {
            opacity: 0.85;
            transform: scale(1);
            pointer-events: auto;
            background: rgba(0, 0, 0, 0.65);
            color: #ffffff;
            border-color: rgba(255, 255, 255, 0.3);
        }

        .reel-bottom-bar {
            display: flex;
            flex-direction: column;
            gap: 7px;
            width: 100%;
            z-index: 3;
        }

        .reel-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.72rem;
            font-family: 'Space Mono', monospace;
        }

        .reel-insta-handle {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            color: rgba(255, 255, 255, 0.85);
            font-weight: 600;
        }

        .reel-dur-pill {
            background: rgba(0, 0, 0, 0.55);
            padding: 2px 7px;
            border-radius: 10px;
            color: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .reel-footer-title {
            font-family: 'Syne', sans-serif;
            font-size: 0.98rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.25;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .reel-progress-track {
            width: 100%;
            height: 3px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 2px;
            overflow: hidden;
            margin-top: 3px;
        }

        .reel-progress-bar {
            height: 100%;
            width: 0%;
            background: var(--accent-lime);
            box-shadow: 0 0 8px var(--accent-lime);
            transition: width 0.1s linear;
        }

        /* Instagram Reel Lightbox Modal */
        .reel-lightbox-modal {
            display: none;
            position: fixed;
            inset: 0;
            z-index: 10000;
            align-items: center;
            justify-content: center;
            padding: 20px;
            box-sizing: border-box;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .reel-lightbox-modal.is-active {
            display: flex;
            opacity: 1;
            pointer-events: auto;
        }

        .reel-lightbox-backdrop {
            position: absolute;
            inset: 0;
            background: rgba(3, 3, 5, 0.9);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
        }

        .reel-lightbox-container {
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 420px;
            height: min(840px, 90vh);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .lightbox-close-btn {
            position: absolute;
            top: -46px;
            right: 0;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            z-index: 10;
        }

        .lightbox-close-btn:hover {
            background: var(--accent-lime);
            color: #000000;
            transform: scale(1.1);
        }

        .lightbox-phone-frame {
            width: 100%;
            height: 100%;
            position: relative;
            border-radius: 24px;
            overflow: hidden;
            background: #000000;
            border: 1.5px solid rgba(255, 255, 255, 0.15);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 50px rgba(168, 255, 83, 0.2);
        }

        .lightbox-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .lightbox-overlay {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 1.5rem;
            box-sizing: border-box;
            background: linear-gradient(180deg, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.1) 40%, rgba(0,0,0,0.85) 100%);
            pointer-events: none;
        }

        .lightbox-top-bar, .lightbox-bottom-bar, .lightbox-center-play {
            pointer-events: auto;
        }

        .lightbox-top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .lightbox-profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .lightbox-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: 1.5px solid var(--accent-lime);
        }

        .lightbox-handle {
            display: block;
            font-family: 'Space Mono', monospace;
            font-size: 0.85rem;
            font-weight: 700;
            color: #ffffff;
        }

        .lightbox-sub {
            display: block;
            font-size: 0.7rem;
            color: rgba(255, 255, 255, 0.65);
        }

        .lightbox-btn {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .lightbox-btn:hover {
            background: var(--accent-lime);
            color: #000000;
        }

        .lightbox-center-play {
            align-self: center;
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.3);
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            opacity: 0;
            transition: opacity 0.2s, transform 0.2s;
            cursor: pointer;
        }

        .lightbox-phone-frame.is-paused .lightbox-center-play {
            opacity: 1;
        }

        .lightbox-bottom-bar {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .lightbox-tag {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            color: var(--accent-lime);
            letter-spacing: 0.15em;
        }

        .lightbox-title {
            font-family: 'Syne', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            line-height: 1.3;
        }

        .lightbox-caption {
            font-size: 0.82rem;
            color: rgba(255, 255, 255, 0.75);
            margin: 0;
            line-height: 1.4;
        }

        .lightbox-progress-track {
            width: 100%;
            height: 3px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 2px;
            overflow: hidden;
            margin-top: 6px;
        }

        .lightbox-progress-bar {
            height: 100%;
            width: 0%;
            background: var(--accent-lime);
            box-shadow: 0 0 10px var(--accent-lime);
        }

        .lightbox-nav-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #ffffff;
            font-size: 1.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.25s;
            z-index: 5;
            user-select: none;
        }

        .lightbox-nav-btn:hover {
            background: var(--accent-lime);
            color: #000000;
            border-color: var(--accent-lime);
            transform: translateY(-50%) scale(1.1);
        }

        .lightbox-nav-btn.prev {
            left: -58px;
        }

        .lightbox-nav-btn.next {
            right: -58px;
        }

        @media (max-width: 600px) {
            .lightbox-nav-btn.prev { left: 8px; }
            .lightbox-nav-btn.next { right: 8px; }
            .lightbox-close-btn { top: 12px; right: 12px; background: rgba(0,0,0,0.7); }
        }

        /* ===================================================
           CONTACT US SECTION (EXACT BROCHURE DETAILS + FORM)
        =================================================== */
        .contact-section {
            width: 100%;
            padding: 8rem 3.5rem 4rem;
            background-color: #030304;
            box-sizing: border-box;
            position: relative;
        }

        .contact-container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .contact-header-wrap {
            text-align: center;
            margin-bottom: 5rem;
        }

        .footer-logo-badge {
            width: 95px;
            height: 95px;
            border-radius: 50%;
            margin: 0 auto 2rem;
            filter: drop-shadow(0 0 35px var(--accent-glow));
        }

        .footer-logo-badge img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
        }

        .cta-eyebrow {
            font-family: 'Space Mono', monospace;
            font-size: 0.78rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--accent-lime);
            display: inline-block;
            margin-bottom: 1.2rem;
        }

        .cta-big-link {
            font-family: 'Syne', sans-serif;
            font-size: clamp(3.2rem, 8vw, 7.5rem);
            font-weight: 900;
            text-decoration: none;
            color: #ffffff;
            letter-spacing: -0.04em;
            line-height: 0.95;
            display: inline-block;
            transition: color 0.3s, transform 0.3s var(--ease-out);
        }

        .cta-big-link:hover {
            color: var(--accent-lime);
            transform: scale(1.02);
            text-shadow: 0 0 60px var(--accent-glow);
        }

        /* 2-Column Enhanced Contact Layout */
        .contact-layout-grid {
            display: grid;
            grid-template-columns: 0.9fr 1.1fr;
            gap: 3.5rem;
            margin-bottom: 6rem;
            align-items: stretch;
        }

        /* Green Brochure Card Replica */
        .brochure-contact-box {
            background: #00d665;
            border-radius: 24px;
            padding: 3rem 2.8rem;
            color: #000000;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 20px 50px rgba(0, 214, 101, 0.25);
            position: relative;
        }

        .brochure-contact-box h3 {
            font-family: 'Syne', sans-serif;
            font-size: 2.4rem;
            font-weight: 900;
            color: #000000;
            margin-bottom: 2rem;
            letter-spacing: -0.03em;
        }

        .brochure-info-list {
            display: flex;
            flex-direction: column;
            gap: 1.4rem;
        }

        .brochure-info-item {
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }

        .brochure-label-pill {
            display: inline-block;
            width: fit-content;
            background: #000000;
            color: #ffffff;
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            font-weight: 700;
            padding: 3px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        .brochure-val {
            font-family: 'Syne', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #000000;
            text-decoration: none;
            transition: opacity 0.2s;
        }

        .brochure-val:hover {
            opacity: 0.8;
        }

        .brochure-action-row {
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
            padding-top: 1.8rem;
            border-top: 1px solid rgba(0, 0, 0, 0.15);
        }

        .brochure-btn-dark {
            flex: 1;
            padding: 12px 18px;
            border-radius: 30px;
            background: #000000;
            color: #ffffff;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            text-decoration: none;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: transform 0.2s, background 0.2s;
        }

        .brochure-btn-dark:hover {
            transform: translateY(-2px);
            background: #151515;
        }

        /* Interactive Booking Form */
        .contact-form-box {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 3rem 2.8rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .contact-form-box h3 {
            font-family: 'Syne', sans-serif;
            font-size: 1.8rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.4rem;
        }

        .contact-form-box p {
            font-size: 0.88rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.2rem;
            margin-bottom: 1.2rem;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .form-group.full-width {
            grid-column: span 2;
        }

        .form-group label {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.7);
        }

        .form-input, .form-select, .form-textarea {
            width: 100%;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px 14px;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            font-size: 0.88rem;
            outline: none;
            transition: border-color 0.25s;
        }

        .form-input:focus, .form-select:focus, .form-textarea:focus {
            border-color: var(--accent-lime);
            box-shadow: 0 0 10px rgba(168, 255, 83, 0.2);
        }

        .form-textarea {
            resize: vertical;
            min-height: 85px;
        }

        .form-submit-btn {
            font-family: 'Space Mono', monospace;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            padding: 15px 28px;
            border-radius: 30px;
            background: var(--accent-lime);
            color: #000000;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.8rem;
            box-shadow: 0 0 25px var(--accent-glow);
            transition: all 0.3s;
            outline: none;
            margin-top: 1rem;
        }

        .form-submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 40px var(--accent-lime);
        }

        .footer-bottom-bar {
            max-width: 1400px;
            margin: 0 auto;
            padding-top: 2.5rem;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.08em;
            color: var(--text-secondary);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .footer-bottom-bar a {
            color: var(--accent-lime);
            text-decoration: none;
        }

        /* ===================================================
           RESPONSIVE MOBILE ADJUSTMENTS
        =================================================== */
        @media (max-width: 1100px) {
            .services-grid { grid-template-columns: repeat(2, 1fr); }
            .service-card.span-2 { grid-column: span 2; }
            .pricing-grid { grid-template-columns: 1fr; }
            .pricing-card.featured { transform: none; }
            .pricing-card.featured:hover { transform: translateY(-8px); }
            .why-grid { grid-template-columns: repeat(2, 1fr); }
            .contact-layout-grid { grid-template-columns: 1fr; }
        }

        /* Footer Terms & Conditions Link Button */
        .footer-terms-trigger-btn {
            background: rgba(0, 214, 101, 0.1);
            border: 1px solid rgba(0, 214, 101, 0.35);
            color: var(--accent-emerald);
            font-family: 'Space Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.1em;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 20px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.25s ease;
            -webkit-tap-highlight-color: transparent;
        }

        .footer-terms-trigger-btn:hover {
            background: var(--accent-emerald);
            color: #000000;
            border-color: var(--accent-emerald);
            box-shadow: 0 0 18px rgba(0, 214, 101, 0.45);
            transform: translateY(-1px);
        }

        .terms-nav-arrow {
            transition: transform 0.25s ease;
        }

        
        .footer-terms-trigger-btn.active .terms-nav-arrow {
            transform: rotate(180deg);
        }

        @media (max-width: 868px) {
            /* Intro Overlay on Mobile */
            #liquid-container {
                padding: 1.5rem 1.25rem !important;
            }
            .intro-top-bar {
                font-size: 0.65rem !important;
                letter-spacing: 0.15em !important;
            }
            .intro-top-bar > div:nth-child(2) {
                display: none !important;
            }
            .intro-brand-name {
                gap: 0.5rem !important;
                font-size: 0.72rem !important;
            }
            .intro-brand-name img {
                width: 22px !important;
                height: 22px !important;
            }
            .enter-experience-btn {
                padding: 12px 24px !important;
                font-size: 0.75rem !important;
                letter-spacing: 0.18em !important;
            }
            .intro-instruction {
                font-size: 0.56rem !important;
                letter-spacing: 0.12em !important;
                text-align: center;
                padding: 0 10px;
            }

            /* General Navigation & Section Spacing for Mobile Devices */
            .site-nav { padding: 0.9rem 1.25rem; }
            .site-nav-menu { display: none; }
            
            /* Section Paddings: replace 3.5rem desktop gutters with mobile-friendly gutters */
            .hero-statement-section { padding: 6.8rem 1.25rem 3rem; }
            .work-section { padding: 4.5rem 0; }
            /* Selected Work Mobile Video Cards & Smooth Marquee */
            .work-card {
                width: 200px !important;
                aspect-ratio: 9/16 !important;
                border-radius: 14px !important;
            }
            .auto-slider-track {
                gap: 1.1rem !important;
                animation: marqueeSlideMobile 32s linear infinite !important;
            }
            @keyframes marqueeSlideMobile {
                0% { transform: translateX(0); }
                100% { transform: translateX(calc(-200px * 9 - 1.1rem * 9)); }
            }
            .work-sound-badge {
                width: 32px !important;
                height: 32px !important;
                bottom: 10px !important;
                right: 10px !important;
            }
            .section-header-row {
                padding: 0 1.25rem;
                margin-bottom: 2rem;
                flex-direction: column;
                align-items: flex-start;
                gap: 1.2rem;
            }
            .about-section { padding: 4.5rem 1.25rem 2.5rem; }
            .services-section { padding: 4.5rem 1.25rem; }
            .pricing-section { padding: 4.5rem 1.25rem; }
            .why-section { padding: 4.5rem 1.25rem; }
            .instagram-direct-section { padding: 4.5rem 1.25rem; }
            .contact-section { padding: 4.5rem 1.25rem 3rem; }
            .site-footer { padding: 4rem 1.25rem 2rem; }

            /* Typography Scaling */
            .hero-giant-title {
                font-size: clamp(2.2rem, 9.5vw, 4.6rem);
                line-height: 1.05;
                margin-bottom: 1.8rem;
                letter-spacing: -0.03em;
                word-break: break-word;
            }
            .section-headline {
                font-size: clamp(1.8rem, 7.5vw, 2.6rem);
                word-break: break-word;
            }

            /* Layout Grids */
            .hero-bottom-grid { grid-template-columns: 1fr; gap: 1.5rem; text-align: center; }
            .hero-bottom-left, .hero-bottom-right { text-align: center; }
            .about-grid { grid-template-columns: 1fr; gap: 2.5rem; }
            .about-sticky-col { position: relative; top: 0; }
            .about-stats-row { grid-template-columns: 1fr 1fr; gap: 1.2rem; }
            .services-grid { grid-template-columns: 1fr; }
            .service-card.span-2 { grid-column: span 1; }
            .software-niches-grid { grid-template-columns: 1fr; }
            .why-grid { grid-template-columns: 1fr; }
            
            /* Instagram Section Mobile Fixes */
            .insta-header-wrap {
                flex-direction: column;
                align-items: flex-start;
                gap: 1.5rem;
                margin-bottom: 2rem;
                padding-bottom: 1.5rem;
            }
            .insta-profile-bar {
                gap: 12px !important;
                width: 100%;
                align-items: center !important;
            }
            .insta-avatar-big {
                width: 54px !important;
                height: 54px !important;
                flex-shrink: 0 !important;
            }
            .insta-title {
                font-size: clamp(1.15rem, 5vw, 1.45rem) !important;
                word-break: normal !important;
                white-space: nowrap !important;
                margin: 0 !important;
            }
            .insta-btn-link {
                width: 100%;
                justify-content: center;
                box-sizing: border-box;
                text-align: center;
            }
            .insta-reels-grid { grid-template-columns: repeat(2, 1fr); gap: 1rem; }

            /* Mobile Horizontal Scrub Pin & Track (<= 868px) */
            .pricing-section {
                overflow: visible !important;
            }
            .pricing-container {
                overflow: visible !important;
            }
            .pricing-scroll-pin-wrapper {
                display: block !important;
                position: relative !important;
                height: 310vh !important;
                width: 100% !important;
                box-sizing: border-box !important;
                margin-bottom: 2.5rem !important;
            }

            .pricing-sticky-viewport {
                display: flex !important;
                position: sticky !important;
                top: 76px !important;
                width: 100% !important;
                height: calc(100vh - 86px) !important;
                max-height: 740px !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-items: center !important;
                overflow: hidden !important;
                box-sizing: border-box !important;
                padding: 10px 0 !important;
            }

            .pricing-mobile-progress {
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 8px !important;
                margin-bottom: 16px !important;
                z-index: 10 !important;
                width: 100% !important;
            }

            .pricing-progress-pill {
                font-family: 'Space Mono', monospace !important;
                font-size: 0.65rem !important;
                padding: 5px 12px !important;
                border-radius: 20px !important;
                background: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                color: var(--text-secondary) !important;
                letter-spacing: 0.08em !important;
                transition: all 0.3s ease !important;
                cursor: pointer !important;
            }

            .pricing-progress-pill.active {
                background: rgba(168, 255, 83, 0.15) !important;
                border-color: var(--accent-lime) !important;
                color: var(--accent-lime) !important;
                box-shadow: 0 0 14px rgba(168, 255, 83, 0.28) !important;
            }

            .pricing-grid {
                display: flex !important;
                flex-direction: row !important;
                flex-wrap: nowrap !important;
                align-items: center !important;
                gap: 20px !important;
                width: max-content !important;
                will-change: transform !important;
                margin: 0 !important;
                padding: 0 !important;
                transition: none !important;
            }

            .pricing-card.shader-card {
                width: min(340px, 86vw) !important;
                min-width: min(340px, 86vw) !important;
                max-width: min(340px, 86vw) !important;
                height: auto !important;
                max-height: calc(100vh - 185px) !important;
                padding: 1.8rem 1.4rem !important;
                border-radius: 20px !important;
                box-sizing: border-box !important;
                flex-shrink: 0 !important;
                overflow-y: auto !important;
                transform-origin: center center !important;
                transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.25s ease !important;
            }

            .pricing-card.shader-card.featured {
                transform: none !important;
            }
            .pricing-card.shader-card.featured:hover {
                transform: none !important;
            }
            .pricing-tier-name {
                font-size: 1.45rem !important;
            }
            .pricing-tier-desc {
                font-size: 0.82rem !important;
                margin-bottom: 1.2rem !important;
                line-height: 1.4 !important;
            }
            .pricing-price-wrap {
                margin-bottom: 1.4rem !important;
                padding-bottom: 1.2rem !important;
            }
            .pricing-currency {
                font-size: 1.6rem !important;
            }
            .pricing-amount {
                font-size: 2.6rem !important;
            }
            .pricing-checklist {
                gap: 0.75rem !important;
                margin-bottom: 1.6rem !important;
            }
            .pricing-checklist li {
                font-size: 0.78rem !important;
                line-height: 1.35 !important;
            }
            .pricing-cta-btn {
                padding: 12px 18px !important;
                font-size: 0.72rem !important;
            }

            /* Callout Banner & Pricing */
            .pricing-custom-callout { flex-direction: column; text-align: left; padding: 2.2rem 1.4rem; }

            /* Web & Software Mobile Sideways Slider */
            .callout-mobile-nav {
                display: flex !important;
                align-items: center;
                justify-content: space-between;
                margin-top: 1.2rem;
                margin-bottom: 0.8rem;
                padding: 0 0.2rem;
                width: 100%;
                box-sizing: border-box;
            }

            .callout-nav-indicator {
                display: flex;
                align-items: center;
                gap: 12px;
            }

            .plan-step-badge {
                font-family: 'Space Mono', monospace;
                font-size: 0.65rem;
                letter-spacing: 0.12em;
                color: var(--accent-lime);
                background: rgba(168, 255, 83, 0.08);
                border: 1px solid rgba(168, 255, 83, 0.35);
                padding: 5px 12px;
                border-radius: 20px;
                font-weight: 700;
                text-transform: uppercase;
            }

            .callout-nav-dots {
                display: flex;
                gap: 6px;
                align-items: center;
            }

            .callout-nav-dots .nav-dot {
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.22);
                border: none;
                padding: 0;
                cursor: pointer;
                transition: all 0.3s ease;
            }

            .callout-nav-dots .nav-dot.active {
                width: 22px;
                border-radius: 10px;
                background: var(--accent-lime);
                box-shadow: 0 0 10px rgba(168, 255, 83, 0.55);
            }

            .callout-nav-arrows {
                display: flex;
                gap: 8px;
                align-items: center;
            }

            .callout-arrow-btn {
                width: 38px;
                height: 38px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.18);
                color: #ffffff;
                font-size: 1.3rem;
                line-height: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                transition: all 0.25s ease;
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }

            .callout-arrow-btn:active {
                transform: scale(0.92);
                border-color: var(--accent-lime);
                color: var(--accent-lime);
            }

            .callout-arrow-btn:disabled {
                opacity: 0.25;
                cursor: not-allowed;
                border-color: rgba(255, 255, 255, 0.08);
            }

            /* Sideways horizontal scroll track */
            .callout-offerings-grid {
                display: flex !important;
                flex-direction: row !important;
                overflow-x: auto !important;
                scroll-snap-type: x mandatory !important;
                scroll-behavior: smooth !important;
                -webkit-overflow-scrolling: touch !important;
                scrollbar-width: none !important;
                gap: 16px !important;
                padding: 0.5rem 0.2rem 0.6rem !important;
                margin-top: 0.3rem !important;
                width: 100% !important;
                box-sizing: border-box !important;
            }

            .callout-offerings-grid::-webkit-scrollbar {
                display: none !important;
            }

            /* Each plan card in the sideways slider */
            .callout-subcard {
                flex: 0 0 100% !important;
                width: 100% !important;
                max-width: 100% !important;
                min-width: 100% !important;
                box-sizing: border-box !important;
                scroll-snap-align: center !important;
                scroll-snap-stop: always !important;
                padding: 1.8rem 1.4rem !important;
                gap: 1.6rem !important;
            }

            /* Bottom "NEXT PLAN" CTA Button */
            .callout-mobile-bottom-ctl {
                display: flex !important;
                flex-direction: column;
                margin-top: 1rem;
                width: 100%;
                box-sizing: border-box;
            }

            .callout-next-plan-cta {
                width: 100%;
                background: rgba(168, 255, 83, 0.08);
                border: 1px solid rgba(168, 255, 83, 0.4);
                color: var(--accent-lime);
                padding: 14px 18px;
                border-radius: 12px;
                font-family: 'Space Mono', monospace;
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.08em;
                display: flex;
                align-items: center;
                justify-content: space-between;
                cursor: pointer;
                transition: all 0.25s ease;
                -webkit-tap-highlight-color: transparent;
                text-transform: uppercase;
            }

            .callout-next-plan-cta:active {
                background: var(--accent-lime);
                color: #000000;
                transform: scale(0.98);
            }
            .callout-top-row { flex-direction: column; align-items: flex-start; gap: 1.6rem; }
            .callout-header-content { max-width: 100%; }
            .callout-header-headline {
                font-size: clamp(1.4rem, 5.5vw, 2.2rem);
                word-break: break-word;
            }
            .callout-header-cta-wrap { width: 100%; }

            /* Contact Form & Brochure */
            .contact-layout-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            .brochure-contact-box,
            .contact-form-box {
                padding: 2.2rem 1.4rem;
                border-radius: 20px;
                box-sizing: border-box;
            }
            .form-grid { grid-template-columns: 1fr; }
            .form-group.full-width { grid-column: span 1; }
            .footer-bottom-bar { flex-direction: column; text-align: center; gap: 0.8rem; }
        }

        /* Extra Compact Mobile Phones (<= 480px) */
        @media (max-width: 480px) {
            .site-nav {
                padding: 0.8rem 1rem;
            }
            .site-brand {
                font-size: 0.82rem;
                gap: 0.5rem;
            }
            .brand-logo-badge {
                width: 28px;
                height: 28px;
            }
            .cash-toggle-btn {
                padding: 6px 10px;
                font-size: 0.65rem;
                gap: 5px;
            }
            .cash-toggle-badge {
                display: none; /* Keep toggle ultra-compact on narrow phone headers */
            }
            .hero-statement-section {
                padding: 5.8rem 1rem 2.5rem;
            }
            .hero-giant-title {
                font-size: clamp(1.85rem, 9vw, 3.2rem);
                line-height: 1.05;
                margin-bottom: 1.4rem;
            }
            .section-headline {
                font-size: clamp(1.5rem, 7.5vw, 2.2rem);
            }
            .about-section,
            .services-section,
            .pricing-section,
            .why-section,
            .instagram-direct-section,
            .contact-section,
            .site-footer {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .section-header-row {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            .insta-reels-grid {
                grid-template-columns: repeat(2, 1fr) !important;
                gap: 10px !important;
            }
            .reel-overlay {
                padding: 0.9rem !important;
            }
            .reel-tag {
                font-size: 0.52rem !important;
                padding: 3px 6px !important;
            }
            .reel-action-btn {
                width: 26px !important;
                height: 26px !important;
            }
            .reel-center-play {
                width: 42px !important;
                height: 42px !important;
                font-size: 1rem !important;
            }
            .reel-footer-title {
                font-size: 0.78rem !important;
            }
            .scd-20__deck {
                width: calc(100vw - 32px);
                max-width: 320px;
                height: 480px;
            }
            .scd-20__card {
                padding: 1.4rem 1.15rem;
            }
            .scd-20__ctl {
                width: calc(100vw - 32px);
                max-width: 320px;
            }
            .scd-20__ctl p {
                font-size: 0.68rem;
                padding: 6px 8px;
            }
            .pricing-card.shader-card {
                max-width: calc(100vw - 32px) !important;
                padding: 1.8rem 1.3rem !important;
            }
            .pricing-amount {
                font-size: 2.35rem !important;
            }
            .pricing-checklist {
                gap: 0.75rem !important;
                margin-bottom: 1.8rem !important;
            }
            .pricing-checklist li {
                font-size: 0.76rem !important;
            }
            .brochure-contact-box,
            .contact-form-box {
                padding: 1.8rem 1.15rem;
            }
        }
    </style>
</head>
<body>

    <!-- ==========================================
         3D FULL ZOOM DOLLAR BILL VORTEX PORTAL (3 CASH BILLS)
    ========================================== -->
    <div id="cash-zoom-portal">
        <div class="zoom-dollar-bill" id="zoom-bill-l">
            <img src="___DOLLAR_B64___" alt="Zooming Dollar Bill Left">
        </div>
        <div class="zoom-dollar-bill" id="zoom-bill">
            <img src="___DOLLAR_B64___" alt="Zooming Dollar Bill Center">
        </div>
        <div class="zoom-dollar-bill" id="zoom-bill-r">
            <img src="___DOLLAR_B64___" alt="Zooming Dollar Bill Right">
        </div>
    </div>

    <!-- ==========================================
         BACKGROUND FALLING CASH CANVAS (RAIN)
    ========================================== -->
    <canvas id="cash-rain-canvas"></canvas>

    <!-- ==========================================
         LANDING SCREEN: THREE.JS LIQUID FLUID LOGO
    ========================================== -->
    <div id="liquid-container">
        <div class="intro-top-bar">
            <div class="intro-brand-name">
                <img src="___LOGO_B64___" alt="Savkar Media">
                <span>SAVKAR MEDIA</span>
            </div>
            <div>BENGALURU / EST. 2025</div>
            <div>DIGITAL MARKETING AGENCY</div>
        </div>

        <canvas id="liquid-canvas"></canvas>

        <div class="intro-bottom-bar">
            <button class="enter-experience-btn" id="enter-experience-btn">
                <span>ENTER EXPERIENCE</span>
                <span>💸</span>
            </button>
            <div class="intro-instruction">SCROLL DOWN TO ZOOM INTO CASH & MAIN PAGE ↓</div>
        </div>
    </div>

    <!-- ==========================================
         STICKY NAVIGATION WITH CASH RAIN TOGGLE
    ========================================== -->
    <nav class="site-nav" id="main-nav">
        <a href="#" class="site-brand">
            <img src="___LOGO_B64___" class="brand-logo-badge" alt="Savkar Media">
            SAVKAR MEDIA
        </a>
        <ul class="site-nav-menu">
            <li><a href="#work">Work</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#why-us">Why Us</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
        <div class="nav-actions">
            <!-- DEFAULT OFF: Users can turn it ON if they want -->
            <button class="cash-toggle-btn off" id="cash-rain-toggle-btn" title="Toggle Falling Cash ON / OFF">
                <span class="cash-toggle-icon">💵</span>
                <span class="cash-toggle-text">CASH RAIN:</span>
                <span class="cash-toggle-badge" id="cash-status-text">OFF</span>
                <span class="cash-toggle-switch">
                    <span class="cash-toggle-knob"></span>
                </span>
            </button>
        </div>
    </nav>

    <!-- ==========================================
         HERO SECTION: RADICAL DIGITAL GROWTH
    ========================================== -->
    <section class="hero-statement-section" id="hero-statement">
        
        <div class="hero-logo-badge-center">
            <img src="___LOGO_B64___" alt="Savkar Media Official Logo">
        </div>

        <div class="hero-meta-top">DIGITAL MARKETING AGENCY · BENGALURU · EST. 2025</div>

        <h1 class="hero-giant-title" id="main-title">
            <span class="word-row"><span class="word-inner">RADICAL</span></span>
            <span class="word-row"><span class="word-inner outline-row">DIGITAL</span></span>
            <span class="word-row"><span class="word-inner">GROWTH.</span></span>
        </h1>

        <!-- Direct Tagline From Brochure -->
        <p class="hero-tagline-quote">
            Fueling business growth with <strong>powerful content</strong> that captures attention and builds trust.
        </p>

        <div class="hero-slogan-pill">
            <span>⚡</span>
            <span>BUILT FOR BRANDS THAT WANT MORE THAN AVERAGE</span>
        </div>

        <div class="hero-bottom-grid">
            <div class="hero-bottom-left">
                [ 01 ] REEL PRODUCTION & SOCIAL MEDIA MARKETING<br>
                [ 02 ] WEB DEV & CUSTOM SOFTWARE (GYM, CLINIC, CAFE, RESTAURANT)
            </div>
            <div class="hero-bottom-center">
                <div class="scroll-down-pill">
                    <span>SCROLL TO EXPLORE</span>
                    <div class="scroll-down-line"></div>
                </div>
            </div>
            <div class="hero-bottom-right">
                SAVKAR MEDIA © 2026<br>
                JAYANAGAR 4TH BLOCK · BENGALURU
            </div>
        </div>
    </section>

    <!-- ==========================================
         INSTAGRAM DIRECT FROM @SAVKAR_MEDIA (8 LIVE 4K REELS)
    ========================================== -->
    <section class="instagram-direct-section" id="instagram">
        <div class="insta-header-wrap">
            <div class="insta-profile-bar">
                <img src="___LOGO_B64___" class="insta-avatar-big" alt="@savkar_media profile">
                <div>
                    <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.4rem; flex-wrap:wrap;">
                        <span class="section-tagline">[ INSTAGRAM FEED ]</span>
                        <span class="insta-live-badge">● 8 EXCLUSIVE REELS</span>
                    </div>
                    <h2 class="insta-title">@savkar_media</h2>
                    <p class="insta-subtitle">Real 4K Reels scripted, shot &amp; distributed for our clients. Tap any reel to play with sound.</p>
                </div>
            </div>
            <a href="https://www.instagram.com/savkar_media" target="_blank" rel="noopener noreferrer" class="insta-btn-link">
                <span>FOLLOW ON INSTAGRAM</span>
                <span>↗</span>
            </a>
        </div>

        <div class="insta-reels-grid" id="insta-reels-grid">
            
            <!-- Reel 1: REEL 1.mp4 -->
            <div class="reel-tile" data-index="0" data-video="videos/REEL%201.mp4" data-tag="VIRAL HOOK" data-title="What If Your Brand Had Real Engagement?" data-caption="Mastering the 3-second hook to turn casual scrollers into paying clients.">
                <video class="reel-video" src="videos/REEL%201.mp4" poster="videos/posters/poster_1.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">VIRAL HOOK</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:32</span>
                        </div>
                        <div class="reel-footer-title">What If Your Brand Had Real Engagement?</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 2: REELS 2.mp4 -->
            <div class="reel-tile" data-index="1" data-video="videos/REELS%202.mp4" data-tag="BRAND STORY" data-title="Struggling With Reach? We Fix It" data-caption="Relatable Kannada &amp; English storytelling tailored for Bengaluru businesses.">
                <video class="reel-video" src="videos/REELS%202.mp4" poster="videos/posters/poster_2.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">BRAND STORY</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:35</span>
                        </div>
                        <div class="reel-footer-title">Struggling With Reach? We Fix It</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 3: REELS 3.mp4 -->
            <div class="reel-tile" data-index="2" data-video="videos/REELS%203.mp4" data-tag="MARKET STRATEGY" data-title="Why Most Agency Ads Fail in 2026" data-caption="High-converting creative direction vs traditional boring marketing campaigns.">
                <video class="reel-video" src="videos/REELS%203.mp4" poster="videos/posters/poster_3.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">MARKET STRATEGY</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:30</span>
                        </div>
                        <div class="reel-footer-title">Why Most Agency Ads Fail in 2026</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 4: Copy of REELS 7.mp4 -->
            <div class="reel-tile" data-index="3" data-video="videos/Copy%20of%20REELS%207.mp4" data-tag="LOCAL BUSINESS" data-title="Just Opened Your Business? Watch This" data-caption="The proven blueprint for Gyms, Cafes &amp; Clinics to pack their doors with leads.">
                <video class="reel-video" src="videos/Copy%20of%20REELS%207.mp4" poster="videos/posters/poster_4.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">LOCAL BUSINESS</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:25</span>
                        </div>
                        <div class="reel-footer-title">Just Opened Your Business? Watch This</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 5: Copy of REELS 2.mp4 -->
            <div class="reel-tile" data-index="4" data-video="videos/Copy%20of%20REELS%202.mp4" data-tag="CASE STUDY" data-title="How We Scaled A Client's Lead Pipeline" data-caption="Rapid audience growth &amp; booked consultations through high-intent paid reels.">
                <video class="reel-video" src="videos/Copy%20of%20REELS%202.mp4" poster="videos/posters/poster_5.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">CASE STUDY</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:18</span>
                        </div>
                        <div class="reel-footer-title">How We Scaled A Client's Lead Pipeline</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 6: lv_0_20260315161236.mp4 -->
            <div class="reel-tile" data-index="5" data-video="videos/lv_0_20260315161236.mp4" data-tag="ORGANIC GROWTH" data-title="Building Real Authority On Instagram" data-caption="Why founder-led personal brand presence outperforms generic graphic templates.">
                <video class="reel-video" src="videos/lv_0_20260315161236.mp4" poster="videos/posters/poster_6.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">ORGANIC GROWTH</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:30</span>
                        </div>
                        <div class="reel-footer-title">Building Real Authority On Instagram</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 7: lv_0_20260225191249.mp4 -->
            <div class="reel-tile" data-index="6" data-video="videos/lv_0_20260225191249.mp4" data-tag="AGENCY BLUEPRINT" data-title="Strategy — What We Do Best" data-caption="End-to-end scripting, shooting, editing, and distribution under one roof.">
                <video class="reel-video" src="videos/lv_0_20260225191249.mp4" poster="videos/posters/poster_7.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">AGENCY BLUEPRINT</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:08</span>
                        </div>
                        <div class="reel-footer-title">Strategy — What We Do Best</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Reel 8: lv_0_20260225190002.mp4 -->
            <div class="reel-tile" data-index="7" data-video="videos/lv_0_20260225190002.mp4" data-tag="BEHIND THE SCENES" data-title="On-Location 4K Shoot in Action" data-caption="Pro filming on location with cinema stabilization &amp; luxury brand aesthetic.">
                <video class="reel-video" src="videos/lv_0_20260225190002.mp4" poster="videos/posters/poster_8.jpg" preload="metadata" playsinline loop muted></video>
                <div class="reel-overlay">
                    <div class="reel-top-bar">
                        <span class="reel-tag">BEHIND THE SCENES</span>
                        <div class="reel-top-actions">
                            <button class="reel-action-btn reel-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <svg class="sound-off-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.2.05-.41.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/></svg>
                                <svg class="sound-on-icon" viewBox="0 0 24 24" width="13" height="13" fill="currentColor" style="display:none;"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>
                            </button>
                            <button class="reel-action-btn reel-expand-btn" title="Watch Fullscreen Reel" aria-label="Fullscreen">
                                <svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
                            </button>
                        </div>
                    </div>
                    <div class="reel-center-play">
                        <span class="play-symbol">▶</span>
                        <span class="pause-symbol" style="display:none;">❚❚</span>
                    </div>
                    <div class="reel-bottom-bar">
                        <div class="reel-meta-row">
                            <span class="reel-insta-handle">
                                <svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                                @savkar_media
                            </span>
                            <span class="reel-dur-pill">0:21</span>
                        </div>
                        <div class="reel-footer-title">On-Location 4K Shoot in Action</div>
                        <div class="reel-progress-track">
                            <div class="reel-progress-bar"></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Instagram Reel Lightbox Modal -->
    <div class="reel-lightbox-modal" id="reel-lightbox" aria-hidden="true">
        <div class="reel-lightbox-backdrop" id="reel-lightbox-backdrop"></div>
        <div class="reel-lightbox-container">
            <button class="lightbox-close-btn" id="lightbox-close" title="Close Reel Modal" aria-label="Close">✕</button>
            <div class="lightbox-phone-frame" id="lightbox-phone-frame">
                <video class="lightbox-video" id="lightbox-video" playsinline loop></video>
                <div class="lightbox-overlay">
                    <div class="lightbox-top-bar">
                        <div class="lightbox-profile">
                            <img src="___LOGO_B64___" class="lightbox-avatar" alt="@savkar_media">
                            <div>
                                <span class="lightbox-handle">@savkar_media</span>
                                <span class="lightbox-sub">Savkar Media · 4K Client Work</span>
                            </div>
                        </div>
                        <div class="lightbox-top-controls">
                            <button class="lightbox-btn" id="lightbox-sound-btn" title="Toggle Sound" aria-label="Toggle Sound">
                                <span class="lightbox-sound-icon">🔇</span>
                            </button>
                        </div>
                    </div>

                    <div class="lightbox-center-play" id="lightbox-center-play">
                        <span>▶</span>
                    </div>

                    <div class="lightbox-bottom-bar">
                        <span class="lightbox-tag" id="lightbox-tag">[ VIRAL HOOK ]</span>
                        <h3 class="lightbox-title" id="lightbox-title">What If Your Brand Had Real Engagement?</h3>
                        <p class="lightbox-caption" id="lightbox-caption">Mastering the 3-second hook to turn casual scrollers into paying clients.</p>
                        <div class="lightbox-progress-track">
                            <div class="lightbox-progress-bar" id="lightbox-progress-bar"></div>
                        </div>
                    </div>
                </div>
                <button class="lightbox-nav-btn prev" id="lightbox-prev" title="Previous Reel" aria-label="Previous Reel">‹</button>
                <button class="lightbox-nav-btn next" id="lightbox-next" title="Next Reel" aria-label="Next Reel">›</button>
            </div>
        </div>
    </div>

    <!-- ==========================================
         SELECTED WORK (AUTO MOVEMENT SLIDER)
    ========================================== -->
    <section class="work-section" id="work">
        <div class="section-header-row">
            <div class="section-title-wrap">
                <span class="section-tagline">[ PORTFOLIO ARCHITECTURE ]</span>
                <h2 class="section-headline">SELECTED WORK</h2>
            </div>
            <div class="slider-controls">
                <button class="slider-btn" id="slide-prev" title="Previous">←</button>
                <button class="slider-btn" id="slide-next" title="Next">→</button>
            </div>
        </div>

        <!-- Continuous Auto-Sliding Marquee Track -->
        <div class="auto-slider-container" id="slider-container">
            <div class="auto-slider-track" id="slider-track">
                <!-- Card 01: Jagannath Travels Reel -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Jagannath%20travels%20reel.mp4" poster="work%20videos/posters/work_poster_1.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 02: Kalpana Roadlines Volvo -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Kalpana%20Roadlines%27s%20Volvo.mp4" poster="work%20videos/posters/work_poster_2.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 03: Commercial Reel 1 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260512171141.mp4" poster="work%20videos/posters/work_poster_3.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 04: Commercial Reel 2 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260605140912.mp4" poster="work%20videos/posters/work_poster_4.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 05: Commercial Reel 3 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260605141115.mp4" poster="work%20videos/posters/work_poster_5.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 06: Commercial Reel 4 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260610140842.mp4" poster="work%20videos/posters/work_poster_6.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 07: Commercial Reel 5 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260724183038.mp4" poster="work%20videos/posters/work_poster_7.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 08: Commercial Reel 6 -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260724183116.mp4" poster="work%20videos/posters/work_poster_8.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Card 09: Malnad Stays Long Weekend -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Malnad%20stays%20long%20weekend.mp4" poster="work%20videos/posters/work_poster_9.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Seamless Loop Set -->
                <!-- Duplicate Card 01: Jagannath Travels Reel (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Jagannath%20travels%20reel.mp4" poster="work%20videos/posters/work_poster_1.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 02: Kalpana Roadlines Volvo (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Kalpana%20Roadlines%27s%20Volvo.mp4" poster="work%20videos/posters/work_poster_2.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 03: Commercial Reel 1 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260512171141.mp4" poster="work%20videos/posters/work_poster_3.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 04: Commercial Reel 2 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260605140912.mp4" poster="work%20videos/posters/work_poster_4.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 05: Commercial Reel 3 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260605141115.mp4" poster="work%20videos/posters/work_poster_5.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 06: Commercial Reel 4 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260610140842.mp4" poster="work%20videos/posters/work_poster_6.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 07: Commercial Reel 5 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260724183038.mp4" poster="work%20videos/posters/work_poster_7.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 08: Commercial Reel 6 (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/lv_0_20260724183116.mp4" poster="work%20videos/posters/work_poster_8.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>

                <!-- Duplicate Card 09: Malnad Stays Long Weekend (Seamless Loop) -->
                <div class="work-card">
                    <video class="work-video" src="work%20videos/Malnad%20stays%20long%20weekend.mp4" poster="work%20videos/posters/work_poster_9.jpg" autoplay muted loop playsinline preload="metadata"></video>
                    <button class="work-sound-badge" aria-label="Toggle Audio" title="Toggle Audio">
                        <svg class="sound-off-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>
                        <svg class="sound-on-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
                    </button>
                </div>
            </div>
        </div>
    </section>

    <!-- ==========================================
         ABOUT US SECTION (DIRECT FROM BROCHURE)
    ========================================== -->
    <section class="about-section" id="about">
        <div class="about-grid">
            <div class="about-sticky-col">
                <span class="section-tagline">[ ABOUT SAVKAR MEDIA ]</span>
                <h2 class="about-title">BUILT FOR BRANDS THAT WANT MORE THAN AVERAGE.</h2>
                
                <div class="about-quote-box">
                    <p>"We don't just create content—we create opportunities for growth."</p>
                </div>
            </div>

            <div class="about-content-col">
                <h3 class="about-headline">
                    At Savkar Media, we help businesses transform their online presence through <span style="color:var(--accent-lime);">creative storytelling</span>, strategic content creation, and result-driven digital marketing solutions.
                </h3>

                <p class="about-body-text">
                    Our goal is to help brands connect with the right audience, build trust, and stand out in a competitive digital landscape. We deliver end-to-end marketing solutions designed to increase brand awareness, customer engagement, and business growth.
                </p>

                <p class="about-body-text">
                    Whether you are an ambitious local gym, specialty clinic, lively cafe, bustling restaurant, or high-growth brand, we bring cutting-edge visual production and tailored engineering systems together under one roof.
                </p>
            </div>

            <!-- Full Horizontal 3D Ribbon Type Component -->
            <div class="about-ribbon-full-row">
                <div class="ribbon-type-wrapper" id="ribbon-type-wrapper" role="region" aria-label="About Savkar Media 3D Ribbon Type">
                    <div class="ribbon-type-canvas-container" id="ribbon-canvas-container">
                        <canvas id="ribbon-type-canvas"></canvas>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ==========================================
         OUR SERVICES / WHAT WE OFFER SECTION
         (Including Web Development & Custom Software)
    ========================================== -->
    <section class="services-section" id="services">
        <div class="services-container">
            <div class="services-header-wrap">
                <span class="section-tagline">[ WHAT WE OFFER ]</span>
                <h2 class="section-headline">OUR SERVICES.</h2>
                <p style="color:var(--text-secondary);margin-top:1rem;line-height:1.7;font-size:1.05rem;">
                    From social media management and cinematic reel creation to custom software and high-speed web development, we deliver solutions that boost visibility, engagement, and exponential business growth.
                </p>
            </div>

            <!-- BounceCards Interactive Container -->
            <div class="bounce-cards-stage-wrap">
                <div class="bounce-cards" id="services-bounce-cards">
                    
                    <!-- Card 01: Content Creation -->
                    <div class="service-card bounce-cards__card" data-index="0" role="button" tabindex="0" aria-label="Service 01 Content Creation">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">01 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Content Creation</h3>
                            <p class="service-desc">
                                Professional photography, videography, drone shots, and cinematic reels for your business that turn casual viewers into loyal advocates.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Commercial 4K Video Production</li>
                            <li>High-Altitude Drone Aerial Cinematography</li>
                            <li>High-Impact Product & Food Photography</li>
                            <li>Studio Lighting & Professional Staging</li>
                        </ul>
                    </div>

                    <!-- Card 02: Social Media Marketing -->
                    <div class="service-card bounce-cards__card" data-index="1" role="button" tabindex="0" aria-label="Service 02 Social Media Marketing">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">02 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Social Media Marketing</h3>
                            <p class="service-desc">
                                Instagram, Facebook, and Google Business Profile management to grow your online presence, build authority, and engage local audiences.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Instagram & Facebook Page Optimization</li>
                            <li>Google Business Profile & Local Maps SEO</li>
                            <li>Targeted Community Engagement & DM Funnels</li>
                            <li>High-ROAS Meta & Google Ad Campaigns</li>
                        </ul>
                    </div>

                    <!-- Card 03: Reel Production -->
                    <div class="service-card bounce-cards__card" data-index="2" role="button" tabindex="0" aria-label="Service 03 Reel Production">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">03 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Reel Production</h3>
                            <p class="service-desc">
                                End-to-end reel creation: content planning, shooting, editing, captions, and posting support designed for maximum algorithmic reach.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>0.5-Second Attention Hooks & Scripting</li>
                            <li>Fast-Paced Motion Editing & Kinetic Captions</li>
                            <li>Trending Audio Selection & Sound Design</li>
                            <li>Scheduled Publishing & Cadence Strategy</li>
                        </ul>
                    </div>

                    <!-- Card 04: Website Development & SEO -->
                    <div class="service-card bounce-cards__card" data-index="3" role="button" tabindex="0" aria-label="Service 04 Website Development & SEO">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">04 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Website Development & SEO</h3>
                            <p class="service-desc">
                                High-speed modern websites and technical SEO engineered to dominate search rankings, maximize organic traffic, and convert visitors into high-paying clients.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>High-Performance Jamstack & Next.js Websites</li>
                            <li>Technical SEO & Core Web Vitals Optimization</li>
                            <li>Local SEO, Schema Markup & Google Rankings</li>
                            <li>Mobile-First Conversion Architecture & Speed</li>
                        </ul>
                    </div>

                    <!-- Card 05: UI/UX & Digital Design -->
                    <div class="service-card bounce-cards__card" data-index="4" role="button" tabindex="0" aria-label="Service 05 UI/UX & Digital Design">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">05 / SERVICE</span>
                            </div>
                            <h3 class="service-title">UI/UX & Digital Design</h3>
                            <p class="service-desc">
                                Visually arresting digital experiences, intuitive interfaces, and comprehensive brand identity systems crafted to captivate audiences and establish market dominance.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>High-Fidelity UI/UX Prototyping & Figma Design</li>
                            <li>Modern Brand Identity Systems & Typography</li>
                            <li>Micro-Interactions & Fluid Motion Graphics</li>
                            <li>Frictionless User Journey & Conversion CRO</li>
                        </ul>
                    </div>

                    <!-- Card 06: SaaS & Custom Software -->
                    <div class="service-card bounce-cards__card" data-index="5" role="button" tabindex="0" aria-label="Service 06 SaaS & Custom Software">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">06 / SERVICE</span>
                            </div>
                            <h3 class="service-title">SaaS & Custom Software</h3>
                            <p class="service-desc">
                                Bespoke software platforms, cloud applications, and automated workflows tailored for Gyms, Clinics, Cafes & Restaurants to streamline daily operations and scale revenue.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Tailored Software: Gym, Clinic, Cafe & Restaurant POS</li>
                            <li>Automated Billing, Member Systems & Invoicing</li>
                            <li>WhatsApp & SMS Automated Reminders / Retention</li>
                            <li>Secure Cloud Architecture & Real-Time Dashboards</li>
                        </ul>
                    </div>

                </div>

                <!-- BounceCards Navigation & Indicator Dock -->
                <div class="bounce-cards-dock">
                    <div class="bounce-cards-hint">
                        <span class="bounce-pulse-dot"></span>
                        <span>HOVER OR CLICK CARDS TO SPREAD & BOUNCE</span>
                    </div>
                    <div class="bounce-pills-list" id="bounce-cards-pills">
                        <button class="bounce-pill-btn active" data-index="0">01 Content</button>
                        <button class="bounce-pill-btn" data-index="1">02 Marketing</button>
                        <button class="bounce-pill-btn" data-index="2">03 Reels</button>
                        <button class="bounce-pill-btn" data-index="3">04 Web & SEO</button>
                        <button class="bounce-pill-btn" data-index="4">05 UI/UX</button>
                        <button class="bounce-pill-btn" data-index="5">06 SaaS Dev</button>
                    </div>
                    <div class="bounce-nav-arrows">
                        <button class="bounce-arrow-btn" id="bounce-prev-btn" aria-label="Previous Service">←</button>
                        <button class="bounce-arrow-btn" id="bounce-next-btn" aria-label="Next Service">→</button>
                    </div>
                </div>
            </div>

            <!-- Touch Swipe Media Stack Container (Mobile Interface Only) -->
            <div class="services-mobile-deck scd-20" aria-label="Touch swipe media stack">
                <div class="scd-20__deck" id="scd-20-deck">
                    
                    <!-- Mobile Card 01: Content Creation -->
                    <article class="scd-20__card" data-service-num="01/06" data-service-title="Content Creation">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">01 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Content Creation</h3>
                            <p class="service-desc">
                                Professional photography, videography, drone shots, and cinematic reels for your business that turn casual viewers into loyal advocates.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Commercial 4K Video Production</li>
                            <li>High-Altitude Drone Aerial Cinematography</li>
                            <li>High-Impact Product & Food Photography</li>
                            <li>Studio Lighting & Professional Staging</li>
                        </ul>
                    </article>

                    <!-- Mobile Card 02: Social Media Marketing -->
                    <article class="scd-20__card" data-service-num="02/06" data-service-title="Social Media Marketing">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">02 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Social Media Marketing</h3>
                            <p class="service-desc">
                                Instagram, Facebook, and Google Business Profile management to grow your online presence, build authority, and engage local audiences.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Instagram & Facebook Page Optimization</li>
                            <li>Google Business Profile & Local Maps SEO</li>
                            <li>Targeted Community Engagement & DM Funnels</li>
                            <li>High-ROAS Meta & Google Ad Campaigns</li>
                        </ul>
                    </article>

                    <!-- Mobile Card 03: Reel Production -->
                    <article class="scd-20__card" data-service-num="03/06" data-service-title="Reel Production">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">03 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Reel Production</h3>
                            <p class="service-desc">
                                End-to-end reel creation: content planning, shooting, editing, captions, and posting support designed for maximum algorithmic reach.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>0.5-Second Attention Hooks & Scripting</li>
                            <li>Fast-Paced Motion Editing & Kinetic Captions</li>
                            <li>Trending Audio Selection & Sound Design</li>
                            <li>Scheduled Publishing & Cadence Strategy</li>
                        </ul>
                    </article>

                    <!-- Mobile Card 04: Website Development & SEO -->
                    <article class="scd-20__card" data-service-num="04/06" data-service-title="Website Development & SEO">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">04 / SERVICE</span>
                            </div>
                            <h3 class="service-title">Website Development & SEO</h3>
                            <p class="service-desc">
                                High-speed modern websites and technical SEO engineered to dominate search rankings, maximize organic traffic, and convert visitors into high-paying clients.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>High-Performance Jamstack & Next.js Websites</li>
                            <li>Technical SEO & Core Web Vitals Optimization</li>
                            <li>Local SEO, Schema Markup & Google Rankings</li>
                            <li>Mobile-First Conversion Architecture & Speed</li>
                        </ul>
                    </article>

                    <!-- Mobile Card 05: UI/UX & Digital Design -->
                    <article class="scd-20__card" data-service-num="05/06" data-service-title="UI/UX & Digital Design">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">05 / SERVICE</span>
                            </div>
                            <h3 class="service-title">UI/UX & Digital Design</h3>
                            <p class="service-desc">
                                Visually arresting digital experiences, intuitive interfaces, and comprehensive brand identity systems crafted to captivate audiences and establish market dominance.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>High-Fidelity UI/UX Prototyping & Figma Design</li>
                            <li>Modern Brand Identity Systems & Typography</li>
                            <li>Micro-Interactions & Fluid Motion Graphics</li>
                            <li>Frictionless User Journey & Conversion CRO</li>
                        </ul>
                    </article>

                    <!-- Mobile Card 06: SaaS & Custom Software -->
                    <article class="scd-20__card" data-service-num="06/06" data-service-title="SaaS & Custom Software">
                        <div>
                            <div class="service-top-row">
                                <span class="service-num">06 / SERVICE</span>
                            </div>
                            <h3 class="service-title">SaaS & Custom Software</h3>
                            <p class="service-desc">
                                Bespoke software platforms, cloud applications, and automated workflows tailored for Gyms, Clinics, Cafes & Restaurants to streamline daily operations and scale revenue.
                            </p>
                        </div>
                        <ul class="service-features-list">
                            <li>Tailored Software: Gym, Clinic, Cafe & Restaurant POS</li>
                            <li>Automated Billing, Member Systems & Invoicing</li>
                            <li>WhatsApp & SMS Automated Reminders / Retention</li>
                            <li>Secure Cloud Architecture & Real-Time Dashboards</li>
                        </ul>
                    </article>

                </div>
                <div class="scd-20__ctl">
                    <button id="scd-20-prev" aria-label="Previous">‹</button>
                    <p id="scd-20-live" aria-live="polite">01/06 · Content Creation</p>
                    <button id="scd-20-next" aria-label="Next">›</button>
                </div>
                <div class="scd-20__hint">
                    <span class="pulse-dot"></span>
                    <span>SWIPE CARDS OR USE ARROWS</span>
                </div>
            </div>
        </div>
    </section>


        <!-- ==========================================
         PRICE PACKAGES (EXACT DETAILS FROM BROCHURE)
    ========================================== -->
    <section class="pricing-section" id="pricing">
        <div class="pricing-container">
            <div class="pricing-header-wrap">
                <span class="section-tagline">[ TRANSPARENT INVESTMENT ]</span>
                <h2 class="section-headline">PRICE PACKAGES.</h2>
                <p style="color:var(--text-secondary);margin-top:1rem;line-height:1.7;">
                    Clear, honest pricing with zero hidden surprises. Pick the tier built to scale your business.
                </p>
            </div>

            <!-- Mobile Horizontal Scrub Pin Wrapper -->
            <div class="pricing-scroll-pin-wrapper" id="pricing-pin-wrapper">
                <div class="pricing-sticky-viewport" id="pricing-sticky-viewport">
                    <div class="pricing-mobile-progress" id="pricing-mobile-progress">
                        <span class="pricing-progress-pill active" data-step="0">01 STARTER</span>
                        <span class="pricing-progress-pill" data-step="1">02 GROWTH</span>
                        <span class="pricing-progress-pill" data-step="2">03 PREMIUM</span>
                    </div>
                    <div class="pricing-grid" id="pricing-horizontal-track">
                
                <!-- Package 01: Starter Package (Shader Card) -->
                <div class="pricing-card shader-card" data-card-color="0.0, 0.96, 0.61" data-highlight-color="0.63, 1.0, 0.39" style="--card-glow-color: rgba(0, 245, 155, 0.38);">
                    <div class="shader-card-canvas-wrap">
                        <canvas class="shader-card-canvas"></canvas>
                    </div>
                    <div class="shader-card-glow"></div>
                    <div class="shader-card-dark-layer"></div>
                    <div class="shader-card-content">
                        <div>
                            <div class="pricing-tier-name">Starter Package</div>
                            <div class="pricing-tier-desc">Essential launchpad for emerging local brands & cafes.</div>
                            <div class="pricing-price-wrap">
                                <span class="pricing-currency">₹</span>
                                <span class="pricing-amount">9,999</span>
                                <span class="pricing-period">/ pack</span>
                            </div>
                            <ul class="pricing-checklist">
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>3 Professional Reels</strong> (4K Cinema Shot & Edited)</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>1 Shoot Session</strong> ( 2–3 hrs on-location )</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Basic Content Guidance</strong> & Hook Ideation</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span>Color Grading & Trending Audio Selection</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span>Optimized Captions & Hashtag Strategy</span>
                                </li>
                            </ul>
                        </div>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20book%20the%20Starter%20Package%20(₹9,999)!" target="_blank" class="pricing-cta-btn">
                            <span>SELECT STARTER</span>
                            <span>→</span>
                        </a>
                    </div>
                </div>

                <!-- Package 02: Growth Package (Shader Card Featured) -->
                <div class="pricing-card shader-card featured" data-card-color="0.45, 0.95, 0.25" data-highlight-color="0.75, 1.0, 0.4" style="--card-glow-color: rgba(160, 255, 100, 0.5);">
                    <div class="pricing-badge">★ MOST POPULAR</div>
                    <div class="shader-card-canvas-wrap">
                        <canvas class="shader-card-canvas"></canvas>
                    </div>
                    <div class="shader-card-glow"></div>
                    <div class="shader-card-dark-layer"></div>
                    <div class="shader-card-content">
                        <div>
                            <div class="pricing-tier-name">Growth Package</div>
                            <div class="pricing-tier-desc">Accelerated growth engine for scaling businesses, gyms & clinics.</div>
                            <div class="pricing-price-wrap">
                                <span class="pricing-currency">₹</span>
                                <span class="pricing-amount">19,999</span>
                                <span class="pricing-period">/ pack</span>
                            </div>
                            <ul class="pricing-checklist">
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>6 Professional Reels</strong> (Cinematic & High-Energy)</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>4 Graphic Posts</strong> (Promotional Banners & Carousels)</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Monthly Shoot Session</strong> ( 1 Full Day On-Site )</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Comprehensive Content Planning</strong> & Scripts</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Basic Page Management</strong> & Posting Support</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span>Audience Engagement & Organic Growth Guidance</span>
                                </li>
                            </ul>
                        </div>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20scale%20with%20the%20Growth%20Package%20(₹19,999)!" target="_blank" class="pricing-cta-btn">
                            <span>SCALE WITH GROWTH</span>
                            <span>→</span>
                        </a>
                    </div>
                </div>

                <!-- Package 03: Premium Package (Shader Card) -->
                <div class="pricing-card shader-card" data-card-color="0.71, 0.09, 0.62" data-highlight-color="0.97, 0.15, 0.52" style="--card-glow-color: rgba(181, 23, 158, 0.42);">
                    <div class="shader-card-canvas-wrap">
                        <canvas class="shader-card-canvas"></canvas>
                    </div>
                    <div class="shader-card-glow"></div>
                    <div class="shader-card-dark-layer"></div>
                    <div class="shader-card-content">
                        <div>
                            <div class="pricing-tier-name">Premium Package</div>
                            <div class="pricing-tier-desc">Complete social media dominance and full authority management.</div>
                            <div class="pricing-price-wrap">
                                <span class="pricing-currency">₹</span>
                                <span class="pricing-amount">34,999</span>
                                <span class="pricing-period">/ pack</span>
                            </div>
                            <ul class="pricing-checklist">
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>10–12 Professional Reels</strong> (Full Production)</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>8 Graphic Posts</strong> (Custom Brand Art Direction)</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Full Instagram Management</strong> & Strategy</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>Monthly Analytics Report</strong> & Performance Review</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span><strong>30-Day Content Calendar</strong> & Roadmap</span>
                                </li>
                                <li>
                                    <span class="pricing-check-icon">✓</span>
                                    <span>Priority Turnaround & Dedicated Creative Director</span>
                                </li>
                            </ul>
                        </div>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20book%20the%20Premium%20Package%20(₹34,999)!" target="_blank" class="pricing-cta-btn">
                            <span>GO PREMIUM</span>
                            <span>→</span>
                        </a>
                    </div>
                </div>

            </div>
                </div>
            </div>

            <!-- Custom Tech & Web Architecture Callout Banner -->
            <div class="pricing-custom-callout">
                <div class="callout-top-row">
                    <div class="callout-header-content">
                        <span class="callout-eyebrow">[ BESPOKE WEB &amp; SOFTWARE ENGINEERING ]</span>
                        <h4>Need Custom Web Development or Software (Gym, Clinic, Cafe, Restaurant)?</h4>
                        <p>We build tailored digital platforms with custom POS, booking systems, and automated billing. Talk to our engineering team for a customized demo and quotation.</p>
                    </div>

                    <div class="callout-header-cta-wrap">
                        <a href="web-clients.html" class="clients-showcase-btn" title="View Our Web Development Clients &amp; Live Works">
                            <div class="showcase-btn-top">
                                <span class="showcase-live-dot"></span>
                                <span class="showcase-pill-tag">CLIENT PORTFOLIO</span>
                                <span class="showcase-arrow">↗</span>
                            </div>
                            <div class="showcase-btn-title">OUR CLIENTS FOR WEB DEVELOPMENT</div>
                            <div class="showcase-btn-sub">View live client websites, management portals &amp; custom software works</div>
                            <div class="showcase-btn-action">
                                <span>VIEW CLIENT WEBSITES</span>
                                <span>→</span>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Mobile Navigation Controls (only visible on mobile <= 868px) -->
                <div class="callout-mobile-nav" aria-label="Web &amp; Software Plans Navigation">
                    <div class="callout-nav-indicator">
                        <span class="plan-step-badge" id="plan-step-badge">PLAN 1 OF 3</span>
                        <div class="callout-nav-dots" id="callout-nav-dots">
                            <button class="nav-dot active" data-index="0" aria-label="Plan 1: Starting Website Plan"></button>
                            <button class="nav-dot" data-index="1" aria-label="Plan 2: 3D Interactive Website"></button>
                            <button class="nav-dot" data-index="2" aria-label="Plan 3: Software &amp; Custom POS"></button>
                        </div>
                    </div>
                    <div class="callout-nav-arrows">
                        <button class="callout-arrow-btn" id="callout-prev-btn" aria-label="Previous Plan" disabled>‹</button>
                        <button class="callout-arrow-btn" id="callout-next-btn" aria-label="Next Plan">›</button>
                    </div>
                </div>

                <div class="callout-offerings-grid" id="callout-offerings-slider">
                    
                    <!-- 1. Starting Website Plan -->
                    <div class="callout-subcard highlighted">
                        <div class="subcard-top">
                            <span class="subcard-pill">STARTING PLAN</span>
                            <h5 class="subcard-title">Starting Website Plan</h5>
                            <p class="subcard-desc">Modern high-converting business website, clean mobile-responsive layout, SEO architecture & fast turnaround.</p>
                        </div>
                        <div class="subcard-bottom">
                            <div class="subcard-price-row">
                                <span class="subcard-price-val">₹8,000</span>
                                <span class="subcard-price-sub">/ starting website plan</span>
                            </div>
                            <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'm%20interested%20in%20the%20Starting%20Website%20Plan%20(%E2%82%B98,000)!" target="_blank" class="subcard-btn btn-lime">
                                <span>GET STARTED (₹8,000)</span>
                                <span>↗</span>
                            </a>
                        </div>
                    </div>

                    <!-- 2. Interactive 3D Website -->
                    <div class="callout-subcard">
                        <div class="subcard-top">
                            <span class="subcard-pill">NEXT-GEN 3D</span>
                            <h5 class="subcard-title">3D Interactive Website</h5>
                            <p class="subcard-desc">Three.js WebGL experiences, interactive 3D physics, real-time shaders, dynamic camera motion & luxury brand immersion.</p>
                        </div>
                        <div class="subcard-bottom">
                            <div class="subcard-price-row">
                                <span class="subcard-price-val" style="font-size:1.55rem; letter-spacing:0.02em;">CUSTOM 3D</span>
                                <span class="subcard-price-sub">/ bespoke quote</span>
                            </div>
                            <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'd%20like%20to%20contact%20you%20for%20an%20Interactive%203D%20Website!" target="_blank" class="subcard-btn btn-outline">
                                <span>CONTACT US (3D WEB)</span>
                                <span>↗</span>
                            </a>
                        </div>
                    </div>

                    <!-- 3. Custom Software (Gym, Clinic, Cafe, Restaurant) -->
                    <div class="callout-subcard">
                        <div class="subcard-top">
                            <span class="subcard-pill">CUSTOM SOFTWARE</span>
                            <h5 class="subcard-title">Software & Custom POS</h5>
                            <p class="subcard-desc">Engineered management platforms for Gyms, Clinics, Cafes & Restaurants with custom POS, member portals & automated billing.</p>
                        </div>
                        <div class="subcard-bottom">
                            <div class="subcard-price-row">
                                <span class="subcard-price-val" style="font-size:1.55rem; letter-spacing:0.02em;">TAILORED POS</span>
                                <span class="subcard-price-sub">/ demo & quote</span>
                            </div>
                            <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'd%20like%20to%20contact%20you%20for%20Custom%20Software%20(Gym,%20Clinic,%20Cafe,%20Restaurant,%20POS)!" target="_blank" class="subcard-btn btn-outline">
                                <span>CONTACT US (SOFTWARE)</span>
                                <span>↗</span>
                            </a>
                        </div>
                    </div>

                </div>

                <!-- Mobile 'Next Plan' Bottom Action Button (only visible on mobile) -->
                <div class="callout-mobile-bottom-ctl">
                    <button class="callout-next-plan-cta" id="callout-bottom-next-btn" aria-label="Next Plan">
                        <span class="btn-text">NEXT PLAN: 3D INTERACTIVE WEBSITE</span>
                        <span class="btn-arrow">→</span>
                    </button>
                </div>

            </div>
        </div>
    </section>

    <!-- ==========================================
         WHY CHOOSE US? (ELASTIC REEL - REACT BITS PRO)
    ========================================== -->
    <section class="why-section" id="why-us">
        <div class="why-container">
            <div class="section-header-row" style="padding:0;margin-bottom:2.5rem;">
                <div class="section-title-wrap">
                    <span class="section-tagline">[ OUR ADVANTAGE ]</span>
                    <h2 class="section-headline">WHY CHOOSE US?</h2>
                </div>
            </div>

            <!-- Elastic Reel Component (React Bits Pro) -->
            <div class="elastic-reel-wrap" role="region" aria-label="Why Choose Us Elastic Reel">
                <div class="elastic-reel" id="elastic-reel">
                    
                    <!-- Slice 01 -->
                    <div class="elastic-slice is-active" data-index="0">
                        <div class="elastic-slice-bg" style="background-image: url('assets/work_fintech_crypto.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">01</span>
                            <div class="elastic-col-title-vertical">GROWTH STRATEGY</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">01 / PILLAR</span>
                                <span class="elastic-exp-tag">[ ROI & REVENUE ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Growth-Focused Strategy</h3>
                            <p class="elastic-exp-desc">Algorithmic execution strictly aligned with customer retention, footfall, and actual bottom-line revenue, not vanity metrics.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20your%20Growth%20Strategy!" target="_blank" class="elastic-cta-pill">
                                    <span>EXPLORE STRATEGY</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 02 -->
                    <div class="elastic-slice" data-index="1">
                        <div class="elastic-slice-bg" style="background-image: url('assets/service_cinematic_camera.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">02</span>
                            <div class="elastic-col-title-vertical">CONTENT CREATION</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">02 / PILLAR</span>
                                <span class="elastic-exp-tag">[ 4K CINEMA & DRONE ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Professional Content Creation</h3>
                            <p class="elastic-exp-desc">4K commercial cameras, aerial drone videography, cinematic lighting, and studio-grade art direction on every shoot.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'm%20interested%20in%204K%20Cinematic%20Content!" target="_blank" class="elastic-cta-pill">
                                    <span>VIEW PRODUCTION</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 03 -->
                    <div class="elastic-slice" data-index="2">
                        <div class="elastic-slice-bg" style="background-image: url('assets/service_drone_cinema.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">03</span>
                            <div class="elastic-col-title-vertical">FAST DELIVERY</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">03 / PILLAR</span>
                                <span class="elastic-exp-tag">[ RAPID TURNAROUND ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Fast Delivery</h3>
                            <p class="elastic-exp-desc">Rapid concept-to-publish turnaround times so your brand can capitalize on trending cultural moments without delay.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20your%20Fast%20Delivery%20turnaround!" target="_blank" class="elastic-cta-pill">
                                    <span>SPEED TO MARKET</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 04 -->
                    <div class="elastic-slice" data-index="3">
                        <div class="elastic-slice-bg" style="background-image: url('assets/why_us_team_art.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">04</span>
                            <div class="elastic-col-title-vertical">AFFORDABLE PACKAGES</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">04 / PILLAR</span>
                                <span class="elastic-exp-tag">[ TRANSPARENT PRICING ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Affordable Packages</h3>
                            <p class="elastic-exp-desc">High-end agency quality at honest, transparent rates starting at just ₹9,999 with zero hidden fees or surprises.</p>
                            <div class="elastic-exp-footer">
                                <a href="#pricing" class="elastic-cta-pill">
                                    <span>VIEW PACKAGES</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 05 -->
                    <div class="elastic-slice" data-index="4">
                        <div class="elastic-slice-bg" style="background-image: url('assets/work_restaurant_viral.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">05</span>
                            <div class="elastic-col-title-vertical">LOCAL EXPERTISE</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">05 / PILLAR</span>
                                <span class="elastic-exp-tag">[ BENGALURU PULSE ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Local Market Expertise</h3>
                            <p class="elastic-exp-desc">Deep cultural and consumer understanding of Bengaluru and Indian audiences to drive real walk-ins and conversions.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20grow%20my%20Bengaluru%20business!" target="_blank" class="elastic-cta-pill">
                                    <span>LOCAL STRATEGY</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 06 -->
                    <div class="elastic-slice" data-index="5">
                        <div class="elastic-slice-bg" style="background-image: url('assets/service_reel_shoot.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">06</span>
                            <div class="elastic-col-title-vertical">CUSTOM BLUEPRINT</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">06 / PILLAR</span>
                                <span class="elastic-exp-tag">[ TAILORED SOLUTIONS ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Personalized Marketing Solutions</h3>
                            <p class="elastic-exp-desc">Custom blueprints tailored specifically to your business model, whether you are a gym, healthcare clinic, cafe, or retail brand.</p>
                            <div class="elastic-exp-footer">
                                <a href="#services" class="elastic-cta-pill">
                                    <span>CUSTOM BLUEPRINT</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 07 -->
                    <div class="elastic-slice" data-index="6">
                        <div class="elastic-slice-bg" style="background-image: url('assets/work_fashion_brand.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">07</span>
                            <div class="elastic-col-title-vertical">BRAND BUILDING</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">07 / PILLAR</span>
                                <span class="elastic-exp-tag">[ AUTHORITY & IDENTITY ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Consistent Brand Building</h3>
                            <p class="elastic-exp-desc">Cohesive visual aesthetics, distinctive tone of voice, and predictable weekly cadence that establishes lasting market dominance.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20build%20my%20brand%20authority!" target="_blank" class="elastic-cta-pill">
                                    <span>BUILD AUTHORITY</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Slice 08 -->
                    <div class="elastic-slice" data-index="7">
                        <div class="elastic-slice-bg" style="background-image: url('assets/about_creative_studio.jpg');"></div>
                        <div class="elastic-slice-overlay"></div>
                        <div class="elastic-slice-collapsed">
                            <span class="elastic-col-num">08</span>
                            <div class="elastic-col-title-vertical">TRANSPARENT AUDIT</div>
                            <div class="elastic-col-indicator"></div>
                        </div>
                        <div class="elastic-slice-expanded">
                            <div class="elastic-exp-badge-row">
                                <span class="elastic-exp-num">08 / PILLAR</span>
                                <span class="elastic-exp-tag">[ DATA & METRICS ]</span>
                            </div>
                            <h3 class="elastic-exp-title">Transparent Reporting</h3>
                            <p class="elastic-exp-desc">Clear monthly analytics reports, conversion tracking, reach performance, and open communication every single step of the way.</p>
                            <div class="elastic-exp-footer">
                                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20show%20me%20your%20reporting%20process!" target="_blank" class="elastic-cta-pill">
                                    <span>SEE ANALYTICS</span>
                                    <span>→</span>
                                </a>
                            </div>
                        </div>
                    </div>

                </div>

                <!-- Dock Controls Bar -->
                <div class="elastic-dock-bar">
                    <div class="elastic-dock-hint">
                        <span class="pulse-dot"></span>
                        <span>HOVER OR CLICK SLICES TO SWELL REEL</span>
                    </div>

                    <div class="elastic-dots-list" id="elastic-dots">
                        <button class="elastic-dot-btn active" data-index="0" title="01 Growth Strategy" aria-label="Pillar 1"></button>
                        <button class="elastic-dot-btn" data-index="1" title="02 Content Creation" aria-label="Pillar 2"></button>
                        <button class="elastic-dot-btn" data-index="2" title="03 Fast Delivery" aria-label="Pillar 3"></button>
                        <button class="elastic-dot-btn" data-index="3" title="04 Affordable Packages" aria-label="Pillar 4"></button>
                        <button class="elastic-dot-btn" data-index="4" title="05 Local Expertise" aria-label="Pillar 5"></button>
                        <button class="elastic-dot-btn" data-index="5" title="06 Custom Blueprint" aria-label="Pillar 6"></button>
                        <button class="elastic-dot-btn" data-index="6" title="07 Brand Building" aria-label="Pillar 7"></button>
                        <button class="elastic-dot-btn" data-index="7" title="08 Transparent Reporting" aria-label="Pillar 8"></button>
                    </div>

                    <div class="elastic-nav-arrows">
                        <button class="elastic-arrow-btn" id="elastic-prev-btn" aria-label="Previous Pillar">←</button>
                        <button class="elastic-arrow-btn" id="elastic-next-btn" aria-label="Next Pillar">→</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- ==========================================
         CONTACT US SECTION (EXACT DETAILS + INTERACTIVE BOOKING)
    ========================================== -->
    <footer class="contact-section" id="contact">
        <div class="contact-container">
            
            <div class="contact-header-wrap">
                <div class="footer-logo-badge">
                    <img src="___LOGO_B64___" alt="Savkar Media Official Badge">
                </div>
                <span class="cta-eyebrow">BUILT FOR BRANDS THAT WANT MORE THAN AVERAGE</span><br>
                <a href="tel:+919743155527" class="cta-big-link">
                    LET'S TALK.
                </a>
            </div>

            <div class="contact-layout-grid">
                
                <!-- Green Brochure Contact Card Replica -->
                <div class="brochure-contact-box">
                    <div>
                        <h3>Contact Us</h3>
                        <div class="brochure-info-list">
                            
                            <div class="brochure-info-item">
                                <span class="brochure-label-pill">Call</span>
                                <a href="tel:+919743155527" class="brochure-val">+91 97431 55527</a>
                            </div>

                            <div class="brochure-info-item">
                                <span class="brochure-label-pill">Email</span>
                                <a href="mailto:hello@savkarmedia.in" class="brochure-val">hello@savkarmedia.in</a>
                            </div>

                            <div class="brochure-info-item">
                                <span class="brochure-label-pill">Instagram</span>
                                <a href="https://www.instagram.com/savkar_media" target="_blank" class="brochure-val">@savkar_media</a>
                            </div>

                            <div class="brochure-info-item">
                                <span class="brochure-label-pill">Address</span>
                                <span class="brochure-val" style="font-size:1.1rem;">Jayanagar 4th Block, Bengaluru</span>
                            </div>

                        </div>
                    </div>

                    <div class="brochure-action-row">
                        <a href="tel:+919743155527" class="brochure-btn-dark">
                            <span>📞</span>
                            <span>CALL DIRECT</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20discuss%20a%20project!" target="_blank" class="brochure-btn-dark" style="background:#004d25;">
                            <span>💬</span>
                            <span>WHATSAPP</span>
                        </a>
                    </div>
                </div>

                <!-- Interactive Project Inquiry Form -->
                <div class="contact-form-box">
                    <div>
                        <h3>Send A Direct Inquiry</h3>
                        <p>Fill out the details below to instantly message our team via WhatsApp.</p>

                        <form id="inquiry-form" onsubmit="handleInquirySubmit(event)">
                            <div class="form-grid">
                                <div class="form-group">
                                    <label>Your Name</label>
                                    <input type="text" id="form-name" class="form-input" placeholder="e.g. Rahul Sharma" required>
                                </div>
                                <div class="form-group">
                                    <label>Business</label>
                                    <input type="text" id="form-business" class="form-input" placeholder="e.g. Elite Fitness / Cafe Bloom" required>
                                </div>
                                <div class="form-group">
                                    <label>Service Needed</label>
                                    <select id="form-service" class="form-select">
                                        <option value="Reel Production & Content">Reel Production & Content</option>
                                        <option value="Social Media Marketing">Social Media Marketing</option>
                                        <option value="Web Development">Web Development</option>
                                        <option value="Custom Software: Gym Management">Custom Software: Gym Management</option>
                                        <option value="Custom Software: Clinic & EMR">Custom Software: Clinic & Healthcare</option>
                                        <option value="Custom Software: Cafe POS">Custom Software: Cafe Management & POS</option>
                                        <option value="Custom Software: Restaurant POS">Custom Software: Restaurant POS</option>
                                        <option value="Full Branding & Ads">Full Branding & Performance Ads</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <label>Package Tier</label>
                                    <select id="form-package" class="form-select">
                                        <option value="Growth Package (₹19,999)">Growth Package (₹19,999) - Most Popular</option>
                                        <option value="Starter Package (₹9,999)">Starter Package (₹9,999)</option>
                                        <option value="Premium Package (₹34,999)">Premium Package (₹34,999)</option>
                                        <option value="Website Starting Plan (₹8,000)">Website Starting Plan (₹8,000)</option>
                                        <option value="Interactive 3D Website Quote">Interactive 3D Website Quote</option>
                                        <option value="Custom Software Development Quote">Custom Software Development Quote</option>
                                    </select>
                                </div>
                                <div class="form-group full-width">
                                    <label>Project Details / Requirements</label>
                                    <textarea id="form-message" class="form-textarea" placeholder="Tell us about your brand, goals, or timeline..."></textarea>
                                </div>
                            </div>
                            <button type="submit" class="form-submit-btn">
                                <span>SEND INQUIRY VIA WHATSAPP</span>
                                <span>↗</span>
                            </button>
                        </form>
                    </div>
                </div>

            </div>

            <!-- FOOTER BOTTOM BAR: DEDICATED TERMS & CONDITIONS PAGE LINK -->
            <div class="footer-bottom-bar">
                <div class="footer-address-col">SAVKAR MEDIA — JAYANAGAR 4TH BLOCK, BENGALURU, KARNATAKA, INDIA</div>
                <div class="footer-terms-col">
                    <a href="terms.html" class="footer-terms-trigger-btn" id="footer-terms-nav-btn">
                        <span>📜</span>
                        <span>TERMS &amp; CONDITIONS (MOU)</span>
                        <span class="terms-nav-arrow">↗</span>
                    </a>
                </div>
                <div class="footer-copyright-col">© 2026 ALL RIGHTS RESERVED</div>
            </div>

        </div>
    </footer>

    <!-- ===================================================
         CINEMATIC THREE.JS SHADER & SCRIPT ENGINE
    =================================================== -->
    <script>
    (function() {
        'use strict';

        // 1. Lenis Smooth Scroll
        const lenis = new Lenis({
            duration: 1.0,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            smoothWheel: true,
            smoothTouch: false
        });

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);

        // Form Submission to WhatsApp
        window.handleInquirySubmit = function(e) {
            e.preventDefault();
            const name = document.getElementById('form-name').value;
            const business = document.getElementById('form-business').value;
            const service = document.getElementById('form-service').value;
            const packageTier = document.getElementById('form-package').value;
            const msg = document.getElementById('form-message').value;

            const text = `Hi Savkar Media!%0A%0A*Name:* ${encodeURIComponent(name)}%0A*Business:* ${encodeURIComponent(business)}%0A*Service:* ${encodeURIComponent(service)}%0A*Package:* ${encodeURIComponent(packageTier)}%0A*Details:* ${encodeURIComponent(msg)}`;
            window.open(`https://wa.me/919743155527?text=${text}`, '_blank');
        };

        // ==========================================
        // 2. REAL CURVED DOLLAR BILL FALLING RAIN
        // ==========================================
        const cashCanvas = document.getElementById('cash-rain-canvas');
        const ctx = cashCanvas.getContext('2d');
        const dollarImg = new Image();
        dollarImg.src = '___DOLLAR_B64___';

        let width = window.innerWidth;
        let height = window.innerHeight;

        function resizeCashCanvas() {
            width = window.innerWidth;
            height = window.innerHeight;
            cashCanvas.width = width;
            cashCanvas.height = height;
        }
        resizeCashCanvas();
        window.addEventListener('resize', resizeCashCanvas);

        let isCashRainEnabled = false; // HOME PAGE DEFAULTS TO OFF!
        let isIntroRaining = true;     // LANDING PAGE HAS AMBIENT RAIN

        class DollarBill {
            constructor(startX, startY, isTemporary = false) {
                this.isTemporary = isTemporary;
                this.reset(startX, startY);
            }

            reset(startX, startY) {
                this.x = startX !== undefined ? startX : Math.random() * width;
                this.y = startY !== undefined ? startY : -140 - Math.random() * 200;
                this.speedY = 1.4 + Math.random() * 2.5;
                this.speedX = (Math.random() - 0.5) * 1.2;
                this.width = 75 + Math.random() * 65;
                this.height = this.width * 1.4;
                this.rotation = Math.random() * Math.PI * 2;
                this.rotSpeed = (Math.random() - 0.5) * 0.035;
                this.scaleX = 0.8 + Math.random() * 0.4;
                this.flutterSpeed = 0.025 + Math.random() * 0.035;
                this.flutterAngle = Math.random() * Math.PI * 2;
                this.opacity = 0.5 + Math.random() * 0.45;
            }

            update() {
                this.y += this.speedY;
                this.x += this.speedX + Math.sin(this.flutterAngle) * 0.8;
                this.rotation += this.rotSpeed;
                this.flutterAngle += this.flutterSpeed;
                this.scaleX = Math.cos(this.flutterAngle) * 0.9;

                if (this.y > height + 220) {
                    if (this.isTemporary) {
                        return false;
                    }
                    this.reset();
                }
                return true;
            }

            draw() {
                if (!dollarImg.complete || dollarImg.naturalWidth === 0) return;
                ctx.save();
                ctx.translate(this.x, this.y);
                ctx.rotate(this.rotation);
                ctx.scale(this.scaleX, 1.0);
                ctx.globalAlpha = this.opacity;
                ctx.drawImage(dollarImg, -this.width / 2, -this.height / 2, this.width, this.height);
                ctx.restore();
            }
        }

        const bills = [];
        const TOTAL_AMBIENT_BILLS = 28;
        for (let i = 0; i < TOTAL_AMBIENT_BILLS; i++) {
            bills.push(new DollarBill(Math.random() * width, Math.random() * height));
        }

        function burstTemporaryCash(count = 6) {
            for (let i = 0; i < count; i++) {
                bills.push(new DollarBill(Math.random() * width, -100 - Math.random() * 80, true));
            }
            startCashLoop();
        }

        let cashAnimationRunning = false;
        let cashRafId = null;

        function startCashLoop() {
            if (cashAnimationRunning) return;
            cashAnimationRunning = true;
            cashRafId = requestAnimationFrame(animateCash);
        }

        function stopCashLoop() {
            cashAnimationRunning = false;
            if (cashRafId) {
                cancelAnimationFrame(cashRafId);
                cashRafId = null;
            }
            ctx.clearRect(0, 0, width, height);
        }

        function animateCash() {
            if (!cashAnimationRunning) return;

            // When intro is done, cash rain toggle is OFF, and all temporary burst bills have expired:
            if (!isIntroRaining && !isCashRainEnabled && bills.length === 0) {
                stopCashLoop();
                return;
            }

            ctx.clearRect(0, 0, width, height);
            for (let i = bills.length - 1; i >= 0; i--) {
                const alive = bills[i].update();
                if (!alive) {
                    bills.splice(i, 1);
                } else {
                    bills[i].draw();
                }
            }

            cashRafId = requestAnimationFrame(animateCash);
        }

        dollarImg.onload = () => {
            startCashLoop();
        };

        // ==========================================
        // 3. CASH RAIN ON/OFF TOGGLE CONTROLLER
        // ==========================================
        const cashToggleBtn = document.getElementById('cash-rain-toggle-btn');
        const cashStatusText = document.getElementById('cash-status-text');

        function toggleCashRain() {
            isCashRainEnabled = !isCashRainEnabled;
            if (isCashRainEnabled) {
                cashToggleBtn.classList.remove('off');
                cashStatusText.textContent = 'ON';
                cashCanvas.style.opacity = '1';
                if (bills.length < TOTAL_AMBIENT_BILLS) {
                    for (let i = bills.length; i < TOTAL_AMBIENT_BILLS; i++) {
                        bills.push(new DollarBill(Math.random() * width, -100 - Math.random() * 200));
                    }
                }
                startCashLoop();
            } else {
                cashToggleBtn.classList.add('off');
                cashStatusText.textContent = 'OFF';
                cashCanvas.style.opacity = '0';
                bills.length = 0;
                stopCashLoop();
            }
        }

        cashToggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            toggleCashRain();
        });

        // ==========================================
        // 4. THREE.JS LIQUID FLUID LOGO ON INTRO
        // ==========================================
        const liquidContainer = document.getElementById('liquid-container');
        const liquidCanvas = document.getElementById('liquid-canvas');

        const scene = new THREE.Scene();
        const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
        const renderer = new THREE.WebGLRenderer({
            canvas: liquidCanvas,
            alpha: true,
            antialias: true,
            powerPreference: 'high-performance'
        });

        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        renderer.setPixelRatio(dpr);
        renderer.setSize(window.innerWidth, window.innerHeight);

        const textureLoader = new THREE.TextureLoader();
        const logoTexture = textureLoader.load('___LOGO_B64___');
        logoTexture.generateMipmaps = true;
        logoTexture.minFilter = THREE.LinearMipMapLinearFilter;
        logoTexture.magFilter = THREE.LinearFilter;

        const vertexShader = `
            varying vec2 vUv;
            void main() {
                vUv = uv;
                gl_Position = vec4(position, 1.0);
            }
        `;

        const fragmentShader = `
            uniform float u_time;
            uniform vec2 u_mouse;
            uniform vec2 u_resolution;
            uniform float u_scale;
            uniform sampler2D u_texture;
            varying vec2 vUv;

            void main() {
                vec2 st = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / min(u_resolution.x, u_resolution.y);
                vec2 mouse = (u_mouse * 2.0 - u_resolution.xy) / min(u_resolution.x, u_resolution.y);

                float dist = length(st);
                float mouseDist = length(st - mouse);

                float wave1 = sin(dist * 14.0 - u_time * 2.2) * 0.025;
                float wave2 = cos(atan(st.y, st.x) * 4.0 + u_time * 1.4) * 0.018;
                float mouseWave = exp(-mouseDist * 3.5) * sin(mouseDist * 22.0 - u_time * 5.0) * 0.04;

                vec2 uv = ((st * u_scale) / (1.0 + wave1 + wave2 + mouseWave)) * 0.5 + 0.5;

                if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
                    discard;
                }

                vec4 texColor = texture2D(u_texture, uv);
                if (texColor.a < 0.02) {
                    discard;
                }

                gl_FragColor = texColor;
            }
        `;

        const getLiquidScale = () => (window.innerWidth <= 768 ? 1.35 : 1.12);

        const uniforms = {
            u_time: { value: 0 },
            u_mouse: { value: new THREE.Vector2(renderer.domElement.width / 2, renderer.domElement.height / 2) },
            u_resolution: { value: new THREE.Vector2(renderer.domElement.width, renderer.domElement.height) },
            u_scale: { value: getLiquidScale() },
            u_texture: { value: logoTexture }
        };

        const material = new THREE.ShaderMaterial({
            vertexShader,
            fragmentShader,
            uniforms,
            transparent: true
        });

        const geometry = new THREE.PlaneGeometry(2, 2);
        const mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);

        let targetMouse = new THREE.Vector2(renderer.domElement.width / 2, renderer.domElement.height / 2);
        window.addEventListener('pointermove', (e) => {
            const curDpr = renderer.getPixelRatio();
            targetMouse.x = e.clientX * curDpr;
            targetMouse.y = (window.innerHeight - e.clientY) * curDpr;
        });

        function resizeLiquid() {
            const curDpr = Math.min(window.devicePixelRatio || 1, 2);
            renderer.setPixelRatio(curDpr);
            renderer.setSize(window.innerWidth, window.innerHeight);
            uniforms.u_resolution.value.set(renderer.domElement.width, renderer.domElement.height);
            uniforms.u_scale.value = getLiquidScale();
        }
        window.addEventListener('resize', resizeLiquid);

        let shaderActive = true;
        let animationFrameId;
        const clock = new THREE.Clock();

        function renderShader() {
            if (!shaderActive) return;
            uniforms.u_time.value = clock.getElapsedTime();
            uniforms.u_mouse.value.lerp(targetMouse, 0.08);
            renderer.render(scene, camera);
            animationFrameId = requestAnimationFrame(renderShader);
        }
        renderShader();

        // ==========================================
        // 5. 3D CASH ZOOM TRANSITION (THE 3 CASH BILLS ZOOM EFFECT)
        // ==========================================
        let isTransitioned = false;
        const cashZoomPortal = document.getElementById('cash-zoom-portal');
        const zoomBill = document.getElementById('zoom-bill');
        const zoomBillL = document.getElementById('zoom-bill-l');
        const zoomBillR = document.getElementById('zoom-bill-r');

        function cinematicCashZoomAndEnter() {
            if (isTransitioned) return;
            isTransitioned = true;

            // Step 1: Burst 22 temporary high-speed bills
            burstTemporaryCash(22);

            // Step 2: Make 3D zoom portal visible
            cashZoomPortal.style.opacity = '1';

            // Step 3: Animate the massive 3D dollar bill vortex FLYING FORWARD INTO FULL ZOOM!
            // Center bill exploding right into camera/screen
            gsap.fromTo(zoomBill, 
                {
                    x: 0,
                    y: 0,
                    z: -250,
                    scale: 0.28,
                    rotationX: 20,
                    rotationY: -15,
                    rotationZ: -10,
                    opacity: 0.95
                },
                {
                    z: 1150,
                    scale: 28, // FULL ZOOM EXPLODING RIGHT INTO CAMERA / SCREEN!
                    rotationX: 8,
                    rotationY: 15,
                    rotationZ: 32,
                    opacity: 1,
                    duration: 1.1,
                    ease: 'power3.in',
                    onComplete: () => {
                        cashZoomPortal.style.display = 'none';
                    }
                }
            );

            // Flanking left bill rushing past camera
            gsap.fromTo(zoomBillL,
                { x: -280, y: 80, z: -400, scale: 0.2, rotationZ: -35, opacity: 0.85 },
                { x: -900, y: 250, z: 900, scale: 14, rotationZ: -60, opacity: 1, duration: 1.0, ease: 'power3.in' }
            );

            // Flanking right bill rushing past camera
            gsap.fromTo(zoomBillR,
                { x: 280, y: -80, z: -400, scale: 0.2, rotationZ: 25, opacity: 0.85 },
                { x: 900, y: -250, z: 900, scale: 14, rotationZ: 55, opacity: 1, duration: 1.0, ease: 'power3.in' }
            );

            gsap.to(liquidContainer, {
                opacity: 0,
                scale: 1.18,
                filter: 'blur(14px)',
                duration: 0.75,
                delay: 0.35,
                ease: 'power2.inOut',
                onComplete: () => {
                    liquidContainer.style.opacity = '0';
                    liquidContainer.style.visibility = 'hidden';
                    liquidContainer.style.pointerEvents = 'none';

                    shaderActive = false;
                    if (animationFrameId) {
                        cancelAnimationFrame(animationFrameId);
                    }

                    // Turn intro rain off: home page defaults to OFF!
                    isIntroRaining = false;
                    if (!isCashRainEnabled) {
                        bills.length = 0;
                        ctx.clearRect(0, 0, cashCanvas.width, cashCanvas.height);
                    }

                    // Reveal main hero typography
                    gsap.fromTo('.hero-giant-title .word-inner', 
                        { y: '120%', opacity: 0, scale: 0.88 },
                        { 
                            y: '0%', 
                            opacity: 1, 
                            scale: 1.0,
                            stagger: 0.12, 
                            duration: 1.2, 
                            ease: 'power4.out',
                            delay: 0.05
                        }
                    );

                    gsap.fromTo('.hero-logo-badge-center',
                        { scale: 0, rotation: -180 },
                        { scale: 1, rotation: 0, duration: 1.1, ease: 'back.out(1.8)' }
                    );
                }
            });
        }

        // Click on Enter Button OR click on canvas triggers transition
        document.getElementById('enter-experience-btn').addEventListener('click', (e) => {
            e.stopPropagation();
            cinematicCashZoomAndEnter();
        });
        liquidCanvas.addEventListener('click', cinematicCashZoomAndEnter);

        // Scrolling down on intro triggers transition
        window.addEventListener('wheel', (e) => {
            if (!isTransitioned && e.deltaY > 5) {
                cinematicCashZoomAndEnter();
            }
        }, { passive: true });

        let touchStartY = 0;
        window.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
        }, { passive: true });
        window.addEventListener('touchmove', (e) => {
            if (!isTransitioned && (touchStartY - e.touches[0].clientY) > 15) {
                cinematicCashZoomAndEnter();
            }
        }, { passive: true });

        // Fast scroll triggers subtle burst if enabled
        let lastScrollY = 0;
        window.addEventListener('scroll', () => {
            const currentScroll = window.scrollY;
            if (Math.abs(currentScroll - lastScrollY) > 220 && isTransitioned && isCashRainEnabled) {
                if (Math.random() > 0.5) {
                    burstTemporaryCash(5);
                }
                lastScrollY = currentScroll;
            }
        }, { passive: true });

        // ==========================================
        // 6. MANUAL SLIDER ARROW CONTROLS (NEXT / PREV)
        // ==========================================
        const track = document.getElementById('slider-track');
        let currentShift = 0;
        const cardStep = 340;

        document.getElementById('slide-next').addEventListener('click', () => {
            currentShift -= cardStep;
            track.style.animation = 'none';
            gsap.to(track, {
                x: currentShift,
                duration: 0.5,
                ease: 'power2.out',
                onComplete: () => {
                    if (Math.abs(currentShift) > (340 * 5)) {
                        currentShift = 0;
                        gsap.set(track, { x: 0 });
                    }
                }
            });
        });

        document.getElementById('slide-prev').addEventListener('click', () => {
            currentShift += cardStep;
            if (currentShift > 0) {
                currentShift = -(340 * 4);
            }
            track.style.animation = 'none';
            gsap.to(track, {
                x: currentShift,
                duration: 0.5,
                ease: 'power2.out'
            });
        });

    })();


        // ==========================================
        // ELASTIC REEL (React Bits Pro Inspired Dock Reel)
        // ==========================================
        (() => {
            const reel = document.getElementById('elastic-reel');
            if (!reel) return;

            const slices = Array.from(reel.querySelectorAll('.elastic-slice'));
            const dots = Array.from(document.querySelectorAll('.elastic-dot-btn'));
            const prevBtn = document.getElementById('elastic-prev-btn');
            const nextBtn = document.getElementById('elastic-next-btn');

            let currentIndex = 0;

            function setActiveIndex(idx) {
                if (idx < 0) idx = slices.length - 1;
                if (idx >= slices.length) idx = 0;
                currentIndex = idx;

                slices.forEach((slice, i) => {
                    slice.classList.remove('is-active', 'is-neighbor');
                    if (i === currentIndex) {
                        slice.classList.add('is-active');
                    } else if (Math.abs(i - currentIndex) === 1) {
                        slice.classList.add('is-neighbor');
                    }
                });

                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === currentIndex);
                });
            }

            // Mouse interaction on individual slice
            slices.forEach((slice, i) => {
                slice.addEventListener('mouseenter', () => {
                    setActiveIndex(i);
                });

                slice.addEventListener('click', () => {
                    setActiveIndex(i);
                });
            });

            // Dock Navigation arrows
            prevBtn?.addEventListener('click', (e) => {
                e.preventDefault();
                setActiveIndex(currentIndex - 1);
            });

            nextBtn?.addEventListener('click', (e) => {
                e.preventDefault();
                setActiveIndex(currentIndex + 1);
            });

            // Dots click
            dots.forEach((dot, i) => {
                dot.addEventListener('click', (e) => {
                    e.preventDefault();
                    setActiveIndex(i);
                });
            });

            // Touch swipe support for mobile
            let touchStartX = 0;
            reel.addEventListener('touchstart', e => {
                touchStartX = e.changedTouches[0].clientX;
            }, { passive: true });

            reel.addEventListener('touchend', e => {
                const diff = e.changedTouches[0].clientX - touchStartX;
                if (Math.abs(diff) > 40) {
                    if (diff < 0) setActiveIndex(currentIndex + 1);
                    else setActiveIndex(currentIndex - 1);
                }
            }, { passive: true });

            // Keyboard navigation when near section
            window.addEventListener('keydown', e => {
                const rect = reel.getBoundingClientRect();
                const inView = rect.top < window.innerHeight && rect.bottom > 0;
                if (!inView) return;

                if (e.key === 'ArrowRight') setActiveIndex(currentIndex + 1);
                if (e.key === 'ArrowLeft') setActiveIndex(currentIndex - 1);
            });

            // Initial active slice
            setActiveIndex(0);
        })();

        // ==========================================
        // SHADER CARD COMPONENT (React Bits Pro Inspired)
        // 3D Interactive WebGL Flame Shader with Pointer Wind Reaction
        // ==========================================
        (() => {
            const cards = Array.from(document.querySelectorAll('.shader-card'));
            if (!cards.length) return;

            const vsSource = `
                attribute vec2 position;
                void main() {
                    gl_Position = vec4(position, 0.0, 1.0);
                }
            `;

            const fsSource = `
                precision highp float;
                uniform vec2 u_resolution;
                uniform float u_time;
                uniform vec2 u_mouse;
                uniform vec3 u_color;
                uniform vec3 u_highlight;
                uniform float u_intensity;

                float hash(vec2 p) {
                    p = fract(p * vec2(123.34, 456.21));
                    p += dot(p, p + 45.32);
                    return fract(p.x * p.y);
                }

                float noise(vec2 p) {
                    vec2 i = floor(p);
                    vec2 f = fract(p);
                    f = f * f * (3.0 - 2.0 * f);
                    float a = hash(i);
                    float b = hash(i + vec2(1.0, 0.0));
                    float c = hash(i + vec2(0.0, 1.0));
                    float d = hash(i + vec2(1.0, 1.0));
                    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
                }

                float fbm(vec2 p) {
                    float v = 0.0;
                    float a = 0.5;
                    mat2 rot = mat2(0.8775, 0.4794, -0.4794, 0.8775);
                    for (int i = 0; i < 4; ++i) {
                        v += a * noise(p);
                        p = rot * p * 2.05 + vec2(1.7, 9.2);
                        a *= 0.5;
                    }
                    return v;
                }

                void main() {
                    vec2 uv = gl_FragCoord.xy / u_resolution.xy;
                    vec2 p = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / min(u_resolution.x, u_resolution.y);
                    
                    // Wind / mouse influence
                    vec2 m = u_mouse * 2.0 - 1.0;
                    float d = length(p - m);
                    vec2 wind = (p - m) * 0.16 / (d + 0.28);
                    
                    float t = u_time * 0.75;
                    vec2 q = p + wind * (0.35 + u_intensity * 0.4);
                    q.y -= t * 0.65;
                    
                    // Procedural rising flames
                    float f1 = fbm(q * 2.1);
                    float f2 = fbm(q * 4.2 - vec2(0.0, t * 0.85));
                    float f = f1 * 0.65 + f2 * 0.35;
                    
                    // Flame mask rising from bottom of card
                    float rise = (1.0 - uv.y) * 1.35;
                    float flame = smoothstep(0.12, 0.85, f * rise + 0.18 + u_intensity * 0.16);
                    
                    // Luminous color blending
                    vec3 col = mix(u_color * 0.18, u_color, flame);
                    col = mix(col, u_highlight, pow(flame, 2.5) * (0.8 + u_intensity * 0.6));
                    
                    // Alpha transparency
                    float alpha = clamp(flame * (0.55 + u_intensity * 0.35), 0.0, 0.92);
                    
                    gl_FragColor = vec4(col, alpha);
                }
            `;

            function createShader(gl, type, source) {
                const s = gl.createShader(type);
                gl.shaderSource(s, source);
                gl.compileShader(s);
                return s;
            }

            const cardInstances = [];

            cards.forEach(card => {
                const canvas = card.querySelector('.shader-card-canvas');
                if (!canvas) return;
                const gl = canvas.getContext('webgl', { alpha: true, antialias: false, powerPreference: 'high-performance' });
                if (!gl) return;

                const program = gl.createProgram();
                gl.attachShader(program, createShader(gl, gl.VERTEX_SHADER, vsSource));
                gl.attachShader(program, createShader(gl, gl.FRAGMENT_SHADER, fsSource));
                gl.linkProgram(program);

                const posBuf = gl.createBuffer();
                gl.bindBuffer(gl.ARRAY_BUFFER, posBuf);
                gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
                    -1, -1,
                     1, -1,
                    -1,  1,
                    -1,  1,
                     1, -1,
                     1,  1
                ]), gl.STATIC_DRAW);

                const posAttr = gl.getAttribLocation(program, 'position');
                const uRes = gl.getUniformLocation(program, 'u_resolution');
                const uTime = gl.getUniformLocation(program, 'u_time');
                const uMouse = gl.getUniformLocation(program, 'u_mouse');
                const uColor = gl.getUniformLocation(program, 'u_color');
                const uHighlight = gl.getUniformLocation(program, 'u_highlight');
                const uIntensity = gl.getUniformLocation(program, 'u_intensity');

                // Read colors from data attributes
                const cArr = (card.dataset.cardColor || '0.63, 1.0, 0.39').split(',').map(v => parseFloat(v.trim()));
                const hArr = (card.dataset.highlightColor || '1.0, 1.0, 1.0').split(',').map(v => parseFloat(v.trim()));

                const instance = {
                    card,
                    canvas,
                    gl,
                    program,
                    posAttr,
                    posBuf,
                    uRes,
                    uTime,
                    uMouse,
                    uColor,
                    uHighlight,
                    uIntensity,
                    color: cArr,
                    highlight: hArr,
                    intensity: 0.0,
                    targetIntensity: 0.0,
                    mouse: [0.5, 0.5],
                    targetMouse: [0.5, 0.5],
                    width: 0,
                    height: 0
                };

                // Resize handler
                function resize() {
                    const rect = card.getBoundingClientRect();
                    const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
                    const w = Math.floor(rect.width * dpr);
                    const h = Math.floor(rect.height * dpr);
                    if (canvas.width !== w || canvas.height !== h) {
                        canvas.width = w;
                        canvas.height = h;
                        instance.width = w;
                        instance.height = h;
                    }
                }
                resize();
                window.addEventListener('resize', resize, { passive: true });

                // 3D Tilt & Pointer Tracking
                card.addEventListener('mousemove', e => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const cX = rect.width / 2;
                    const cY = rect.height / 2;
                    const rotX = ((y - cY) / cY) * -8;
                    const rotY = ((x - cX) / cX) * 8;
                    
                    const isFeatured = card.classList.contains('featured');
                    const baseScale = isFeatured ? 'scale3d(1.05, 1.05, 1.05)' : 'scale3d(1.02, 1.02, 1.02)';
                    card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-8px) ${baseScale}`;
                    card.style.setProperty('--mouse-x', `${(x / rect.width * 100).toFixed(1)}%`);
                    card.style.setProperty('--mouse-y', `${(y / rect.height * 100).toFixed(1)}%`);

                    instance.targetMouse = [x / rect.width, 1.0 - (y / rect.height)];
                    instance.targetIntensity = 1.0;
                });

                card.addEventListener('mouseenter', () => {
                    instance.targetIntensity = 1.0;
                });

                card.addEventListener('mouseleave', () => {
                    const isFeatured = card.classList.contains('featured');
                    const baseScale = isFeatured ? 'scale(1.03)' : 'scale(1)';
                    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) ${baseScale}`;
                    instance.targetIntensity = 0.0;
                    instance.targetMouse = [0.5, 0.5];
                });

                cardInstances.push(instance);
            });

            // Intersection Observer to run loop only when visible
            let isVisible = false;
            const pricingSec = document.getElementById('pricing');
            if (pricingSec && 'IntersectionObserver' in window) {
                const observer = new IntersectionObserver(entries => {
                    isVisible = entries[0].isIntersecting;
                }, { threshold: 0.05 });
                observer.observe(pricingSec);
            }

            let startTime = performance.now();
            function render() {
                requestAnimationFrame(render);
                if (!isVisible) return;

                const time = (performance.now() - startTime) * 0.001;

                cardInstances.forEach(inst => {
                    const gl = inst.gl;
                    if (!inst.width || !inst.height) return;

                    // Smooth mouse and intensity interpolation
                    inst.intensity += (inst.targetIntensity - inst.intensity) * 0.08;
                    inst.mouse[0] += (inst.targetMouse[0] - inst.mouse[0]) * 0.1;
                    inst.mouse[1] += (inst.targetMouse[1] - inst.mouse[1]) * 0.1;

                    gl.viewport(0, 0, inst.width, inst.height);
                    gl.useProgram(inst.program);

                    gl.bindBuffer(gl.ARRAY_BUFFER, inst.posBuf);
                    gl.enableVertexAttribArray(inst.posAttr);
                    gl.vertexAttribPointer(inst.posAttr, 2, gl.FLOAT, false, 0, 0);

                    gl.uniform2f(inst.uRes, inst.width, inst.height);
                    gl.uniform1f(inst.uTime, time);
                    gl.uniform2f(inst.uMouse, inst.mouse[0], inst.mouse[1]);
                    gl.uniform3f(inst.uColor, inst.color[0], inst.color[1], inst.color[2]);
                    gl.uniform3f(inst.uHighlight, inst.highlight[0], inst.highlight[1], inst.highlight[2]);
                    gl.uniform1f(inst.uIntensity, inst.intensity);

                    gl.drawArrays(gl.TRIANGLES, 0, 6);
                });
            }
            requestAnimationFrame(render);
        })();

        // ==========================================
        // ==========================================
        // MOBILE HORIZONTAL SCROLL SCRUBBING
        // FOR 3 MAIN PRICING CARDS (<= 868px)
        // Cards sit on the same horizontal line and glide
        // from right to left one by one as the user scrolls down,
        // and reverse cleanly when scrolling back up
        // ==========================================
        (() => {
            const pinWrapper = document.getElementById('pricing-pin-wrapper');
            const track = document.getElementById('pricing-horizontal-track');
            const pills = Array.from(document.querySelectorAll('.pricing-progress-pill'));
            if (!pinWrapper || !track) return;

            const cards = Array.from(track.querySelectorAll(':scope > .pricing-card.shader-card'));
            if (!cards.length) return;

            let ticking = false;

            function updatePricingHorizontalScroll() {
                const isMobile = window.innerWidth <= 868;
                if (!isMobile) {
                    track.style.transform = '';
                    cards.forEach(c => {
                        c.style.transform = '';
                        c.style.opacity = '';
                    });
                    ticking = false;
                    return;
                }

                const rect = pinWrapper.getBoundingClientRect();
                const vh = window.innerHeight;
                const vw = window.innerWidth;
                const cardWidth = Math.min(340, vw * 0.86);
                const gap = 20;

                const cardStride = cardWidth + gap;

                // .pricing-sticky-viewport aligns items center, so Card 1 (Growth)
                // is naturally centered at trackX = 0.
                // Shifting track to +cardStride centers Card 0 (Starter).
                // Shifting track to -cardStride centers Card 2 (Premium).
                const target0 = cardStride;
                const target1 = 0;
                const target2 = -cardStride;

                // Available scroll distance inside pin wrapper
                const scrollDistance = pinWrapper.offsetHeight - vh;
                if (scrollDistance <= 0) {
                    ticking = false;
                    return;
                }

                // Top offset when sticky header kicks in
                const stickyTop = 76;
                const scrollProgress = Math.max(0, Math.min(1, (stickyTop - rect.top) / scrollDistance));

                let trackX;
                if (rect.top > stickyTop) {
                    // Before pinning (scrolling into view from top):
                    // Starter package glides in smoothly from right to center
                    const enterProgress = Math.max(0, Math.min(1, (vh - rect.top) / (vh - stickyTop)));
                    const enterEase = Math.sin(enterProgress * Math.PI * 0.5);
                    const enterOffset = (1 - enterEase) * (vw * 0.85);
                    trackX = target0 + enterOffset;
                } else if (scrollProgress <= 0.5) {
                    // From Card 0 (Starter) to Card 1 (Growth):
                    // Starter exits to left, Growth arrives from right to center
                    const p = scrollProgress / 0.5;
                    const ease = Math.sin(p * Math.PI * 0.5);
                    trackX = target0 + (target1 - target0) * ease;
                } else {
                    // From Card 1 (Growth) to Card 2 (Premium):
                    // Growth exits to left, Premium arrives from right to center
                    const p = (scrollProgress - 0.5) / 0.5;
                    const ease = Math.sin(p * Math.PI * 0.5);
                    trackX = target1 + (target2 - target1) * ease;
                }

                track.style.transform = `translate3d(${trackX.toFixed(1)}px, 0, 0)`;

                // Update active pill indicator
                const activeIndex = scrollProgress < 0.33 ? 0 : (scrollProgress < 0.67 ? 1 : 2);
                pills.forEach((pill, idx) => {
                    pill.classList.toggle('active', idx === activeIndex);
                });

                // Subtle focus depth effect for cards
                cards.forEach((card, idx) => {
                    let cardTarget;
                    if (idx === 0) cardTarget = target0;
                    else if (idx === 1) cardTarget = target1;
                    else cardTarget = target2;

                    const distFromCenter = Math.abs(trackX - cardTarget);
                    const focus = Math.max(0, 1 - distFromCenter / (cardWidth + gap));
                    const opacity = 0.55 + focus * 0.45;
                    const scale = 0.95 + focus * 0.05;
                    card.style.opacity = opacity.toFixed(2);
                    card.style.transform = `scale(${scale.toFixed(3)})`;
                });

                ticking = false;
            }

            window.addEventListener('scroll', () => {
                if (!ticking) {
                    ticking = true;
                    requestAnimationFrame(updatePricingHorizontalScroll);
                }
            }, { passive: true });

            window.addEventListener('resize', () => {
                updatePricingHorizontalScroll();
            }, { passive: true });

            // Allow clicking pills to smoothly jump to that card
            pills.forEach((pill, idx) => {
                pill.addEventListener('click', () => {
                    const scrollDistance = pinWrapper.offsetHeight - window.innerHeight;
                    const stickyTop = 76;
                    const pinTop = pinWrapper.getBoundingClientRect().top + window.scrollY - stickyTop;
                    const progressTargets = [0.05, 0.5, 0.95];
                    const targetScrollY = pinTop + scrollDistance * progressTargets[idx];
                    window.scrollTo({ top: targetScrollY, behavior: 'smooth' });
                });
            });

            // Initial calculation
            updatePricingHorizontalScroll();
        })();

        // ==========================================
        // INSTAGRAM 4K REELS INTERACTIVE ENGINE
        // Single-video + audio playback, instant unmute on click,
        // previous video & audio auto-stop, and full-screen Lightbox
        // Strictly protected against accidental playback during mobile scrolling
        // ==========================================
        (() => {
            const grid = document.getElementById('insta-reels-grid');
            if (!grid) return;

            const tiles = Array.from(grid.querySelectorAll('.reel-tile'));
            let activePlayingTile = null;

            // Silence/mute all Selected Work video audio
            function muteAllOtherPageAudio() {
                document.querySelectorAll('.work-video').forEach(wv => {
                    wv.muted = true;
                    const card = wv.closest('.work-card');
                    if (card) {
                        const offIcon = card.querySelector('.sound-off-icon');
                        const onIcon = card.querySelector('.sound-on-icon');
                        if (offIcon) offIcon.style.display = 'block';
                        if (onIcon) onIcon.style.display = 'none';
                    }
                });
            }

            // Pause all grid videos & completely stop previous audio
            function pauseAllGridVideos(exceptTile = null) {
                tiles.forEach(tile => {
                    if (tile === exceptTile) return;
                    const v = tile.querySelector('video');
                    if (v) {
                        v.pause();
                        v.muted = true; // Stop and silence audio immediately
                    }
                    tile.classList.remove('is-playing');

                    const playSym = tile.querySelector('.play-symbol');
                    const pauseSym = tile.querySelector('.pause-symbol');
                    if (playSym) playSym.style.display = 'block';
                    if (pauseSym) pauseSym.style.display = 'none';

                    const soundBtn = tile.querySelector('.reel-sound-btn');
                    const soundOff = tile.querySelector('.sound-off-icon');
                    const soundOn = tile.querySelector('.sound-on-icon');
                    if (soundBtn) soundBtn.classList.remove('is-unmuted');
                    if (soundOff) soundOff.style.display = 'block';
                    if (soundOn) soundOn.style.display = 'none';
                });
                if (!exceptTile) activePlayingTile = null;
            }

            // Expose globally so Selected Work unmuting can pause Instagram reels
            window.pauseAllInstaReels = pauseAllGridVideos;

            // Auto-pause playing Instagram reels when scrolled out of view!
            const instaSection = document.getElementById('instagram');
            if ('IntersectionObserver' in window && instaSection) {
                const instaObserver = new IntersectionObserver((entries) => {
                    if (!entries[0].isIntersecting) {
                        pauseAllGridVideos();
                    }
                }, { threshold: 0.05 });
                instaObserver.observe(instaSection);
            }

            // Wire up each reel tile with scroll drag detection
            tiles.forEach((tile, idx) => {
                const video = tile.querySelector('video');
                const soundBtn = tile.querySelector('.reel-sound-btn');
                const expandBtn = tile.querySelector('.reel-expand-btn');
                const soundOff = tile.querySelector('.sound-off-icon');
                const soundOn = tile.querySelector('.sound-on-icon');
                const progressBar = tile.querySelector('.reel-progress-bar');
                const playSym = tile.querySelector('.play-symbol');
                const pauseSym = tile.querySelector('.pause-symbol');

                // Track touch movement to ensure scrolling NEVER triggers video playback or lightbox
                let touchStartX = 0;
                let touchStartY = 0;
                let isDraggingOrScrolling = false;

                tile.addEventListener('touchstart', (e) => {
                    if (e.touches && e.touches.length > 0) {
                        touchStartX = e.touches[0].clientX;
                        touchStartY = e.touches[0].clientY;
                        isDraggingOrScrolling = false;
                    }
                }, { passive: true });

                tile.addEventListener('touchmove', (e) => {
                    if (e.touches && e.touches.length > 0) {
                        const dx = Math.abs(e.touches[0].clientX - touchStartX);
                        const dy = Math.abs(e.touches[0].clientY - touchStartY);
                        // Any finger movement > 6px means the user is scrolling the page!
                        if (dx > 6 || dy > 6) {
                            isDraggingOrScrolling = true;
                        }
                    }
                }, { passive: true });

                tile.addEventListener('touchend', () => {
                    if (isDraggingOrScrolling) {
                        // Keep scroll lock active for 250ms to swallow synthesized click events
                        setTimeout(() => {
                            isDraggingOrScrolling = false;
                        }, 250);
                    }
                }, { passive: true });

                function updateTileSoundUI(isUnmuted) {
                    if (soundBtn) soundBtn.classList.toggle('is-unmuted', isUnmuted);
                    if (soundOff) soundOff.style.display = isUnmuted ? 'none' : 'block';
                    if (soundOn) soundOn.style.display = isUnmuted ? 'block' : 'none';
                }

                function playWithAudio() {
                    // 1. Stop previous playing video and its audio immediately
                    pauseAllGridVideos(tile);
                    muteAllOtherPageAudio();

                    // 2. Play this video with full audio
                    video.muted = false;
                    video.volume = 1.0;
                    updateTileSoundUI(true);

                    video.play().then(() => {
                        tile.classList.add('is-playing');
                        if (playSym) playSym.style.display = 'none';
                        if (pauseSym) pauseSym.style.display = 'block';
                        activePlayingTile = tile;
                    }).catch(err => {
                        console.warn('Autoplay unmuted blocked by browser, falling back to muted play:', err);
                        video.muted = true;
                        updateTileSoundUI(false);
                        video.play().then(() => {
                            tile.classList.add('is-playing');
                            if (playSym) playSym.style.display = 'none';
                            if (pauseSym) pauseSym.style.display = 'block';
                            activePlayingTile = tile;
                        }).catch(() => {});
                    });
                }

                function stopPlaying() {
                    video.pause();
                    video.muted = true;
                    tile.classList.remove('is-playing');
                    if (playSym) playSym.style.display = 'block';
                    if (pauseSym) pauseSym.style.display = 'none';
                    updateTileSoundUI(false);
                    if (activePlayingTile === tile) activePlayingTile = null;
                }

                // Sound toggle button on card
                if (soundBtn) {
                    soundBtn.addEventListener('click', (e) => {
                        e.stopPropagation();
                        if (isDraggingOrScrolling) return; // Prevent sound toggle when scrolling
                        if (!video) return;

                        if (video.paused) {
                            playWithAudio();
                        } else {
                            video.muted = !video.muted;
                            updateTileSoundUI(!video.muted);
                            if (!video.muted) {
                                muteAllOtherPageAudio();
                            }
                        }
                    });
                }

                // Expand into Lightbox modal
                if (expandBtn) {
                    expandBtn.addEventListener('click', (e) => {
                        e.stopPropagation();
                        if (isDraggingOrScrolling) return; // Prevent modal popup when scrolling
                        openLightbox(idx);
                    });
                }

                // Main card click (play with audio / stop) - strictly protected against scrolling!
                tile.addEventListener('click', (e) => {
                    if (isDraggingOrScrolling) {
                        e.preventDefault();
                        e.stopPropagation();
                        return; // User was scrolling, DO NOT PLAY VIDEO!
                    }
                    if (!video) return;

                    if (video.paused) {
                        playWithAudio();
                    } else {
                        stopPlaying();
                    }
                });

                // Update progress bar
                if (video && progressBar) {
                    video.addEventListener('timeupdate', () => {
                        if (video.duration) {
                            const pct = (video.currentTime / video.duration) * 100;
                            progressBar.style.width = pct + '%';
                        }
                    });

                    video.addEventListener('ended', () => {
                        if (!video.loop) {
                            stopPlaying();
                        }
                    });
                }
            });

            // ==========================================
            // REELS LIGHTBOX MODAL CONTROLLER
            // ==========================================
            const modal = document.getElementById('reel-lightbox');
            const backdrop = document.getElementById('reel-lightbox-backdrop');
            const closeBtn = document.getElementById('lightbox-close');
            const lbVideo = document.getElementById('lightbox-video');
            const lbSoundBtn = document.getElementById('lightbox-sound-btn');
            const lbSoundIcon = lbSoundBtn ? lbSoundBtn.querySelector('.lightbox-sound-icon') : null;
            const lbCenterPlay = document.getElementById('lightbox-center-play');
            const lbPhoneFrame = document.getElementById('lightbox-phone-frame');
            const lbTag = document.getElementById('lightbox-tag');
            const lbTitle = document.getElementById('lightbox-title');
            const lbCaption = document.getElementById('lightbox-caption');
            const lbProgressBar = document.getElementById('lightbox-progress-bar');
            const prevBtn = document.getElementById('lightbox-prev');
            const nextBtn = document.getElementById('lightbox-next');

            let currentLightboxIndex = 0;

            function openLightbox(index) {
                if (!modal || !lbVideo || index < 0 || index >= tiles.length) return;
                currentLightboxIndex = index;
                const tile = tiles[index];
                const gridVideo = tile.querySelector('video');

                // Pause any playing grid video and stop audio
                pauseAllGridVideos();
                muteAllOtherPageAudio();

                const videoSrc = tile.getAttribute('data-video');
                const tag = tile.getAttribute('data-tag') || 'INSTAGRAM REEL';
                const title = tile.getAttribute('data-title') || '@savkar_media';
                const caption = tile.getAttribute('data-caption') || '';

                lbVideo.src = videoSrc;
                lbVideo.muted = false; // Unmuted by default with audio
                lbVideo.volume = 1.0;
                if (lbSoundIcon) lbSoundIcon.textContent = '🔊';
                if (lbTag) lbTag.textContent = '[ ' + tag + ' ]';
                if (lbTitle) lbTitle.textContent = title;
                if (lbCaption) lbCaption.textContent = caption;

                if (gridVideo && gridVideo.currentTime > 0) {
                    lbVideo.currentTime = gridVideo.currentTime;
                } else {
                    lbVideo.currentTime = 0;
                }

                modal.classList.add('is-active');
                modal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';

                lbVideo.play().then(() => {
                    if (lbPhoneFrame) lbPhoneFrame.classList.remove('is-paused');
                }).catch(() => {
                    lbVideo.muted = true;
                    if (lbSoundIcon) lbSoundIcon.textContent = '🔇';
                    lbVideo.play().catch(() => {});
                });
            }

            function closeLightbox() {
                if (!modal || !lbVideo) return;
                lbVideo.pause();
                lbVideo.muted = true;
                lbVideo.src = '';
                modal.classList.remove('is-active');
                modal.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = '';
            }

            if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
            if (backdrop) backdrop.addEventListener('click', closeLightbox);

            // Lightbox Sound Button
            if (lbSoundBtn && lbVideo) {
                lbSoundBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    lbVideo.muted = !lbVideo.muted;
                    if (lbSoundIcon) {
                        lbSoundIcon.textContent = lbVideo.muted ? '🔇' : '🔊';
                    }
                });
            }

            // Lightbox Video Play/Pause Toggle
            if (lbPhoneFrame && lbVideo) {
                lbPhoneFrame.addEventListener('click', (e) => {
                    if (e.target.closest('.lightbox-btn') || e.target.closest('.lightbox-nav-btn')) return;
                    if (lbVideo.paused) {
                        lbVideo.play();
                        lbPhoneFrame.classList.remove('is-paused');
                    } else {
                        lbVideo.pause();
                        lbPhoneFrame.classList.add('is-paused');
                    }
                });
            }

            // Lightbox Progress Bar
            if (lbVideo && lbProgressBar) {
                lbVideo.addEventListener('timeupdate', () => {
                    if (lbVideo.duration) {
                        const pct = (lbVideo.currentTime / lbVideo.duration) * 100;
                        lbProgressBar.style.width = pct + '%';
                    }
                });
            }

            // Next / Prev Navigation
            function showNextReel() {
                const nextIdx = (currentLightboxIndex + 1) % tiles.length;
                openLightbox(nextIdx);
            }
            function showPrevReel() {
                const prevIdx = (currentLightboxIndex - 1 + tiles.length) % tiles.length;
                openLightbox(prevIdx);
            }

            if (nextBtn) nextBtn.addEventListener('click', (e) => { e.stopPropagation(); showNextReel(); });
            if (prevBtn) prevBtn.addEventListener('click', (e) => { e.stopPropagation(); showPrevReel(); });

            // Keyboard navigation
            window.addEventListener('keydown', (e) => {
                if (!modal || !modal.classList.contains('is-active')) return;
                if (e.key === 'Escape') closeLightbox();
                else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') showNextReel();
                else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') showPrevReel();
                else if (e.key === ' ' && lbVideo) {
                    e.preventDefault();
                    if (lbVideo.paused) { lbVideo.play(); if (lbPhoneFrame) lbPhoneFrame.classList.remove('is-paused'); }
                    else { lbVideo.pause(); if (lbPhoneFrame) lbPhoneFrame.classList.add('is-paused'); }
                }
            });

            // Touch swipe gesture on mobile lightbox (swipe up for next, swipe down for prev)
            let touchStartY = 0;
            if (lbPhoneFrame) {
                lbPhoneFrame.addEventListener('touchstart', (e) => {
                    touchStartY = e.touches[0].clientY;
                }, { passive: true });
                lbPhoneFrame.addEventListener('touchend', (e) => {
                    const diffY = e.changedTouches[0].clientY - touchStartY;
                    if (diffY < -50) showNextReel(); // Swiped up -> next
                    else if (diffY > 50) showPrevReel(); // Swiped down -> prev
                }, { passive: true });
            }
        })();

        // BOUNCE CARDS PHYSICS ENGINE (React Bits)
        // Spring Physics Simulation for OUR SERVICES
        // ==========================================
        (() => {
            const root = document.getElementById('services-bounce-cards');
            if (!root) return;

            const PATTERN = [1, 0.5, -0.3, -1, 0.2, 0.75, -0.6, 0.35, -0.85, 0.1];
            const clamp = (value, min, max) => Math.min(max, Math.max(min, value));

            const cardEls = Array.from(root.querySelectorAll('.bounce-cards__card'));
            const pillBtns = Array.from(document.querySelectorAll('.bounce-pill-btn'));
            const prevBtn = document.getElementById('bounce-prev-btn');
            const nextBtn = document.getElementById('bounce-next-btn');

            const count = cardEls.length;
            const middle = (count - 1) / 2;
            const reach = Math.max(1, middle);

            let spread = 165;
            let rotation = 3.5;
            let arc = 22;
            let cardSize = 350;
            let animationDelay = 0.3;
            let animationStagger = 0.08;
            let bounciness = 0.6;
            let pushDistance = 155;
            let hoverScale = 1.05;

            function computeSlots() {
                const w = root.clientWidth || window.innerWidth;
                if (w < 768) {
                    spread = Math.min(65, (w - 160) / 4);
                    pushDistance = 90;
                    rotation = 2.5;
                    cardSize = 280;
                } else if (w < 1024) {
                    spread = Math.min(120, (w - 220) / 4);
                    pushDistance = 125;
                    rotation = 3.0;
                    cardSize = 310;
                } else {
                    spread = 165;
                    pushDistance = 155;
                    rotation = 3.5;
                    cardSize = 350;
                }

                return cardEls.map((_, i) => {
                    const offset = i - middle;
                    return {
                        x: offset * spread,
                        y: arc * (offset / reach) ** 2,
                        rotate: rotation * PATTERN[i % PATTERN.length]
                    };
                });
            }

            let slots = computeSlots();
            window.addEventListener('resize', () => {
                slots = computeSlots();
                wake();
            }, { passive: true });

            const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false;
            const bodies = [];
            const state = { hovered: -1, time: 0, layer: -1 };
            let raf = 0;
            let last = performance.now();
            let alive = true;

            const body = i => {
                if (!bodies[i]) {
                    const slot = slots[i] ?? { x: 0, y: 0, rotate: 0 };
                    bodies[i] = {
                        x: slot.x,
                        y: slot.y,
                        rotate: slot.rotate,
                        scale: reduce ? 1 : 0,
                        vx: 0,
                        vy: 0,
                        vr: 0,
                        vs: 0,
                        born: state.time
                    };
                }
                return bodies[i];
            };

            const step = (value, velocity, target, stiffness, damping, dt) => {
                const next = velocity + ((target - value) * stiffness - velocity * damping) * dt;
                return [value + next * dt, next];
            };

            const frame = now => {
                raf = 0;
                if (!alive) return;
                const dt = Math.min(1 / 30, Math.max(1 / 240, (now - last) / 1000));
                last = now;
                state.time += dt;

                const hovered = state.hovered;
                const popStiffness = 170;
                const popDamping = 2 * (1 - 0.85 * bounciness) * Math.sqrt(popStiffness);
                const moveStiffness = 210;
                const moveDamping = 2 * (reduce ? 1 : 0.72) * Math.sqrt(moveStiffness);
                const substeps = Math.ceil(dt / (1 / 240));
                const h = dt / substeps;
                let moving = 0;

                for (let i = 0; i < slots.length; i++) {
                    const el = cardEls[i];
                    if (!el) continue;
                    const card = body(i);
                    const slot = slots[i];
                    const appeared = reduce || state.time - card.born >= animationDelay + i * animationStagger;
                    let targetX = slot.x;
                    let targetY = slot.y;
                    let targetRotate = slot.rotate;
                    let targetScale = appeared ? 1 : 0;

                    if (hovered >= 0 && appeared) {
                        if (i === hovered) {
                            targetY = slot.y - cardSize * 0.05;
                            targetRotate = 0;
                            targetScale = hoverScale;
                        } else {
                            targetX = slot.x + Math.sign(i - hovered) * pushDistance;
                        }
                    }

                    for (let k = 0; k < substeps; k++) {
                        [card.x, card.vx] = step(card.x, card.vx, targetX, moveStiffness, moveDamping, h);
                        [card.y, card.vy] = step(card.y, card.vy, targetY, moveStiffness, moveDamping, h);
                        [card.rotate, card.vr] = step(card.rotate, card.vr, targetRotate, moveStiffness, moveDamping, h);
                        if (reduce) {
                            card.scale = targetScale;
                            card.vs = 0;
                        } else {
                            [card.scale, card.vs] = step(card.scale, card.vs, targetScale, popStiffness, popDamping, h);
                        }
                    }

                    moving +=
                        Math.abs(card.vx) +
                        Math.abs(card.vy) +
                        Math.abs(card.vr) +
                        Math.abs(card.vs) * 100 +
                        Math.abs(targetX - card.x) +
                        Math.abs(targetY - card.y) +
                        Math.abs(targetRotate - card.rotate) +
                        Math.abs(targetScale - card.scale) * 100 +
                        (appeared ? 0 : 1);

                    el.style.transform = `translate(-50%, -50%) translate3d(${card.x.toFixed(2)}px, ${card.y.toFixed(2)}px, 0) rotate(${card.rotate.toFixed(3)}deg) scale(${Math.max(0, card.scale).toFixed(4)})`;
                }

                if (state.layer !== hovered) {
                    state.layer = hovered;
                    cardEls.forEach((el, i) => {
                        if (!el) return;
                        el.style.zIndex = i === hovered ? String(slots.length + 10) : String(i + 1);
                        el.toggleAttribute('data-active', i === hovered);
                    });
                    pillBtns.forEach((btn, i) => {
                        btn.classList.toggle('active', i === hovered);
                    });
                }

                if (moving > 0.02) raf = requestAnimationFrame(frame);
            };

            const wake = () => {
                if (raf || !alive) return;
                last = performance.now();
                raf = requestAnimationFrame(frame);
            };

            // Card hover and click interactions
            cardEls.forEach((el, i) => {
                el.addEventListener('pointerenter', () => {
                    state.hovered = i;
                    wake();
                });
                el.addEventListener('click', () => {
                    const card = bodies[i];
                    if (card && !reduce) card.vs -= 2.2;
                    wake();
                });
            });

            root.addEventListener('pointerleave', () => {
                if (state.hovered !== -1) {
                    state.hovered = -1;
                    wake();
                }
            });

            // Dock Navigation
            pillBtns.forEach((btn, i) => {
                btn.addEventListener('click', e => {
                    e.preventDefault();
                    state.hovered = i;
                    const card = bodies[i];
                    if (card && !reduce) card.vs -= 2.2;
                    wake();
                });
            });

            prevBtn?.addEventListener('click', e => {
                e.preventDefault();
                let next = state.hovered <= 0 ? count - 1 : state.hovered - 1;
                state.hovered = next;
                const card = bodies[next];
                if (card && !reduce) card.vs -= 2.2;
                wake();
            });

            nextBtn?.addEventListener('click', e => {
                e.preventDefault();
                let next = state.hovered >= count - 1 ? 0 : state.hovered + 1;
                state.hovered = next;
                const card = bodies[next];
                if (card && !reduce) card.vs -= 2.2;
                wake();
            });

            // Trigger entrance when scrolled into view
            if ('IntersectionObserver' in window) {
                const observer = new IntersectionObserver(entries => {
                    if (entries[0].isIntersecting) {
                        state.time = 0;
                        bodies.forEach(b => { if (b) b.born = 0; });
                        wake();
                    }
                }, { threshold: 0.1 });
                observer.observe(root);
            } else {
                wake();
            }
        })();

        // ==========================================
        // TOUCH SWIPE MEDIA STACK ENGINE (scd-20)
        // Mobile Animation Controller for OUR SERVICES
        // ==========================================
        (() => {
            const root = document.querySelector('.scd-20');
            if (!root) return;
            const deck = root.querySelector('#scd-20-deck');
            if (!deck) return;
            const live = root.querySelector('#scd-20-live');
            const THRESHOLD = 75;

            const paint = () => {
                const cards = Array.from(deck.children);
                cards.forEach((c, i) => c.style.setProperty('--d', i));
                const first = deck.firstElementChild;
                if (first && live) {
                    const num = first.getAttribute('data-service-num') || '';
                    const title = first.getAttribute('data-service-title') || first.querySelector('.service-title')?.textContent?.trim() || '';
                    live.textContent = num ? `${num} · ${title}` : title;
                }
                if (first) {
                    first.setAttribute('tabindex', '0');
                    bind(first);
                }
            };

            function sendBack(card) {
                card.classList.add('scd-20__fly');
                const onEnd = () => {
                    card.removeEventListener('transitionend', onEnd);
                    card.classList.remove('scd-20__fly');
                    card.style.transform = '';
                    deck.appendChild(card);
                    paint();
                };
                card.addEventListener('transitionend', onEnd, { once: true });
                // Fallback in case transitionend does not fire
                setTimeout(() => {
                    if (card.classList.contains('scd-20__fly')) {
                        onEnd();
                    }
                }, 480);
            }

            function bringFront() {
                const last = deck.lastElementChild;
                if (!last) return;
                deck.insertBefore(last, deck.firstElementChild);
                paint();
            }

            function bind(card) {
                if (card.dataset.b) return;
                card.dataset.b = '1';
                let sx = 0, dx = 0, drag = false;

                card.addEventListener('pointerdown', e => {
                    if (card !== deck.firstElementChild) return;
                    if (e.button !== undefined && e.button !== 0) return;
                    drag = true;
                    sx = e.clientX;
                    card.setPointerCapture(e.pointerId);
                    card.classList.add('scd-20__drag');
                });

                card.addEventListener('pointermove', e => {
                    if (!drag) return;
                    dx = e.clientX - sx;
                    card.style.transform = 'translate3d(' + dx + 'px,0,0) rotate(' + (dx / 22) + 'deg)';
                });

                const endDrag = () => {
                    if (!drag) return;
                    drag = false;
                    card.classList.remove('scd-20__drag');
                    if (Math.abs(dx) > THRESHOLD) {
                        card.style.transform = 'translate3d(' + (dx > 0 ? 140 : -140) + '%,0,0) rotate(' + (dx > 0 ? 18 : -18) + 'deg)';
                        sendBack(card);
                    } else {
                        card.style.transform = '';
                    }
                    dx = 0;
                };

                card.addEventListener('pointerup', endDrag);
                card.addEventListener('pointercancel', endDrag);
            }

            const nextBtn = root.querySelector('#scd-20-next');
            if (nextBtn) {
                nextBtn.addEventListener('click', () => {
                    const c = deck.firstElementChild;
                    if (!c) return;
                    c.style.transform = 'translate3d(-140%,0,0) rotate(-16deg)';
                    sendBack(c);
                });
            }

            const prevBtn = root.querySelector('#scd-20-prev');
            if (prevBtn) {
                prevBtn.addEventListener('click', bringFront);
            }

            deck.addEventListener('keydown', e => {
                if (e.key === 'ArrowLeft') {
                    const c = deck.firstElementChild;
                    if (!c) return;
                    c.style.transform = 'translate3d(-140%,0,0)';
                    sendBack(c);
                }
                if (e.key === 'ArrowRight') bringFront();
            });

            paint();
        })();

        // ==========================================
        // RIBBON TYPE 3D COMPONENT (React Bits Pro)
        // Full Screen-Fit 3D Satin Ribbon with Continuous Auto-Running Typography
        // ==========================================
        (async () => {
            const container = document.getElementById('ribbon-canvas-container');
            const canvas = document.getElementById('ribbon-type-canvas');
            if (!container || !canvas || typeof THREE === 'undefined') return;

            if (document.fonts) {
                await document.fonts.ready;
            }

            const textItems = [
                'SOCIAL MEDIA',
                'ADVERTISING',
                'REEL CREATION',
                'WEB DEVELOPMENT',
                'CUSTOM SOFTWARE',
                'BRAND ARCHITECTURE'
            ];

            function createRibbonTexture() {
                const offCanvas = document.createElement('canvas');
                offCanvas.height = 150;
                const ctx = offCanvas.getContext('2d');
                ctx.font = '900 50px Syne, sans-serif';

                const itemSpacings = textItems.map(item => {
                    const w = ctx.measureText(item).width;
                    return { item, width: w };
                });

                const starWidth = ctx.measureText('✦').width;
                const pad = 50; // tight, rhythmic, premium spacing

                let totalWidth = 0;
                itemSpacings.forEach(it => {
                    totalWidth += pad + starWidth + pad + it.width;
                });

                const finalWidth = Math.ceil(totalWidth);
                offCanvas.width = finalWidth;

                function render() {
                    ctx.clearRect(0, 0, offCanvas.width, offCanvas.height);

                    // Deep obsidian satin base
                    ctx.fillStyle = '#080a10';
                    ctx.fillRect(0, 0, offCanvas.width, offCanvas.height);

                    // Subtle satin sheen
                    const grad = ctx.createLinearGradient(0, 0, 0, offCanvas.height);
                    grad.addColorStop(0, 'rgba(160, 255, 100, 0.22)');
                    grad.addColorStop(0.12, 'rgba(255, 255, 255, 0.1)');
                    grad.addColorStop(0.5, 'rgba(0, 0, 0, 0.0)');
                    grad.addColorStop(0.88, 'rgba(0, 0, 0, 0.35)');
                    grad.addColorStop(1, 'rgba(160, 255, 100, 0.15)');
                    ctx.fillStyle = grad;
                    ctx.fillRect(0, 0, offCanvas.width, offCanvas.height);

                    // Glowing neon borders
                    ctx.strokeStyle = '#a0ff64';
                    ctx.lineWidth = 4;
                    ctx.beginPath();
                    ctx.moveTo(0, 2);
                    ctx.lineTo(offCanvas.width, 2);
                    ctx.moveTo(0, offCanvas.height - 2);
                    ctx.lineTo(offCanvas.width, offCanvas.height - 2);
                    ctx.stroke();

                    const y = offCanvas.height / 2;
                    let curX = 0;

                    itemSpacings.forEach(it => {
                        curX += pad;
                        // Draw Star ✦
                        ctx.font = '800 30px Syne, sans-serif';
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillStyle = '#ffffff';
                        ctx.fillText('✦', curX + starWidth / 2, y);
                        curX += starWidth + pad;

                        // Draw Text
                        ctx.font = '900 50px Syne, sans-serif';
                        ctx.textAlign = 'left';
                        ctx.textBaseline = 'middle';
                        ctx.fillStyle = '#a0ff64';
                        ctx.fillText(it.item, curX, y);
                        curX += it.width;
                    });
                }

                render();

                const texture = new THREE.CanvasTexture(offCanvas);
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.ClampToEdgeWrapping;
                texture.repeat.set(1.0, 1.0);

                return { texture, aspect: finalWidth / offCanvas.height };
            }

            const { texture: tex, aspect: texAspect } = createRibbonTexture();

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(34, container.clientWidth / container.clientHeight, 0.1, 100);
            camera.position.set(0, 0, 8.6);

            const renderer = new THREE.WebGLRenderer({
                canvas: canvas,
                alpha: true,
                antialias: true,
                powerPreference: 'high-performance'
            });
            renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
            renderer.setSize(container.clientWidth, container.clientHeight);

            const ambLight = new THREE.AmbientLight(0xffffff, 1.15);
            scene.add(ambLight);

            const dirLight1 = new THREE.DirectionalLight(0xa0ff64, 0.5);
            dirLight1.position.set(-8, 10, 6);
            scene.add(dirLight1);

            const ribbonHeight = 1.9;
            const visibleWidthAtZ0 = 2 * 8.6 * Math.tan(34 * Math.PI / 360) * (container.clientWidth / container.clientHeight);
            const ribbonWidth = Math.max(ribbonHeight * texAspect, visibleWidthAtZ0 + 10);
            tex.repeat.set(ribbonWidth / (ribbonHeight * texAspect), 1.0);

            const segW = 240;
            const segH = 20;
            const ribbonGeom = new THREE.PlaneGeometry(ribbonWidth, ribbonHeight, segW, segH);
            const origPos = Float32Array.from(ribbonGeom.attributes.position.array);

            const mat = new THREE.MeshStandardMaterial({
                map: tex,
                roughness: 0.35,
                metalness: 0.1,
                side: THREE.DoubleSide
            });

            const ribbon = new THREE.Mesh(ribbonGeom, mat);
            scene.add(ribbon);

            let targetRotX = 0, targetRotY = 0;
            let isDragging = false, prevPointerX = 0, prevPointerY = 0;

            container.addEventListener('pointerdown', e => {
                isDragging = true;
                prevPointerX = e.clientX;
                prevPointerY = e.clientY;
            });

            window.addEventListener('pointerup', () => { isDragging = false; });

            container.addEventListener('pointermove', e => {
                const rect = container.getBoundingClientRect();
                const nx = ((e.clientX - rect.left) / rect.width) * 2 - 1;
                const ny = -(((e.clientY - rect.top) / rect.height) * 2 - 1);

                if (isDragging) {
                    const dx = e.clientX - prevPointerX;
                    const dy = e.clientY - prevPointerY;
                    targetRotY += dx * 0.008;
                    targetRotX += dy * 0.008;
                    prevPointerX = e.clientX;
                    prevPointerY = e.clientY;
                } else {
                    targetRotY = nx * 0.15;
                    targetRotX = -ny * 0.12;
                }
            });

            container.addEventListener('pointerleave', () => {
                targetRotX = 0;
                targetRotY = 0;
            });

            function onResize() {
                if (!container.clientWidth || !container.clientHeight) return;
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            }
            window.addEventListener('resize', onResize, { passive: true });

            let isVisible = false;
            const aboutSec = document.getElementById('about');
            if (aboutSec && 'IntersectionObserver' in window) {
                const obs = new IntersectionObserver(entries => {
                    isVisible = entries[0].isIntersecting;
                }, { threshold: 0.05 });
                obs.observe(aboutSec);
            }

            let lastTime = performance.now();
            let simTime = 0;

            function animate(now) {
                requestAnimationFrame(animate);
                if (!isVisible) return;

                const dt = Math.min((now - lastTime) * 0.001, 0.05);
                lastTime = now;
                simTime += dt;

                scene.rotation.x += (targetRotX - scene.rotation.x) * 0.06;
                scene.rotation.y += (targetRotY - scene.rotation.y) * 0.06;

                tex.offset.x -= dt * 0.05;

                const pos = ribbonGeom.attributes.position;
                for (let i = 0; i < pos.count; i++) {
                    const ox = origPos[i * 3];
                    const oy = origPos[i * 3 + 1];

                    const waveZ = Math.sin(ox * 0.16 + simTime * 1.2) * 0.95;
                    const waveY = Math.cos(ox * 0.14 + simTime * 0.9) * 0.26;
                    const twist = Math.sin(ox * 0.10 + simTime * 0.8) * 0.12;

                    pos.setXYZ(i, ox, oy * Math.cos(twist) + waveY, oy * Math.sin(twist) + waveZ);
                }
                pos.needsUpdate = true;
                ribbonGeom.computeVertexNormals();

                renderer.render(scene, camera);
            }
            requestAnimationFrame(animate);
        })();

        // ==========================================
        // SELECTED WORK AUTOPLAY & SOUND TOGGLE (PERFORMANCE OPTIMIZED)
        // ==========================================
        (function() {
            const workSection = document.getElementById('work');
            const sliderTrack = document.getElementById('slider-track');
            const workCards = Array.from(document.querySelectorAll('.work-card'));
            const workVideos = Array.from(document.querySelectorAll('.work-video'));
            
            let isWorkSectionVisible = false;

            // Safe play/pause helpers to avoid uncaught promise rejections
            function safePlay(v) {
                if (v && v.paused) {
                    const p = v.play();
                    if (p !== undefined) {
                        p.catch(() => {});
                    }
                }
            }

            function safePause(v) {
                if (v && !v.paused) {
                    v.pause();
                }
            }

            // IntersectionObserver for the entire Selected Work section
            // Pauses ALL videos and stops the marquee animation when off-screen!
            if ('IntersectionObserver' in window && workSection) {
                const sectionObserver = new IntersectionObserver((entries) => {
                    const entry = entries[0];
                    isWorkSectionVisible = entry.isIntersecting;
                    if (isWorkSectionVisible) {
                        if (sliderTrack) sliderTrack.style.animationPlayState = 'running';
                        updateVisibleCardVideos();
                    } else {
                        if (sliderTrack) sliderTrack.style.animationPlayState = 'paused';
                        workVideos.forEach(v => safePause(v));
                    }
                }, { threshold: 0.05 });
                sectionObserver.observe(workSection);
            }

            // Only decode and play cards visible in the horizontal viewport
            function updateVisibleCardVideos() {
                if (!isWorkSectionVisible) return;
                const vw = window.innerWidth;
                workCards.forEach(card => {
                    const rect = card.getBoundingClientRect();
                    const vid = card.querySelector('.work-video');
                    // Check if card is within or near the screen viewport
                    if (rect.right > -80 && rect.left < vw + 80) {
                        safePlay(vid);
                    } else {
                        safePause(vid);
                    }
                });
            }

            // Periodic lightweight check during marquee movement
            let cardCheckTimer = null;
            function startCardChecking() {
                if (cardCheckTimer) return;
                cardCheckTimer = setInterval(() => {
                    if (isWorkSectionVisible) {
                        updateVisibleCardVideos();
                    }
                }, 400);
            }
            startCardChecking();

            // Handle background tab switching to save battery and GPU
            document.addEventListener('visibilitychange', () => {
                if (document.hidden) {
                    if (sliderTrack) sliderTrack.style.animationPlayState = 'paused';
                    workVideos.forEach(v => safePause(v));
                } else if (isWorkSectionVisible) {
                    if (sliderTrack) sliderTrack.style.animationPlayState = 'running';
                    updateVisibleCardVideos();
                }
            });

            // Card Sound Toggle
            workCards.forEach(card => {
                const vid = card.querySelector('.work-video');
                const btn = card.querySelector('.work-sound-badge');
                const offIcon = card.querySelector('.sound-off-icon');
                const onIcon = card.querySelector('.sound-on-icon');

                function toggleSound(e) {
                    e.stopPropagation();
                    if (!vid) return;

                    if (vid.muted) {
                        // Mute all other videos first
                        workVideos.forEach(otherVid => {
                            if (otherVid !== vid) {
                                otherVid.muted = true;
                                const otherCard = otherVid.closest('.work-card');
                                if (otherCard) {
                                    const oOff = otherCard.querySelector('.sound-off-icon');
                                    const oOn = otherCard.querySelector('.sound-on-icon');
                                    if (oOff) oOff.style.display = 'block';
                                    if (oOn) oOn.style.display = 'none';
                                }
                            }
                        });
                        vid.muted = false;
                        safePlay(vid);
                        if (typeof window.pauseAllInstaReels === 'function') {
                            window.pauseAllInstaReels();
                        }
                        if (offIcon) offIcon.style.display = 'none';
                        if (onIcon) onIcon.style.display = 'block';
                    } else {
                        vid.muted = true;
                        if (offIcon) offIcon.style.display = 'block';
                        if (onIcon) onIcon.style.display = 'none';
                    }
                }

                if (btn) btn.addEventListener('click', toggleSound);
                card.addEventListener('click', toggleSound);
            });
        })();


        // ==========================================
        // MOBILE SIDEWAYS SLIDER FOR WEB & SOFTWARE PLANS
        // ==========================================
        (() => {
            const slider = document.getElementById('callout-offerings-slider');
            const prevBtn = document.getElementById('callout-prev-btn');
            const nextBtn = document.getElementById('callout-next-btn');
            const bottomNextBtn = document.getElementById('callout-bottom-next-btn');
            const stepBadge = document.getElementById('plan-step-badge');
            const dotsContainer = document.getElementById('callout-nav-dots');
            if (!slider) return;

            const cards = Array.from(slider.querySelectorAll('.callout-subcard'));
            const total = cards.length;
            if (total === 0) return;

            const nextPlanNames = [
                "3D INTERACTIVE WEBSITE",
                "SOFTWARE & CUSTOM POS",
                "STARTING WEBSITE PLAN"
            ];

            let currentIndex = 0;

            function updateUI(idx) {
                currentIndex = idx;
                
                // Update Step Badge
                if (stepBadge) {
                    stepBadge.textContent = `PLAN ${idx + 1} OF ${total}`;
                }

                // Update Dots
                if (dotsContainer) {
                    const dots = dotsContainer.querySelectorAll('.nav-dot');
                    dots.forEach((dot, dIdx) => {
                        dot.classList.toggle('active', dIdx === idx);
                    });
                }

                // Update Top Arrows
                if (prevBtn) {
                    prevBtn.disabled = idx === 0;
                }
                if (nextBtn) {
                    nextBtn.disabled = idx === total - 1;
                }

                // Update Bottom Next CTA
                if (bottomNextBtn) {
                    const btnText = bottomNextBtn.querySelector('.btn-text');
                    const btnArrow = bottomNextBtn.querySelector('.btn-arrow');
                    if (idx < total - 1) {
                        if (btnText) btnText.textContent = `NEXT PLAN: ${nextPlanNames[idx]}`;
                        if (btnArrow) btnArrow.textContent = "→";
                    } else {
                        if (btnText) btnText.textContent = "BACK TO FIRST PLAN: STARTING WEBSITE";
                        if (btnArrow) btnArrow.textContent = "↺";
                    }
                }
            }

            function scrollToCard(idx) {
                if (idx < 0) idx = 0;
                if (idx >= total) idx = total - 1;
                const card = cards[idx];
                if (!card) return;
                
                slider.scrollTo({
                    left: card.offsetLeft - slider.offsetLeft,
                    behavior: 'smooth'
                });
                updateUI(idx);
            }

            if (prevBtn) {
                prevBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    if (currentIndex > 0) {
                        scrollToCard(currentIndex - 1);
                    }
                });
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    if (currentIndex < total - 1) {
                        scrollToCard(currentIndex + 1);
                    }
                });
            }

            if (bottomNextBtn) {
                bottomNextBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    if (currentIndex < total - 1) {
                        scrollToCard(currentIndex + 1);
                    } else {
                        scrollToCard(0);
                    }
                });
            }

            if (dotsContainer) {
                const dots = dotsContainer.querySelectorAll('.nav-dot');
                dots.forEach((dot, dIdx) => {
                    dot.addEventListener('click', (e) => {
                        e.preventDefault();
                        scrollToCard(dIdx);
                    });
                });
            }

            // Sync with touch swipe gestures
            let scrollTimeout;
            slider.addEventListener('scroll', () => {
                clearTimeout(scrollTimeout);
                scrollTimeout = setTimeout(() => {
                    const scrollLeft = slider.scrollLeft;
                    const cardWidth = cards[0].offsetWidth;
                    if (cardWidth > 0) {
                        const nearestIdx = Math.round(scrollLeft / cardWidth);
                        const clamped = Math.max(0, Math.min(total - 1, nearestIdx));
                        if (clamped !== currentIndex) {
                            updateUI(clamped);
                        }
                    }
                }, 70);
            }, { passive: true });

            updateUI(0);
        })();

    </script>




    <!-- ==========================================
         FLOATING STICKY WHATSAPP BUTTON (BOTTOM-RIGHT)
    ========================================== -->
    <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'm%20interested%20in%20scaling%20my%20brand!" 
       target="_blank" 
       rel="noopener noreferrer" 
       class="floating-whatsapp-btn" 
       id="floating-whatsapp-btn" 
       aria-label="Chat with Savkar Media on WhatsApp (+91 97431 55527)">
        <span class="floating-wa-icon">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.101-.477-.15-.678.15-.201.3-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.151-1.27-.468-2.42-1.493-.895-.798-1.5-1.784-1.675-2.085-.176-.3-.019-.463.132-.613.136-.135.301-.351.452-.527.15-.175.201-.3.301-.501.101-.201.05-.376-.025-.526-.075-.151-.678-1.634-.928-2.236-.244-.587-.492-.507-.678-.517-.175-.01-.376-.01-.577-.01s-.527.075-.803.376c-.276.301-1.054 1.03-1.054 2.511s1.079 2.912 1.23 3.113c.15.201 2.123 3.242 5.143 4.547.719.311 1.28.497 1.718.636.722.23 1.378.198 1.9.12.581-.088 1.78-.727 2.03-1.43.251-.703.251-1.306.176-1.431-.076-.126-.276-.201-.577-.351zM12 21.84c-1.77 0-3.5-.46-5.02-1.33l-.36-.21-3.73.98 1-3.64-.23-.37C2.71 15.69 2.2 13.88 2.2 12c0-5.4 4.4-9.8 9.8-9.8 2.62 0 5.08 1.02 6.93 2.87 1.85 1.85 2.87 4.31 2.87 6.93 0 5.4-4.4 9.8-9.8 9.8zm0-21.6c-6.51 0-11.8 5.29-11.8 11.8 0 2.08.54 4.11 1.57 5.9L0 24l6.09-1.6c1.73.94 3.68 1.44 5.91 1.44 6.51 0 11.8-5.29 11.8-11.8 0-3.15-1.23-6.11-3.46-8.34C18.11 1.47 15.15.24 12 .24z"/>
            </svg>
        </span>
        <span class="floating-wa-tooltip">Chat with us</span>
    </a>

</body>
</html>
"""

# Replace base64 tokens cleanly


web_clients_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Web Development Clients &amp; Live Works — SAVKAR MEDIA</title>
    <meta name="description" content="Explore live client websites, management portals, and custom software systems engineered by Savkar Media for Gyms, Clinics, Cafes, Restaurants, and 3D Brands.">
    <link rel="icon" type="image/png" href="___LOGO_B64___">

    <!-- Fonts: Syne + Space Mono + Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-color: #060608;
            --surface: #0d0e14;
            --surface-elevated: #13141e;
            --text-primary: #ffffff;
            --text-secondary: #9ea2b0;
            --text-muted: #646877;
            --accent-emerald: #00D665;
            --accent-lime: #A8FF53;
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(168, 255, 83, 0.35);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            overflow-x: clip;
            padding-bottom: 5rem;
        }

        /* Top Sticky Navigation */
        .clients-nav {
            position: sticky;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(6, 6, 8, 0.9);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 1.1rem 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .clients-brand {
            display: flex;
            align-items: center;
            gap: 0.9rem;
            text-decoration: none;
            color: #ffffff;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.15rem;
            letter-spacing: 0.06em;
            transition: opacity 0.2s;
        }

        .clients-brand:hover {
            opacity: 0.85;
        }

        .clients-brand-logo {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 1.5px solid var(--accent-lime);
        }

        .clients-nav-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .btn-nav-back {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #ffffff;
            text-decoration: none;
            padding: 8px 18px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.05);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.25s;
        }

        .btn-nav-back:hover {
            border-color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            color: var(--accent-lime);
            transform: translateX(-2px);
        }

        .btn-nav-inquire {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #000000;
            background: var(--accent-lime);
            border: 1px solid var(--accent-lime);
            padding: 8px 18px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.25s;
        }

        .btn-nav-inquire:hover {
            box-shadow: 0 0 18px rgba(168, 255, 83, 0.5);
            transform: translateY(-1px);
        }

        /* Container */
        .page-container {
            max-width: 1300px;
            margin: 3.5rem auto 0;
            padding: 0 2rem;
        }

        /* Hero Header */
        .hero-showcase-header {
            text-align: center;
            max-width: 860px;
            margin: 0 auto 3.5rem;
            position: relative;
        }

        .hero-badge {
            display: inline-block;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.15em;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.1);
            border: 1px solid rgba(168, 255, 83, 0.3);
            padding: 6px 18px;
            border-radius: 30px;
            margin-bottom: 1.2rem;
            text-transform: uppercase;
            font-weight: 700;
        }

        .hero-headline {
            font-family: 'Syne', sans-serif;
            font-weight: 900;
            font-size: clamp(2.2rem, 5vw, 3.8rem);
            line-height: 1.08;
            letter-spacing: -0.02em;
            color: #ffffff;
            margin-bottom: 1.2rem;
        }

        .hero-headline span {
            background: linear-gradient(135deg, #ffffff 40%, var(--accent-lime) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-sub {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            color: var(--text-secondary);
            line-height: 1.65;
            margin-bottom: 2.2rem;
        }

        /* Filter Tabs */
        .filter-tabs-row {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 3.5rem;
        }

        .filter-btn {
            font-family: 'Space Mono', monospace;
            font-size: 0.75rem;
            letter-spacing: 0.08em;
            color: var(--text-secondary);
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            padding: 8px 18px;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        .filter-btn:hover, .filter-btn.active {
            color: #000000;
            background: var(--accent-lime);
            border-color: var(--accent-lime);
            font-weight: 700;
            box-shadow: 0 0 16px rgba(168, 255, 83, 0.4);
        }

        /* Client Works Grid */
        .works-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 2.5rem;
            margin-bottom: 4.5rem;
        }

        .work-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
        }

        .work-card:hover {
            transform: translateY(-6px);
            border-color: var(--border-hover);
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 30px rgba(168, 255, 83, 0.12);
        }

        .work-preview-wrap {
            position: relative;
            width: 100%;
            height: 280px;
            overflow: hidden;
            background: #000000;
        }

        .work-preview-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s;
            filter: brightness(0.92);
        }

        .work-card:hover .work-preview-img {
            transform: scale(1.06);
            filter: brightness(1.02);
        }

        .work-preview-badge {
            position: absolute;
            top: 1rem;
            left: 1rem;
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.12em;
            background: rgba(6, 6, 8, 0.85);
            backdrop-filter: blur(8px);
            border: 1px solid var(--accent-lime);
            color: var(--accent-lime);
            padding: 4px 12px;
            border-radius: 20px;
            font-weight: 700;
        }

        .work-body {
            padding: 2rem;
            display: flex;
            flex-direction: column;
            flex: 1;
            gap: 1.2rem;
        }

        .work-meta-top {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }

        .work-title {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.4rem;
            color: #ffffff;
            line-height: 1.25;
            letter-spacing: -0.01em;
        }

        .work-desc {
            font-family: 'Inter', sans-serif;
            font-size: 0.92rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }

        /* Feature Pills */
        .work-features {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: auto;
            padding-top: 0.6rem;
        }

        .feature-pill {
            font-family: 'Space Mono', monospace;
            font-size: 0.7rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            padding: 4px 10px;
            border-radius: 12px;
            color: #cdd0db;
        }

        /* Action Row */
        .work-actions-row {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding-top: 1.2rem;
            border-top: 1px solid var(--border);
        }

        .btn-live-site {
            flex: 1;
            font-family: 'Space Mono', monospace;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            background: var(--accent-lime);
            color: #000000;
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 30px;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.4rem;
            transition: all 0.25s;
        }

        .btn-live-site:hover {
            background: #ffffff;
            box-shadow: 0 0 16px rgba(255, 255, 255, 0.4);
            transform: translateY(-1px);
        }

        .btn-chat-inquire {
            font-family: 'Space Mono', monospace;
            font-size: 0.74rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            background: rgba(0, 214, 101, 0.12);
            border: 1px solid var(--accent-emerald);
            color: #ffffff;
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 30px;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.25s;
        }

        .btn-chat-inquire:hover {
            background: var(--accent-emerald);
            color: #000000;
            box-shadow: 0 0 16px rgba(0, 214, 101, 0.45);
        }

        /* Upload / Add Work Banner for User */
        .upload-guidance-card {
            background: linear-gradient(145deg, #10141f 0%, #0b0d14 100%);
            border: 1.5px dashed rgba(168, 255, 83, 0.45);
            border-radius: 20px;
            padding: 2.8rem;
            text-align: center;
            margin-bottom: 4.5rem;
            position: relative;
        }

        .guidance-badge {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            border: 1px solid rgba(168, 255, 83, 0.3);
            padding: 5px 14px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 1rem;
            font-weight: 700;
        }

        .guidance-title {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.5rem;
            color: #ffffff;
            margin-bottom: 0.8rem;
        }

        .guidance-text {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            color: var(--text-secondary);
            max-width: 720px;
            margin: 0 auto 1.5rem;
            line-height: 1.6;
        }

        .guidance-code-hint {
            font-family: 'Space Mono', monospace;
            font-size: 0.76rem;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid var(--border);
            padding: 8px 16px;
            border-radius: 10px;
            display: inline-block;
            color: var(--accent-lime);
        }

        /* Bottom Conversion Section */
        .bottom-cta-banner {
            background: radial-gradient(ellipse at 50% 0%, rgba(26, 36, 52, 0.9) 0%, rgba(10, 12, 18, 0.98) 80%);
            border: 1px solid rgba(168, 255, 83, 0.35);
            border-radius: 24px;
            padding: 4rem 3rem;
            text-align: center;
            margin-bottom: 3.5rem;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
        }

        .bottom-cta-headline {
            font-family: 'Syne', sans-serif;
            font-weight: 900;
            font-size: clamp(1.8rem, 3.8vw, 2.8rem);
            color: #ffffff;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
        }

        .bottom-cta-desc {
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            color: var(--text-secondary);
            max-width: 650px;
            margin: 0 auto 2.2rem;
            line-height: 1.6;
        }

        .bottom-cta-actions {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 1.2rem;
            flex-wrap: wrap;
        }

        .cta-btn-primary {
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            background: var(--accent-lime);
            color: #000000;
            text-decoration: none;
            padding: 14px 28px;
            border-radius: 40px;
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            transition: all 0.25s;
        }

        .cta-btn-primary:hover {
            box-shadow: 0 0 25px rgba(168, 255, 83, 0.6);
            transform: translateY(-2px);
            background: #ffffff;
        }

        .cta-btn-outline {
            font-family: 'Space Mono', monospace;
            font-size: 0.82rem;
            letter-spacing: 0.08em;
            background: transparent;
            border: 1.5px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            text-decoration: none;
            padding: 14px 26px;
            border-radius: 40px;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.25s;
        }

        .cta-btn-outline:hover {
            border-color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.1);
            color: var(--accent-lime);
        }

        /* Footer */
        .clients-footer {
            max-width: 1300px;
            margin: 3.5rem auto 0;
            padding: 2.2rem 2rem 0;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: var(--text-muted);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .clients-footer a {
            color: var(--accent-lime);
            text-decoration: none;
            transition: color 0.2s;
        }

        .clients-footer a:hover {
            color: #ffffff;
        }

        /* Floating WhatsApp Button */
        .floating-whatsapp-btn {
            position: fixed;
            bottom: 28px;
            right: 28px;
            z-index: 85000;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45);
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            -webkit-tap-highlight-color: transparent;
        }

        .floating-whatsapp-btn:hover {
            transform: scale(1.1) translateY(-3px);
            box-shadow: 0 12px 32px rgba(37, 211, 102, 0.65);
        }

        .floating-wa-icon {
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .floating-wa-icon svg {
            width: 100%;
            height: 100%;
            fill: #ffffff;
        }

        /* Mobile Viewport */
        @media (max-width: 868px) {
            .clients-nav { padding: 0.8rem 1.2rem; }
            .btn-nav-inquire { padding: 6px 12px; font-size: 0.65rem; }
            .page-container { padding: 0 1.2rem; }
            .hero-showcase-header { margin-bottom: 2.5rem; }
            .hero-headline { font-size: 1.8rem; word-break: break-word; }
            .works-grid { grid-template-columns: 1fr; gap: 2rem; }
            .work-preview-wrap { height: 230px; }
            .work-body { padding: 1.5rem; }
            .bottom-cta-banner { padding: 2.5rem 1.4rem; }
            .clients-footer { flex-direction: column; text-align: center; }
            .floating-whatsapp-btn { bottom: 20px; right: 20px; width: 54px; height: 54px; }
            .floating-wa-icon { width: 28px; height: 28px; }
        }
    </style>
</head>
<body>

    <!-- TOP NAVIGATION -->
    <header class="clients-nav">
        <a href="index.html" class="clients-brand">
            <img src="___LOGO_B64___" class="clients-brand-logo" alt="Savkar Media">
            SAVKAR MEDIA
        </a>
        <div class="clients-nav-actions">
            <a href="index.html" class="btn-nav-back">← Back to Site</a>
            <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'd%20like%20to%20discuss%20a%20Web%20Development%20/%20Software%20project!" target="_blank" class="btn-nav-inquire">💬 Inquire Now</a>
        </div>
    </header>

    <main class="page-container">

        <!-- HERO HEADER -->
        <div class="hero-showcase-header">
            <span class="hero-badge">[ CLIENT SHOWCASE &amp; LIVE WORKS ]</span>
            <h1 class="hero-headline">OUR CLIENTS FOR<br><span>WEB DEVELOPMENT</span></h1>
            <p class="hero-sub">Explore tailored business platforms, high-converting websites, and custom software systems built for Gyms, Clinics, Cafes, Restaurants, and 3D Brands.</p>

            <!-- Interactive Category Filter Tabs -->
            <div class="filter-tabs-row" id="filter-tabs">
                <button class="filter-btn active" data-filter="all">ALL WORKS (6)</button>
                <button class="filter-btn" data-filter="gym">GYM SOFTWARE</button>
                <button class="filter-btn" data-filter="cafe">CAFE &amp; RESTAURANT POS</button>
                <button class="filter-btn" data-filter="clinic">CLINIC &amp; EMR</button>
                <button class="filter-btn" data-filter="3d">3D WEB EXPERIENCES</button>
                <button class="filter-btn" data-filter="starter">WEBSITE (₹8,000)</button>
            </div>
        </div>

        <!-- ===================================================================
             CLIENT WORKS GRID
             TO UPLOAD / ADD A NEW WORK:
             Duplicate any of the .work-card elements below.
             Update image in src="assets/your-screenshot.jpg", title, description, and link!
             =================================================================== -->
        <div class="works-grid" id="works-grid">

            <!-- WORK 1: GYM MANAGEMENT -->
            <div class="work-card" data-category="gym">
                <div class="work-preview-wrap">
                    <img src="assets/software_gym.jpg" alt="IronForge Gym &amp; Fitness Management Platform" class="work-preview-img">
                    <span class="work-preview-badge">GYM PLATFORM</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">IronForge Athletic Club &amp; Fitness Platform</h3>
                    </div>
                    <p class="work-desc">Comprehensive gym management system featuring member portals, QR check-in scanning, automated monthly retainer billing, and trainer workout scheduling.</p>
                    <div class="work-features">
                        <span class="feature-pill">QR Check-in</span>
                        <span class="feature-pill">Auto Billing</span>
                        <span class="feature-pill">Member App</span>
                        <span class="feature-pill">WhatsApp Reminders</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20a%20demo%20of%20the%20IronForge%20Gym%20Platform!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20Custom%20Gym%20Software!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- WORK 2: CAFE POS -->
            <div class="work-card" data-category="cafe">
                <div class="work-preview-wrap">
                    <img src="assets/software_pos_cafe.jpg" alt="Bloom Artisan Cafe &amp; Specialty POS" class="work-preview-img">
                    <span class="work-preview-badge">CAFE &amp; POS</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">Bloom Artisan Cafe &amp; Fast Table POS</h3>
                    </div>
                    <p class="work-desc">Tailored cafe web application with seamless digital menu, counter POS integration, kitchen order tickets (KOT), UPI reconciliation, and customer loyalty points.</p>
                    <div class="work-features">
                        <span class="feature-pill">Table QR Ordering</span>
                        <span class="feature-pill">Kitchen Display</span>
                        <span class="feature-pill">Instant UPI</span>
                        <span class="feature-pill">Inventory Alerts</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20a%20demo%20of%20the%20Bloom%20Cafe%20POS!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20Cafe%20POS%20Systems!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- WORK 3: CLINIC EMR -->
            <div class="work-card" data-category="clinic">
                <div class="work-preview-wrap">
                    <img src="assets/software_clinic.jpg" alt="Aura Dental &amp; Healthcare Clinic" class="work-preview-img">
                    <span class="work-preview-badge">CLINIC &amp; HEALTHCARE</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">Aura Dental &amp; Clinical Management Portal</h3>
                    </div>
                    <p class="work-desc">Patient appointment self-booking portal with calendar synchronization, electronic medical records (EMR), digital prescriptions, and automated appointment reminders.</p>
                    <div class="work-features">
                        <span class="feature-pill">Doctor Calendar</span>
                        <span class="feature-pill">EMR System</span>
                        <span class="feature-pill">Patient Portal</span>
                        <span class="feature-pill">Digital Rx</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20a%20demo%20of%20the%20Aura%20Clinic%20Platform!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20Clinic%20Software!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- WORK 4: RESTAURANT POS -->
            <div class="work-card" data-category="cafe">
                <div class="work-preview-wrap">
                    <img src="assets/work_restaurant_viral.jpg" alt="The Royal Table Bistro &amp; Multi-Table POS" class="work-preview-img">
                    <span class="work-preview-badge">RESTAURANT MULTI-TABLE</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">The Royal Table Bistro &amp; Dining Engine</h3>
                    </div>
                    <p class="work-desc">High-volume restaurant software engine managing multi-floor seating, captain order entry, split billing, customer review pipelines, and GST automated invoicing.</p>
                    <div class="work-features">
                        <span class="feature-pill">Floor Plan Map</span>
                        <span class="feature-pill">Captain Handheld</span>
                        <span class="feature-pill">Split Bills</span>
                        <span class="feature-pill">GST Billing</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20a%20demo%20of%20The%20Royal%20Table%20Restaurant%20POS!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20Restaurant%20POS!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- WORK 5: 3D WEB -->
            <div class="work-card" data-category="3d">
                <div class="work-preview-wrap">
                    <img src="assets/work_fashion_brand.jpg" alt="NeoVogue 3D Luxury Interactive Experience" class="work-preview-img">
                    <span class="work-preview-badge">NEXT-GEN 3D WEB</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">NeoVogue Luxury 3D Studio &amp; WebGL Experience</h3>
                    </div>
                    <p class="work-desc">Award-winning 3D interactive web showcase built with Three.js and custom GLSL shaders, enabling real-time 360° product rotation and viral brand retention.</p>
                    <div class="work-features">
                        <span class="feature-pill">Three.js WebGL</span>
                        <span class="feature-pill">Real-Time Shaders</span>
                        <span class="feature-pill">3D Product Orbit</span>
                        <span class="feature-pill">60 FPS Smooth</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20want%20to%20view%20the%20NeoVogue%203D%20Experience!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20tell%20me%20about%20Interactive%203D%20Websites!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- WORK 6: STARTING WEBSITE PLAN -->
            <div class="work-card" data-category="starter">
                <div class="work-preview-wrap">
                    <img src="assets/service_web_dev.jpg" alt="Apex Commerce High-Converting Website" class="work-preview-img">
                    <span class="work-preview-badge">STARTING PLAN (₹8,000)</span>
                </div>
                <div class="work-body">
                    <div class="work-meta-top">
                        <h3 class="work-title">Apex Commerce &amp; Scaled Business Website</h3>
                    </div>
                    <p class="work-desc">Ultra-fast high-converting business website built with clean responsive architecture, local SEO schema, rapid turnaround, and direct WhatsApp lead funnels.</p>
                    <div class="work-features">
                        <span class="feature-pill">Starting ₹8,000</span>
                        <span class="feature-pill">Sub-Second Load</span>
                        <span class="feature-pill">Mobile First</span>
                        <span class="feature-pill">SEO Structured</span>
                    </div>
                    <div class="work-actions-row">
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'm%20interested%20in%20the%20Starting%20Website%20Plan%20(%E2%82%B98,000)!" target="_blank" class="btn-live-site">
                            <span>VIEW DEMO / SITE</span>
                            <span>↗</span>
                        </a>
                        <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20book%20my%20Starting%20Website%20Plan!" target="_blank" class="btn-chat-inquire">
                            <span>💬 Inquire</span>
                        </a>
                    </div>
                </div>
            </div>

        </div>

        <!-- UPLOAD GUIDANCE BOX FOR THE USER -->
        <div class="upload-guidance-card">
            <span class="guidance-badge">⚙️ READY FOR YOUR WORK UPLOADS</span>
            <h3 class="guidance-title">Ready to Add More Client Works?</h3>
            <p class="guidance-text">This portfolio is designed to grow with your agency! Whenever you complete a new client website or software project, you can easily add it right here.</p>
            <div class="guidance-code-hint">
                💡 In <code>website/web-clients.html</code>, duplicate any <code>.work-card</code> and add your new client's screenshot, title, and live link!
            </div>
        </div>

        <!-- BOTTOM CONVERSION CTA BANNER -->
        <div class="bottom-cta-banner">
            <h2 class="bottom-cta-headline">NEED A HIGH-CONVERTING WEBSITE OR CUSTOM SOFTWARE?</h2>
            <p class="bottom-cta-desc">Whether you need an ₹8,000 business website, an interactive 3D platform, or custom management software for your Gym, Clinic, Cafe, or Restaurant, our engineering team is ready to build it.</p>
            <div class="bottom-cta-actions">
                <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'd%20like%20to%20build%20a%20website%20/%20custom%20software!" target="_blank" class="cta-btn-primary">
                    <span>START YOUR PROJECT ON WHATSAPP</span>
                    <span>↗</span>
                </a>
                <a href="tel:+919743155527" class="cta-btn-outline">
                    <span>CALL DIRECT (+91 97431 55527)</span>
                    <span>📞</span>
                </a>
            </div>
        </div>

        <!-- FOOTER -->
        <footer class="clients-footer">
            <div>SAVKAR MEDIA — JAYANAGAR 4TH BLOCK, BENGALURU, KARNATAKA, INDIA</div>
            <div><a href="index.html">← Back to Savkar Media Homepage</a></div>
            <div>© 2026 ALL RIGHTS RESERVED</div>
        </footer>

    </main>

    <!-- FLOATING WHATSAPP BUTTON -->
    <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I'd%20like%20to%20discuss%20a%20Web%20Development%20/%20Software%20project!" 
       target="_blank" 
       rel="noopener noreferrer" 
       class="floating-whatsapp-btn" 
       id="floating-whatsapp-btn" 
       aria-label="Chat with Savkar Media on WhatsApp (+91 97431 55527)">
        <span class="floating-wa-icon">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.101-.477-.15-.678.15-.201.3-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.151-1.27-.468-2.42-1.493-.895-.798-1.5-1.784-1.675-2.085-.176-.3-.019-.463.132-.613.136-.135.301-.351.452-.527.15-.175.201-.3.301-.501.101-.201.05-.376-.025-.526-.075-.151-.678-1.634-.928-2.236-.244-.587-.492-.507-.678-.517-.175-.01-.376-.01-.577-.01s-.527.075-.803.376c-.276.301-1.054 1.03-1.054 2.511s1.079 2.912 1.23 3.113c.15.201 2.123 3.242 5.143 4.547.719.311 1.28.497 1.718.636.722.23 1.378.198 1.9.12.581-.088 1.78-.727 2.03-1.43.251-.703.251-1.306.176-1.431-.076-.126-.276-.201-.577-.351zM12 21.84c-1.77 0-3.5-.46-5.02-1.33l-.36-.21-3.73.98 1-3.64-.23-.37C2.71 15.69 2.2 13.88 2.2 12c0-5.4 4.4-9.8 9.8-9.8 2.62 0 5.08 1.02 6.93 2.87 1.85 1.85 2.87 4.31 2.87 6.93 0 5.4-4.4 9.8-9.8 9.8zm0-21.6c-6.51 0-11.8 5.29-11.8 11.8 0 2.08.54 4.11 1.57 5.9L0 24l6.09-1.6c1.73.94 3.68 1.44 5.91 1.44 6.51 0 11.8-5.29 11.8-11.8 0-3.15-1.23-6.11-3.46-8.34C18.11 1.47 15.15.24 12 .24z"/>
            </svg>
        </span>
    </a>

    <!-- FILTER SCRIPT -->
    <script>
    (function() {
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.work-card');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.getAttribute('data-filter');

                cards.forEach(card => {
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    })();
    </script>

</body>
</html>
"""

terms_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms &amp; Conditions (MOU) — SAVKAR MEDIA</title>
    <meta name="description" content="Savkar Media Client Service Agreement and Memorandum of Understanding (MOU). Official terms of service, financial policies, revisions, intellectual property, and legal governance.">
    <link rel="icon" type="image/png" href="___LOGO_B64___">

    <!-- Fonts: Syne + Space Mono + Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@700;800;900&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg-color: #060608;
            --surface: #0d0e14;
            --surface-elevated: #13141d;
            --text-primary: #ffffff;
            --text-secondary: #9ea2b0;
            --text-muted: #646877;
            --accent-emerald: #00D665;
            --accent-lime: #A8FF53;
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(0, 214, 101, 0.35);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            overflow-x: clip;
            padding-bottom: 5rem;
        }

        /* Top Sticky Navigation */
        .terms-nav {
            position: sticky;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(6, 6, 8, 0.9);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 1.1rem 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .terms-brand {
            display: flex;
            align-items: center;
            gap: 0.9rem;
            text-decoration: none;
            color: #ffffff;
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.15rem;
            letter-spacing: 0.06em;
            transition: opacity 0.2s;
        }

        .terms-brand:hover {
            opacity: 0.85;
        }

        .terms-brand-logo {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 1.5px solid var(--accent-lime);
        }

        .terms-nav-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .btn-nav-back {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #ffffff;
            text-decoration: none;
            padding: 8px 18px;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: rgba(255, 255, 255, 0.05);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.25s;
        }

        .btn-nav-back:hover {
            border-color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.12);
            color: var(--accent-lime);
            transform: translateX(-2px);
        }

        .btn-nav-print {
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: #000000;
            background: var(--accent-lime);
            border: 1px solid var(--accent-lime);
            padding: 8px 18px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.25s;
        }

        .btn-nav-print:hover {
            box-shadow: 0 0 18px rgba(168, 255, 83, 0.5);
            transform: translateY(-1px);
        }

        /* Container */
        .terms-container {
            max-width: 1060px;
            margin: 3.5rem auto 0;
            padding: 0 1.5rem;
        }

        /* Hero Header */
        .terms-hero-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 3.5rem 3rem;
            text-align: center;
            margin-bottom: 2.5rem;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }

        .terms-hero-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 50%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--accent-emerald), var(--accent-lime), transparent);
        }

        .terms-hero-badge {
            display: inline-block;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.15em;
            color: var(--accent-lime);
            background: rgba(168, 255, 83, 0.1);
            border: 1px solid rgba(168, 255, 83, 0.3);
            padding: 6px 18px;
            border-radius: 30px;
            margin-bottom: 1.2rem;
            text-transform: uppercase;
        }

        .terms-hero-title {
            font-family: 'Syne', sans-serif;
            font-weight: 900;
            font-size: clamp(2rem, 4.5vw, 3.2rem);
            line-height: 1.1;
            letter-spacing: -0.02em;
            color: #ffffff;
            margin-bottom: 1rem;
        }

        .terms-hero-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            color: var(--text-secondary);
            max-width: 760px;
            margin: 0 auto 2.2rem;
            line-height: 1.65;
        }

        /* Meta Grid */
        .terms-meta-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.2rem;
            border-top: 1px solid var(--border);
            padding-top: 2rem;
        }

        .meta-item {
            text-align: center;
        }

        .meta-label {
            font-family: 'Space Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.12em;
            color: var(--text-muted);
            text-transform: uppercase;
            margin-bottom: 0.35rem;
        }

        .meta-value {
            font-family: 'Space Mono', monospace;
            font-size: 0.8rem;
            font-weight: 700;
            color: #ffffff;
        }

        /* Section Cards */
        .terms-section-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 2.8rem;
            margin-bottom: 2.2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transition: border-color 0.3s;
        }

        .terms-section-card:hover {
            border-color: rgba(255, 255, 255, 0.14);
        }

        .section-tag-row {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 1rem;
        }

        .section-tag {
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.12em;
            color: var(--accent-emerald);
            background: rgba(0, 214, 101, 0.1);
            border: 1px solid rgba(0, 214, 101, 0.3);
            padding: 5px 14px;
            border-radius: 20px;
            text-transform: uppercase;
        }

        .section-heading {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.55rem;
            color: #ffffff;
            margin-bottom: 1.5rem;
            letter-spacing: -0.01em;
        }

        /* 2-Column Grid for Section 4 */
        .cards-dual-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.8rem;
        }

        .sub-card {
            background: var(--surface-elevated);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2rem;
            transition: border-color 0.3s;
        }

        .sub-card:hover {
            border-color: var(--border-hover);
        }

        .sub-card-title {
            display: flex;
            align-items: center;
            gap: 0.7rem;
            font-family: 'Syne', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.2rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid var(--border);
        }

        .sub-card-icon {
            font-size: 1.3rem;
        }

        .policy-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .policy-list li {
            position: relative;
            padding-left: 1.5rem;
            font-size: 0.92rem;
            color: #c9cddb;
            line-height: 1.6;
        }

        .policy-list li::before {
            content: '•';
            position: absolute;
            left: 0;
            color: var(--accent-emerald);
            font-size: 1.4rem;
            line-height: 1;
            top: 0;
        }

        .policy-list li strong {
            color: #ffffff;
            font-weight: 600;
        }

        /* Section 5 Clauses Stack */
        .clauses-stack {
            display: flex;
            flex-direction: column;
            gap: 1.3rem;
        }

        .clause-box {
            display: flex;
            align-items: flex-start;
            gap: 1.4rem;
            background: var(--surface-elevated);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.6rem 2rem;
            transition: all 0.25s;
        }

        .clause-box:hover {
            border-color: var(--border-hover);
            transform: translateX(4px);
            background: #161822;
        }

        .clause-num {
            font-family: 'Space Mono', monospace;
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--accent-emerald);
            background: rgba(0, 214, 101, 0.12);
            border: 1px solid rgba(0, 214, 101, 0.35);
            padding: 6px 14px;
            border-radius: 8px;
            flex-shrink: 0;
        }

        .clause-content h5 {
            font-family: 'Syne', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.4rem;
            letter-spacing: 0.01em;
        }

        .clause-content p {
            font-size: 0.92rem;
            line-height: 1.65;
            color: #b5b8c4;
        }

        /* Section 6 Declaration Card */
        .declaration-card {
            background: linear-gradient(145deg, #10121a 0%, #0c0d13 100%);
            border: 1.5px solid rgba(168, 255, 83, 0.35);
            border-radius: 20px;
            padding: 3rem;
            margin-bottom: 2.5rem;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
        }

        .declaration-quote {
            font-family: 'Syne', sans-serif;
            font-style: italic;
            font-weight: 600;
            font-size: 1.18rem;
            line-height: 1.7;
            color: #f0f2f5;
            padding-left: 1.8rem;
            border-left: 3.5px solid var(--accent-lime);
            margin-bottom: 2.5rem;
        }

        .signoff-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.8rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
        }

        .signoff-box {
            background: rgba(0, 0, 0, 0.45);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.6rem 1.8rem;
        }

        .signoff-box.client-side {
            border-style: dashed;
            border-color: rgba(255, 255, 255, 0.18);
        }

        .signoff-party {
            font-family: 'Space Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.12em;
            color: var(--accent-emerald);
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }

        .signoff-name {
            font-family: 'Syne', sans-serif;
            font-weight: 800;
            font-size: 1.25rem;
            color: #ffffff;
            margin-bottom: 0.25rem;
        }

        .signoff-title {
            font-family: 'Space Mono', monospace;
            font-size: 0.78rem;
            color: var(--accent-lime);
            margin-bottom: 0.3rem;
        }

        .signoff-details {
            font-size: 0.82rem;
            color: var(--text-muted);
        }

        /* Scope & Package Summary Card (Section 1, 2, 3) */
        .scope-tags-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 1rem;
        }

        .scope-tag-item {
            font-family: 'Space Mono', monospace;
            font-size: 0.74rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            padding: 6px 14px;
            border-radius: 20px;
            color: #d1d5db;
        }

        /* Bottom Footer */
        .terms-footer {
            max-width: 1060px;
            margin: 3.5rem auto 0;
            padding: 2.2rem 1.5rem 0;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: 'Space Mono', monospace;
            font-size: 0.72rem;
            color: var(--text-muted);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .terms-footer a {
            color: var(--accent-lime);
            text-decoration: none;
            transition: color 0.2s;
        }

        .terms-footer a:hover {
            color: #ffffff;
        }

        /* Floating WhatsApp Button */
        .floating-whatsapp-btn {
            position: fixed;
            bottom: 28px;
            right: 28px;
            z-index: 85000;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            box-shadow: 0 8px 24px rgba(37, 211, 102, 0.45);
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            -webkit-tap-highlight-color: transparent;
        }

        .floating-whatsapp-btn:hover {
            transform: scale(1.1) translateY(-3px);
            box-shadow: 0 12px 32px rgba(37, 211, 102, 0.65);
        }

        .floating-wa-icon {
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .floating-wa-icon svg {
            width: 100%;
            height: 100%;
            fill: #ffffff;
        }

        /* Print Styles */
        @media print {
            body {
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
            }
            .terms-nav, .floating-whatsapp-btn, .btn-nav-print, .btn-nav-back {
                display: none !important;
            }
            .terms-container {
                max-width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .terms-hero-card, .terms-section-card, .sub-card, .clause-box, .declaration-card, .signoff-box {
                background: #ffffff !important;
                border: 1px solid #cccccc !important;
                color: #000000 !important;
                box-shadow: none !important;
            }
            .terms-hero-title, .section-heading, .clause-content h5, .signoff-name, .sub-card-title {
                color: #000000 !important;
            }
            .policy-list li, .clause-content p, .declaration-quote, .terms-hero-subtitle {
                color: #222222 !important;
            }
            .section-tag, .terms-hero-badge, .clause-num, .scope-tag-item {
                background: #f0f0f0 !important;
                color: #000000 !important;
                border: 1px solid #aaaaaa !important;
            }
        }

        /* Mobile Viewport */
        @media (max-width: 868px) {
            .terms-nav { padding: 0.8rem 1.2rem; }
            .btn-nav-print { display: none; }
            .terms-hero-card { padding: 2.2rem 1.2rem; }
            .terms-hero-title { font-size: 1.6rem; word-break: break-word; }
            .section-heading { font-size: 1.25rem; word-break: break-word; }
            .terms-meta-grid { grid-template-columns: 1fr 1fr; gap: 1.2rem; }
            .terms-section-card { padding: 1.8rem 1.2rem; }
            .cards-dual-grid { grid-template-columns: 1fr; }
            .clause-box { flex-direction: column; gap: 0.7rem; padding: 1.2rem; }
            .signoff-grid { grid-template-columns: 1fr; }
            .declaration-card { padding: 1.8rem 1.2rem; }
            .terms-footer { flex-direction: column; text-align: center; }
            .floating-whatsapp-btn { bottom: 20px; right: 20px; width: 54px; height: 54px; }
            .floating-wa-icon { width: 28px; height: 28px; }
        }
    </style>
</head>
<body>

    <!-- TOP NAVIGATION -->
    <header class="terms-nav">
        <a href="index.html" class="terms-brand">
            <img src="___LOGO_B64___" class="terms-brand-logo" alt="Savkar Media">
            SAVKAR MEDIA
        </a>
        <div class="terms-nav-actions">
            <a href="index.html" class="btn-nav-back">← Back to Site</a>
            <button onclick="window.print()" class="btn-nav-print">🖨️ Print MOU</button>
        </div>
    </header>

    <main class="terms-container">

        <!-- HERO HEADER -->
        <div class="terms-hero-card">
            <span class="terms-hero-badge">MEMORANDUM OF UNDERSTANDING (MOU) • ESTD. 2025</span>
            <h1 class="terms-hero-title">CLIENT SERVICE AGREEMENT<br>&amp; TERMS OF SERVICE</h1>
            <p class="terms-hero-subtitle">Official binding operational policies, payment governance, creative revisions, intellectual property, and legal provisions between Savkar Media and the Client.</p>
            
            <div class="terms-meta-grid">
                <div class="meta-item">
                    <div class="meta-label">AGENCY</div>
                    <div class="meta-value">SAVKAR MEDIA</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">JURISDICTION</div>
                    <div class="meta-value">BENGALURU, INDIA</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">DOCUMENT TYPE</div>
                    <div class="meta-value">CLIENT MOU / CSA</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">MIN. COMMITMENT</div>
                    <div class="meta-value">3 CONSECUTIVE MOS.</div>
                </div>
            </div>
        </div>

        <!-- 1, 2, 3 SCOPE & SERVICE SUMMARY -->
        <div class="terms-section-card">
            <div class="section-tag-row">
                <span class="section-tag">SECTIONS 1, 2 &amp; 3</span>
            </div>
            <h2 class="section-heading">ENGAGEMENT TERM &amp; SERVICE SELECTION</h2>
            <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.2rem;">All client engagements are initiated under a mutually binding Memorandum of Understanding (MOU) covering the selected service categories and agreed package tier:</p>
            
            <div class="scope-tags-grid">
                <span class="scope-tag-item">Reel Creation &amp; Production</span>
                <span class="scope-tag-item">Social Media Management</span>
                <span class="scope-tag-item">Photography &amp; 4K Shoots</span>
                <span class="scope-tag-item">Videography &amp; Drone Cinematography</span>
                <span class="scope-tag-item">Graphic Design &amp; Brand Art</span>
                <span class="scope-tag-item">Content Planning &amp; Social Calendar</span>
                <span class="scope-tag-item">Brand Strategy &amp; Positioning</span>
                <span class="scope-tag-item">Performance Advertising Campaigns</span>
                <span class="scope-tag-item">High-Conversion Web Development</span>
                <span class="scope-tag-item">Custom Software (Gym, Clinic, Cafe, Restaurant POS)</span>
            </div>
        </div>

        <!-- SECTION 4: FINANCIAL & PRODUCTION TERMS -->
        <div class="terms-section-card">
            <div class="section-tag-row">
                <span class="section-tag">SECTION 4</span>
            </div>
            <h2 class="section-heading">FINANCIAL &amp; PRODUCTION TERMS</h2>

            <div class="cards-dual-grid">
                <!-- Payment Terms -->
                <div class="sub-card">
                    <div class="sub-card-title">
                        <span class="sub-card-icon">💳</span>
                        <span>PAYMENT TERMS</span>
                    </div>
                    <ul class="policy-list">
                        <li><strong>100% Advance Payment:</strong> 100% advance payment required before project onboarding and initiation.</li>
                        <li><strong>Advance Monthly Retainers:</strong> Monthly retainers are payable in advance at the start of each billing cycle.</li>
                        <li><strong>Suspension of Deliverables:</strong> Delayed payments may lead to immediate suspension of active deliverables.</li>
                        <li><strong>Strict Commercial Exclusions:</strong> Third-party costs, ad spend, travel, and accommodation are strictly excluded from retainer fees.</li>
                    </ul>
                </div>

                <!-- Revisions & Production Policy -->
                <div class="sub-card">
                    <div class="sub-card-title">
                        <span class="sub-card-icon">🎬</span>
                        <span>REVISIONS &amp; PRODUCTION POLICY</span>
                    </div>
                    <ul class="policy-list">
                        <li><strong>2 Script Revisions:</strong> 2 script revisions are included within the standard project scope.</li>
                        <li><strong>Post-Production Tweaks:</strong> Minor video changes and post-production tweaks are accommodated.</li>
                        <li><strong>Scope Shifts &amp; Reshoots:</strong> Major scope shifts, conceptual changes, or reshoots will attract additional commercial charges.</li>
                        <li><strong>Minimum Term:</strong> Standard minimum 3-month commitment period applies to retainer engagements.</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- SECTION 5: TERMS & CONDITIONS (SECTION B : LEGAL TERMS) -->
        <div class="terms-section-card">
            <div class="section-tag-row">
                <span class="section-tag">SECTION B : 5</span>
            </div>
            <h2 class="section-heading">TERMS &amp; CONDITIONS (LEGAL GOVERNANCE)</h2>

            <div class="clauses-stack">
                
                <!-- 5.1 -->
                <div class="clause-box">
                    <span class="clause-num">5.1</span>
                    <div class="clause-content">
                        <h5>Content Approval</h5>
                        <p>The Client agrees to provide prompt written approvals or revision requests within 48 hours of asset submission. Delays in response may directly impact subsequent production schedules, social calendars, and guaranteed delivery timelines.</p>
                    </div>
                </div>

                <!-- 5.2 -->
                <div class="clause-box">
                    <span class="clause-num">5.2</span>
                    <div class="clause-content">
                        <h5>Client Responsibilities</h5>
                        <p>The Client agrees to provide accurate brand assets, required account access credentials, product materials, and necessary project direction essential for uninterrupted execution.</p>
                    </div>
                </div>

                <!-- 5.3 -->
                <div class="clause-box">
                    <span class="clause-num">5.3</span>
                    <div class="clause-content">
                        <h5>Intellectual Property</h5>
                        <p>Upon complete settlement of all agreed invoices, all final approved deliverables become the exclusive intellectual property of the Client. Savkar Media retains full proprietary ownership over internal workflows, raw project files, master templates, scripts, and production frameworks.</p>
                    </div>
                </div>

                <!-- 5.4 -->
                <div class="clause-box">
                    <span class="clause-num">5.4</span>
                    <div class="clause-content">
                        <h5>Portfolio Rights</h5>
                        <p>The Client grants Savkar Media an irrevocable, royalty-free license to display and publish produced deliverables across agency portfolios, award entries, case studies, agency websites, and social media channels for self-promotional purposes.</p>
                    </div>
                </div>

                <!-- 5.5 -->
                <div class="clause-box">
                    <span class="clause-num">5.5</span>
                    <div class="clause-content">
                        <h5>No Guarantee Clause</h5>
                        <p>Savkar Media applies industry best practices; however, the agency makes no warranties or explicit guarantees regarding direct sales volume, lead conversions, revenue figures, platform follower increments, or viral algorithm performance.</p>
                    </div>
                </div>

                <!-- 5.6 -->
                <div class="clause-box">
                    <span class="clause-num">5.6</span>
                    <div class="clause-content">
                        <h5>Confidentiality</h5>
                        <p>Both parties mutually agree to treat all exchanged proprietary insights, marketing roadmaps, strategic documents, commercial terms, and operational data as strictly confidential.</p>
                    </div>
                </div>

                <!-- 5.7 -->
                <div class="clause-box">
                    <span class="clause-num">5.7</span>
                    <div class="clause-content">
                        <h5>Minimum Commitment Period</h5>
                        <p>The Client commits to an initial minimum term of three (3) consecutive months as indicated in Section 1. In the event of early termination before the conclusion of this period, the Client remains legally liable for the payment of the remainder of committed service fees.</p>
                    </div>
                </div>

                <!-- 5.8 -->
                <div class="clause-box">
                    <span class="clause-num">5.8</span>
                    <div class="clause-content">
                        <h5>Termination</h5>
                        <p>Following the initial commitment window, either party may terminate this Agreement by issuing a formal 15 days prior written notice.</p>
                    </div>
                </div>

                <!-- 5.9 -->
                <div class="clause-box">
                    <span class="clause-num">5.9</span>
                    <div class="clause-content">
                        <h5>Jurisdiction &amp; Governing Law</h5>
                        <p>This Agreement shall be governed by the laws of India, and any legal proceedings or disputes arising shall fall under the exclusive jurisdiction of the competent courts in Bengaluru, Karnataka.</p>
                    </div>
                </div>

            </div>
        </div>

        <!-- FOOTER -->
        <footer class="terms-footer">
            <div>SAVKAR MEDIA — JAYANAGAR 4TH BLOCK, BENGALURU, KARNATAKA, INDIA</div>
            <div><a href="index.html">← Back to Savkar Media Homepage</a></div>
            <div>© 2026 ALL RIGHTS RESERVED</div>
        </footer>

    </main>

    <!-- FLOATING WHATSAPP BUTTON -->
    <a href="https://wa.me/919743155527?text=Hi%20Savkar%20Media,%20I%20have%20a%20question%20regarding%20your%20Terms%20%26%20Conditions%20(MOU)!" 
       target="_blank" 
       rel="noopener noreferrer" 
       class="floating-whatsapp-btn" 
       id="floating-whatsapp-btn" 
       aria-label="Chat with Savkar Media on WhatsApp (+91 97431 55527)">
        <span class="floating-wa-icon">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.276-.101-.477-.15-.678.15-.201.3-.778.98-.954 1.18-.175.201-.351.226-.652.075-.301-.151-1.27-.468-2.42-1.493-.895-.798-1.5-1.784-1.675-2.085-.176-.3-.019-.463.132-.613.136-.135.301-.351.452-.527.15-.175.201-.3.301-.501.101-.201.05-.376-.025-.526-.075-.151-.678-1.634-.928-2.236-.244-.587-.492-.507-.678-.517-.175-.01-.376-.01-.577-.01s-.527.075-.803.376c-.276.301-1.054 1.03-1.054 2.511s1.079 2.912 1.23 3.113c.15.201 2.123 3.242 5.143 4.547.719.311 1.28.497 1.718.636.722.23 1.378.198 1.9.12.581-.088 1.78-.727 2.03-1.43.251-.703.251-1.306.176-1.431-.076-.126-.276-.201-.577-.351zM12 21.84c-1.77 0-3.5-.46-5.02-1.33l-.36-.21-3.73.98 1-3.64-.23-.37C2.71 15.69 2.2 13.88 2.2 12c0-5.4 4.4-9.8 9.8-9.8 2.62 0 5.08 1.02 6.93 2.87 1.85 1.85 2.87 4.31 2.87 6.93 0 5.4-4.4 9.8-9.8 9.8zm0-21.6c-6.51 0-11.8 5.29-11.8 11.8 0 2.08.54 4.11 1.57 5.9L0 24l6.09-1.6c1.73.94 3.68 1.44 5.91 1.44 6.51 0 11.8-5.29 11.8-11.8 0-3.15-1.23-6.11-3.46-8.34C18.11 1.47 15.15.24 12 .24z"/>
            </svg>
        </span>
    </a>

</body>
</html>
"""

final_html = template.replace('___LOGO_B64___', logo_b64).replace('___DOLLAR_B64___', dollar_b64).replace('___CURSOR_B64___', cursor_b64)

with open(os.path.join('website', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(final_html)

final_terms_html = terms_template.replace('___LOGO_B64___', logo_b64)
with open(os.path.join('website', 'terms.html'), 'w', encoding='utf-8') as f:
    f.write(final_terms_html)

final_web_clients_html = web_clients_template.replace('___LOGO_B64___', logo_b64)
with open(os.path.join('website', 'web-clients.html'), 'w', encoding='utf-8') as f:
    f.write(final_web_clients_html)

print("Successfully compiled website/index.html, website/terms.html & website/web-clients.html!")
