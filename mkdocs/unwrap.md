# Unwrap

!!! Panel
     | 3D Viewport | UV Editor| 
     |---|---|  
     | ![3D Viewport Panel](img/screen/unwrap/unwrap_panel_3d.png) | ![UV Editor Panel](img/screen/unwrap/unwrap_panel_uv.png) | 

---
### Global Mark Settings

Controls global edge-marking behavior across all operators in the Mark System.

Enabling global settings provides centralized control over edge flags, ensuring tools throughout the Mark System apply Seams and Sharp edges consistently without needing to adjust settings on individual operators.

| ![Global Mark Settings](img/screen/unwrap/unwrap_global_mark_settings.png) |
| :---: |
| *Fig. 1. Global Mark Settings menu* |

- **Use Global Mark Settings** — Overrides individual tool settings with these global defaults. When disabled, each Mark System operator uses its own independent configuration.
- **Mark Seams** — Automatically marks target edges as UV Seams during marking operations.
- **Mark Sharp Edges** — Automatically marks target edges as Sharp Edges during marking operations.

---
## Unwrap Inplace

Unwrap Islands and Faces keeping their Size, Orientation and Location in UV Space.

!!! Properties
    ![](img/screen/unwrap/unwrap_inplace_settings.png)

- **Mode** - Choose what to unwrap Islands or Faces.
    - *Islands* - Affect selected Islands.
    - *Faces* - Affect selected Faces only.
- **Location** - Restore Islands Location and gabarit.
- **Orientation** - What Orientation to use after unwrapping.
    - *Keep* - Preserve initial orientation. 
    - *World Orient* - Aligns UV to match their world orientation.
    - *Skip* - Leaves the orientation of UV unchanged, without any adjustment after Unwrap.
- **Size** - Preserve initial size.
    - *Keep* - UV Island size will be adjusted by initial width or height depending with the Orientation results.
    - *Global Preset* - Set value described in the Texel Density panel as [Global TD Preset](texel_density.md/#global-td-preset).
    - *Skip* - Leaves the size of UV unchanged, without any adjustment after Unwrap.
- **Ignore Pins** - Ignore Pins.
- **Fill Holes** - Virtual fill holes in meshes before unwrapping.
- **Correct Aspect** - Map UVs taking image aspect ratio into account.
- **Use Subsurf Modifier** - Map UVs taking vertex position after subsurf into account.

!!! Note
    Available only in UV Editor.

---

## Prepare Unwrap

Prepares the object for unwrapping. Remove all UV maps, seams, sharp edges, and finished UV marks.
Apply all geometry modifications before resetting for a clean unwrap

![Prepare Unwrap operator properties](img/screen/unwrap/prepare_unwrap_op_prop.png)

- **UV Maps** - Choose how to prepare the UV maps.
    - *Remove All* - Remove all existing UV maps from the mesh before preparing for a new unwrap.
    - *Iso Projection* - Create a default UV isometric unwrap projection for the active mesh.
    - *Skip* - Skip editing UV maps.
- **Clear Seams** - Remove all marked UV seams from mesh edges before preparing for a new unwrap.
- **Clear Sharps** - Remove all sharp edge markings from the mesh before preparing for a new unwrap.
- **Tag Unfinished** - Remove all finished island marks and tag the mesh as unfinished for a fresh unwrap

!!! Note
    The **Apply Scale** and **Apply Modifiers** options may destroy animation data. A warning is shown in the operator properties.

---

!!! Warning
    Applying Geometry options (Scale / Modifiers)
    may break rigs, constraints, or animations.

- **Apply Scale** - Apply object scale transformations before preparing the mesh for UV unwrapping.
- **Apply Modifiers** - Apply all geometry modifiers to the mesh before preparing for UV unwrapping.
---

- **Display Seams** - Display UV unwrapping seams and switch off all other overlays (Crease, Sharp, Bevel).
- **UV Checker** - Enable a UV checker texture overlay to visually inspect UV layout quality during unwrapping.
- **Darken Image** - Darken the UV checker or background image overlay to improve contrast during inspection.


---
## Mark System
!!! Panel
    ![](img/screen/unwrap/unwrap_mark_section.png)

---
### Mark by Angle

Mark edges as Seams and/or Sharp edges by Angle.

!!! Tip
    This operator supports the ability to [save default properties](user_interface.md/#save-as-default-operator-properties).

!!! Properties
    ![](img/screen/unwrap/mark_by_angle_settings.png)

- **Keep init marks** - Keep the state of intital Seams and Sharp edges.
- **Selection Respect** - Mark only within current selection.
- **Mark Settings** - Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.
---
### Mark ![Mark Seams](img/icons/mark-seams@2x.png)

Mark selected edges or face borders as Seams and/or Sharp edges.

!!! Properties
    ![](img/screen/unwrap/mark_mark_pref.png)

- **Clear** - Clear marking inside of selected Faces.
- **Mark Settings** - Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

---
### Unmark ![Unmark Seams](img/icons/unmark-seams@2x.png)

Unmark selected edges or face borders as Seams and/or Sharp edges.

!!! Properties
    ![](img/screen/unwrap/mark_unmark_pref.png)

- **Mark Settings** - Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

---
### Unmark All

Remove all the Seams and/or Sharp edges from the mesh.

!!! Properties
    ![](img/screen/unwrap/mark_unmark_all_pref.png)

- **Clear Pinned** - Clear all the Pins.
- **Mark Settings** - Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

---
## Conversion System
!!! Panel
    ![](img/screen/unwrap/conversion_system.png)

- **Seams by UV Borders** - Mark Seams by existing UV Borders.
- **Sharp by UV Borders** - Mark Sharp by existing UV Borders.
- **Seams by Sharp Edges** - Mark Seams by existing Sharp edges.
- **Sharp Edges by Seams** - Mark Sharp edges by existing Seams.
- **Seams by Open Edges** - Mark Seams by Open Edges. The way that looks in the viewport.

---
## Mirror Seams

Mirror Seams along selected Axis (`X`,`Y`,`Z`) in a given direction (`+` or `-`). If the source side has no seams, the operator will halt without performing any actions to prevent the loss of adjusted seams.

![](img/screen/unwrap/unwrap_mirror_1.gif)

Instead of **Replacing** existing marked Seams you can **Add** them.

![](img/screen/unwrap/unwrap_mirror_2.gif)

Holding `Shift` you can select both directions and flip Seams along the selected Axis and direction.

![](img/screen/unwrap/unwrap_mirror_3.gif)

---
## Auto Seams & Unwrap

Partitions mesh geometry into logical topological charts based on surface planarity, automatically places UV seams along chart boundaries, and optionally unwraps the resulting UV islands in a single pass.

This operator provides an automated unwrapping pipeline suitable for both organic meshes and hard-surface models, eliminating manual seam placement while minimizing UV area distortion and preventing micro-island fragmentation.

!!! Properties
    ![Auto Seams & Unwrap Operator Properties](img/screen/unwrap/auto_seams_op_prop.png)

- **Mode** — Quick presets tailored for standard surface workflows:
    - *Hard Surface* — Sets **Quality** to `0.5` and **Hard Edge Angle** to `30°` for mechanical objects and hard-surface models with bevels.
    - *Organic* — Sets **Quality** to `0.32` and **Hard Edge Angle** to `0°` (disabled) for character models, creatures, and smooth organic surfaces.
    - *Custom* — Switches to manual control, allowing custom property adjustments.
- **Hard Edge Angle** — Angle threshold at which sharp edges are strictly marked as UV seams. Setting this to `0°` disables hard-edge seam splitting for organic geometry.
- **Quality** — Controls chart merging aggressiveness:
    - *Lower values* — Produce more UV islands with sharper, highly accurate topological boundaries.
    - *Higher values* — Merge charts more aggressively, producing fewer total islands at the expense of higher UV stretch.
- **Boundary Smoothing** — Aggressiveness of chart boundary contour smoothing after region merging. Helps create cleaner, less jagged UV seam lines.
- **Min Island Faces** — Minimum face count required for an island. Smaller chart fragments are absorbed into surrounding neighbor charts before seam generation to prevent micro-islands.
- **Unwrap** — Enables automatic execution of the standard UV Unwrap pass immediately after seams are placed.
- **UV Unwrap Panel** — Embedded Blender UV Unwrap settings (e.g., **Method**, **Margin**, **Correct Aspect**, **Iterations**) applied when **Unwrap** is active.

---
## Smooth by Sharp
Before Blender v 4.1.0 - Toggle between Auto Smooth 180° (with sharp edges) and regular smooth modes

Since Blender v 4.1.0: - Sets the "Shade Smooth" mode for all the mesh faces

For more details, refer to the ["Emergency Light Tutorial"](tutorial/emergency_light/emergency_light_eng.md#set-sharp-edges).


--- 

## Finishing System

Finishing system helps to Mark, Sort and Display Islands that you have already unwrapped. It can be used to check the progress of unwrapping as well as prevent Finished Islands from accidental Unwraping.

!!! Panel
    ![](img/screen/unwrap/finished_system.png)

---
### Sort Islands by Tags

Finished Islands move to the right side from Main UV Tile, Unfinished — to the left.

!!! Properties
    ![sort islands by tags properties](img/screen/unwrap/unwrap_finished_sorting_props.png)

- **Move Finished** - Determines whether to move islands marked as Finished
- **Move Unfinished** - Determines whether to move islands marked as Finished

|![](img/screen/unwrap/unwrap_finished_sort.gif)|
|---|
|Sot Islands by Tags|

---
### Tag Finished

Tag Islands as Finished and move them to the right sied from main UV Tile. These Islands won't be unwrapped.

![](img/screen/unwrap/unwrap_finished_tag.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_tag.gif)


!!! Warning
    Islands tagged as Finished are locked for Unwrapping. To unlock them use **Tag Unfinished** operator.

![](img/screen/unwrap/unwrap_finished_lockunwrap.gif)

---
### Tag Unfinished

Tag Islands as Unfinished and move them to the left sied from main UV Tile. 

![](img/screen/unwrap/unwrap_finished_untag.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_untag.gif)

---
### Select Finished

Select Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_select.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_select.gif)

---
### Deselect Finished

Deselect Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_deselect.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_deselect.gif)

---
### Hide

Hide Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_hide.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_hide.gif)

---
### Unhide

Unhide Islands tagged as Finished.

---
### Display Finished (Toggle)

Display Finished/Unfinished Islands in the viewport.

![](img/screen/unwrap/unwrap_finished_display.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview.gif)

---
### Finished preferences

!!! Properties
    ![Unwrap](img/screen/unwrap/finishing_prefs.png)

- **Pin Finished** - Pin Islands after Tag Finished operation.
- **Auto Sort Islands** - Automatically Sort Islands by Tags. Finished Islands move to the right side from Main UV Tile, Unfinished — to the left
- **Auto Update Draw** - Update draw cache every time when mesh is changed.
- **Finished Color** - Finished Islands viewport display color.
- **Unfinished Color** - Unfinished Islands viewport display color.