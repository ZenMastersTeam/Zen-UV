# Version 5.0.0

## **General**

- Added **Zen UV Touch Tool** for performing basic transformations in UV Editor.
- Added **Auto Unwrap Operator** operator that represents a bridge for the Ministry of flat Auto unwrap application.
- Added **Zen Sync** operator for switching UV Sync Selection while keeping the selection between modes.

## **Operators**

### **Select**

- Added **Zen Sync** operator for switching UV Sync Selection while keeping the selection between modes.
- Added **Select Faces By Normal** operator to select polygons by reference normal.
- Added **Filter Islands by Property** operator to sort and select islands by height, width, and aspect ratio.
- Added **Select Self-Intersecting Faces** operator to select polygons that intersect with themselves.
- Added **Select Stretched Faces** operator to select polygons that are distorted in UV compared to 3D view.
- Updated **Select** panel. Grouping of operators has been changed.

### **Unwrap**

- Added **Auto Unwrap Operator** operator that represents a bridge for the Ministry of flat Auto unwrap application.
- Added **Minimum Stretch** algorithm to **Zen Unwrap** and other operators using native Unwrap.
- Updated the algorithm of marking seams for **Quadrify** operator. Now seams are added only for the processed island and not for the whole mesh.
- Optimized the algorithm for **Quadrify** operator by reducing operations with sampling. This significantly increased performance, which is especially noticeable for big meshes.
- Fixed a bug in **Zen Unwrap** operator when it is in Selection Only mode and nothing is selected and a warning dialog is cycling.

### **Transform**

- Updated the algorithm for **World Orient** operator. Now it works more accurately and does not require selecting the island type (Hard Surface, Organic).

### **Checker**

- Updated the logic for **Checker Texture Toggle** operator. Now it uses keys to enable checker, disable checker and toggle checker. This does not affect the work in UI, but adds convenience when using the operator in scripts.

### **Trimsheet**

- Added **Normal** (normal vector) and **World Position** (position Vector) properties for Trim to sort islands based on their location in 3D space.
- Added **Directional Hotspot** operator to distribute islands into trims based on the direction of the normal.
- Added **Get Normal** operator to get the normal from the selected polygon and set it to the Normal property of the active trim.
- Updated **Add Trim** operator, it now always runs with default settings. This helps to avoid freezing situation in case of generation of several trims.
- Fixed a bug in the Trim packing process.

### **Texel Density**

- Added a **Set TD** operator to each line of the Texel Density preset list.

## **Other**

- Optimized display of **Favorites** properties.