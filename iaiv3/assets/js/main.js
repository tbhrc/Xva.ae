
document.addEventListener("DOMContentLoaded", function () {
  const progressBar = document.getElementById("scroll-progress");
  const mobileToggle = document.getElementById("mobile-menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  // ==================== SCROLL REVEAL ANIMATION ====================
  // Observe elements with fade-section class and reveal them on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all fade-section elements
  document.querySelectorAll('.fade-section').forEach(el => {
    observer.observe(el);
  });

  // ==================== METRIC BAR ANIMATION ====================
  // Animate metric bars when they come into view
  const metricBarObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target.querySelector('.metric-bar-fill');
        if (bar && bar.hasAttribute('data-bar-target')) {
          const targetWidth = bar.getAttribute('data-bar-target');
          setTimeout(() => {
            bar.style.width = targetWidth + '%';
          }, 100);
        }
        metricBarObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.metric-bar').forEach(el => {
    metricBarObserver.observe(el);
  });

  function updateProgress() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    if (progressBar) {
      progressBar.style.width = progress + "%";
    }
  }

  updateProgress();
  window.addEventListener("scroll", updateProgress);
  window.addEventListener("resize", updateProgress);

  if (mobileToggle && mobileMenu) {
    // Initialize aria attributes
    mobileToggle.setAttribute('aria-expanded', 'false');
    mobileToggle.setAttribute('aria-controls', 'mobile-menu');
    mobileToggle.setAttribute('aria-label', 'Open main menu');
    mobileMenu.setAttribute('aria-hidden', 'true');

    mobileToggle.addEventListener("click", function () {
      const expanded = mobileToggle.getAttribute('aria-expanded') === 'true';
      mobileToggle.setAttribute('aria-expanded', String(!expanded));
      mobileMenu.classList.toggle("hidden");
      mobileMenu.setAttribute('aria-hidden', String(expanded));
      if (!expanded) {
        const firstLink = mobileMenu.querySelector('a');
        if (firstLink) firstLink.focus();
      } else {
        mobileToggle.focus();
      }
    });

    // Close the menu on Escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        mobileMenu.setAttribute('aria-hidden', 'true');
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileToggle.focus();
      }
    });
  }

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          const bars = entry.target.querySelectorAll(".metric-bar-fill");
          bars.forEach(bar => {
            const target = bar.getAttribute("data-bar-target");
            // Add accessible progressbar attributes
            bar.setAttribute('role', 'progressbar');
            bar.setAttribute('aria-valuemin', '0');
            bar.setAttribute('aria-valuemax', '100');
            if (target) {
              bar.setAttribute('aria-valuenow', String(target));
              bar.setAttribute('aria-label', `${target}%`);
            }
            if (target && !bar.dataset.filled) {
              bar.dataset.filled = "true";
              requestAnimationFrame(() => {
                bar.style.width = target + "%";
              });
            }
          });
        }
      });
    },
    { threshold: 0.12 }
  );

  document.querySelectorAll(".fade-section").forEach(el => observer.observe(el));

  const readinessForm = document.getElementById("readiness-form");
  const readinessProgressBar = document.getElementById("readiness-progress-bar");
  const readinessProgressLabel = document.getElementById("readiness-progress-label");

  function updateReadinessProgress() {
    if (!readinessForm || !readinessProgressBar || !readinessProgressLabel) return;
    const questions = readinessForm.querySelectorAll(".readiness-question");
    const total = questions.length;
    let answered = 0;
    questions.forEach(q => {
      const anyChecked = q.querySelector("input[type='radio']:checked");
      if (anyChecked) answered += 1;
    });
    const pct = total > 0 ? Math.round((answered / total) * 100) : 0;
    readinessProgressLabel.textContent = pct;
    readinessProgressBar.style.width = pct + "%";
    readinessProgressBar.setAttribute('role', 'progressbar');
    readinessProgressBar.setAttribute('aria-valuemin', '0');
    readinessProgressBar.setAttribute('aria-valuemax', '100');
    readinessProgressBar.setAttribute('aria-valuenow', String(pct));
  }

  if (readinessForm) {
    readinessForm.addEventListener("change", updateReadinessProgress);
    updateReadinessProgress();

    readinessForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(readinessForm);
      const pillars = { strategy: [], people: [], technology: [], governance: [] };
      const questions = readinessForm.querySelectorAll(".readiness-question");
      questions.forEach((q, index) => {
        const pillar = q.dataset.pillar;
        const name = "q" + (index + 1);
        const value = parseInt(formData.get(name), 10);
        if (pillar && value) {
          pillars[pillar].push(value);
        }
      });
      function average(arr) {
        if (!arr.length) return 0;
        return arr.reduce((a, b) => a + b, 0) / arr.length;
      }
      const strategy = average(pillars.strategy);
      const people = average(pillars.people);
      const technology = average(pillars.technology);
      const governance = average(pillars.governance);
      const overall = average([strategy, people, technology, governance]);
      const overallPct = Math.round((overall / 5) * 100);

      let band = "Foundations needed";
      let message = "Your score suggests that some important foundations are not yet in place. This is common. Focusing on a small number of structural improvements in strategy, people, technology or governance can unlock value later.";
      let nextSteps = "A good starting point is an executive workshop to align expectations, followed by a light strategy and readiness engagement. From there, you can decide whether to run a focused pilot or address specific gaps in systems and governance.";

      if (overallPct >= 40 && overallPct <= 69) {
        band = "Ready for targeted pilots";
        message = "Your organisation appears ready for targeted AI pilots provided they are well governed and linked to clear business outcomes.";
        nextSteps = "Consider a short strategy sprint to refine your roadmap, then choose one or two workflows where pilots can be run with clear success criteria. A fractional CAIO arrangement on a light basis can help maintain alignment.";
      } else if (overallPct >= 70) {
        band = "Ready to scale";
        message = "Your readiness profile indicates a strong foundation for scaling AI initiatives across multiple functions.";
        nextSteps = "You may benefit from a combination of delivery sprints and a more structured fractional CAIO or AI governance function, focusing on portfolio management, risk oversight and structured value tracking.";
      }

      const profile = {
        overallPct,
        band,
        message,
        nextSteps,
        pillars: {
          strategy: Math.round((strategy / 5) * 100),
          people: Math.round((people / 5) * 100),
          technology: Math.round((technology / 5) * 100),
          governance: Math.round((governance / 5) * 100)
        }
      };
      try {
        localStorage.setItem("implementai_readiness_profile", JSON.stringify(profile));
      } catch (err) {}

      window.location.href = "ai-readiness-result.html";
    });
  }

  // Contact form - basic client side validation and success message (no server)
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const name = contactForm.querySelector('#name');
      const email = contactForm.querySelector('#email');
      const successEl = document.getElementById('contact-success');
      let ok = true;
      if (name && !name.value.trim()) { name.setAttribute('aria-invalid','true'); ok = false; } else if (name) { name.removeAttribute('aria-invalid'); }
      if (email && (!email.value.trim() || !/\S+@\S+\.\S+/.test(email.value))) { email.setAttribute('aria-invalid','true'); ok = false; } else if (email) { email.removeAttribute('aria-invalid'); }
      if (!ok) return;
      if (successEl) {
        successEl.classList.remove('hidden');
        setTimeout(() => successEl.classList.add('hidden'), 8000);
      }
      contactForm.reset();
    });
  }

  const resultContainer = document.getElementById("result-container");
  if (resultContainer) {
    let profile = null;
    try {
      const raw = localStorage.getItem("implementai_readiness_profile");
      if (raw) profile = JSON.parse(raw);
    } catch (err) {}

    const overallScoreEl = document.getElementById("overall-score");
    const overallBandEl = document.getElementById("overall-band");
    const overallMessageEl = document.getElementById("overall-message");
    const nextStepsEl = document.getElementById("next-steps");
    const gaugeArc = document.getElementById("gauge-arc");
    const gaugeKnob = document.getElementById("gauge-knob");

    const scoreStrategyEl = document.getElementById("score-strategy");
    const scorePeopleEl = document.getElementById("score-people");
    const scoreTechnologyEl = document.getElementById("score-technology");
    const scoreGovernanceEl = document.getElementById("score-governance");
    const barStrategy = document.getElementById("bar-strategy");
    const barPeople = document.getElementById("bar-people");
    const barTechnology = document.getElementById("bar-technology");
    const barGovernance = document.getElementById("bar-governance");

    if (!profile || !overallScoreEl || !overallBandEl) {
      if (overallMessageEl) {
        overallMessageEl.textContent = "No readiness data was found. Please complete the readiness check first.";
      }
      return;
    }

    const totalLength = 157;
    const pct = profile.overallPct || 0;
    const offset = totalLength - (totalLength * pct) / 100;

    overallScoreEl.textContent = String(pct);
    overallBandEl.textContent = profile.band || "";
    if (overallMessageEl && profile.message) {
      overallMessageEl.textContent = profile.message;
    }
    if (nextStepsEl && profile.nextSteps) {
      nextStepsEl.textContent = profile.nextSteps;
    }
    if (gaugeArc) {
      gaugeArc.style.transition = "stroke-dashoffset 1.2s ease-out";
      gaugeArc.style.strokeDashoffset = offset;
    }
    if (gaugeKnob) {
      const angle = (pct / 100) * 180 + 180;
      const radius = 50;
      const centerX = 60;
      const centerY = 50;
      const rad = (angle * Math.PI) / 180;
      const x = centerX + radius * Math.cos(rad);
      const y = centerY + radius * Math.sin(rad);
      gaugeKnob.setAttribute("cx", x);
      gaugeKnob.setAttribute("cy", y);
    }

    function applyPillar(elBar, elScore, value) {
      if (!elBar || !elScore) return;
      elScore.textContent = value + " / 100";
      elBar.setAttribute("data-bar-target", value);
      elBar.setAttribute('role', 'progressbar');
      elBar.setAttribute('aria-valuemin', '0');
      elBar.setAttribute('aria-valuemax', '100');
      elBar.setAttribute('aria-valuenow', String(value));
      elBar.setAttribute('aria-label', `${value}%`);
      requestAnimationFrame(() => {
        elBar.style.width = value + "%";
      });
    }

    applyPillar(barStrategy, scoreStrategyEl, profile.pillars.strategy || 0);
    applyPillar(barPeople, scorePeopleEl, profile.pillars.people || 0);
    applyPillar(barTechnology, scoreTechnologyEl, profile.pillars.technology || 0);
    applyPillar(barGovernance, scoreGovernanceEl, profile.pillars.governance || 0);
  }

  // Clear readiness data button on result page
  const clearReadinessBtn = document.getElementById('clear-readiness');
  if (clearReadinessBtn) {
    clearReadinessBtn.addEventListener('click', function () {
      try { localStorage.removeItem('implementai_readiness_profile'); } catch (err) {}
      // Redirect back to the questionnaire so users can retake
      window.location.href = 'ai-readiness.html';
    });
  }
});
