/**
 * Shared Expert Card component.
 * Returns a DOM node styled like the Team page cards.
 */
(function () {
  const toInitials = (name = '') =>
    name
      .split(' ')
      .filter(Boolean)
      .map((part) => part[0])
      .slice(0, 2)
      .join('')
      .toUpperCase();

  const buildLinkedInButton = (url) => {
    if (!url) return null;

    const link = document.createElement('a');
    link.href = url;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.className = 'prem-btn prem-btn-outline';
    link.style.display = 'inline-flex';
    link.style.alignItems = 'center';
    link.style.gap = '0.5rem';
    link.innerHTML = `
      <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
        <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
      </svg>
      LinkedIn Profile
    `;

    return link;
  };

  const createExpertCard = (expert = {}, options = {}) => {
    const {
      delayClass = '',
      includeTags = false,
      imageSize = 200
    } = options;

    const card = document.createElement('div');
    card.className = ['scroll-reveal', delayClass].filter(Boolean).join(' ');
    card.style.cssText =
      'display:flex;gap:2rem;align-items:start;background:#fff;padding:2rem;border-radius:18px;' +
      'border:1px solid var(--prem-border, #e6edf5);box-shadow:0 22px 60px rgba(18,38,63,0.12);' +
      'transition:transform 0.25s ease, box-shadow 0.25s ease;height:100%;';

    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-4px)';
      card.style.boxShadow = '0 26px 70px rgba(18,38,63,0.14)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0)';
      card.style.boxShadow = '0 22px 60px rgba(18,38,63,0.12)';
    });

    const left = document.createElement('div');
    left.style.flexShrink = '0';

    const baseImageStyle =
      `width:${imageSize}px;height:${imageSize}px;border-radius:50%;object-fit:cover;object-position:center;` +
      'border:4px solid var(--prem-border, #eef2f7);box-shadow:0 4px 12px rgba(0,0,0,0.1);';

    if (expert.imageUrl) {
      const img = document.createElement('img');
      img.src = expert.imageUrl;
      img.alt = expert.name || 'AI expert';
      img.style.cssText = baseImageStyle;
      left.appendChild(img);
    } else {
      const placeholder = document.createElement('div');
      placeholder.style.cssText =
        baseImageStyle +
        'display:grid;place-items:center;background:linear-gradient(135deg,#0c2640 0%,#1f4068 100%);color:#fff;font-size:2.5rem;font-weight:700;';
      placeholder.textContent = toInitials(expert.name);
      left.appendChild(placeholder);
    }

    const content = document.createElement('div');

    const nameEl = document.createElement('h3');
    nameEl.textContent = expert.name || '';
    nameEl.style.fontSize = '1.75rem';
    nameEl.style.marginBottom = '0.5rem';
    content.appendChild(nameEl);

    const titleEl = document.createElement('div');
    titleEl.textContent = expert.title || '';
    titleEl.style.color = 'var(--prem-accent-blue)';
    titleEl.style.fontSize = '0.9rem';
    titleEl.style.marginBottom = '1rem';
    titleEl.style.textTransform = 'uppercase';
    titleEl.style.letterSpacing = '1px';
    titleEl.style.fontWeight = '600';
    content.appendChild(titleEl);

    if (includeTags && Array.isArray(expert.expertise) && expert.expertise.length) {
      const tagsRow = document.createElement('div');
      tagsRow.style.display = 'flex';
      tagsRow.style.flexWrap = 'wrap';
      tagsRow.style.gap = '0.5rem';
      tagsRow.style.marginBottom = '1rem';

      expert.expertise.forEach((tag) => {
        const pill = document.createElement('span');
        pill.textContent = tag;
        pill.style.background = '#f0f4f8';
        pill.style.color = '#4a5670';
        pill.style.padding = '0.25rem 0.75rem';
        pill.style.borderRadius = '6px';
        pill.style.fontSize = '0.8rem';
        pill.style.fontWeight = '500';
        tagsRow.appendChild(pill);
      });

      content.appendChild(tagsRow);
    }

    const summaryEl = document.createElement('p');
    summaryEl.textContent = expert.summary || '';
    summaryEl.style.color = 'var(--prem-text-secondary, #6a768e)';
    summaryEl.style.lineHeight = '1.7';
    summaryEl.style.marginBottom = '1.5rem';
    content.appendChild(summaryEl);

    const linkedinLink = buildLinkedInButton(expert.linkedinUrl);
    if (linkedinLink) {
      content.appendChild(linkedinLink);
    }

    card.appendChild(left);
    card.appendChild(content);

    return card;
  };

  window.createExpertCard = createExpertCard;
})();
