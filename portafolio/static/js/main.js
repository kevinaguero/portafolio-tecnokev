// ========================================
// PORTAFOLIO TECNOKEV - JavaScript Interactivo
// ========================================

// Utilidades
const $ = (sel, el = document) => el.querySelector(sel);
const $$ = (sel, el = document) => Array.from(el.querySelectorAll(sel));

// ========================================
// INICIALIZACIÓN
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    initScrollProgress();
    initRevealOnScroll();
    // initParticles(); // partículas desactivadas
    initNavbarScroll();
    initSmoothScroll();
    initYear();
    initParallax();
    initTypingEffect();
});

// ========================================
// SCROLL PROGRESS BAR
// ========================================

function initScrollProgress() {
    let progressBar = $('.scroll-progress');
    
    if (!progressBar) {
        progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';
        document.body.appendChild(progressBar);
    }
    
    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    }, { passive: true });
}

// ========================================
// REVEAL ON SCROLL CON INTERSECTION OBSERVER
// ========================================

function initRevealOnScroll() {
    const revealElements = $$('.reveal, .reveal-left, .reveal-right');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                // Animación inmediata sin delay acumulativo para evitar lag
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    });
    
    revealElements.forEach(el => observer.observe(el));
}

// Partículas desactivadas: código eliminado para mejorar rendimiento y limpieza.
// Si necesitas restaurarlas, recupera la función initParticles() y createParticle(container).

// ========================================
// NAVBAR SCROLL EFFECT
// ========================================

function initNavbarScroll() {
    const navbar = $('.navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;
        
        if (currentScroll > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Auto-hide navbar en scroll down (opcional)
        // if (currentScroll > lastScroll && currentScroll > 500) {
        //     navbar.style.transform = 'translateY(-100%)';
        // } else {
        //     navbar.style.transform = 'translateY(0)';
        // }
        
        lastScroll = currentScroll;
    }, { passive: true });
}

// ========================================
// SMOOTH SCROLL PARA ENLACES INTERNOS
// ========================================

function initSmoothScroll() {
    $$('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Ignorar links vacíos o solo "#"
            if (href === '#' || href === '') return;
            
            const target = $(href);
            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80; // 80px para navbar
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ========================================
// ACTUALIZAR AÑO EN FOOTER
// ========================================

function initYear() {
    const yearElement = $('#year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}

// ========================================
// PARALLAX EFFECT
// ========================================

function initParallax() {
    const parallaxBg = $('#parallaxBg');
    
    if (parallaxBg) {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            parallaxBg.style.transform = `translateY(${scrolled * 0.4}px)`;
        }, { passive: true });
    }
}

// ========================================
// EFECTO DE ESCRITURA EN HERO
// ========================================

function initTypingEffect() {
    const typingElements = $$('.typing-effect');
    
    typingElements.forEach(element => {
        const text = element.textContent;
        element.textContent = '';
        element.style.opacity = '1';
        
        let i = 0;
        const typeInterval = setInterval(() => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
            } else {
                clearInterval(typeInterval);
            }
        }, 100);
    });
}

// ========================================
// CONTADOR DE VISITAS ANIMADO
// ========================================

function animateCounter(el, start, end, duration) {
    if (!el) return;
    
    let startTime = null;
    
    function step(timestamp) {
        if (!startTime) startTime = timestamp;
        const progress = Math.min((timestamp - startTime) / duration, 1);
        el.textContent = Math.floor(progress * (end - start) + start).toLocaleString();
        
        if (progress < 1) {
            requestAnimationFrame(step);
        }
    }
    
    requestAnimationFrame(step);
}

// Fetch del contador de visitas
fetch('https://visitor.6developer.com/visit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        domain: window.location.hostname,
        page_path: window.location.pathname
    })
})
.then(res => res.json())
.then(data => {
    const counterEl = $('#visitor-count');
    if (counterEl && data.totalCount !== undefined) {
        animateCounter(counterEl, 0, data.totalCount, 1000);
    }
})
.catch(err => console.error('Error al registrar visita:', err));

// ========================================
// LOADING SCREEN
// ========================================

window.addEventListener('load', () => {
    const loader = $('.loading-overlay');
    if (loader) {
        setTimeout(() => {
            loader.classList.add('hidden');
            setTimeout(() => loader.remove(), 500);
        }, 500);
    }
});

// ========================================
// CURSOR PERSONALIZADO (OPCIONAL)
// ========================================

function initCustomCursor() {
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    document.body.appendChild(cursor);
    
    const cursorDot = document.createElement('div');
    cursorDot.className = 'custom-cursor-dot';
    document.body.appendChild(cursorDot);
    
    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    });
    
    function animateCursor() {
        const speed = 0.15;
        cursorX += (mouseX - cursorX) * speed;
        cursorY += (mouseY - cursorY) * speed;
        
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';
        
        requestAnimationFrame(animateCursor);
    }
    
    animateCursor();
    
    // Efectos en hover
    $$('a, button, .tk-card').forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'scale(2)';
            cursor.style.background = 'rgba(0, 224, 255, 0.2)';
        });
        
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'scale(1)';
            cursor.style.background = 'rgba(0, 224, 255, 0.5)';
        });
    });
}

// Inicializar cursor solo en desktop
if (window.innerWidth > 768) {
    // initCustomCursor(); // Descomentar si quieres cursor personalizado
}

// ========================================
// GESTIÓN DE NAVEGACIÓN ACTIVA
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    const navLinks = $$('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });
});

// ========================================
// VANILLA TILT (Si está incluido)
// ========================================

if (typeof VanillaTilt !== 'undefined') {
    VanillaTilt.init($$('.tilt-card'), {
        max: 10,
        speed: 400,
        glare: true,
        'max-glare': 0.2,
        scale: 1.03
    });
}

// ========================================
// CONSOLE MESSAGE
// ========================================

console.log('%c¡Hola Developer! 👋', 'color: #00e0ff; font-size: 20px; font-weight: bold;');
console.log('%cGracias por visitar mi portafolio. ¿Te interesa el código? Encuéntralo en GitHub.', 'color: #7c3aed; font-size: 14px;');
