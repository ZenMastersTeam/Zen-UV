# Version 4.1

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
<iframe src="https://www.youtube.com/embed/JZxBGPZg1ok" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
</div>
<br>

## General
- Added **Unwrap in Place** operator.
- Added the ability to **export Trims to bitmap format (PNG, BMP, TGA)**.
- Added the ability to **import Trimsheet from DECALmachine add-on**.
- **Switching from BGL module to GPU** due to the transition of Blender developers to GPU.
- Bugfixes.

### Unwrap
- Added **Unwrap in Place** operator. (UV Editor mode)
- Added ability to **Display Finished** in UV Editor.
- Added an alert to **Zen Unwrap** operator if islands tagged as **Finished** are encountered.
- Fixed a bug with **Unwrap Constraint** operator, which does not work correctly if several islands consisting of only one polygon are selected.
- Fixed a bug with **Zen Unwrap** operator when it didn't work stably in **Seam Switch** mode.

### Select
- Optimized and fixed the algorithm for determining Flipped Islands.

### Treemsheet

- Added the ability to **export Trims to bitmap format (PNG, BMP, TGA)**.
- Added the ability to **import Trimsheet from DECALmachine add-on**.
- Added an option to the **Align to Trim** operator. **Align Direction** parameter can be taken from the active trim and not from the operator.
- Added the ability to manually select a texture for Trimsheet in 3D View.
- Fixed a bug with **Keep Proportion** option in **Hotspot Mapping** operator.

### UV Checker
- Added the ability to **Display all Draw Modes** in Display panel.
- Added **UV Islands Counter** operator to get the number of Islands.
- Added **Empty Objects** operator to search for objects that do not contain polygons.
- Added **Clear Attributes** operator to clear mesh attributes used in Zen UV (Pack Excluded, Finished).
- Fixed a bug in the **Checker Texture** operator if the texture was not found on disk.

### Pack
- Added the ability to display **Pack Excluded** in UV Editor.

### Other
- **Switching from BGL module to GPU** due to the transition of Blender developers to GPU.
- Fixed a bug where launching Blender from the command line with Zen UV installed would result in a crash.
- Fixed potential bugs when switching Blender to Python 3.11.
- Fixed possible tagging of islands by Pack Excluded, Finished systems if the systems are not explicitly enabled.