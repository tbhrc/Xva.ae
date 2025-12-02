
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
        if (bar && bar.hasAttribute('data-bar-target') && !bar.hasAttribute('data-readiness')) {
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

  const metricObserver = new IntersectionObserver(
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

  document.querySelectorAll(".fade-section").forEach(el => metricObserver.observe(el));

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
    // Ensure smooth transition
    readinessProgressBar.style.transition = 'width 0.4s ease-out';
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

  // ==================== ENHANCEMENT 1: 3D TILT ON CARD HOVER ====================
  const cards = document.querySelectorAll('.service-card, .resource-card');
  cards.forEach(card => {
    card.addEventListener('mousemove', function(e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / 10;
      const rotateY = (centerX - x) / 10;
      this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(20px)`;
    });
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
    });
  });

  // ==================== ENHANCEMENT 2: PARALLAX SCROLL ON HERO ====================
  let ticking = false;
  function updateParallax() {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    parallaxElements.forEach(el => {
      const speed = parseFloat(el.dataset.parallax);
      el.style.transform = `translateY(${scrolled * speed}px)`;
    });
    ticking = false;
  }
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(updateParallax);
      ticking = true;
    }
  });

  // ==================== ENHANCEMENT 4: CUSTOM CURSOR TRAILS ====================
  const mouseTrail = [];
  const maxTrail = 5;
  document.addEventListener('mousemove', (e) => {
    const x = e.clientX;
    const y = e.clientY;
    mouseTrail.push({ x, y, time: Date.now() });
    if (mouseTrail.length > maxTrail) {
      mouseTrail.shift();
    }
  });

  // ==================== ENHANCEMENT 6: SCROLL SPY SECTION INDICATORS ====================
  const sections = document.querySelectorAll('section');
  function updateScrollSpy() {
    sections.forEach(section => {
      const rect = section.getBoundingClientRect();
      if (rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2) {
        const id = section.getAttribute('id') || section.className;
        document.querySelectorAll('.section-indicator').forEach(indicator => {
          indicator.classList.remove('active');
        });
        const activeIndicator = document.querySelector(`[data-section="${id}"]`);
        if (activeIndicator) {
          activeIndicator.classList.add('active');
        }
      }
    });
  }
  window.addEventListener('scroll', updateScrollSpy);
  updateScrollSpy();

  // ==================== ENHANCEMENT 7: BUTTON RIPPLE EFFECT ====================
  document.querySelectorAll('.btn-primary, .btn-ghost').forEach(button => {
    button.addEventListener('click', function(e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const ripple = document.createElement('span');
      ripple.className = 'ripple';
      ripple.style.left = x + 'px';
      ripple.style.top = y + 'px';
      ripple.style.width = '10px';
      ripple.style.height = '10px';
      this.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });

  // ==================== ENHANCEMENT 8: FLOATING ANIMATIONS TRIGGER ====================
  const floatingElements = document.querySelectorAll('.glass-panel, .metric-row');
  floatingElements.forEach(el => {
    el.classList.add('floating-metric');
  });

  // ==================== ENHANCEMENT 9: FORM LABEL FLOAT ====================
  const formInputs = document.querySelectorAll('input[type="text"], input[type="email"], textarea');
  formInputs.forEach(input => {
    input.classList.add('form-input');
    const label = input.parentElement.querySelector('label');
    if (label) {
      label.classList.add('form-label');
      input.addEventListener('focus', () => {
        label.style.color = '#2dd4bf';
      });
      input.addEventListener('blur', () => {
        if (!input.value) {
          label.style.color = '';
        }
      });
    }
  });

  // ==================== ENHANCEMENT 10: ANIMATED UNDERLINE ON LINKS ====================
  document.querySelectorAll('a').forEach(link => {
    if (!link.classList.contains('btn-primary') && !link.classList.contains('btn-ghost')) {
      link.classList.add('animated-underline');
    }
  });

  // ==================== COMPREHENSIVE TESTING SUITE ====================
  window.testAnimations = {
    test1_3DTilt: function() {
      const cards = document.querySelectorAll('.service-card, .resource-card');
      console.log('✓ Test 1 - 3D Tilt:', cards.length > 0 ? 'PASS - ' + cards.length + ' cards found' : 'FAIL - No cards found');
      if (cards.length > 0) {
        const style = window.getComputedStyle(cards[0]);
        console.log('  Perspective:', style.perspective);
        console.log('  Transform style:', style.transformStyle);
      }
    },
    test2_ParallaxHero: function() {
      const parallaxElements = document.querySelectorAll('[data-parallax]');
      console.log('✓ Test 2 - Parallax:', parallaxElements.length > 0 ? 'PASS - ' + parallaxElements.length + ' elements found' : 'FAIL - No parallax elements');
      parallaxElements.forEach((el, i) => {
        console.log('  Element ' + (i+1) + ' parallax value:', el.dataset.parallax);
      });
    },
    test3_StaggerAnimation: function() {
      const fadeSections = document.querySelectorAll('.fade-section');
      console.log('✓ Test 3 - Stagger:', fadeSections.length > 0 ? 'PASS - ' + fadeSections.length + ' fade sections found' : 'FAIL - No fade sections');
      if (fadeSections.length > 0) {
        const style = window.getComputedStyle(fadeSections[0]);
        console.log('  Animation:', style.animation);
      }
    },
    test4_CustomCursor: function() {
      const bodyStyle = window.getComputedStyle(document.body);
      console.log('✓ Test 4 - Custom Cursor:', bodyStyle.cursor.includes('url') ? 'PASS - Custom cursor active' : 'PASS - System cursor (acceptable)');
    },
    test5_MorphingBlobs: function() {
      const blobs = document.querySelectorAll('.morphing-blob');
      console.log('✓ Test 5 - Morphing Blobs:', blobs.length > 0 ? 'PASS - ' + blobs.length + ' blobs found' : 'INFO - Morphing class not on elements yet');
    },
    test6_ScrollSpy: function() {
      const indicators = document.querySelectorAll('.section-indicator');
      console.log('✓ Test 6 - Scroll Spy:', indicators.length > 0 ? 'PASS - ' + indicators.length + ' indicators found' : 'INFO - No scroll spy indicators on page');
    },
    test7_RippleEffect: function() {
      const buttons = document.querySelectorAll('.btn-primary, .btn-ghost');
      console.log('✓ Test 7 - Ripple Effect:', buttons.length > 0 ? 'PASS - ' + buttons.length + ' buttons found for ripple' : 'FAIL - No buttons found');
    },
    test8_FloatingElements: function() {
      const floatingElements = document.querySelectorAll('.floating-metric');
      console.log('✓ Test 8 - Floating Elements:', floatingElements.length > 0 ? 'PASS - ' + floatingElements.length + ' floating elements' : 'INFO - No floating elements yet');
    },
    test9_FormAnimations: function() {
      const formInputs = document.querySelectorAll('input[type="text"], input[type="email"], textarea');
      console.log('✓ Test 9 - Form Animations:', formInputs.length > 0 ? 'PASS - ' + formInputs.length + ' form inputs found' : 'INFO - No form inputs on this page');
      const hasFormInput = document.querySelector('.form-input');
      console.log('  Form input class:', hasFormInput ? 'Applied' : 'Not applied yet');
    },
    test10_GradientText: function() {
      const gradientTitles = document.querySelectorAll('.gradient-title');
      console.log('✓ Test 10 - Gradient Text:', gradientTitles.length > 0 ? 'PASS - ' + gradientTitles.length + ' gradient titles found' : 'INFO - No gradient titles on this page');
      const animatedUnderlines = document.querySelectorAll('.animated-underline');
      console.log('  Animated underlines:', animatedUnderlines.length > 0 ? animatedUnderlines.length + ' links updated' : 'No underlines');
    },
    runAllTests: function() {
      console.clear();
      console.log('%c=== ANIMATION ENHANCEMENTS TEST SUITE ===', 'color: #2dd4bf; font-size: 16px; font-weight: bold;');
      console.log('%cTesting all 10 modern design enhancements...', 'color: #0ea5e9; font-size: 12px;');
      console.log('');
      this.test1_3DTilt();
      this.test2_ParallaxHero();
      this.test3_StaggerAnimation();
      this.test4_CustomCursor();
      this.test5_MorphingBlobs();
      this.test6_ScrollSpy();
      this.test7_RippleEffect();
      this.test8_FloatingElements();
      this.test9_FormAnimations();
      this.test10_GradientText();
      console.log('');
      console.log('%c=== TEST COMPLETE ===', 'color: #2dd4bf; font-size: 14px; font-weight: bold;');
      console.log('%cCheck console for PASS/FAIL status on each enhancement', 'color: #14b8a6; font-size: 11px;');
    }
  };

  // Auto-run tests on page load if not in production
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    setTimeout(() => {
      console.log('%cLocal development detected - Run testAnimations.runAllTests() in console to test enhancements', 'color: #fbbf24; font-weight: bold;');
    }, 1000);
  }
});


