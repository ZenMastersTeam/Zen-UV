# Version 4.4.1

## **General**

- Optimization of the speed of **Quadrify** algorithm.
- Added the ability to use any project texture as a **Checker Texture**.
- Added **Topology** mode to **Mirror Seam** operator.
- Added color display of faces belonging to Trim.

## **Operators**

### **Unwrap**

- Added **Topology** mode to **Mirror Seam** operator.

### **Transform**

- Optimization of the speed of **Quadrify** algorithm.
- Added a widget for setting up **Quadrify** operator before launch.
- Added an alternative algorithm to **Quadrify** operator based on the native operator **Follow Active Quad**. This allows you to process larger meshes faster.
- Added progress bar with the ability to cancel an operation for **Quadrify** operator.

### **Trimsheet**

- Added **Inset** property to **Hotspot Mapping** operator to set the margin when placing the island in Trim.
- Added **Add Trim UDIM** operator for creating trims in UDIM Tiles positions.
- Added the ability to show that polygons belong specifically to a trim by coloring them.
- Added **UV Area** notification when using **Zen Tool** in 3D Viewport if there is no active texture or the texture does not contain trims.
- Added **Select Trim by Eyedropper** operator for selecting the active trim using eyedropper.

### **Stack**

- Added a mode to **Unstack** operator in which islands located outside the UV Area will be processed.
- Added the ability to identify islands by seams to **Unstack** operator. This allows you to avoid a situation where stacked islands are welded if they have common mesh vertices.

### **Checker Texture** 

- Added **Set Viewport Display Mode** operator to the **Tools** section for group setting of object display properties.
- Added **Update Draw System** button in the **Display** section for forced redrawing.
-  Added a warning if the mesh properties are set to a display type other than Texture.
- Added the ability to use any project texture as a **Checker Texture**.

### **Other**

- Added an operator for moving islands to a UDIM tile by specifying the destination tile with the mouse cursor.