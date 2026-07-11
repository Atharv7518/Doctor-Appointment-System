/**
 * Vaidyam Home Page Interactions (Presentation Optimized)
 */

document.addEventListener("DOMContentLoaded", () => {
    
    // Snappy Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal-up');
    
    const revealOptions = {
        threshold: 0.05, // Lower threshold triggers animation almost instantly
        rootMargin: "0px 0px -20px 0px" // Triggers slightly before element enters view
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Play once
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // Form Validation Feedback
    const searchForm = document.getElementById('hero-search-form');
    if(searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const queryInput = searchForm.querySelector('input[name="q"]');
            
            if(queryInput.value.trim() === '') {
                e.preventDefault(); 
                queryInput.parentElement.style.border = "1px solid #E11D48";
                queryInput.focus();
                
                setTimeout(() => {
                    queryInput.parentElement.style.border = "";
                }, 1500);
            }
        });
    }
});