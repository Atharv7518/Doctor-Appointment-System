// patient/dashboard.js

document.addEventListener("DOMContentLoaded", () => {
    
    // Dynamic Time-based Greeting
    const greetingElement = document.getElementById("dynamic-greeting");
    
    if (greetingElement) {
        const hour = new Date().getHours();
        let greeting = "Welcome back,";

        if (hour >= 5 && hour < 12) {
            greeting = "Good Morning,";
        } else if (hour >= 12 && hour < 17) {
            greeting = "Good Afternoon,";
        } else if (hour >= 17 && hour < 22) {
            greeting = "Good Evening,";
        } else {
            greeting = "Hello,"; // Late night fallback
        }

        greetingElement.innerText = greeting;
    }
});