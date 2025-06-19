// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      const offsetTop = target.offsetTop - 70 // Account for fixed navbar
      window.scrollTo({
        top: offsetTop,
        behavior: "smooth",
      })
    }
  })
})

// Navbar background change on scroll
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar")
  if (window.scrollY > 50) {
    navbar.style.backgroundColor = "rgba(26, 26, 46, 0.95)"
    navbar.style.backdropFilter = "blur(10px)"
  } else {
    navbar.style.backgroundColor = ""
    navbar.style.backdropFilter = ""
  }
})

// Active navigation link highlighting
window.addEventListener("scroll", () => {
  const sections = document.querySelectorAll("section[id]")
  const navLinks = document.querySelectorAll(".nav-link")

  let current = ""
  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 100
    const sectionHeight = section.clientHeight
    if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
      current = section.getAttribute("id")
    }
  })

  navLinks.forEach((link) => {
    link.classList.remove("active")
    if (link.getAttribute("href") === `#${current}`) {
      link.classList.add("active")
    }
  })
})

// Form submission handler
document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault()

  // Get form data
  const formData = new FormData(this)
  const data = Object.fromEntries(formData)

  // Simple validation
  if (!data.name || !data.class || !data.message) {
    alert("Please fill in all required fields.")
    return
  }

  // Simulate form submission
  const submitBtn = this.querySelector('button[type="submit"]')
  const originalText = submitBtn.innerHTML

  submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...'
  submitBtn.disabled = true

  setTimeout(() => {
    alert(
      "Thank you for your application! We will review it and get back to you within 24-48 hours. Please join our Discord for faster communication.",
    )
    this.reset()
    submitBtn.innerHTML = originalText
    submitBtn.disabled = false
  }, 2000)
})

// Gallery image modal (simple implementation)
document.querySelectorAll(".gallery-item img").forEach((img) => {
  img.addEventListener("click", function () {
    // Create modal overlay
    const modal = document.createElement("div")
    modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            cursor: pointer;
        `

    // Create modal image
    const modalImg = document.createElement("img")
    modalImg.src = this.src
    modalImg.style.cssText = `
            max-width: 90%;
            max-height: 90%;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        `

    modal.appendChild(modalImg)
    document.body.appendChild(modal)

    // Close modal on click
    modal.addEventListener("click", () => {
      document.body.removeChild(modal)
    })
  })
})

// Animate elements on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("fade-in-up")
    }
  })
}, observerOptions)

// Observe all cards and major elements
document.querySelectorAll(".card, .hero-section, .section-title").forEach((el) => {
  observer.observe(el)
})

// Dynamic copyright year
document.addEventListener("DOMContentLoaded", () => {
  const currentYear = new Date().getFullYear()
  const copyrightElements = document.querySelectorAll("footer p")
  copyrightElements.forEach((el) => {
    if (el.textContent.includes("2024")) {
      el.textContent = el.textContent.replace("2024", currentYear)
    }
  })
})

// Easter egg: Konami code
const konamiCode = []
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65] // Up Up Down Down Left Right Left Right B A

document.addEventListener("keydown", (e) => {
  konamiCode.push(e.keyCode)
  if (konamiCode.length > konamiSequence.length) {
    konamiCode.shift()
  }

  if (
    konamiCode.length === konamiSequence.length &&
    konamiCode.every((code, index) => code === konamiSequence[index])
  ) {
    // Easter egg activated
    document.body.style.animation = "rainbow 2s infinite"
    setTimeout(() => {
      document.body.style.animation = ""
      alert("🎉 For the Alliance! You found the secret code! 🎉")
    }, 2000)
  }
})

// Add rainbow animation for easter egg
const style = document.createElement("style")
style.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
`
document.head.appendChild(style)

// Tooltip initialization (if using Bootstrap tooltips)
document.addEventListener("DOMContentLoaded", () => {
  // Initialize tooltips if Bootstrap is loaded
  const bootstrap = window.bootstrap // Declare the bootstrap variable
  if (typeof bootstrap !== "undefined") {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl))
  }
})

// Lazy loading for images
document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll('img[src*="placeholder"]')

  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target
        img.style.opacity = "1"
        observer.unobserve(img)
      }
    })
  })

  images.forEach((img) => {
    imageObserver.observe(img)
  })
})

// Mobile menu auto-close
document.querySelectorAll(".nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    const navbarCollapse = document.querySelector(".navbar-collapse")
    if (navbarCollapse.classList.contains("show")) {
      const bsCollapse = new window.bootstrap.Collapse(navbarCollapse) // Use window.bootstrap
      bsCollapse.hide()
    }
  })
})

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Apply debounce to scroll events
const debouncedScrollHandler = debounce(() => {
  // Your scroll handling code here
}, 10)

window.addEventListener("scroll", debouncedScrollHandler)
