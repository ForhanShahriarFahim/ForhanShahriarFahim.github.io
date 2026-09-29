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
    // Old publication URLs and paper bookmarks lead to the canonical one-page
    // list. Without scripting, publications.html offers the same title links.
    if (document.body.hasAttribute("data-legacy-publications")) {
      var oldId = window.location.hash.slice(1);
      var anchor = oldId && document.getElementById(oldId);
      var target = (anchor && anchor.getAttribute("data-canonical-target")) || "publications";
      window.location.replace("/#" + target);
      return;
    }

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

    // The homepage top navigation follows the section in view. The thin bar
    // shows reading progress in both desktop and compact layouts.
    (function () {
      var nav = document.querySelector(".site-nav");
      var sections = Array.prototype.slice.call(
        document.querySelectorAll("main > .wrap > section[id]")
      );
      if (!nav || !document.getElementById("research") || !sections.length) return;

      var links = Array.prototype.slice.call(
        nav.querySelectorAll(".site-nav__links a, .site-nav__menu-links a")
      );
      var menu = nav.querySelector(".site-nav__menu");
      var currentLabel = nav.querySelector(".site-nav__current");
      if (menu) {
        menu.querySelectorAll("a").forEach(function (link) {
          link.addEventListener("click", function () { menu.open = false; });
        });
      }
      document.addEventListener("keydown", function (event) {
        if (event.key !== "Escape" || !menu || !menu.open) return;
        menu.open = false;
        menu.querySelector("summary").focus();
      });
      document.addEventListener("click", function (event) {
        if (menu && menu.open && !menu.contains(event.target)) menu.open = false;
      });

      var progress = document.createElement("span");
      progress.className = "scroll-progress";
      progress.setAttribute("aria-hidden", "true");
      document.body.appendChild(progress);

      var sync = function () {
        var page = document.documentElement;
        var maxScroll = Math.max(0, page.scrollHeight - page.clientHeight);
        var amount = maxScroll ? Math.min(1, Math.max(0, window.scrollY / maxScroll)) : 0;
        progress.style.transform = "scaleX(" + amount + ")";

        var marker = nav.getBoundingClientRect().bottom + 32;
        var currentId = "";
        sections.forEach(function (section) {
          if (section.getBoundingClientRect().top <= marker) currentId = section.id;
        });
        // Short final sections cannot reach the top marker at the page end.
        if (maxScroll > 0 && window.scrollY >= maxScroll - 2) {
          currentId = sections[sections.length - 1].id;
        }
        if (currentId === "about") currentId = "";
        var inResearch = ["research", "publications", "research-work"].indexOf(currentId) !== -1;
        var inCommunity = ["updates", "blog", "contact"].indexOf(currentId) !== -1;
        var currentGroup = inResearch ? "research" : currentId;
        links.forEach(function (link) {
          var target = link.hash.slice(1);
          if ((link.classList.contains("site-nav__community") && inCommunity) ||
              (!link.classList.contains("site-nav__community") && target === currentGroup)) {
            link.setAttribute("aria-current", "location");
          }
          else link.removeAttribute("aria-current");
        });
        if (currentLabel) {
          var active = links.find(function (link) {
            return link.classList.contains("site-nav__sublink") && link.hash.slice(1) === currentId;
          }) || links.find(function (link) { return link.hash.slice(1) === currentGroup; });
          currentLabel.textContent = active ? active.textContent.trim() : "All sections";
        }
      };

      var ticking = false;
      var schedule = function () {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () { sync(); ticking = false; });
      };
      var settleTimer;
      window.addEventListener("scroll", function () {
        schedule();
        clearTimeout(settleTimer);
        settleTimer = setTimeout(sync, 150);
      }, { passive: true });
      window.addEventListener("scrollend", sync);
      window.addEventListener("resize", schedule, { passive: true });
      window.addEventListener("hashchange", schedule);
      window.addEventListener("load", schedule);
      window.addEventListener("pageshow", schedule);
      if ("IntersectionObserver" in window) {
        var sectionObserver = new IntersectionObserver(schedule);
        sections.forEach(function (section) { sectionObserver.observe(section); });
      }
      sync();
    })();

    var blogPreview = document.querySelector(".blog-preview");
    if (blogPreview && blogPreview.children.length > 3) {
      blogPreview.classList.add("blog-preview--scrollable");
      blogPreview.tabIndex = 0;
      blogPreview.setAttribute("aria-label", "Recent blog posts; scroll to read");
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
