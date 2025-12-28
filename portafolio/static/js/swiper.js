// Inicialización lazy de Swipers para mejor rendimiento
let swiperProyectos = null;
let swiperBlog = null;
let swiperProyectosIniciado = false;
let swiperBlogIniciado = false;

// Configuración común optimizada
const swiperConfigBase = {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: false,
    autoHeight: false,
    lazy: {
        loadPrevNext: true,
        loadPrevNextAmount: 2,
    },
    preloadImages: false,
    watchSlidesProgress: true,
    watchSlidesVisibility: true,
    observer: true,
    observeParents: true,
    updateOnWindowResize: true,
    resistanceRatio: 0.85,
    breakpoints: {
        768: { slidesPerView: 2 },
        992: { slidesPerView: 3 }
    }
};

// Función para inicializar Swiper de proyectos
function inicializarSwiperProyectos() {
    if (swiperProyectosIniciado) return;
    swiperProyectosIniciado = true;
    
    // Pequeño delay para que no bloquee el render
    setTimeout(() => {
        swiperProyectos = new Swiper('#proyectos-slider', {
            ...swiperConfigBase,
            autoplay: {
                delay: 9000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination-proyectos',
                clickable: true,
                dynamicBullets: true,
            },
        });
        
        aplicarFiltros(swiperProyectos, 'dropdown-proyectos');
    }, 50);
}

// Función para inicializar Swiper de blog
function inicializarSwiperBlog() {
    if (swiperBlogIniciado) return;
    swiperBlogIniciado = true;
    
    // Pequeño delay para que no bloquee el render
    setTimeout(() => {
        swiperBlog = new Swiper('#blog-slider', {
            ...swiperConfigBase,
            autoplay: {
                delay: 9000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination-blog',
                clickable: true,
                dynamicBullets: true,
            },
        });
        
        aplicarFiltros(swiperBlog, 'dropdown-blogs');
    }, 50);
}

// Intersection Observer para inicializar Swipers cuando sean visibles
const observerOptions = {
    root: null,
    rootMargin: '100px',  // Reducido de 200px a 100px para iniciar más cerca
    threshold: 0.01
};

const swiperObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const swiperId = entry.target.id;
            
            if (swiperId === 'proyectos-slider' && !swiperProyectosIniciado) {
                // Usar requestIdleCallback si está disponible, sino requestAnimationFrame
                if ('requestIdleCallback' in window) {
                    requestIdleCallback(() => inicializarSwiperProyectos(), { timeout: 500 });
                } else {
                    requestAnimationFrame(() => inicializarSwiperProyectos());
                }
                swiperObserver.unobserve(entry.target);
            } else if (swiperId === 'blog-slider' && !swiperBlogIniciado) {
                if ('requestIdleCallback' in window) {
                    requestIdleCallback(() => inicializarSwiperBlog(), { timeout: 500 });
                } else {
                    requestAnimationFrame(() => inicializarSwiperBlog());
                }
                swiperObserver.unobserve(entry.target);
            }
        }
    });
}, observerOptions);

// Observar los contenedores de Swiper cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    const proyectosSlider = document.getElementById('proyectos-slider');
    const blogSlider = document.getElementById('blog-slider');
    
    if (proyectosSlider) {
        swiperObserver.observe(proyectosSlider);
    }
    
    if (blogSlider) {
        swiperObserver.observe(blogSlider);
    }
});

function aplicarFiltros(swiper, dropdownId) {
    const dropdownItems = document.querySelectorAll(`#${dropdownId} + .dropdown-menu-filter .dropdown-item`);
    
    dropdownItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Obtener el dropdown button
            const dropdownButton = document.getElementById(dropdownId);
            const filterText = dropdownButton.querySelector('.filter-text');
            
            // Quitar "active" de todos y activar el actual
            dropdownItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            
            // Actualizar el texto del botón
            filterText.textContent = item.textContent;

            const f = item.dataset.filter;

            // Filtrar slides usando estilo inline para mejor compatibilidad con Swiper
            swiper.slides.forEach(slide => {
                const cats = (slide.dataset.cat || '').split(' ').filter(c => c);
                const show = f === '*' || cats.includes(f);
                
                if (show) {
                    slide.style.display = '';
                    slide.classList.remove('swiper-slide-hidden');
                } else {
                    slide.style.display = 'none';
                    slide.classList.add('swiper-slide-hidden');
                }
            });

            // Actualizar swiper después del filtrado
            swiper.updateSlides();
            swiper.updateProgress();
            swiper.updateSlidesClasses();
            swiper.slideTo(0);
            swiper.pagination.render();
            swiper.pagination.update();
        });
    });
}