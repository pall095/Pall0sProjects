
let slideIndex = 0;
const slides = document.querySelectorAll('.slide');

function showSlides() {
    slides.forEach(slide => (slide.style.display = 'none'));
    slideIndex++;
    if (slideIndex > slides.length) slideIndex = 1;
    slides[slideIndex - 1].style.display = 'block';
    setTimeout(showSlides, 4000); // Change slide every 4 seconds
  }

  // Start the slideshow once the DOM is loaded
document.addEventListener('DOMContentLoaded', showSlides);