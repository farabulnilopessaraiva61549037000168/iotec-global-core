// ═══════════════════════════════════════════════════
// IOTEC BL — Sistema Interativo Premium v2.0
// ═══════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initNavbar();
  initScrollAnimations();
  initDiagnostico();
  initParticles();
  initFlash();
  initPaymentOptions();
});

// ─── Tema Claro/Escuro ───────────────────────────
function initTheme() {
  const saved = localStorage.getItem('iotec-theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcon(saved);

  const toggle = document.getElementById('themeToggle');
  if (toggle) {
    toggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('iotec-theme', next);
      updateThemeIcon(next);
    });
  }
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('themeIcon');
  if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
}

// ─── Navbar: scroll shadow ───────────────────────
function initNavbar() {
  const nav = document.querySelector('.navbar');
  if (!nav) return;
  const onScroll = () => {
    nav.style.boxShadow = window.scrollY > 20
      ? '0 4px 32px rgba(0,0,0,0.12)'
      : 'none';
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const open = mobileMenu.style.display === 'flex';
      mobileMenu.style.display = open ? 'none' : 'flex';
    });
  }
}

// ─── Scroll Animations ───────────────────────────
function initScrollAnimations() {
  const els = document.querySelectorAll('.fade-up');
  if (!els.length) return;
  const obs = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
    }),
    { threshold: 0.12 }
  );
  els.forEach(el => obs.observe(el));
}

// ─── Diagnóstico Inteligente ─────────────────────
function initDiagnostico() {
  const textarea = document.getElementById('diagTexto');
  const results = document.getElementById('diagResults');
  const typingEl = document.getElementById('diagTyping');
  if (!textarea || !results) return;

  let timer = null;

  textarea.addEventListener('input', () => {
    clearTimeout(timer);
    const val = textarea.value.trim();

    if (!val || val.length < 5) {
      results.innerHTML = '';
      if (typingEl) typingEl.style.display = 'none';
      return;
    }

    if (typingEl) typingEl.style.display = 'flex';

    timer = setTimeout(async () => {
      try {
        const res = await fetch('/api/analisar', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ texto: val })
        });
        const data = await res.json();
        if (typingEl) typingEl.style.display = 'none';

        if (!data.servicos || data.servicos.length === 0) {
          results.innerHTML = `<p style="color:rgba(255,255,255,0.5);font-size:.85rem;text-align:center;padding:16px 0">
            Descreva com mais detalhes sua necessidade para identificarmos o serviço ideal.</p>`;
          return;
        }

        results.innerHTML = data.servicos.map(s => `
          <div class="diag-result-item" onclick="window.location='/servicos/${s.id}'">
            <div class="diag-result-icon">⚡</div>
            <div>
              <div class="diag-result-name">${s.nome}</div>
              <div class="diag-result-price">${s.preco_texto}</div>
            </div>
            <svg style="margin-left:auto;color:rgba(255,255,255,.4)" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>
          </div>`).join('');
      } catch {
        if (typingEl) typingEl.style.display = 'none';
      }
    }, 600);
  });
}

// ─── Partículas no Hero ──────────────────────────
function initParticles() {
  const canvas = document.getElementById('heroParticles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const resize = () => {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  };
  resize();
  window.addEventListener('resize', resize, { passive: true });

  const particles = Array.from({ length: 55 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    vx: (Math.random() - 0.5) * 0.4,
    vy: (Math.random() - 0.5) * 0.4,
    r: Math.random() * 1.8 + 0.4,
    a: Math.random() * 0.5 + 0.1
  }));

  const draw = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width) p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(200,168,75,${p.a})`;
      ctx.fill();
    });

    // Conexões
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(200,168,75,${0.12 * (1 - d / 120)})`;
          ctx.lineWidth = 0.6;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  };
  draw();
}

// ─── Flash auto-dismiss ───────────────────────────
function initFlash() {
  document.querySelectorAll('.flash').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity 0.5s';
      el.style.opacity = '0';
      setTimeout(() => el.remove(), 500);
    }, 4000);
  });
}

// ─── Seleção de Pagamento ─────────────────────────
function initPaymentOptions() {
  document.querySelectorAll('.payment-option').forEach(opt => {
    opt.addEventListener('click', () => {
      document.querySelectorAll('.payment-option').forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      const method = opt.dataset.method;
      const paypalArea = document.getElementById('paypalArea');
      const picpayArea = document.getElementById('picpayArea');
      if (paypalArea) paypalArea.style.display = method === 'paypal' ? 'block' : 'none';
      if (picpayArea) picpayArea.style.display = method === 'picpay' ? 'block' : 'none';
    });
  });
}

// ─── Filtro de Serviços ───────────────────────────
function filtrarServicos(cat) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');

  document.querySelectorAll('.service-card').forEach(card => {
    const c = card.dataset.cat || '';
    card.style.display = (!cat || c === cat) ? 'flex' : 'none';
  });
}

// ─── Contador animado ─────────────────────────────
function animateCounters() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count);
    let current = 0;
    const step = target / 60;
    const update = () => {
      current = Math.min(current + step, target);
      el.textContent = Math.round(current) + (el.dataset.suffix || '');
      if (current < target) requestAnimationFrame(update);
    };
    update();
  });
}

