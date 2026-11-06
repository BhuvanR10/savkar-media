# Savkar Media — Production Agency Website

Official high-performance production website for **Savkar Media** (`@savkar_media`), featuring interactive 3D WebGL experiences, 4K reel architectures, custom software & web development showcase, and responsive mobile interfaces.

---

## 🚀 Key Features

- **Cinematic Entry**: 3D interactive logo canvas with smooth zoom-vortex transition.
- **Selected Work**: Seamless infinite marquee auto-sliding reel showcase with real-time video playback and audio toggles.
- **Instagram Feed (`@savkar_media`)**: 8 exclusive client reels with FastStart streaming, single-audio mutual exclusivity, and full-screen Reels Lightbox modal.
- **Pricing & Packages**: Interactive horizontal scroll-scrub animations on mobile devices.
- **Bespoke Web & Software Engineering**: Dedicated showcase for gym, clinic, cafe & restaurant systems, starting website plans, and interactive 3D platforms with mobile sideways navigation.
- **Web Development Portfolio**: Dedicated client showcase page ([`web-clients.html`](website/web-clients.html)) with category filtering (Gym, Cafe, Clinic, 3D Web).
- **Direct Lead Gen**: WhatsApp inquiry integration and interactive quotation request engine.

---

## 🛠️ Project Architecture

```
savkar-media/
├── .github/
│   └── workflows/
│       └── deploy.yml        # Automatic GitHub Pages deployment workflow
├── website/                  # Live production web build
│   ├── index.html            # Main agency experience
│   ├── terms.html            # Terms of service & declaration
│   ├── web-clients.html      # Client websites & software showcase
│   ├── assets/               # Brand logos, posters & media assets
│   ├── videos/               # Instagram reels (FastStart H.264 streams)
│   └── work videos/          # Selected work reels (FastStart H.264 streams)
├── build_full_site.py        # Master build compiler
├── generate.py               # Static HTML generation engine
├── .gitignore
└── README.md
```

---

## 💻 Local Development & Building

### 1. Compile Website
```bash
python build_full_site.py
python generate.py
```

### 2. Run Local Development Server
```bash
cd website
python -m http.server 3000
```
Open `http://localhost:3000` in your browser.

---

## 🌐 Deployment to GitHub Pages

This repository is configured with an automated GitHub Actions workflow (`.github/workflows/deploy.yml`) that deploys the `website/` directory directly to GitHub Pages upon pushing to `main`.

To enable GitHub Pages:
1. In your GitHub repository, go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **GitHub Actions**.
3. Push to `main`, and your site will be live at `https://<username>.github.io/<repository-name>/`.
