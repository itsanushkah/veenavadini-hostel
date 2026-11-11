// Reveal sections as they scroll into view
(function () {
  var items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  items.forEach(function (el) { io.observe(el); });
})();

// Gallery: category filter + lightbox
(function () {
  var grid = document.querySelector(".gallery-grid");
  if (!grid) return;
  var items = Array.prototype.slice.call(grid.querySelectorAll(".gallery-item"));
  var buttons = document.querySelectorAll(".filter-btn");

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var cat = btn.getAttribute("data-filter");
      buttons.forEach(function (b) { b.classList.toggle("active", b === btn); b.setAttribute("aria-pressed", b === btn); });
      items.forEach(function (it) {
        it.classList.toggle("is-hidden", cat !== "all" && it.getAttribute("data-cat") !== cat);
      });
    });
  });

  var lb = document.getElementById("lightbox");
  var lbImg = lb.querySelector("img");
  var lbCount = lb.querySelector(".lb-count");
  var current = 0;
  function visible() { return items.filter(function (it) { return !it.classList.contains("is-hidden"); }); }
  function show(i) {
    var list = visible();
    current = (i + list.length) % list.length;
    var it = list[current];
    lbImg.src = it.getAttribute("data-full");
    lbImg.alt = it.querySelector("img").alt;
    lbCount.textContent = (current + 1) + " / " + list.length;
  }
  function open(it) { show(visible().indexOf(it)); lb.classList.add("open"); document.body.style.overflow = "hidden"; lb.querySelector(".lb-close").focus(); }
  function close() { lb.classList.remove("open"); document.body.style.overflow = ""; }

  items.forEach(function (it) { it.addEventListener("click", function () { open(it); }); });
  lb.querySelector(".lb-close").addEventListener("click", close);
  lb.querySelector(".lb-prev").addEventListener("click", function () { show(current - 1); });
  lb.querySelector(".lb-next").addEventListener("click", function () { show(current + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });
})();
