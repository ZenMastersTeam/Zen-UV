# Version 5.0.2

## **General**

- Hotfixes.
- Added support for **UV Packmaster 3.4.0**.
## **Operators**

### **Transform**

- Fixed a bug in **Fit** operator in multi-object mode where the **Overall** option behaved like **One by One**.
- Fixed a bug in **World Orient** operator (division by zero error).
### **Texel Density**

- Optimized **Select Current TD** operator for selecting islands with the **TD** value specified in the panel.
- Added a universal **Select by TD** operator to the **TD** panel.
### **Trimsheet**

- Added an operator to select an island by **trim name**.
- Added an algorithm to compensate for errors when importing legacy-type **Image Presets**.
- Fixed a bug when creating a preset in **Image** mode in the **3D Viewport**.
### **System**

- Updated the image search algorithm due to the removal of the Python **imghdr** module in **Python 3.13**.
- Adjusted **annotations** to support **Blender 4.4**.