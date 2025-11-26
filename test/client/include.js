async function includeHTML() {
    const elements = document.querySelectorAll("[include-html]");

    for (const el of elements) {
        const file = el.getAttribute("include-html");
        if (!file) continue;

        const response = await fetch(file);

        if (response.ok) {
            el.innerHTML = await response.text();
        } else {
            el.innerHTML = "Page not found.";
        }

        el.removeAttribute("include-html");
    }

    return true;
}
