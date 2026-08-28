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

    // "Last updated" comes from the page's own Last-Modified header, which on
    // GitHub Pages is the deploy time. If the header is missing the browser
    // returns "now", so anything in the future is rejected and the date
    // written into the HTML is left in place as the fallback.
    var updated = document.getElementById("updated");
    if (updated) {
      var when = new Date(document.lastModified);
      if (!isNaN(when) && when.getTime() <= Date.now() + 60000) {
        updated.textContent = when.toLocaleDateString("en-GB", {
          day: "numeric", month: "long", year: "numeric"
        });
        updated.setAttribute("datetime", when.toISOString().slice(0, 10));
      }
    }

    // News grows over time. Past a threshold the older entries collapse behind a
    // toggle, so the homepage stays short without a nested scrollbar (which traps
    // touch scrolling, hides items from in-page search, and prints badly).
    // With scripting off every item simply stays visible.
    var NEWS_VISIBLE = 6;
    var newsList = document.querySelector(".news");
    if (newsList && newsList.children.length > NEWS_VISIBLE) {
      var hidden = Array.prototype.slice.call(newsList.children, NEWS_VISIBLE);
      var label = "Show " + hidden.length + " earlier update" + (hidden.length === 1 ? "" : "s");

      var toggle = document.createElement("button");
      toggle.type = "button";
      toggle.className = "news-toggle";
      toggle.textContent = label;
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-controls", "news-list");
      newsList.id = newsList.id || "news-list";

      var setHidden = function (state) {
        hidden.forEach(function (li) { li.hidden = state; });
      };
      setHidden(true);

      toggle.addEventListener("click", function () {
        var expanded = toggle.getAttribute("aria-expanded") === "true";
        setHidden(expanded);
        toggle.setAttribute("aria-expanded", String(!expanded));
        toggle.textContent = expanded ? label : "Show fewer";
      });
      newsList.insertAdjacentElement("afterend", toggle);
    }

    // Progressive enhancement: add a copy button to each BibTeX panel. Done in
    // JS so that with scripting off the citation is still plain selectable text.
    if (navigator.clipboard) {
      document.querySelectorAll(".bibtex pre").forEach(function (pre) {
        var wrap = document.createElement("div");
        wrap.className = "bibtex__panel";
        pre.parentNode.insertBefore(wrap, pre);
        wrap.appendChild(pre);

        var copy = document.createElement("button");
        copy.type = "button";
        copy.className = "bibtex__copy";
        copy.textContent = "Copy";
        copy.addEventListener("click", function () {
          navigator.clipboard.writeText(pre.textContent.trim()).then(function () {
            copy.textContent = "Copied";
            setTimeout(function () { copy.textContent = "Copy"; }, 1600);
          }, function () {
            copy.textContent = "Press Ctrl+C";
            setTimeout(function () { copy.textContent = "Copy"; }, 1600);
          });
        });
        wrap.appendChild(copy);
      });
    }

    // Back-to-top control. Built here rather than in markup so it exists on every
    // page without duplicating HTML, and so readers without scripting are not
    // shown a control that could not work anyway.
    (function () {
      var toTop = document.createElement("button");
      toTop.type = "button";
      toTop.className = "to-top";
      toTop.setAttribute("aria-label", "Back to top");
      toTop.innerHTML =
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" ' +
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
        '<path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>';
      document.body.appendChild(toTop);

      var showAfter = function () { return Math.max(300, window.innerHeight * 0.6); };
      var sync = function () {
        toTop.classList.toggle("is-visible", window.pageYOffset > showAfter());
      };

      var ticking = false;
      window.addEventListener("scroll", function () {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () { sync(); ticking = false; });
      }, { passive: true });
      window.addEventListener("resize", sync, { passive: true });
      sync();

      toTop.addEventListener("click", function () {
        var reduce = window.matchMedia &&
                     window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
        // Send keyboard focus back to the top too, without fighting the scroll.
        var first = document.querySelector(".site-nav__name");
        if (first) {
          try { first.focus({ preventScroll: true }); } catch (e) { first.focus(); }
        }
      });
    })();

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
