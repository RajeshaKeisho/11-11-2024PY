// Run when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // Highlight the current page in the navigation
    highlightCurrentPage();

    // Add functionality to the FAQ accordion
    setupFAQAccordion();

    // Dynamically load features
    loadFeatures();

    // Set up testimonials slider
    setupTestimonialsSlider();

    // Scroll animations for feature cards
    setupScrollAnimations();

    // Add form validation for the Contact page
    if (document.querySelector("form")) {
        setupFormValidation();
    }

    // Add a scroll-to-top button
    setupScrollToTop();

    // Dynamic greeting on the Home page
    if (document.querySelector(".greeting")) {
        displayDynamicGreeting();
    }

    // // Scroll animations for mission and vision cards
    // setupScrollAnimations();

    // // FAQ toggle
    // setupFAQAccordion();

    // Contact form validation
    if (document.querySelector("#contact-form")) {
        setupContactFormValidation();
    }
});

// 1. Highlight Current Page in the Navigation
function highlightCurrentPage() {
    const navLinks = document.querySelectorAll("nav ul li a");
    const currentURL = window.location.pathname;
    navLinks.forEach((link) => {
        if (link.getAttribute("href") === currentURL) {
            link.style.color = "yellow";
            link.style.fontWeight = "bold";
        }
    });
}

// FAQ toggle for About page
function setupFAQAccordion() {
    const questions = document.querySelectorAll(".faq-question");
    questions.forEach((question) => {
        question.addEventListener("click", () => {
            const answer = question.nextElementSibling;
            answer.style.display = answer.style.display === "block" ? "none" : "block";
        });
    });
}

// 3. Contact Form Validation
function setupFormValidation() {
    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        const name = form.querySelector("#name").value.trim();
        const email = form.querySelector("#email").value.trim();
        const message = form.querySelector("#message").value.trim();

        if (!name || !email || !message) {
            event.preventDefault();
            alert("All fields are required.");
        } else if (!validateEmail(email)) {
            event.preventDefault();
            alert("Please enter a valid email address.");
        }
    });
}

// Helper function to validate email
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// 4. Scroll-to-Top Button
function setupScrollToTop() {
    const scrollButton = document.createElement("button");
    scrollButton.innerText = "↑";
    scrollButton.style.position = "fixed";
    scrollButton.style.bottom = "20px";
    scrollButton.style.right = "20px";
    scrollButton.style.display = "none";
    scrollButton.style.backgroundColor = "#333";
    scrollButton.style.color = "white";
    scrollButton.style.border = "none";
    scrollButton.style.padding = "10px";
    scrollButton.style.cursor = "pointer";
    document.body.appendChild(scrollButton);

    window.addEventListener("scroll", () => {
        if (window.scrollY > 200) {
            scrollButton.style.display = "block";
        } else {
            scrollButton.style.display = "none";
        }
    });

    scrollButton.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
}

// 5. Dynamic Greeting on Home Page
function displayDynamicGreeting() {
    const greetingElement = document.querySelector(".greeting");
    const currentHour = new Date().getHours();
    let greeting;

    if (currentHour < 12) {
        greeting = "Good Morning!";
    } else if (currentHour < 18) {
        greeting = "Good Afternoon!";
    } else {
        greeting = "Good Evening!";
    }

    greetingElement.innerText = greeting;
}


// Dynamically load features
function loadFeatures() {
    const features = [
        { title: "High Quality", description: "We offer the best services." },
        { title: "Fast Delivery", description: "We value your time." },
        { title: "24/7 Support", description: "We are here to help anytime." },
        { title: "Affordable Prices", description: "Get the best value for your money." }
    ];

    const container = document.querySelector(".features-container");

    features.forEach((feature) => {
        const card = document.createElement("div");
        card.className = "feature-card";
        card.innerHTML = `
            <h3>${feature.title}</h3>
            <p>${feature.description}</p>
        `;
        container.appendChild(card);
    });
}

// Scroll animations for feature cards
function setupScrollAnimations() {
    const featureCards = document.querySelectorAll(".feature-card");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    });

    featureCards.forEach((card) => observer.observe(card));
}

// Testimonials slider
function setupTestimonialsSlider() {
    const slider = document.querySelector(".testimonials-slider");
    const testimonials = document.querySelectorAll(".testimonial");
    let currentIndex = 0;

    setInterval(() => {
        currentIndex = (currentIndex + 1) % testimonials.length;
        slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    }, 3000);
}


// Contact form validation
function setupContactFormValidation() {
    const form = document.querySelector("#contact-form");

    form.addEventListener("submit", (event) => {
        const name = form.querySelector("#name").value.trim();
        const email = form.querySelector("#email").value.trim();
        const message = form.querySelector("#message").value.trim();

        if (!name || !email || !message) {
            event.preventDefault();
            alert("All fields are required.");
        } else if (!validateEmail(email)) {
            event.preventDefault();
            alert("Please enter a valid email address.");
        }
    });
}



document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contact-form");
    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const messageInput = document.getElementById("message");

    const nameError = document.getElementById("name-error");
    const emailError = document.getElementById("email-error");
    const messageError = document.getElementById("message-error");

    form.addEventListener("submit", (event) => {
        let isValid = true;

        // Validate name
        if (nameInput.value.trim() === "") {
            nameError.textContent = "Name is required.";
            nameError.style.display = "block";
            isValid = false;
        } else {
            nameError.style.display = "none";
        }

        // Validate email
        if (!validateEmail(emailInput.value.trim())) {
            emailError.textContent = "Please enter a valid email address.";
            emailError.style.display = "block";
            isValid = false;
        } else {
            emailError.style.display = "none";
        }

        // Validate message
        if (messageInput.value.trim() === "") {
            messageError.textContent = "Message cannot be empty.";
            messageError.style.display = "block";
            isValid = false;
        } else {
            messageError.style.display = "none";
        }

        // Prevent form submission if invalid
        if (!isValid) {
            event.preventDefault();
        } else {
            alert("Thank you! Your message has been submitted.");
        }
    });

    // Email validation helper function
    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }



     // Scroll animations for article cards
     const articles = document.querySelectorAll(".article");

     const observer = new IntersectionObserver((entries) => {
         entries.forEach((entry) => {
             if (entry.isIntersecting) {
                 entry.target.classList.add("visible");
             }
         });
     });
 
     articles.forEach((article) => observer.observe(article));
});




