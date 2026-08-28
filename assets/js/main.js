/* Theme toggle and footer year. No dependencies.
   The initial theme is applied by a small inline script in each page's <head>
   (the "theme init" block) so there is no flash of the wrong theme. This file
   only wires up the button.

   Note: nothing is written to localStorage until the visitor actually clicks.
   Persisting the resolved system theme on load would silently pin the site to
   whatever the OS happened to be on the first visit. */
(function () {
  "use strict";

  var root = document.documentElement;

  function storedTheme() {
    try {
      var t = localStorage.getItem("theme");
      return t === "dark" || t === "light" ? t : null;
    } catch (e) {
      return null; // private mode or blocked storage
    }
  }

  function systemPrefersDark() {
    return !!(window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
  }

  function activeTheme() {
    return root.getAttribute("data-theme") || (systemPrefersDark() ? "dark" : "light");
  }

  function describe(button, theme) {
    button.setAttribute(
      "aria-label",
      theme === "dark" ? "Switch to light theme" : "Switch to dark theme"
    );
    button.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var year = document.getElementById("year");
    if (year) year.textContent = String(new Date().getFullYear());

    var button = document.querySelector(".theme-toggle");
    if (!button) return;

    describe(button, activeTheme());

    button.addEventListener("click", function () {
      var next = activeTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try {
        localStorage.setItem("theme", next);
      } catch (e) {
        /* the theme still applies for this page view */
      }
      describe(button, next);
    });

    // Keep the button label honest if the OS theme changes and the visitor has
    // not chosen one explicitly. CSS handles the colours on its own.
    if (window.matchMedia) {
      var query = window.matchMedia("(prefers-color-scheme: dark)");
      var onSystemChange = function () {
        if (!storedTheme()) describe(button, activeTheme());
      };
      if (query.addEventListener) query.addEventListener("change", onSystemChange);
      else if (query.addListener) query.addListener(onSystemChange);
    }
  });
})();
