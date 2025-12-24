const swiperProyectos = new Swiper('#proyectos-slider', {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    autoplay: {
    delay: 9000, // 9 segundos
    disableOnInteraction: false,
    },
    pagination: {
    el: '.swiper-pagination',
    clickable: true,
    },
    breakpoints: {
    768: { slidesPerView: 2 },
    992: { slidesPerView: 3 }
    }
});

const swiperBlog = new Swiper('#blog-slider', {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    autoplay: {
    delay: 9000, // 9 segundos
    disableOnInteraction: false,
    },
    pagination: {
    el: '.swiper-pagination',
    clickable: true,
    },
    breakpoints: {
    768: { slidesPerView: 2 },
    992: { slidesPerView: 3 }
    }
});

function aplicarFiltros(swiper, filterSelector) {
    document.querySelectorAll(filterSelector).forEach(btn => {
        btn.addEventListener('click', () => {
            // Quitar "active" de todos y activar el actual
            document.querySelectorAll(filterSelector).forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const f = btn.dataset.filter;

            swiper.slides.forEach(card => {
                const cats = (card.dataset.cat || '').split(' ');
                const show = f === '*' || cats.includes(f);
                if (show) {
                    card.classList.remove('d-none');
                } else {
                    card.classList.add('d-none');
                }
            });

            swiper.update();
        });
    });
}


// Filtros independientes
aplicarFiltros(swiperProyectos, '#filtros-proyectos .btn');
aplicarFiltros(swiperBlog, '#filtros-blogs .btn');