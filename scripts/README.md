# ZenUV Documentation Utils

## Updating Recommended Add-ons

The page has one editable source file:
`mkdocs/data/recommended_addons.json`. Each object in `products` is one card.

To add a product, copy an existing object, change its fields, keep the affiliate
URL in the form `https://superhivemarket.com/products/<slug>?ref=1462`, and set
`image_source` to the original Superhive preview URL. Then run:

```powershell
python -m pip install Pillow  # required only when a preview must be downloaded
python scripts/build_recommended_addons.py --fetch-images
python -m mkdocs build --strict
```

For text, category, or ordering changes, omit `--fetch-images`. To remove a
card, delete its JSON object and its matching file from
`mkdocs/img/recommended_addons/`, then rebuild the page.
