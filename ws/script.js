const imageUrls = [
    "https://static.wikia.nocookie.net/hunterxhunter/images/e/e4/Shizuku_2011.png/revision/latest?cb=20140823152440&path-prefix=es", // URL de la imagen 1
    "https://www.example.com/imagen2.jpg", // URL de la imagen 2
    "https://www.example.com/imagen3.jpg"  // URL de la imagen 3
];

const slideContainer = document.querySelector('.carousel-slide');
const prevButton = document.querySelector('.carousel-prev');
const nextButton = document.querySelector('.carousel-next');
const dotsContainer = document.querySelector('.carousel-dots');

let counter = 0;

// Crear elementos de imagen y puntos dinámicamente
imageUrls.forEach((url, index) => {
    const img = document.createElement('img');
    img.src = url;
    img.alt = `Imagen ${index + 1}`;
    slideContainer.appendChild(img);

    const dot = document.createElement('span');
    dotsContainer.appendChild(dot);
    dot.addEventListener('click', () => {
        counter = index;
        updateSlide();
    });
});

const slides = document.querySelectorAll('.carousel-slide img');
const dots = document.querySelectorAll('.carousel-dots span');

prevButton.addEventListener('click', () => {
    counter--;
    if (counter < 0) {
        counter = slides.length - 1;
    }
    updateSlide();
});

nextButton.addEventListener('click', () => {
    counter++;
    if (counter >= slides.length) {
        counter = 0;
    }
    updateSlide();
});

function updateSlide() {
    slides.forEach(slide => {
        slide.style.transform = `translateX(-${counter * 100}%)`;
    });
    updateDots();
}

function updateDots() {
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === counter);
    });
}

// Mostrar la primera diapositiva y activar el primer punto al cargar la página
updateSlide();
updateDots();
