// Initialize Lucide icons
// lucide.createIcons();

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Update active navigation link on scroll
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 100;
    if (scrollY >= sectionTop) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// Fade in animation on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => {
  observer.observe(el);
});

// Initialize fade-in for hero section
setTimeout(() => {
  document.querySelector('.hero-section .fade-in').classList.add('visible');
}, 500);

// Add pirate-themed interactive effects
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mouseenter', function () {
    this.style.transform = 'translateY(-8px) rotate(2deg) scale(1.02)';
  });

  card.addEventListener('mouseleave', function () {
    this.style.transform = 'translateY(0) rotate(0deg) scale(1)';
  });
});

// Add treasure chest sound effect simulation (visual feedback)
document.querySelectorAll('.treasure-box').forEach(box => {
  box.addEventListener('click', function () {
    this.style.animation = 'none';
    setTimeout(() => {
      this.style.animation = 'float 2s ease-in-out infinite';
    }, 10);
  });
});

// Pirate ship sailing effect for buttons
document.querySelectorAll('.ship-decoration').forEach(btn => {
  btn.addEventListener('mouseenter', function () {
    this.style.transform = 'translateY(-3px) translateX(5px)';
  });

  btn.addEventListener('mouseleave', function () {
    this.style.transform = 'translateY(0) translateX(0)';
  });
});