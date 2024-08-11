// Event listener for DOMContentLoaded to confirm that JavaScript has loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded successfully!');
});

// Function to toggle the navigation menu on mobile devices
function toggleNav() {
    var navLinks = document.getElementById("navLinks");
    if (navLinks.classList.contains("active")) {
        navLinks.classList.remove("active");
    } else {
        navLinks.classList.add("active");
    }
}
