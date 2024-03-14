# Version 4.3.0

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
<iframe src="https://www.youtube.com/embed/OOMVq53_mP4" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
</div>
<br>

### **General**

- Added operators for working with UDIM workflow.
- Added operators to **Display UV Borders** (Margin) and **Seams**.
- Added operators for symmetrizing UV coordinates.
- Added **Snap** and **Lock Size** operators when creating and modifying Trims.
- Optimization for UV Packmaster 3.2.
- Bug fixes.

## **Operators**

### **Advanced UV Maps**

- Added **UDIM Tools** for creating and managing UDIM tiles.
- Added **Clean UV Maps** operator to remove all inactive UV maps.
- Added **Set UV Map Name by Index** operator to rename a UV Map based on its position in the list.
- Fixed a bug with desynchronization in display of Advanced UV Maps in UV Editor and 3D View.
- Fixed a bug in Advanced UV Maps Panel when Users were added to an object.
- Fixed a bug in renaming UV Maps when an extra index of the form ".001" could be added to the name.

### **Seam Groups**

- Added **Assign/Remove Selection** operators to to add and subtract selected from the active Seam Group.

### **Unwrap**

- Added **Hide/Unhide Islands** operators for **Finished system**.
- Added **Select/Deselect Islands** operators for **Finished system**.
- Updated **Mirror Seam** operator. The algorithm and UX have been improved, new options have been added.
- Fixed a bug in **Zen Unwrap** operator if an object has no polygons or all polygons are hidden.
- Fixed a bug in **Zen Unwrap** operator when marking still occurred when Mark was Off.
- Fixed a bug in **Zen Unwrap** algorithm when objects were ignored if they had islands with **Excluded** tag.
- Fixed a bug in **Zen Unwrap** operator when, in the "nothing selected" mode, Seams are created by corner instead of unwrapped by existing Seams if the **Mark by Angle** command from the dialog was previously executed.

### **Select**

- Added **Select in Tile** operator to select Islands based on their position relative to the UDIM Tile or UV Area.
- Added S**elect Half** operator for selecting half of the mesh relative to the pivot to optimize the pipeline of symmetrical objects.

### **Transform**

- Added **Symmetrize** operator to symmetrize UVs for selected elements. 
- Added the ability to ignore non-quad Islands for **Quadrify** operator.
- Added limit on the number of initially selected edges for **Quadrify** operator. If the limit is exceeded, new seams will not be created, which previously led to operator freezes.
- Added **Move 2D Cursor to Selection**. It has also been added to UV Editor RMB menu.
- Added **Order** option for **Transform - Orient** operator to select whether to process Islands individually or all Islands as one.
- Added **Active UDIM Tile** option to **Move to UV Area** operator to move Islands to Active UDIM Tile.
- Improved **Randomize** algorithm. 
- Fixed a bug with non-square textures for **Relax** operator.
- Fixed a bug in **Unwrap Constraint** operator if the island consists of one polygon.
- Fixed a bug in **Match and Stitch** operator when working in multi-object mode.
- Fixed a bug in **Transform - Orient by Selected** operator if border edges are included in the selection.
- Fixed a bug in **Transform - Align** operator if two parallel edges are selected in UV Sync Off mode.
- Fixed a bug in **Transform - Fit** operator when it was impossible to deactivate **Keep Proportions**. 

### **TrimSheet**

- Added the ability to **Snap to Pixels, Grids, Trims** in the process of creating and modifying trims.
- Added **Lock Size** option when creating Trims. This allows you to create square shaped Trims.
- Added notification that scaling limit has been reached (the island has reached the trim boundary) for **Scale In Trim** operator.
- Fixed a bug in **Fit to Trim** operator in **Selection**, **One by One** mode where Islands were scaled to a point in the center of the Trim.
- Fixed a bug where it was impossible to exit Trim editing mode.

### **Stack**

- Added **Expand** option for **Unstack** operator in **Simple mode**.
- Fixed a bug in Stack panel UI if there are no objects in the scene.

### **Texel Density**

- Added **Global** option for **Set TD** operator to operate not only with values taken from Texel Density panel, but also with personal.
- Fixed a bug in **Set TD** operator if no islands are selected.

### **UV Checker**

- Added **Display UV Borders** operator in UV Editor and 3D View to display Pack margin size.
- Added **Display Seams** operator in UV Editor.
- Added **Select Doubled Vertices** operator for Tools.
- Improved **Reset Checker** operator taking into account restoration from previous versions of Blender.
- Improved **Zen Checker Nodes** taking into account the compatibility of old and new versions of Blender.

### **Pack**

- Added compatibility with UVPackmaster 3.2.
- Added **Hide/Unhide Islands** operators for **Excluded** system.
- Added **Select/Deselect Islands** operators for **Excluded** system.

### **Other**

- Added **Open folder** button to Examples panel.
- Added notification mechanism about the release of new Zen UV version.
- Added size optimization in **Pie Assistant** when changing the interface scale.
- Improved Gizmo buttons display algorithms when scaling the interface.
- Fixed a bug with UI in **Zen UV Combo Panel**.
- Disabled the ability to operate with **Handles in Zen Tool** in Object mode.
- Fixed a bug that led to a crash if **Sticky UV Editor** is opened from the right side.
- Disabled the ability to use Alt in combination with **Sticky UV Editor** as it is impossible from the point of view of the Blender API.
- Fixed a bug when using the native functions convex_hull and fit_box_2d.