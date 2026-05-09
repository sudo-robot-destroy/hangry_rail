(function () {
  var STORAGE_KEY = "hangryRailTheme";
  var root = document.documentElement;
  var select = document.getElementById("theme-select");
  var year = document.getElementById("year");

  function setTheme(themeName) {
    root.setAttribute("data-theme", themeName);
    localStorage.setItem(STORAGE_KEY, themeName);
    select.value = themeName;
  }

  var savedTheme = localStorage.getItem(STORAGE_KEY);
  if (savedTheme) {
    setTheme(savedTheme);
  }

  select.addEventListener("change", function (event) {
    setTheme(event.target.value);
  });

  year.textContent = String(new Date().getFullYear());
})();
