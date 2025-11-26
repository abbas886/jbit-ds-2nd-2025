// js/include.js - simple include-html implementation
async function includeHTML() {
  const elements = document.querySelectorAll('[include-html]');
  for (const el of elements) {
    const file = el.getAttribute('include-html');
    if (!file) continue;
    try {
      const resp = await fetch(file);
      if (!resp.ok) {
        el.innerHTML = '<p style="color:red">Failed to load ' + file + '</p>';
      } else {
        el.innerHTML = await resp.text();
      }
    } catch (err) {
      el.innerHTML = '<p style="color:red">Error loading ' + file + '</p>';
    }
    el.removeAttribute('include-html');
  }
  return true;
}
