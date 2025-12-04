/**
 * AI Experts Directory Logic
 * Uses the shared card component and centralized experts data.
 */

(function () {
  const expertsData = Array.isArray(window.expertsData) ? window.expertsData : [];
  const buildCard = typeof window.createExpertCard === 'function' ? window.createExpertCard : null;

  const state = {
    query: '',
    expertise: new Set(),
    availabilityType: '',
    location: '',
    tools: '',
    vettedStatus: 'all'
  };

  const elements = {
    grid: document.getElementById('expertsGrid'),
    emptyState: document.getElementById('emptyState'),
    inputs: {
      search: document.getElementById('searchInput'),
      expertise: document.getElementById('filterExpertise'),
      availability: document.getElementById('filterAvailability'),
      location: document.getElementById('filterLocation'),
      tools: document.getElementById('filterTools'),
      vetted: document.getElementById('filterVetted')
    }
  };

  const debounce = (func, wait) => {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func(...args), wait);
    };
  };

  const renderExperts = (list) => {
    if (!elements.grid) return;
    elements.grid.innerHTML = '';

    if (!list.length) {
      if (elements.emptyState) {
        elements.emptyState.style.display = 'block';
        elements.emptyState.textContent = 'No experts match your search. Try a different name or adjust your filters.';
      }
      return;
    }

    if (elements.emptyState) elements.emptyState.style.display = 'none';

    list.forEach((expert, index) => {
      const delayClass = index ? `delay-${Math.min(index * 100, 400)}` : '';
      const card = buildCard
        ? buildCard(expert, { delayClass, includeTags: false, imageSize: 200 })
        : null;

      if (card) {
        elements.grid.appendChild(card);
      }
    });
  };

  const applyFilters = () => {
    const filtered = expertsData.filter((expert) => {
      const query = state.query.toLowerCase();
      const matchesQuery =
        !query ||
        [
          expert.name,
          expert.title,
          expert.summary,
          expert.location,
          ...(expert.expertise || []),
          ...(expert.tools || [])
        ]
          .filter(Boolean)
          .some((val) => val.toLowerCase().includes(query));

      const matchesExpertise =
        state.expertise.size === 0 ||
        (Array.isArray(expert.expertise) && expert.expertise.some((tag) => state.expertise.has(tag)));

      const matchesAvailability =
        !state.availabilityType || expert.availabilityType === state.availabilityType;

      const matchesLocation =
        !state.location ||
        (expert.location && expert.location.toLowerCase().includes(state.location.toLowerCase()));

      const toolTokens = state.tools
        .toLowerCase()
        .split(/[\s,]+/)
        .filter(Boolean);

      const matchesTools =
        toolTokens.length === 0 ||
        (Array.isArray(expert.tools) &&
          toolTokens.some((token) => expert.tools.some((tool) => tool.toLowerCase().includes(token))));

      const matchesVetted =
        state.vettedStatus === 'all' ||
        (state.vettedStatus === 'vetted' && expert.vettedStatus === 'Vetted');

      return matchesQuery && matchesExpertise && matchesAvailability && matchesLocation && matchesTools && matchesVetted;
    });

    renderExperts(filtered);
  };

  const setupListeners = () => {
    if (elements.inputs.search) {
      elements.inputs.search.addEventListener(
        'input',
        debounce((e) => {
          state.query = e.target.value.trim();
          applyFilters();
        }, 200)
      );
    }

    if (elements.inputs.expertise) {
      elements.inputs.expertise.addEventListener('change', () => {
        state.expertise = new Set(
          Array.from(elements.inputs.expertise.selectedOptions || []).map((opt) => opt.value)
        );
        applyFilters();
      });
    }

    if (elements.inputs.availability) {
      elements.inputs.availability.addEventListener('change', () => {
        state.availabilityType = elements.inputs.availability.value;
        applyFilters();
      });
    }

    if (elements.inputs.location) {
      elements.inputs.location.addEventListener(
        'input',
        debounce((e) => {
          state.location = e.target.value.trim();
          applyFilters();
        }, 200)
      );
    }

    if (elements.inputs.tools) {
      elements.inputs.tools.addEventListener(
        'input',
        debounce((e) => {
          state.tools = e.target.value.trim();
          applyFilters();
        }, 200)
      );
    }

    if (elements.inputs.vetted) {
      elements.inputs.vetted.addEventListener('change', () => {
        state.vettedStatus = elements.inputs.vetted.value;
        applyFilters();
      });
    }
  };

  const init = () => {
    renderExperts(expertsData);
    setupListeners();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
