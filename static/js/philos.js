/* Philos — progressive enhancement. Every form works without JavaScript;
   this file only makes interactions instant. */
(function () {
  "use strict";

  function csrf(form) {
    var input = form.querySelector("input[name=csrfmiddlewaretoken]");
    return input ? input.value : "";
  }

  // Some forms contain controls named "action", which shadow form.action.
  function actionOf(form) {
    return new URL(form.getAttribute("action") || location.href, location.href).href;
  }

  function post(form, extra) {
    var data = new FormData(form);
    if (extra) Object.keys(extra).forEach(function (k) { data.set(k, extra[k]); });
    return fetch(actionOf(form), {
      method: "POST",
      body: data,
      credentials: "same-origin",
      headers: { "X-Requested-With": "XMLHttpRequest", "X-CSRFToken": csrf(form) },
    }).then(function (res) {
      if (!res.ok || res.redirected) throw new Error("Request failed");
      return res.json();
    });
  }

  function setPressed(btn, on) {
    btn.classList.toggle("is-on", on);
    btn.setAttribute("aria-pressed", on ? "true" : "false");
    var label = btn.querySelector("[data-label-on]");
    if (label) label.textContent = on ? label.dataset.labelOn : label.dataset.labelOff;
  }

  function updateStats(stats) {
    if (!stats) return;
    document.querySelectorAll("[data-stat]").forEach(function (el) {
      var key = el.dataset.stat;
      if (!(key in stats)) return;
      var v = stats[key];
      if (key === "rating_avg_5") el.textContent = v ? Number(v).toFixed(1) : "–";
      else if (key === "rating_count") el.textContent = v + " rating" + (v === 1 ? "" : "s");
      else el.textContent = v;
    });
  }

  function applyState(state) {
    document.querySelectorAll("[data-status-form] [data-toggle]").forEach(function (btn) {
      var form = btn.closest("form");
      if (form && actionOf(form) === lastStatusAction) setPressed(btn, !!state[btn.dataset.toggle]);
    });
    var display = document.querySelector("[data-rate-display]");
    if (display) display.style.setProperty("--pct", (state.rating || 0) * 10 + "%");
    var label = document.querySelector("[data-rate-label]");
    if (label) label.textContent = state.rating ? "Rated" : "Rate";
    updateStats(state.stats);
  }

  var lastStatusAction = null;

  // Read / like / to-read toggles.
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-status-form] button[name=action]");
    if (!btn) return;
    e.preventDefault();
    var form = btn.closest("form");
    lastStatusAction = actionOf(form);
    btn.disabled = true;
    post(form, { action: btn.value })
      .then(applyState)
      .catch(function () { form.submit(); })
      .finally(function () { btn.disabled = false; });
  });

  // Quick star rating on the work page.
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-rate-form] button[name=rating]");
    if (!btn) return;
    e.preventDefault();
    var form = btn.closest("form");
    lastStatusAction = actionOf(form);
    var display = form.querySelector("[data-rate-display]");
    var current = display ? parseFloat(display.style.getPropertyValue("--pct")) / 10 : 0;
    var value = btn.value === String(current) ? "0" : btn.value; // click same star again to clear
    post(form, { action: "rate", rating: value }).then(applyState).catch(function () { form.submit(); });
  });

  // Hover preview for any star widget.
  document.addEventListener("mouseover", function (e) {
    var btn = e.target.closest(".star-hits button");
    if (!btn) return;
    var wrap = btn.closest(".star-input");
    var stars = wrap && wrap.querySelector(".stars");
    if (!stars) return;
    if (!stars.dataset.saved) stars.dataset.saved = stars.style.getPropertyValue("--pct") || "0%";
    var value = btn.dataset.value || btn.value;
    stars.style.setProperty("--pct", value * 10 + "%");
  });
  document.addEventListener("mouseout", function (e) {
    var hits = e.target.closest(".star-hits");
    if (!hits || hits.contains(e.relatedTarget)) return;
    var stars = hits.closest(".star-input").querySelector(".stars");
    if (stars && stars.dataset.saved) {
      stars.style.setProperty("--pct", stars.dataset.saved);
      delete stars.dataset.saved;
    }
  });

  // Star input inside forms (log / review).
  document.querySelectorAll("[data-star-input]").forEach(function (wrap) {
    var input = wrap.querySelector("input[name=rating]");
    var stars = wrap.querySelector(".stars");
    function set(v) {
      input.value = v;
      stars.style.setProperty("--pct", v * 10 + "%");
      delete stars.dataset.saved;
      wrap.querySelectorAll(".star-hits button").forEach(function (b) {
        b.setAttribute("aria-checked", String(b.dataset.value === String(v)));
      });
    }
    wrap.addEventListener("click", function (e) {
      var b = e.target.closest(".star-hits button");
      if (b) set(b.dataset.value === input.value ? 0 : b.dataset.value);
      if (e.target.closest("[data-star-clear]")) set(0);
    });
  });

  // Like buttons (reviews, lists).
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("[data-like-form]");
    if (!form) return;
    e.preventDefault();
    post(form).then(function (res) {
      var btn = form.querySelector("button");
      btn.classList.toggle("is-on", res.liked);
      btn.setAttribute("aria-pressed", String(res.liked));
      var label = form.querySelector("[data-like-label]");
      if (label) label.textContent = res.liked ? "Liked" : label.textContent.indexOf("review") > -1 || actionOf(form).indexOf("/review/") > -1 ? "Like review" : "Like";
      var count = form.querySelector("[data-like-count]");
      if (count) count.textContent = res.count;
    }).catch(function () { form.submit(); });
  });

  // Follow button.
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("[data-follow-form]");
    if (!form) return;
    e.preventDefault();
    post(form).then(function (res) {
      var btn = form.querySelector("[data-follow-btn]");
      btn.textContent = res.following ? "Following" : "Follow";
      btn.classList.toggle("btn-primary", !res.following);
      btn.classList.toggle("btn-ghost", res.following);
      btn.setAttribute("aria-pressed", String(res.following));
      var n = document.querySelector("[data-followers]");
      if (n) n.textContent = res.followers;
    }).catch(function () { form.submit(); });
  });

  // Add/remove from list.
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("[data-list-toggle]");
    if (!form) return;
    e.preventDefault();
    post(form).then(function (res) {
      var btn = form.querySelector("button");
      btn.classList.toggle("is-on", res.added);
      btn.setAttribute("aria-pressed", String(res.added));
    }).catch(function () { form.submit(); });
  });

  // Confirm destructive actions.
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("[data-confirm]");
    if (form && !window.confirm(form.dataset.confirm)) e.preventDefault();
  });

  // Auto-submit filter bars.
  document.querySelectorAll("[data-autosubmit]").forEach(function (form) {
    form.addEventListener("change", function () {
      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.name && !el.value) el.disabled = true; // keep URLs clean
      });
      form.submit();
    });
  });

  // Share: native sheet on mobile, clipboard elsewhere.
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-share]");
    if (!btn) return;
    var url = (document.querySelector("link[rel=canonical]") || {}).href || location.href;
    var title = btn.dataset.title || document.title;
    if (navigator.share) {
      navigator.share({ title: title, url: url }).catch(function () {});
    } else if (navigator.clipboard) {
      navigator.clipboard.writeText(url).then(function () {
        var original = btn.innerHTML;
        btn.textContent = "Link copied";
        setTimeout(function () { btn.innerHTML = original; }, 1600);
      });
    }
  });

  // Theme toggle.
  var toggle = document.querySelector("[data-theme-toggle]");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var root = document.documentElement;
      var current = root.dataset.theme ||
        (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
      var next = current === "light" ? "dark" : "light";
      root.dataset.theme = next;
      try { localStorage.setItem("philos-theme", next); } catch (err) {}
    });
  }

  // Close open menus when clicking elsewhere.
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details.user-menu[open], details.add-to-list[open]").forEach(function (d) {
      if (!d.contains(e.target)) d.removeAttribute("open");
    });
  });
})();
