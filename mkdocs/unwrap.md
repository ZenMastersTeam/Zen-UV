# Unwrap

!!! Panel
     | 3D Viewport | UV Editor| 
     |---|---|  
     | ![](img/screen/unwrap/unwrapMainPanel.png) |![](img/screen/unwrap/unwrapMainPanel_uvedtior.png)| 

## Zen Unwrap ![Zen Unwrap](img/icons/zen-unwrap@2x.png)

Magic button to Mark (Seams, Sharp), Set TD, Pack and Sort processed Islands. Zen Unwrap is a context-dependent operator and result of its operation depends on what was selected at the time it was run. 

---

### Basic rules:

- The operator does not work in the **UV Sync Selection Off** mode of the **UV Editor**.
- The properties of the operator show the current selection mode. It matches Blender's selection mode.
- Use only a single mesh selection Mode (Vert, Edge or Face). Multiple Selection Modes will not work (Vert + Edge, etc.).
- The operator works the same way in the **UV Editor** and in the **3D Viewport**.
- Zen Unwrap always operates on islands in the active UV Map.
- If the marking is disabled in the operator, the division into islands will still occur. Seams will remain and lead to desync of what is happening in **UV Editor** and **3D Viewport**.

!!! tip
    Zen Unwrap will ignore existing UV Borders if they are not marked as Seams.
    
    - To mark them use [**Seams by UV Borders**](#seams-by-uv-borders) operator.
    - To save not only UV Borders but Islands [**Tag Finished**](#tag-finished) operator. 
  
---

### Processing Mode
The main operating mode switch.

!!!Panel
    ![Processing Mode](img/screen/unwrap/zwrp_processing_mode.png)

    - **Whole Mesh**. The processing will be done for the whole mesh. All already unwrapped islands will be re-unwrapped.
    - **Selected Only**. Processing will only be performed on the mesh selection.
    - **Seam Switch**. This mode will switch seams with subsequent unwrapping. Only selected edges with seams will be included in the switching process. The seams that are in the selection will be deleted (Unmarked). New seams will be assigned according to the selection mode (Face, Edge).
    - **Unfold Vertices**. In this case, regardless of the Select Mode, any selection will be treated as vertices. Selected vertices will be relaxed.

---

### The behavior of the operator if nothing is selected:

For using this just make sure you have no selection and press the Zen Unwrap button.

- If nothing is selected, the operator assumes that you want to unwrap the whole mesh. This mode can be used if you have already marked seams in some way and just want to unfold islands.
- When you start the operator, it may already be in **Processing Mode - Selected Only**. In this case, you will get a warning that the entire meshes will be unwrapped. If this suits you - confirm your action by pressing Ok.

![Zen Unwrap Nothing Selected](img/screen/unwrap/zwrp_no_selection_popup.png)

- In case you have no marked seams and nothing selected, the operator will offer options for creating seams. Select the one you want.

![Zen Unwrap Nothing Selected](img/screen/unwrap/zwrp_if_no_seams_popup.png)

![Zen Unwrap Nothing Selected Mode](img/gifs/zuwrp_operator/zwrp_no_sel_mode.gif)

---

### The behavior of the operator if something is selected:

The main modes of operation are **Face** and **Edge**. Vertex mode is used as an auxiliary mode.

#### Face selection mode.

![Zen Unwrap Face Mode](img/gifs/zuwrp_operator/zwrp_faces_mode.gif)

This mode will create seams around the selected polygons. The entire mesh will be unwrapped based on the existing (and newly added) seams, depending on the **Processing Mode**. In fact, you will create a new island from the selected polygons.

#### Edge Selection Mode.

In this mode, all selected edges will be marked as seams and then the mesh will be unwrapped.

![Zen Unwrap Edge Mode](img/gifs/zuwrp_operator/zwrp_edges_mode.gif)

#### Vertex selection mode.

Working in **Face** or **Edge** mode makes changes to the selected islands anyway. If you need to unwrap an island without adding seams or splittings it, use **Vertex** selection mode. You can select only one vertex or several. This will tell the operator which island you want to work with. It is most convenient to use this mode together with the **Processing Mode - Selected Only**.

![Zen Unwrap Vertex Mode](img/gifs/zuwrp_operator/zwrp_vertex_mode.gif)

---

### Settings

!!! Preferences
    ![Zen Unwrap Settings](img/screen/unwrap/zwrp_op_prop.png)
    
    - **Unwrap Method**. Unwrapping method.
        - **Conformal**. Fast algorithm that gives good results.
        - **Angle-Based**. More accurate algorithm, but a bit slower.
    - **Mark Settings**. Operator settings to enable automatic seam marking. See [Mark Settings (Global Mode)](#mark-by-angle) for details.
    - **Fill Holes**. Virtual fill holes in mesh before unwrapping, to avoid overlaps and preserve symmetry.
    - **Texel Density**. Sets Texel Density. Works only if Pack Unwrapped option is disabled.
        - **Skip**. Do not make any texel density corrections.
        - **Global Preset.** Set value described in Texel Density panel as Global TD Preset. 
        - **Averaged**. Sets the averaged Texel Density for newly created islands. This keeps all islands about the same size as you work. 
    - **Pack Unwrapped**. After the islands have been created, this option will start the **Packing** process of the islands. The [**Pack Engine**](pack.md/#pack-engine) specified in the **Pack System** will be used.
    - **Sort Unwrapped**. After the islands have been created, this option will start the process of **Sorting** the islands by [**Finished**](#finishing-system) tag.
  
### Additional Options

You can change main Zen Unwrap settings before running the operator.  

!!!Panel
    ![Auto UV Sync](img/screen/unwrap/zwrp_auto_uv_sync.png)

    - **Auto UV Sync**. Automatically enables the **UV Sync Selection** mode every time the operator starts.
    - **Processing Mode**. The main operating mode switch.
    - **Pack Unwrapped**. After the islands have been created, this option will start the **Packing** process of the islands. The [**Pack Engine**](pack.md/#pack-engine) specified in the **Pack System** will be used.
    - **Sort Unwrapped**. After the islands have been created, this option will start the process of **Sorting** the islands by [**Finished**](#finishing-system) tag.
---


## Unwrap Constraint

This operator unwraps Islands and Faces along selected axis.

!!! Preferences
    ![](img/screen/unwrap/unwrap_constraint_settings.png)

    - **Mode**. Choose what to unwrap Islands or Faces.
         - **Islands**. Affect selected Islands.
         - **Faces**. Affect selected Faces only.
    - **Method**. Unwrap method.
         - **Full Unwrap**. Unwrap Islands but keep it in BBox boundaries.
         - **Along Axis**. Unwrap Islands along Axis.
    - **Fit Axis**.
         - **U**. Unwrap / Fit along U axis.
         - **V**. Unwrap / Fit along V axis.
         - **Min**. The minimum length axis will be automatically determined.
         - **Max**. The maximum length axis will be automatically determined.
    - **Current Axis**. Current Axis.
    - **Mark Settings**. Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.
    - **Fill Holes**. Virtual fill holes in meshes before unwrapping.
    - **Correct Aspect**. Map UVs taking image aspect ratio into account.
    - **Use Subsurf Modifier**. Map UVs taking vertex position after subsurf into account.

## Unwrap Inplace

Unwrap Islands and Faces keeping their Size, Orientation and Location in UV Space.

!!! Preferences
    ![](img/screen/unwrap/unwrap_inplace_settings.png)

    - **Mode**. Choose what to unwrap Islands or Faces.
         - **Islands**. Affect selected Islands.
         - **Faces**. Affect selected Faces only.
    - **Location**. Restore Islands Location and gabarit.
    - **Orientation**. What Orientation to use after unwrapping.
         - **Keep**. Use Initial Orientation. 
         - **World Orient**. Use World Orientation for the Islands.
         - **Skip**. Skip Orientation adjustments.
    - **Size**. Restore Islands Size.
    - **Ignore Pins**. Ignore Pins.
    - **Fill Holes**. Virtual fill holes in meshes before unwrapping.
    - **Correct Aspect**. Map UVs taking image aspect ratio into account.
    - **Use Subsurf Modifier**. Map UVs taking vertex position after subsurf into account.

!!! Note
    Available only in UV Editor.

---
## Mark System
!!! Panel
    ![](img/screen/unwrap/unwrap_mark_section.png)

### Mark by Angle

Mark edges as Seams and/or Sharp edges by Angle.

!!! Global Mark Settings
    ![](img/screen/unwrap/mark_by_angle_prefs.png)

    - **Use Global Mark Settings**. In this mode, all the operators from the Mark System use the settings below. If off, every operator uses its own settings.
    - **Mark Seams**. Automatically assign Seams
    - **Mark Sharp Edges**. Automatically assign Sharp edges

!!! Preferences
    ![](img/screen/unwrap/mark_by_angle_settings.png)

    - **Keep init marks**. Keep the state of intital Seams and Sharp edges.
    - **Selection Respect**. Mark only within current selection.
    - **Mark Settings**. Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

### Mark ![Mark Seams](img/icons/mark-seams@2x.png)

Mark selected edges or face borders as Seams and/or Sharp edges.

!!! Preferences
    ![](img/screen/unwrap/mark_mark_pref.png)

    - **Clear**. Clear marking inside of selected Faces.
    - **Mark Settings**. Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

### Unmark ![Unmark Seams](img/icons/unmark-seams@2x.png)

Unmark selected edges or face borders as Seams and/or Sharp edges.

!!! Preferences
    ![](img/screen/unwrap/mark_unmark_pref.png)

    - **Mark Settings**. Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

### Unmark All

Remove all the Seams and/or Sharp edges from the mesh.

!!! Preferences
    ![](img/screen/unwrap/mark_unmark_all_pref.png)

    - **Clear Pinned**. Clear all the Pins.
    - **Mark Settings**. Mark Settings (Global and Local modes) to Mark Seams and Sharp Edges.

## Conversion System
!!! Panel
    ![](img/screen/unwrap/conversion_system.png)

### Seams by UV Borders
Mark Seams by existing UV Borders.
### Sharp by UV Borders
Mark Sharp by existing UV Borders.
### Seams by Sharp Edges
Mark Seams by existing Sharp edges.
### Sharp Edges by Seams
Mark Sharp edges by existing Seams.
### Seams by Open Edges
Mark Seams by Open Edges. The way that looks in the viewport.

## Mirror Seams

Mirror Seams along selected Axis (`X`,`Y`,`Z`) in a given direction (`+` or `-`). 

![](img/screen/unwrap/unwrap_mirror_1.gif)

Instead of **Replacing** existing marked Seams you can **Add** them.

![](img/screen/unwrap/unwrap_mirror_2.gif)

Holding `Shift` you can select both directions and flip Seams along the selected Axis and direction.

![](img/screen/unwrap/unwrap_mirror_3.gif)

## Smooth by Sharp (Toggle)
Toggle between Auto Smooth 180° (with sharp edges) and regular smooth modes.

--- 

## Finishing System

Finishing system helps to Mark, Sort and Display Islands that you have already unwrapped. It can be used to check the progress of unwrapping as well as prevent Finished Islands from accidental Unwraping.

!!! Panel
    ![](img/screen/unwrap/finished_system.png)

### Sort Islands by Tags
Finished Islands move to the right side from Main UV Tile, Unfinished — to the left.

![](img/screen/unwrap/unwrap_finished_sort.gif)

### Tag Finished

Tag Islands as Finished and move them to the right sied from main UV Tile. These Islands won't be unwrapped.

![](img/screen/unwrap/unwrap_finished_tag.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_tag.gif)


!!! Warning
    Islands tagged as Finished are locked for Unwrapping. To unlock them use **Tag Unfinished** operator.

![](img/screen/unwrap/unwrap_finished_lockunwrap.gif)

### Tag Unfinished

Tag Islands as Unfinished and move them to the left sied from main UV Tile. 

![](img/screen/unwrap/unwrap_finished_untag.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_untag.gif)


### Select Finished

Select Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_select.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_select.gif)

### Deselect Finished

Deselect Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_deselect.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_deselect.gif)

### Hide

Hide Islands tagged as Finished.

![](img/screen/unwrap/unwrap_finished_hide.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview_hide.gif)

### Unhide

Unhide Islands tagged as Finished.

### Display Finished (Toggle)

Display Finished/Unfinished Islands in the viewport.

![](img/screen/unwrap/unwrap_finished_display.gif)

![](img/screen/unwrap/unwrap_finished_display_3dview.gif)

!!! Preferences
    ![Unwrap](img/screen/unwrap/finishing_prefs.png)

    - **Pin Finished**. Pin Islands after Tag Finished operation.
    - **Auto Sort Islands**. Automatically Sort Islands by Tags. Finished Islands move to the right side from Main UV Tile, Unfinished — to the left
    - **Auto Update Draw**. Update draw cache every time when mesh is changed.
    - **Finished Color**. Finished Islands viewport display color.
    - **Unfinished Color**. Unfinished Islands viewport display color.