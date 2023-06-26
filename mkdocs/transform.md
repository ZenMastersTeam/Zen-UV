# Transform System

This panel contains tools to transform UVs.

!!! Panel
    ![Transform](img/screen/transform/tr_main_panel.png)

!!! Tip
    ![Transform](img/screen/transform/tr_main_panel_uv_editor.png)

    UV Editor panel contains extra operator [**Reshape Islands. Click to read full information**](operators/reshape_island.md).


---
## Independent Transform Operators

### Relax ![](img/icons/relax-1_32.png)

Allows to reduce the stretching the faces of the island. Uses three algorithms.

!!! Panel
    ![](img/screen/transform/relax.png)
     - **Zen Relax**. The algorithm is most suitable for organic objects.
     - **Angle Based**. Blender's native algorithm. Most suitable for the hard surfaces objects.
     - **Conformal**. Blender's native algorithm. Same as **Angle Based**, but much faster. However, can lead to undesired results if the island is complicated.

### World Orient.

Rotate Islands the way they are oriented on the Models. Each method (Organic/Hard Surface) uses a heuristic approach and correctly orients most of the Islands in its area.

!!! Panel
     ![](img/screen/transform/world_orient_props.png)

     - **Method: Hard Surface / Organic**. The orientation method is suitable for geometry types.
     - **Further orient**. Additional turn. Allows you to turn the island to a horizontal or vertical if the island is located at an angle in the model.
     - **Flip By Axis**. Allow changing direction of the island after basic orientation. Suitable if needed change orientation from legs to head for example.

### Randomize.
  Randomize the position, rotation, and scale of the islands or selected vertices.

!!! Panel
     ![](img/screen/transform/randomize.png)

### Quadrify Islands ![](img/icons/quadrify_32.png)

Straighten rectangular-shaped Islands.

![Quadrify_Example](img/gifs/trasnform_operators/Quadrify_Example.gif)

!!! Preferences

       ![quadrify_op_props](img/screen/transform/quadrify_op_props.png)

    - **By selected Edges**. Selected Edges will be used and marked as Seams during Quadrify Islands operation. Works only in edge selection mode.
    ![Quadrify_SelectedEdge](img/gifs/trasnform_operators/Quadrify_SelectedEdge.gif) 
    - **Mark Borders**. Mark borders as seams/sharp after Quadrify Island operation.
    - **Mark Seams**. Mark seam in case **Mark Borders** is on.
    - **Mark Sharp**. Mark sharp in case **Mark Borders** is on.
    - **Orient to**. How to orient Quadrified Islands.
        - **Initial**. Leave orientation as is.
        - **Vertical**. Set orientation vertical.
        - **Horizontal**. Set orientation horizontal. 
        ![Quadrify_Orient](img/gifs/trasnform_operators/Quadrify_Orient.gif) 

    - **Average Texel Density**. Averaging the size for the processed islands.
    - **Pack Quadrified**. Pack Islands after Quadrify Islands operation.
    - **Pin Quadrified**. Pin Islands after Quadrify Islands operation.
     ![Quadrify_Pack_Pin](img/gifs/trasnform_operators/Quadrify_Pack_Pin.gif)
    - **Tag as Finished**. Tag Quadrified islands as finished.

!!! tip
    Tag Quadrified Islands as [**Finished**](unwrap.md#finishing-system) to preserve them from unwrapping. It's recommended to [**Tag as Finished**](unwrap.md#tag-finished) all manually changed Islands.
    ![](img/gifs/trasnform_operators/Quadrify_Tag_Finished.gif)

### Reshape Island

Changes the island’s shape depending on the preset. [Here is full information](operators/reshape_island.md) about Reshape Island.


!!! Panel
    ![](img/screen/transform/reshape_presets_collected.png)

    - **Selected**. Straighten the selected Edge Loops and relax not selected vertices.
    - **U Direction / V Direction**. Edges is aligned in the indicated direction.
    - **Borders**. Straighten the edges of the island in even lines according to the given parameters.

### Match and Stitch

Matching the position, rotation, and scale of Islands. Stitch the vertices together, if possible.

!!! Panel
    ![](img/screen/transform/match_and_stitch_pref.png)

!!! tip
    Watch the video explaining how **Match and Stitch** works.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/f9meGzMGx2k?start=974&end=1061" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div>

---

## Unified Transform System

!!! Panel
    ![](img/screen/transform/tr_un_tr_sys.png)

### Universal Control Panel

!!! Control
    **Universal Control Panel**

    ![Transform](img/screen/transform/UniversalControl.png)

    The universal control panel has logic and different functions for different types of transformation.

---

### Transform Space

Switch between Islands and Texure-based transforms in 3D View.

!!! Panel
    
    ![](img/screen/transform/tr_space.png)

    - **Island**. Islands-based transforms.
    - **Texture**. Texure-based transforms. Works only for **Move** and **Rotate** tools.

### Mode

!!! Panel
    
    ![](img/screen/transform/tr_un_mode.png)

    - **Islands**. Transformations will affect Islands.
    - **Selection**. Transformation will affect Selection (Faces, Edges, Vertices).

### Order

!!! Panel

    ![](img/screen/transform/tr_un_order.png)
    - **One by one**. Transformations will affect Islands.
    - **Overall**. Transformation will affect Selection (Faces, Edges, Vertices).
    - **System Pivot**. Transformations will affect Islands.

---
## Transform Types

### Move ![](img/icons/transform-move.png)

Move Selected Islands

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Move** represent the direction of shifting.

![Transform](img/screen/transform/MainPanelMove.png)

#### Move Increment

The value on which the island will be shifted.

---

### Scale ![](img/icons/transform-scale.png)

Scale selected Islands.

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Scale** represent Points from where the island will be scaled.

![Transform](img/screen/transform/tr_scale.png)

#### Scale Mode


!!! Axis
    ![](img/screen/transform/tr_scale_mode_axis.png)

    - **Scale**. The value of the scale of the island for each of the axes.
    - **Tuner**. System that helps change values quickly.
         - **"D".** Increase by two times.
         - **"H".** Decrease two times.
         - **"R".** Reset value to 1.0 .
         - **Lock.** - The Lock mode allows changing values as one.

!!! Units
    ![](img/screen/transform/tr_scale_mode_units.png)

     - **UV Size**. The estimated width of the UV area.
     - **Desired size**. The size of which should be set for selected elements relative to UV area.
     - **G**. Grab desired size from current selection. Exist only in the 3D Viewort context. Can be used only for 2 vertices or for one edge selection.
     - **Horizontal / Vertical**. What mean the Desired Size.

---
### Rotate ![](img/icons/transform-rotate.png)

Rotate selected Islands.

!!! Info

    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Scale** works as described. Buttons located in the corners rotate the island in the specified direction.

    The central button performs the automatic aligning of the island horizontally or vertically. The buttons at the top and bottom align the island vertically. Buttons on the left and right align the island horizontally.

![Transform](img/screen/transform/Rotate.png)

#### Rotate Increment

The value on which the island will be rotated.

#### Orient by selected

Reorient the island by selected elements (vertices, edges, polygons).

---
### Flip ![](img/icons/transform-flip.png)

Flip Selected Islands.

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Flip** represent flip direction.

![Transform](img/screen/transform/Flip.png)

---
### Fit ![](img/icons/transform-fit.png)

Fit Island to UV Square.

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Fit** represent origins from where **Fit** will be performed.

![Transform](img/screen/transform/Fit.png)

#### Face by Face

Fit Face by Face.

#### Fill Islands

Fit Islands from Center without keeping proportions.

#### Padding

Clearance between island and UV Square bounds.

#### Bounds

It makes it possible to fill out not UV Square but any other area.

### Fit into Region

!!! Panel
    ![](img/screen/transform/fit_into_region.png)

    - **Grab Region: Selection / Island**. Allow to grab Region size in different manners.
    - **Bottom Left: Top Right:**. The bounding box of the region.
    - **Fit into Region**. Fit selected island in to the Region described in the bounding box.

---

### Align ![](img/icons/transform-orient.png)

Align selected Islands.

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **Align** represent the side by which the islands will be aligned.

![Transform](img/screen/transform/Align.png)

#### Vertex by Vertex
Mode for Vertex Alignment.

#### Center by Axis
Align selected Islands Horizontally or Vertically in Center.

#### Align to

- **Selection Bounding Box**.
- **UV Area Bounds**. 
- **Position**.
- **2D Cursor**.
- **To Active Component**.
---

### Distribute ![](img/icons/transform-distribute.png)

Distribute, Sort and Arrange selected Islands.

![Transform](img/screen/transform/Distribute.png)

#### Islands Mode

 - **Distribute & Sort**. Distributes and Sorts selected Islands.
 - **Arrange**. Arrange selected Islands.

#### Selection Mode

 - **Distribute**. Distribute vertices along the line.

---

### 2D Cursor ![](img/icons/transform-cursor.png)

Align 2D Cursor over the selected island. 

!!! Info
    Buttons of the [**Universal Control Panel**](#universal-control-panel) in the Transform type **2D Cursor** represent sides of the island or selected elements.

![Transform](img/screen/transform/2dCursor.png)


!!! tip
    Don't forget to drink some good beer today!

---

## Advanced Transforms

Advanced Transforms panel represents transforms without **Universal Control Panel**.
Recommended to use if you want to add shortcuts for transform operations. 

!!! Panel
    ![Advanced Transforms](img/screen/transform/tr_advanced_transforms.png)

### Move ![](img/icons/transform-move.png)

#### By Increment
Move Islands by Increment.

#### To the Active Trim
Move Islands to the Active Trim.

#### To Position
Move Islands to Position.

#### To 2D Cursor
Move Islands to 2D Cursor.

#### To Mouse Cursor
Move Islands to Mouse Cursor.

#### To UV Area
Move Islands to UV Area.

---

### Scale ![](img/icons/transform-scale.png)

#### By Axis
Scale Islands by Axis.

#### By Units
Scale Islands by Units.

---

### Rotate ![](img/icons/transform-rotate.png)

#### By Angle
Rotate Islands by Angle.

#### By Increment
Rotate Islands by Increment.

#### Orient by Bounding Box
Orient Islands to Bounding Box.

#### Orient by Selection
Orient Islands by Selection.

---

### Flip ![](img/icons/transform-flip.png)

#### Horizontal
Flip Islands Horizontally.

#### Vertical
Flip Islands Vertically.

---

### Fit ![](img/icons/transform-fit.png)

#### To UV Area
Fit Islands to UV Area.

#### To Region
Fit Islands to Region.

---

### Align ![](img/icons/transform-orient.png)

#### To Selected BBox
Align Islands to Selected BBox.

#### To Position
Align Islands to Position.

#### To 2D Cursor
Align Islands to 2D Cursor.

#### To UV Area
Align Islands to UV Area.

#### To Active Component

Align Islands to Active Component.