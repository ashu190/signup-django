const navMenuIcon = document.querySelector(".navMenuIcon");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

navMenuIcon.addEventListener("click", () => {
    navLinks.classList.toggle("open");
    links.forEach(link => {
        link.classList.toggle("fade");
    });
});