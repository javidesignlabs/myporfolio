/* javidesignlabs — interactions v2 */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  /* ---- fit-text: scale each .fit line to exactly fill its container ---- */
  const fitAll = () => {
    document.querySelectorAll('.fit').forEach(el => {
      const bound = el.closest('.fit-bound') || el.parentElement;
      const cs = getComputedStyle(bound);
      const avail = bound.clientWidth - parseFloat(cs.paddingLeft || 0) - parseFloat(cs.paddingRight || 0);
      const max = parseFloat(el.dataset.max || '230');
      el.style.fontSize = '100px';
      let size = Math.min(100 * (avail / el.scrollWidth) * 0.995, max);
      el.style.fontSize = size.toFixed(2) + 'px';
      // second pass: correct any glyph-hinting drift at large sizes
      const real = el.getBoundingClientRect().width;
      if (real > avail) {
        size = size * (avail / real) * 0.995;
        el.style.fontSize = size.toFixed(2) + 'px';
      }
    });
  };
  fitAll();
  window.addEventListener('resize', fitAll);
  window.addEventListener('load', fitAll);
  if (document.fonts) {
    document.fonts.ready.then(fitAll);
    document.fonts.addEventListener('loadingdone', fitAll);
  }
  setTimeout(fitAll, 350);
  setTimeout(fitAll, 1200);

  /* ---- load sequence ---- */
  window.addEventListener('load', () => {
    requestAnimationFrame(() => document.body.classList.add('is-loaded'));
  });
  setTimeout(() => document.body.classList.add('is-loaded'), 900);

  /* ---- sticky header + floating call button ---- */
  const header = document.querySelector('.site-header');
  const fab = document.querySelector('.fab-call');
  const onScroll = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 24);
    if (fab) fab.classList.toggle('show', window.scrollY > 600);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---- mobile nav ---- */
  const toggle = document.querySelector('.nav-toggle');
  const mnav = document.querySelector('.mobile-nav');
  if (toggle && mnav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      mnav.classList.toggle('open');
      document.body.style.overflow = open ? '' : 'hidden';
    });
    mnav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      mnav.classList.remove('open');
      document.body.style.overflow = '';
    }));
  }

  /* ---- scroll reveals ---- */
  if (!reduced && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    document.querySelectorAll('[data-reveal]').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-in'));
  }

  /* ---- active nav ---- */
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.main-nav a, .mobile-nav a').forEach(a => {
    if (a.getAttribute('href')?.endsWith(path)) a.classList.add('active');
  });

  /* ---- cursor dot ---- */
  if (fine && !reduced) {
    const dot = document.createElement('div');
    dot.className = 'cursor-dot';
    document.body.appendChild(dot);
    document.body.classList.add('has-cursor');
    let x = 0, y = 0, cx = 0, cy = 0;
    window.addEventListener('mousemove', e => { x = e.clientX; y = e.clientY; }, { passive: true });
    (function loop() {
      cx += (x - cx) * 0.22; cy += (y - cy) * 0.22;
      dot.style.transform = `translate(${cx}px,${cy}px) translate(-50%,-50%)`;
      requestAnimationFrame(loop);
    })();
    document.querySelectorAll('a, button, .tl-row').forEach(el => {
      el.addEventListener('mouseenter', () => dot.classList.add('grow'));
      el.addEventListener('mouseleave', () => dot.classList.remove('grow'));
    });
  }

  /* ---- floating work preview ---- */
  const list = document.querySelector('.work-list');
  if (list && fine && !reduced) {
    const box = document.createElement('div');
    box.className = 'work-preview';
    const imgs = new Map();
    list.querySelectorAll('.work-row').forEach(row => {
      const src = row.dataset.img;
      if (!src) return;
      const img = document.createElement('img');
      img.src = src; img.alt = '';
      box.appendChild(img);
      imgs.set(row, img);
    });
    document.body.appendChild(box);

    let px = 0, py = 0, tx = 0, ty = 0, active = false;
    window.addEventListener('mousemove', e => { tx = e.clientX; ty = e.clientY; }, { passive: true });
    (function follow() {
      px += (tx - px) * 0.12; py += (ty - py) * 0.12;
      box.style.left = px + 20 + 'px';
      box.style.top = py - 120 + 'px';
      requestAnimationFrame(follow);
    })();

    list.querySelectorAll('.work-row').forEach(row => {
      row.addEventListener('mouseenter', () => {
        imgs.forEach(i => i.classList.remove('show'));
        const img = imgs.get(row);
        if (img) { img.classList.add('show'); box.classList.add('on'); active = true; }
      });
      row.addEventListener('mouseleave', () => {
        box.classList.remove('on'); active = false;
      });
    });
  }

  /* ---- accordions (career) ---- */
  document.querySelectorAll('.tl-item').forEach(item => {
    const row = item.querySelector('.tl-row');
    const panel = item.querySelector('.tl-panel');
    if (!row || !panel) return;
    const flip = () => {
      const open = item.classList.toggle('open');
      panel.style.maxHeight = open ? panel.scrollHeight + 'px' : '0px';
      row.setAttribute('aria-expanded', String(open));
    };
    row.setAttribute('aria-expanded', 'false');
    row.addEventListener('click', flip);
    row.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); flip(); }
    });
  });

  /* ---- footer year ---- */
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
