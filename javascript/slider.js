let currentIndex = 0;
const images = document.querySelectorAll('.slider-image');

function showImage(index) {
    images.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
}

function prevImage() {
    currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
    showImage(currentIndex);
}

function nextImage() {
    currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
    showImage(currentIndex);
}

function openLightbox(index) {
    const isDesktop = window.matchMedia("(min-width: 769px)").matches;
    if (isDesktop) {
        const lightbox = document.getElementById('lightbox');
        const lightboxImage = document.getElementById('lightboxImage');
        currentIndex = index;
        lightboxImage.src = images[currentIndex].src;
        lightbox.style.display = 'flex'; // Affiche le lightbox en plein écran
    }
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none'; // Masque le lightbox
}

function prevLightboxImage() {
    currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
    document.getElementById('lightboxImage').src = images[currentIndex].src;
}

function nextLightboxImage() {
    currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
    document.getElementById('lightboxImage').src = images[currentIndex].src;
}
