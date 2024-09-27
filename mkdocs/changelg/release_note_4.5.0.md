# Version 4.5.0

## **General**

- Added the ability to group Zen add-ons (Zen UV, Zen Sets, Zen BBQ) into a single Zen tab in N-panel. Add-on Preferences -> UI -> Addon N-Panel Name  -> Zen and restart Blender after.
- Added detailed [Step-by-Step tutorial for Emergency Light 3D model](https://zenmastersteam.github.io/Zen-UV/latest/tutorial/emergency_light/emergency_light_eng/)
- Bug fixes.

## **UI**

- Added option to disable the entire addon panel from N-panel.
- Added the ability to select the name of the addon's N-panel tab (Zen or ZenUV).

## **Operators**

### **Advanced UV Maps**

- Added hints to Advanced UV Maps operators.
- Fixed a bug where when group renaming UV Maps with the same name, the new name consisted of a set of symbols.
- Fixed a bug with duplicate names in the Advanced UV Map list.
- Fixed a bug when creating a new UV Map when instead of the correct name the map was called Float.

### **Unwrap**

- Updated Smooth by Sharp operator due to changes related to auto_smooth_angle object property in Blender 4.1.
- Fixed incorrect behavior of the Isolate Island operator in no sync mode if there are partially hidden islands.
- Fixed a bug in the Zen Unwrap operator when nothing is selected, but the Selected Only mode is set.

### **Select**

- Added Isolate Part operator to perform isolation of a part of a mesh. It also works in UV Editor.
- Fixed a bug in the Select Overlapped operator when the object does not have any UV Map.

### **Transform**

- Added operator to move selection in UV Editor to the location specified by the mouse cursor.
- Added options for working with UDIM tiles to the operators Align to UV Area, Move 2D Cursor, Fit to UV Area.
- Added options to Sort Finished operator to disable moving each type separately.
- Added operators of the Distribute group to the Advanced Transform panel.
- Fixed a bug where the Randomize operator would scatter islands when providing a position not depending on the seed being persistent.
- Fixed a bug where the Quadrify operator did not update the mesh state if the Mark option was disabled.
- Fixed a bug in the Quadrify operator if the edge has zero length.

### **Trimsheet**

- Added the ability to scroll through Trim categories when working with Zen Transform Tool.
- Added the ability to automatically perform Fit to Trim after using operator Trim Preview.
- Added Add Trims From Zen Sets operator. Appears in UI if Zen Sets is installed.
- Fixed a bug when setting a group value for the Trim World Size property.
- Fixed a bug with generating a Trim preview if the trim was outside the UV Area above the upper left corner.
- Fixed a bug when in Zen Transform Tools mode without Trims the UV Area inscription was displayed in Image mode.
- Fixed a bug where renaming a Trim in the list did not change the names in the viewport when using the Zen Transform Tool.

### **Stack**

- Added Islands Counter operator to Stack panel.

### **Favorites**

- Added the ability to not display a category.
- Added functionality for creating a control in the control properties, where only the options specified by the user are included.
- Fixed default Favorites presets to avoid lags when the Favourites panel is open.
- Added Delete All button to Favorites list.
- Added the ability to use user draw functions.

### **Examples**

- Added notification if internet access is disabled in Blender.
- Added the ability for More Info operator to open links on the Internet to documentation and tutorials.

### **Other**

- Fixed a bug where it was not possible to disable user script from the addon preferences window.

## **Optimization**

- Added functionality for deleting information about Finished and Excluded when deleting all UV Maps.
- User data (scripts and presets) have been moved to the ZenUV/user_data folder.















