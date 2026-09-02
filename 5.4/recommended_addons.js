(function () {
  "use strict";

  const root = document.querySelector(".zra");
  if (!root) return;

  const search = root.querySelector("#zra-search");
  const category = root.querySelector("#zra-category");
  const clear = root.querySelector("#zra-clear");
  const count = root.querySelector("#zra-result-count");
  const activeFilters = root.querySelector("#zra-active-filters");
  const empty = root.querySelector("#zra-empty");
  const products = [...root.querySelectorAll(".zra-product")];
  const groups = [...root.querySelectorAll("[data-product-group]")];
  const state = { query: "", category: "all" };

  function mountSidebarNavigation() {
    const currentPage = document.querySelector(".wy-menu-vertical li.toctree-l1.current");
    if (!currentPage || currentPage.querySelector(".zra-sidebar-subnav")) return;

    const subnav = document.createElement("ul");
    subnav.className = "zra-sidebar-subnav";
    groups.forEach((group) => {
      const item = document.createElement("li");
      item.className = "toctree-l2";
      const link = document.createElement("a");
      link.className = "reference internal";
      link.href = `#${group.getAttribute("aria-labelledby")}`;
      link.textContent = group.dataset.productGroup;
      link.addEventListener("click", (event) => {
        event.preventDefault();
        const targetId = group.getAttribute("aria-labelledby");
        Object.assign(state, { query: "", category: "all" });
        search.value = "";
        if (category) category.value = "all";
        render();
        history.replaceState(null, "", `#${targetId}`);
        requestAnimationFrame(() => group.scrollIntoView({ behavior: "smooth", block: "start" }));
      });
      item.appendChild(link);
      subnav.appendChild(item);
    });
    currentPage.appendChild(subnav);
  }

  function normalize(value) {
    return String(value || "").toLocaleLowerCase();
  }

  function render() {
    let visible = 0;
    const query = normalize(state.query);

    products.forEach((product) => {
      const matchesQuery = !query || normalize(product.textContent).includes(query);
      const matchesCategory = state.category === "all" || product.dataset.category === state.category;
      const show = matchesQuery && matchesCategory;
      product.hidden = !show;
      if (show) visible += 1;
    });

    groups.forEach((group) => {
      group.hidden = !group.querySelector(".zra-product:not([hidden])");
    });

    const tags = [];
    if (state.query) tags.push(`Search: ${state.query}`);
    if (state.category !== "all") tags.push(state.category);
    activeFilters.innerHTML = tags.map((tag) => `<span class="zra-filter-tag">${tag.replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[char])}</span>`).join("");
    count.textContent = `${visible} ${visible === 1 ? "recommendation" : "recommendations"}`;
    clear.hidden = tags.length === 0;
    empty.hidden = visible !== 0;
  }

  function setFilter(kind, value) {
    state[kind] = value;
    if (kind === "category" && category) category.value = value;
    render();
    if (kind !== "query") root.querySelector("#zra-catalog-title").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  let searchTimer;
  search.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => setFilter("query", search.value.trim()), 100);
  });
  category?.addEventListener("change", () => setFilter("category", category.value));
  clear.addEventListener("click", () => {
    Object.assign(state, { query: "", category: "all" });
    search.value = "";
    if (category) category.value = "all";
    render();
    search.focus();
  });
  root.addEventListener("click", (event) => {
    const categoryButton = event.target.closest("[data-category]:not(.zra-product)");
    if (categoryButton) setFilter("category", categoryButton.dataset.category);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && !/input|textarea|select/i.test(document.activeElement.tagName)) {
      event.preventDefault();
      search.focus();
    }
  });
  mountSidebarNavigation();
})();
