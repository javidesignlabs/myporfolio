/* Runs in <head> so a saved light theme is applied before first paint. */
(function () {
  try {
    var t = localStorage.getItem('jdl-theme');
    if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
  } catch (e) {}
})();
