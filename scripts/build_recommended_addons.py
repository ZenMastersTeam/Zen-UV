from __future__ import annotations

import argparse
import html
import json
import tempfile
import urllib.request
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "mkdocs/data/recommended_addons.json"
OUTPUT_PATH = ROOT / "mkdocs/recommended_addons.md"
IMAGE_DIR = ROOT / "mkdocs/img/recommended_addons"
IMAGE_SIZE = (600, 375)

GROUP_ORDER = [
    "Modeling",
    "Rigging & Animation",
    "UV",
    "Materials & Texturing",
    "Cameras & Tracking",
    "Rendering & Lighting",
    "Simulation & VFX",
    "Interface & Workflow",
    "Assets & Generators",
    "Blender Training",
]

GROUP_COPY = {
    "Modeling": "Mesh creation, retopology, hard-surface tools, curves, and precision geometry editing.",
    "Rigging & Animation": "Character setup, skinning, posing, motion capture, and animation tools.",
    "UV": "Tools for unwrapping, packing, inspecting, and organizing production UV layouts.",
    "Materials & Texturing": "Decals, procedural surfaces, PBR painting, shaders, and direct material mapping.",
    "Cameras & Tracking": "Camera matching, tracking, photogrammetry, and shot-building utilities.",
    "Rendering & Lighting": "Lighting, HDRIs, atmosphere, color grading, and render management.",
    "Simulation & VFX": "Fluids, cloth, destruction, particles, deformation, and physical effects.",
    "Interface & Workflow": "Import, organization, performance, panels, and everyday productivity helpers.",
    "Assets & Generators": "Reusable libraries and procedural generators for faster scene building.",
    "Blender Training": "Project-based courses that develop reusable modeling and procedural-texturing skills.",
}

LOW_PRIORITY_ZEN_SLUGS = {"addonspresets", "zen-console-top-most-for-blender"}

MODELING_LEAD_ORDER = {
    "boxcutter": 0,
    "hardopsofficial": 1,
    "meshmachine": 2,
    "retopoflow": 3,
    "grid-modeler": 4,
}

REQUIRED_FIELDS = {
    "slug", "title", "creator", "group", "description", "affiliate_url",
    "priority", "image_source",
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def canonical_image_url(value: str) -> str:
    if value.startswith("../img/"):
        return "https://zenmastersteam.github.io/Zen-UV/latest/" + value.removeprefix("../")
    return value


def cache_image(product: dict) -> None:
    """Download and optimize one missing preview. Requires Pillow."""
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise SystemExit("Pillow is required with --fetch-images: python -m pip install Pillow") from exc

    source_url = product["image_source"]
    suffix = Path(source_url.split("?", 1)[0]).suffix or ".img"
    temporary = Path(tempfile.gettempdir()) / f'zra-{product["slug"]}{suffix}'
    request = urllib.request.Request(source_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        temporary.write_bytes(response.read())

    target = IMAGE_DIR / f'{product["slug"]}.webp'
    with Image.open(temporary) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode not in ("RGB", "RGBA"):
            image = image.convert("RGBA" if "transparency" in image.info else "RGB")
        image = ImageOps.fit(image, IMAGE_SIZE, method=Image.Resampling.LANCZOS)
        if image.mode == "RGBA":
            background = Image.new("RGB", image.size, "white")
            background.paste(image, mask=image.getchannel("A"))
            image = background
        image.save(target, "WEBP", quality=74, method=6, optimize=True)


def load_products(fetch_images: bool = False) -> list[dict]:
    payload = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    products = payload.get("products")
    if payload.get("schema_version") != 1 or not isinstance(products, list):
        raise SystemExit(f"{CATALOG_PATH}: unsupported catalog schema")

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    seen: set[str] = set()
    for product in products:
        missing = REQUIRED_FIELDS - product.keys()
        if missing:
            raise SystemExit(f'{product.get("slug", "unknown product")}: missing fields: {", ".join(sorted(missing))}')
        if product["slug"] in seen:
            raise SystemExit(f"Duplicate product slug: {product['slug']}")
        if product["group"] not in GROUP_ORDER:
            raise SystemExit(f'{product["slug"]}: unsupported group: {product["group"]}')
        expected_url = f'https://superhivemarket.com/products/{quote(product["slug"], safe="-")}?ref=1462'
        if product["affiliate_url"] != expected_url:
            raise SystemExit(f'{product["slug"]}: affiliate URL must be exactly {expected_url}')
        image_path = IMAGE_DIR / f'{product["slug"]}.webp'
        if fetch_images and not image_path.exists():
            cache_image(product)
        if not image_path.exists():
            raise SystemExit(f'{product["slug"]}: missing preview {image_path}; run with --fetch-images')
        # The page is served from /recommended_addons/, while images live in
        # /img/recommended_addons/. Raw HTML paths are not rewritten by MkDocs.
        product["image_url"] = f'../img/recommended_addons/{quote(product["slug"], safe="-")}.webp'
        seen.add(product["slug"])

    def editorial_bucket(product: dict) -> int:
        if product["group"] == "Modeling" and product["slug"] in MODELING_LEAD_ORDER:
            return -1
        if product["slug"] in LOW_PRIORITY_ZEN_SLUGS:
            return 2
        if product["creator"].casefold() == "zenmasters":
            return 0
        return 1

    products.sort(key=lambda p: (
        editorial_bucket(p),
        MODELING_LEAD_ORDER.get(p["slug"], 999),
        -int(p.get("priority", 0)),
        p["title"].casefold(),
    ))
    return products


def card(product: dict) -> str:
    alt = f'{product["title"]} Blender preview by {product["creator"]}'
    return f'''<article class="zra-card zra-product" id="{esc(product["slug"])}" data-category="{esc(product["group"])}" data-creator="{esc(product["creator"])}">
  <div class="zra-card__media">
    <img src="{esc(product["image_url"])}" alt="{esc(alt)}" loading="lazy" width="800" height="500">
  </div>
  <div class="zra-card__body">
    <div class="zra-card__overline"><span>{esc(product["group"])}</span><span>by {esc(product["creator"])}</span></div>
    <h3><a class="zra-card__permalink" href="#{esc(product["slug"])}">{esc(product["title"])}</a></h3>
    <p class="zra-card__desc">{esc(product["description"])}</p>
    <div class="zra-card__footer">
      <a class="zra-button" href="{esc(product["affiliate_url"])}" target="_blank" rel="sponsored noopener noreferrer" aria-label="View {esc(product["title"])} on Superhive">View product <span aria-hidden="true">↗</span></a>
    </div>
  </div>
</article>'''


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the catalog, cache missing previews, and rebuild the page.")
    parser.add_argument("--fetch-images", action="store_true", help="Download and optimize previews that are missing locally.")
    args = parser.parse_args()
    products = load_products(fetch_images=args.fetch_images)
    if not products:
        raise SystemExit(f"No products found in {CATALOG_PATH}")
    group_counts = {group: sum(p["group"] == group for p in products) for group in GROUP_ORDER}

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": "https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/#page",
                "url": "https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/",
                "name": "Recommended Blender Add-ons for Artists",
                "description": "A curated collection of Blender add-ons for modeling, texturing, lighting, rendering, and creative workflows.",
                "isPartOf": {"@type": "WebSite", "name": "Zen UV Documentation", "url": "https://zenmastersteam.github.io/Zen-UV/latest/"},
                "mainEntity": {"@id": "https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/#list"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Zen UV Documentation", "item": "https://zenmastersteam.github.io/Zen-UV/latest/"},
                    {"@type": "ListItem", "position": 2, "name": "Recommended Blender Add-ons", "item": "https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/"},
                ],
            },
            {
                "@type": "ItemList",
                "@id": "https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/#list",
                "name": "Recommended Blender add-ons",
                "numberOfItems": len(products),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": index,
                        "item": {
                            "@type": "Course" if p["group"] == "Blender Training" else "SoftwareApplication",
                            "name": p["title"],
                            "description": p["description"],
                            "image": canonical_image_url(p["image_url"]),
                            "url": f'https://zenmastersteam.github.io/Zen-UV/latest/recommended_addons/#{p["slug"]}',
                        },
                    }
                    for index, p in enumerate(products, 1)
                ],
            },
        ],
    }

    sections = []
    for group in GROUP_ORDER:
        items = [p for p in products if p["group"] == group]
        if not items:
            continue
        cards = "\n".join(card(p) for p in items)
        group_id = group.lower().replace(" & ", "-").replace(" ", "-")
        sections.append(f'''<section class="zra-category-section" data-product-group="{esc(group)}" aria-labelledby="{group_id}">
  <div class="zra-category-head">
    <div><h2 id="{group_id}">{esc(group)}</h2></div>
    <p>{esc(GROUP_COPY[group])}</p>
  </div>
  <div class="zra-products">{cards}</div>
</section>''')

    active_groups = [group for group in GROUP_ORDER if group_counts[group]]
    shortcuts = "".join(f'<button class="zra-chip" type="button" data-category="{esc(group)}">{esc(group)}</button>' for group in active_groups)
    page = f'''---
title: Recommended Blender Add-ons for Artists
description: Explore {len(products)} recommended Blender products for modeling, texturing, lighting and rendering, selected by the Zen UV team from active Superhive creators.
image: img/recommended_addons-og.jpg
image_alt: Recommended Blender Add-ons selected by Zenmasters
---

<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>

<div class="zra">
  <header class="zra-hero" aria-labelledby="zra-title">
    <h1 id="zra-title">Recommended Blender Add-ons</h1>
    <p class="zra-hero__lede">Useful tools for modeling, UVs, texturing, rendering, training, and more.</p>
    <div class="zra-search-wrap">
      <label class="zra-sr-only" for="zra-search">Search Blender add-ons</label>
      <input id="zra-search" type="search" autocomplete="off" placeholder="Search add-ons, creators, or workflows">
    </div>
    <nav class="zra-shortcuts" aria-label="Browse add-on categories">{shortcuts}</nav>
  </header>

  <section class="zra-section zra-section--catalog" aria-labelledby="zra-catalog-title">
    <div class="zra-catalog-bar"><h2 id="zra-catalog-title">Browse by workflow</h2><div><span id="zra-result-count" class="zra-sr-only" aria-live="polite">{len(products)} recommendations</span><button id="zra-clear" class="zra-button zra-button--quiet" type="button" hidden>Clear filters</button></div></div>
    <div id="zra-active-filters" class="zra-active-filters" aria-label="Active filters"></div>
    <div id="zra-category-groups">{"".join(sections)}</div>
    <div id="zra-empty" class="zra-empty" hidden><strong>No matching recommendations.</strong><span>Try a broader search or clear the active filter.</span></div>
  </section>
</div>
'''
    OUTPUT_PATH.write_text(page, encoding="utf-8")
    print(f"Rendered {len(products)} products from {CATALOG_PATH} to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
