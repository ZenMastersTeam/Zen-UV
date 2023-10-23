# Version 4.2.0

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
<iframe src="https://www.youtube.com/embed/iUoGZeMTlYo" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
</div>
<br>

### **General**

- Redesigned and improved Texel Density system.
- Redesigned and improved Advanced UV Maps system.
- Updated Pack system for Pack operator in Blender 3.6.1 and higher.
- Added Display UVs in Object mode and Display Overlapped Islands operators. 
- Added Zen UV Core Library v2.0 for Zen UV 4.2 and higher.
  
## **Operators**

### **Advanced UV Maps**

- Updated UV Maps Display and Sync system in multi-object mode.
- Improved Rename operator. Added the ability to rename multiple textures belonging to the same object using a template.
- Added the ability to change the position of the UV Map in all modes including multi-object.
- Added interface for managing native Transfer UV operators (Object mode only).
  
### Unwrap

- Added Set TD option to Zen Unwrap operator.
- Fixed a bug in Zen Unwrap when the UV Map was not created correctly in vertex mode.
  
### **Transform**

- Added Advanced mode for Randomize operator.
- Added Grab Increment operator to Move system.
- Added Set TD option to Quadrify operator.
- Fixed a bug in Align system when vertices of triangular faces were not aligning.
- Fixed a bug in Align to UV Area operator when it aligned islands chaotically in 3D View context.
  
### **TrimSheet**

- Added Clean Trimsheet Preview Folder operator to clean Preview images.
- Added an option to disable the Timsheet Presets loading confirmation dialog.
- Fixed a bug in importing Trimsheet from Adobe Illustrator when Trims without colors and names were imported.
- Fixed a bug in Align To Trim operator for the case when there are no Trims in the scene. Alignment is performed by UV Area.
  
### Stack

- Added Zen UV Core Library v2.0 for Zen UV 4.2 and higher.
- Fixed a bug in Select Stacked operator when UV Sync is disabled.
  
### **Texel Density**

- Added the ability to specify Island Pivot when setting TD.
- Added Calculate TD operator which calculates recommended Texture size based on the desired TD and vice versa.
- Updated Display system. Now it works on the Overlay principle.
- Added Gradient Widget to Display the current state of TD.
- Added TD Range operator to calculate the minimum, average, maximum TD values for selected objects or scene.
- Added Island Size system to control Island size in Pixels and Units.
- Added UV World Size system to control texture size in scene units.
- Added an option indicating the accuracy of TD calculations. By decreasing the value you can get faster calculation speed.
- Updated and optimized Select by TD operator.
  
#### **TD Preset System**

- Added the ability to save texture size and units of measurement along with Presets (optional).
- Added Global TD Preset for use in other operators. Unwrap and Quadrify operators can set the TD specified in this preset.
- Added Sort operator for sorting Presets by TD value.
- Added Create Presets operator to create Presets from selected Islands.
- Added Colorize Presets operator for assigning colors to existing Presets according to the color scheme.
  
### **UV Checker**

- Added Display UV Object operator to display UVs in Object mode. 
- Added Display Overlapped operator to display Overlapped Islands.
- 
### **Pack**

- Added **Pack In Trim** option for Blender Pack Engine for Blender 3.6.1 and higher.
- Added the ability to use Excluded system for UV Packer Pack Engine.
- Updated Get UV Coverage operator. Added options for coverage calculation: Generic, Selected, Exclude Stacked.
- Updated Pack system to the new Pack operator for Blender 3.6.1 and higher.
- Fixed functionality of the Pack operator in Sync Off mode.
- Disabled the ability to use Pack operator for Blender 3.6.0. Added Popup with warning.
  
## **Other**

- Added a cancel action button to Progress Bar Widget.
- Fixed a bug where Island received distortion if it overlapped itself.
- Added Update Widget in Viewport to update Draw when Auto Update Draw is disabled.
