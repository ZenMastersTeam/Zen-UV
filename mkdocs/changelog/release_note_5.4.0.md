# Version 5.4.0

## **General**

- New Stack System.
- Pack Outside Trims.
- New selection operators.
- Bug fixes and improvements.

## **User Interface**

- Added a warning to the main panel indicating that the addon has not been tested on the current Blender version.
- Optimized panels for better combined usage.

## **Zen Draw Sys**

- Added **Colored Islands**: Display assigned colors to each UV island for easier visual distinction in the UV/Image Editor.

## **Unwrap Sys**

- Added the **Auto Seams and Unwrap** operator for automatically creating seams and unwrapping.

## **Sticky UV Editor**

- Added an option to remember the active texture.

## **Trimsheet**

- Added name filter presets to the trim list.
- Added a warning for the trim scrolling process.
- Added the **Fit To Selected Trims** operator for randomly distributing islands across selected trims.
- Optimized and expanded the **Import Trimsheet** operator.

## **Select System**

- Added the ability to select polygons using the **Stretched Angle** algorithm in the **Select Stretched** operator.
- Added the **Filter Islands by Geometry** operator to select islands based on face count and face type.
- Added the **Select Non-Planar Faces** operator to select polygons that are bent along their internal triangulation.
- Added **Island List** with island properties display and color tagging.

## **Transform System**

- Simplified and sped up the **Arrange Islands** operator.
- Improved island position detection in **World Orient** mode.

## **Pack**

- Added new packing modes: **To Active UDIM** and **Outside Trims**.
- Added operators to create a trim from a **Blender UV Custom Region** and a region from a trim.

## **Stack System**

- Completely rewritten **Stack Sys**. Improved stacking algorithms and stack type display.

## **Zen UV Transform Tool**

- Added **snapping** support for the **Rotate** operation.

## **Fixed**

- Fixed the **Pack to Trim** packing mode.
- Fixed an issue in the **Zen Unwrap** operator when an object has no UV islands.
- Fixed selection synchronization between Mesh and UV for Blender 5.0 and higher.
- Fixed detection of selected islands in the 3D View in **EDGE** mode.
- Fixed an issue in **Zen Relax** when using the native Blender algorithm.
- Optimized **Isolate Islands** performance.
- Sped up addon version checking.
- Fixed the **Show Overlapped** operator for **VERTEX** selection mode.
