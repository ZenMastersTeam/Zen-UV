# Version 5.4.1

### **General**

- Added Blender 5.3 compatibility fixes.
- Performance optimizations, UI refinements, and bug fixes.

### **User Interface**

- **ComboPanel**: Added an icon button to switch any tab into a floating panel.
- **Advanced UV Maps**: Improved the layout and usability of the Advanced Maps list.
- **Randomize**: Changed the default offset/transform values from `0` to non-zero defaults for immediate visual feedback.
- **Documentation**: Fixed broken documentation links across Transform operators.

### **Zen Draw**

- Added **Pinned** display mode to visualize pinned UV vertices/islands.
- Changed Draw modes to work as an automatic toggle when activated.

### **Unwrap**

- **Zen Unwrap**: Fixed an error occurring when using the *Sort Unwrapped* option.
- **Auto Unwrap**: Fixed a bug where seams were not being marked.

### **Select**

- **Select by UV Value**: Fixed an issue preventing the *Area* parameter from being adjusted.
- **Select Stretched Faces**: Fixed an operator error in Blender 5.3.

### **Transform**

- **Arrange Islands**: Fixed an error when calling the operator directly without `Invoke`.

### **Trimsheet**

- **Trimsheet Tool**: Fixed a Blender crash that occurred when the UV Editor was open in a separate window.

### **Checker**

- Improved logging so that missing texture files in the Checker folder no longer spam the console/log continuously.

### **Improvements**

- **Islands List**: Optimized island data collection performance.

### **Fix**

- **Draw Sys**: Fixed **Auto Update** not working properly in Blender 5.3.
- **Islands List**: Fixed a timer accessing mesh data after exiting Edit Mode.
- **Checker**: Fixed an exception when importing from its own folder.
- **New Version Checker**: Fixed a bug in the new version detection system.
- **World Size**: Fixed **Set World Size** always using the value embedded in the image instead of operator properties.
- **Select Mode**: Fixed an exception when switching to Face, Edge, or Vertex selection modes on a mesh without a UV map.
- **Select Holed**: Fixed an issue where it selected the cube.
- **Import-Export Settings**: Fixed settings import wiping favorites on read error.
- **Filter Islands by Property**: Fixed issues when working with multi-object selection.
- **Select Similar**: Fixed an error when retrieving the description in the Pie Menu.
- **Zen Sync**: Fixed loop selection remaining on unselected polygons when toggling sync from *Off* to *On*.
- **TexelDensity**: Fixed **Current TD** not showing when opening the UV Editor via the *Sticky* button on the right.
- **Touch Tool**: Fixed the tool not working in Blender 5.3.