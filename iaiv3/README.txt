
iMPLEMENTAi.ae Multi Page Website (v3)
=====================================

New in this version
- Animated hero graphic with SVG line and metric bars.
- Engagement timeline from discovery to fractional CAIO.
- AI readiness check:
  - ai-readiness.html: 12 question assessment across Strategy, People, Technology and Governance.
  - Client-side scoring with progress bar and readiness profile stored in localStorage.
  - ai-readiness-result.html: Overall readiness gauge, per-dimension bars and tailored next steps.

Pages
- index.html               Home page with hero, metrics, engagement journey and readiness CTA.
- services.html            Overview of services and progression.
- workshops.html           Leadership and board workshops.
- strategy.html            AI strategy and value impact consulting.
- fractional-caio.html     Fractional CAIO and embedded AI departments.
- resources.html           Resource hub.
- uae-guide.html           Long form UAE AI adoption guide.
- ai-readiness.html        Interactive readiness questionnaire.
- ai-readiness-result.html Readiness score and narrative.
- about.html               Firm background and approach.
- contact.html             Contact and discovery call intro.

Deploying on Hostinger
1. Download the ZIP file from ChatGPT.
2. Log into Hostinger and open File Manager.
3. Navigate to the folder serving your domain (for example public_html).
4. Upload the ZIP.
5. Extract contents so that index.html sits at the root of that folder.
6. Visit your domain to confirm the site loads.

Tailwind CSS is loaded from CDN in each HTML file.
Custom helpers and animation styles are defined in assets/css/styles.css.
Client-side behaviour (scroll bar, animations, readiness logic) is in assets/js/main.js.

##Version Control
all new developments must be updated in the @v6-Improvements