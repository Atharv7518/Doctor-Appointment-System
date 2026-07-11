document.addEventListener("DOMContentLoaded", () => {
    const TOTAL_DURATION = 3500; 
    const EXIT_DELAY = 400;

    const splashScreen = document.getElementById("splash-screen");
    const progressBar = document.getElementById("progress-fill");
    const statusLabel = document.getElementById("status-label");
    const pageData = document.getElementById("page-data");

    let REDIRECT_URL = "/home/";
    if (pageData && pageData.dataset.homeUrl) {
        REDIRECT_URL = pageData.dataset.homeUrl;
    }

    const phases = [
        { progress: 15, text: "Connecting to clinic network..." },
        { progress: 40, text: "Loading provider schedules..." },
        { progress: 70, text: "Preparing patient dashboard..." },
        { progress: 100, text: "Ready." }
    ];

    let currentPhase = 0;
    const phaseTime = TOTAL_DURATION / phases.length;

    function runLoader() {
        if (currentPhase >= phases.length) {
            if (splashScreen) splashScreen.classList.add("fade-out-screen");
            setTimeout(() => { window.location.href = REDIRECT_URL; }, EXIT_DELAY);
            return;
        }

        const phase = phases[currentPhase];
        if (progressBar) progressBar.style.width = `${phase.progress}%`;
        if (statusLabel) statusLabel.innerText = phase.text;

        currentPhase++;
        setTimeout(runLoader, phaseTime + (Math.random() * 150 - 75));
    }

    setTimeout(runLoader, 500); // Give the logo animation time to play first
});