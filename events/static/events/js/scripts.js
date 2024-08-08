document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded successfully!');
});

function toggleNav() {
    var navLinks = document.getElementById("navLinks");
    if (navLinks.classList.contains("active")) {
        navLinks.classList.remove("active");
    } else {
        navLinks.classList.add("active");
    }
}