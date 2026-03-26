(function () {
  var STORAGE_KEY = "mk-theme";

  function getStored() {
    try {
      var t = localStorage.getItem(STORAGE_KEY);
      if (t === "light" || t === "dark") return t;
    } catch (e) {}
    return null;
  }

  function getResolvedTheme() {
    var explicit = document.documentElement.getAttribute("data-theme");
    if (explicit === "light" || explicit === "dark") return explicit;
    return window.matchMedia("(prefers-color-scheme: light)").matches
      ? "light"
      : "dark";
  }

  function setThemeColor(theme) {
    var meta = document.querySelector('meta[name="theme-color"]');
    if (!meta) return;
    meta.setAttribute("content", theme === "light" ? "#f7f7f8" : "#080808");
  }

  function syncToggleUi() {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    var resolved = getResolvedTheme();
    btn.setAttribute(
      "aria-label",
      resolved === "dark" ? "Switch to light theme" : "Switch to dark theme"
    );
  }

  function onToggle() {
    var current = getResolvedTheme();
    var next = current === "dark" ? "light" : "dark";
    try {
      localStorage.setItem(STORAGE_KEY, next);
    } catch (e) {}
    document.documentElement.setAttribute("data-theme", next);
    setThemeColor(next);
    syncToggleUi();
  }

  function onSystemThemeChange() {
    if (getStored()) return;
    document.documentElement.removeAttribute("data-theme");
    setThemeColor(getResolvedTheme());
    syncToggleUi();
  }

  function init() {
    setThemeColor(getResolvedTheme());

    var btn = document.querySelector(".theme-toggle");
    if (btn) {
      btn.addEventListener("click", onToggle);
      syncToggleUi();
    }

    window
      .matchMedia("(prefers-color-scheme: light)")
      .addEventListener("change", onSystemThemeChange);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
