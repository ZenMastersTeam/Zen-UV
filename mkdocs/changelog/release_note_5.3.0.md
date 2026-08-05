# Version 5.3.0

## **General**


- **Colored Islands**, **UV Background Mask** Display modes.
- **UV Packmaster 4 Support**.
- **Relax Along Axis** operator.
- **Prepare Unwrap** operator.
- **Tweak Transform** operators.
- Bug fixes.

## **Unwrap**


- Added **Prepare Unwrap** operator to prepare an object for UV unwrapping.
- **Auto Unwrap** operator can now automatically create a UV Map if one does not exist.
- Optimized and accelerated **Zen Unwrap** operator for **Blender v5.0**.
- Added **Relax Along Axis** operator to relax selected vertices along a specified axis direction. It also replaces the functionality of **Zen Unwrap – Unfold Vertices**.
- Added the ability for **Relax** operator to automatically create a UV Map if the object does not have one.
- Added user defined props for **Mark By Angle** operator.
- Removed **Unfold Vertices** functionality from **Zen Unwrap**.  It has been replaced by standalone **Relax Along Axis** operator.

## **Select**


- **Select by UV Area** operator renamed to **Select by UV Value**. Added the ability to select islands by height and width.
- **Select Stretched Faces** algorithm is now aligned with Blender’s native **Show UV Stretch – Area** algorithm. Polygons are now selected exactly as they appear stretched when using Blender’s overlay.

## **UV Checker**


- Added **Background Mask** option to shade the space between islands in **UV Editor**.
- Added the ability to enable display modes synchronously in **UV Editor** and **3D View**.
- Added the ability to display islands in different (random) colors.
- Added **Auto Update Draw** option to disable all addon background tasks for maximum **Blender** performance.  When disabled, all draw updates must be updated manually.
- Added the ability to export current **Zen Draw** overlay to an image file.

## **Trimsheet**

- Added the ability to **Sort Trims list by Size** and to **Select by Height or Width**.

## **Transform**

- Added **Tweak** operators for fast Moving, Rotating, and Scaling of UV islands.

## **Pack**

- Added support for **UV Packmaster 4**.

## **UI**

- Added a default panel in **Favourites** with the most frequently used operators (**Most Used UV**).

## **Fixed**

- Fixed an error when quickly switching the current **Trim** in Trimsheet list.
- Fixed incorrect texture proportion detection when the texture is not found in **Blender** datablocks.
- Fixed multi-list mode in **Trimsheet** system for **Blender v5.0**.
- Fixed an issue where an open **Texel Density** tab generated a scene change event.
- Fixed **Isolate Part** operator not executing when a **UV Map** is missing.
- Fixed selection issue in edge mode in **Quadrify** operator.
- Fixed an error in restoring hotkey categories.
- Fixed **Unmark All** operator behavior when the object has no UV Map.
- Optimized and fixed **Unstack** operator.
