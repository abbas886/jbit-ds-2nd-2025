
document.addEventListener("DOMContentLoaded", () => {

    // DARK MODE
    const switcher = document.getElementById("themeSwitch");
    switcher.addEventListener("change", () => {
        document.body.classList.toggle("dark");
    });

    // BACK TO TOP BUTTON
    const topBtn = document.getElementById("backToTop");

    window.onscroll = () => {
        topBtn.style.display = window.scrollY > 300 ? "block" : "none";
    };

    topBtn.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });

    // SEARCH TEAMS
    const search = document.getElementById("teamSearch");
    search.addEventListener("input", () => {
        const filter = search.value.toLowerCase();
        document.querySelectorAll("#teams li").forEach(li => {
            const text = li.textContent.toLowerCase();
            li.style.display = text.includes(filter) ? "" : "none";
        });
    });
});

