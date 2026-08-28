/* Theme toggle. No dependencies.
   The initial theme is applied by a small inline script in each page's <head>
   (see the "theme init" block) so there is no flash of the wrong theme.
   This file only wires up the toggle button. */
(function () {
  "use strict";

  var root = document.documentElement;

  function systemPrefersDark() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }

  function currentTheme() {
    return root.getAttribute("data-theme") || (systemPrefersDark() ? "dark" : "light");
  }

  function setTheme(theme) {
    root.setAttribute("data-theme", theme);
    try {
      localStorage.setItem("theme", theme);
    } catch (e) {
      /* private mode or blocked storage: the theme still applies for this page view */
    }
    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.setAttribute("aria-label", theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    // Footer copyright year, so it never needs editing by hand.
    var year = document.getElementById("year");
    if (year) year.textContent = String(new Date().getFullYear());

    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;

    setTheme(currentTheme());

    btn.addEventListener("click", function () {
      setTheme(currentTheme() === "dark" ? "light" : "dark");
    });
  });
})();
