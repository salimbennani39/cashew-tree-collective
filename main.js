// The Cashew Tree Collective — shared site behaviour

(function () {
  const OPEN_MIN = 7 * 60 + 30; // 07:30
  const CLOSE_MIN = 22 * 60; // 22:00

  // Bali runs on WITA (UTC+8), no daylight saving.
  function baliNow() {
    const now = new Date();
    return new Date(now.getTime() + now.getTimezoneOffset() * 60000 + 8 * 3600000);
  }

  // Header: live open / closed status
  function updateStatus() {
    const t = baliNow();
    const mins = t.getHours() * 60 + t.getMinutes();
    const open = mins >= OPEN_MIN && mins < CLOSE_MIN;
    document.querySelectorAll("[data-status]").forEach((el) => {
      el.classList.toggle("open", open);
      el.querySelector("b").textContent = open
        ? "Open now · until 10pm"
        : "Closed · opens 7:30am";
    });
  }
  updateStatus();
  setInterval(updateStatus, 60000);

  // Header background once the page scrolls
  const header = document.querySelector(".site-header");
  const onScroll = () => header && header.classList.toggle("scrolled", window.scrollY > 24);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Mobile menu
  const btn = document.querySelector(".menu-btn");
  const mnav = document.querySelector(".mobile-nav");
  if (btn && mnav) {
    btn.addEventListener("click", () => {
      const open = mnav.classList.toggle("open");
      btn.textContent = open ? "Close" : "Menu";
      btn.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    });
  }

  // Scroll reveal
  const items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px" }
    );
    items.forEach((el) => io.observe(el));
  } else {
    items.forEach((el) => el.classList.add("in"));
  }

  // Collective list: image follows the cursor on hover (desktop only)
  const preview = document.querySelector(".venue-preview");
  if (preview && window.matchMedia("(hover: hover)").matches) {
    const img = preview.querySelector("img");
    document.querySelectorAll(".venue[data-img]").forEach((row) => {
      row.addEventListener("mouseenter", () => {
        img.src = row.dataset.img;
        preview.classList.add("show");
      });
      row.addEventListener("mouseleave", () => preview.classList.remove("show"));
      row.addEventListener("mousemove", (e) => {
        preview.style.left = e.clientX + 140 + "px";
        preview.style.top = e.clientY + "px";
      });
    });
  }

  // Music page: next Thursday in Bali time
  const nextEl = document.querySelector("[data-next-thursday]");
  if (nextEl) {
    const t = baliNow();
    const diff = (4 - t.getDay() + 7) % 7; // 4 = Thursday
    const d = new Date(t);
    d.setDate(t.getDate() + diff);
    const label = diff === 0 ? "Tonight" : d.toLocaleDateString("en-GB", { day: "numeric", month: "long" });
    nextEl.textContent = label;
    const sub = document.querySelector("[data-next-sub]");
    if (sub) sub.textContent = diff === 0 ? "It's Thursday. See you in the garden." : "Thursday " + d.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  }

  // Footer year
  document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
})();
