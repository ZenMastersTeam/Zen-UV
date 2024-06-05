# Version 4.4.0

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
<iframe src="https://www.youtube.com/embed/W-m9hAitLQU" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
</div>
<br>

## **General**

- Added **Zen UV Quick Favorites Panel**.
- Added **Quadrify Selection** mode to **Quadrify** operator.
- Added new **Select** operators.
- Added operators **Split** and **Merge**.

## **Operators**

### **Advanced UV Maps**

- Fixed a bug with incorrect behavior of the **Add New UV Map** operator for **Select UV Sync - off** when projections were not created.

### **Unwrap**

- Added options for the **Mark Sharp by UV Borders** operator to ignore **Splits** (Cylinder Edges).
- Optimized the output of warning notifications for **Zen Unwrap** operator.
- Fixed a bug where **Zen Unwrap** operator settings in the panel did not have an effect on the operator.
### **Select**

- Added **Select Open Edges** operator to select edges that are clearly open or visually open (adjacent to hidden polygons).
- Added **Select Quaded Islands** operator for selecting islands consisting only of quads.
- Added **Select Seam** operator for selecting edges of **Seam** type.
- Added **Select Sharp** operator for selecting edges of **Sharp** type.
- Added operator **Select Splits** to select edges of type **Splits**, which belong to the same island, but are separated in **UV Editor** (Cylinder Edges).
- Added **Select Linked Loops** operator to select UV edges belonging to one edge in **UV Sync Selection - off** mode.
- Added operators **Face/Edge to Loops** to convert **face**, **edge** selections into **UV loops** selections.
- Added **Select Edges by Condition** operator to select edges based on several conditions. For example, select edges that are **Sharp** but are not **UV Boundary**.
- Added the ability to select borders of a specific island and borders of selected faces to the **Select Borders** operator.
### **Transform**

- Added **Split** operator to split islands into selected edges.
- Added **Merge** operator for welding UV vertices belonging to the same **mesh** vertex.
- Added the ability to display process using **Blender Annotation** for **Quadrify**, **Match and Stitch** and **Fit into Region** operators.
- Added **Select Quaded Islands**, **Select Linked Loops**, **Select UV Borders** operators for ease of use together with **Transform** operators.
- Fixed a bug in **Transform - Move** operator leading to an eternal loop if all UVs are selected and the system is in **Selection** mode.
- Fixed a bug in **Orient by Selected** operator for multi-object selection.
- Fixed a bug in **Relax** operator if the active texture was not found on disk.
  
### **TrimSheet**

- Added notification about successful Trimsheet import.
- Fixed a bug when using **Hotspot - Detect Radial**.
### **Texel Density**

- Added an operator to **UV World Size** system to determine the texture size based on the selected element on the texture using Trims. For example, for a texture with bricks, we can determine the size of the entire texture if we know the size of the brick.
- Added **UV World Size Presets**.
- Added an operator to get the size of the active texture.
- Improved and optimized **Set TD** operator interface for **Global Mode**.
- Fixed a bug in **Get UV World Size** operator for the case when the size is zero.

### **UV Checker**

- Fixed a bug with the **Select Empty Objects** operator, which did not work in Object Mode.
- Fixed a bug when a checker was not applied to objects in Edit mode, but not selected in the scene. It was also fixed when for such cases the checker enable button was not active.

### **Pack**

- Added an operator to get the size of the active texture.

### **Other**

- Added the ability to place buttons on one line for the addon main panel selector.
- Added **Python Operator Wrapper**. An operator that can be executed by another operator.
- Added an operator that can execute code written in **Python**.
- Optimized and simplified search for folder path with user scripts.
- Fixed and optimized operators using rotation transformations for non-square textures.
- Fixed a bug with the orientation of the main panel buttons not being saved in the addon properties.
- Optimized **Sticky UV Editor** - **Save and Restore** settings.
- Fixed a bug in **Sticky UV Editor** leading to a crash for **Shading Layout**.
- Fixed a bug with restoring not-default **Adjust Last Operation** value by clicking **Sticky** that caused Blender crash.
- Fixed a bug in detecting cyclic islands leading to incorrect transformation.
- Fixed a bug with obtaining values for Zen UV Tool in the **Image Editor** mode.
- Fixed tab selector for **BlenderStyle** in **Vertical** mode.
- Fixed a bug when **Pie Menu** was not called in the **UV Editor** if the object did not have any UV maps.
- Fixed abnormal behavior when transforming in a separate **UV Editor** window.
- Fixed a conflict with addons for managing **UI** and **Annotation Zen UV** panel.
