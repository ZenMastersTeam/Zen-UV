# Version 4.5.2

## **General**

- Added support for **Blender 4.3**.
- Added **Color Id Mask** operator to import **Trims** from a bitmap image.
- Added the ability to switch **Seams** sets along with switching the active **UV Map**.
- Fixed bugs.

## **Operators**

### **Advanced UV Maps**

- Added ability to toggle the active **UV Map** using the hotkey even if the **Adv UV Maps** tab is closed.
- Added the ability to switch **Seams** sets along with switching the active **UV Map**.

### **Unwrap**

- Updated **Mirror Seams** operator, eliminating the possibility of erasing seams on the model if the source side does not contain seams.
- Added ability to ignore geometry in hidden state for Mirror Seams operator.
- Fixed a bug in **Relax** in multi-object mode when non-active objects did not receive a status update.

### **Select**

- Added **Select Holed Islands** operator to select islands with holes inside.
- Added the ability to toggle the **UV Sync Selection** state for **Loops to Edges** and **Loops to Faces** operators.
- Added option to check *Margin* - distance from the edge of the island to the border of the specified **UV Area** for islands inside this **UV Area** for the **Select In Tile** operator.
- Added Faces Less than Pixel operator to select polygons smaller than one pixel.
- Added **Select Zero Area Faces** operator.
- Fixed a bug in the **Loop To Edges** operator if bordering island edges were processed.
- Fixed a bug with selection in **3D View** in the **Isolate Island** operator.

### **Transform**

- Fixed a bug in **Quadrify** where when the **Skip Non Quads** option was enabled, islands of any type were ignored.
- Fixed bug with incorrect result **Quadrify** when area of base polygon and polygons in face loop is zero.
- Fixed a bug in **Relax** operator when transitioning objects to **Edit Mode**.
- Fixed a bug in **Annotation** and **Math Visualizer module** due to migration to **Blender 4.3**.

### **Trimsheet**

- Added **Color Id Mask** operator to import **Trims** from a bitmap image.
- **Add Trims** menu has been changed. It is now presented as a single group.
- Fixed a bug in **Select In Tile** operator when the selection was not updated in **Any Cross** mode.
- Fixed a bug in **Trimsheet Export** when source texture proportions were not taken into account.
- Fixed a bug in **Scroll Fit To Trim** where you can't undo a filter by name if there are no filter matches.

### **Stack**

- Updated and optimized **Stack** panel.
- Added **Clear Selection** property to **Select Primaries, Replicas, Singles** operators. Also added this group to the **UV Editor** panel.
- Fixed a bug in Stacked display where the whole object was displayed instead of stacked parts.

### **UV Checker**

- Added **Calc UV Edges Length** operator to calculate the length of selected edges in units and pixels.
- Fixed a bug in **Texture Checker** if **Blender** changed texture name to .001 in case of duplication.
- Added **Calculate UV Pixel Size** operator to calculate pixel size based on texture dimensions.

### **Pack**

- Added **Calculate Recommended Margin** operator to calculate recommended **Margin** based on texture size.
- Due to the fact that in newer versions of Blender the **Pack** operator may not be executed if run from a script, a check for execution has been added. In case of non-execution the standard **Invoke** dialog is displayed.

### **Favorites**

- Added a form for editing all properties of the added operator in a single window instead of a text field.
- Since the name of the preset type and its name are displayed in the same field, the preset type is now marked with an asterisk to visually distinguish it from the name.
- Fixed a bug in **Favorites** where Blender native operators cannot be selected in the **Favorites** operator selection menu.
- Fixed a bug in **Favorites** when after loading a preset at startup, the name is not set active in the list.

### **Preferences**

- Optimized **Display** panel and added also in **UV Editor** context.
- Fixed a bug in saving **Addon Preferences** due to a bug in Blender where 2nd and subsequent level variables are not saved.
