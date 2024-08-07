# Creating your trim sheet with Zen UV
Zen UV addon provides all necessary tools to create your trim sections

!!! tip
    Watch the video explaining how **Trimsheet Creation** works.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/f9meGzMGx2k?start=770&end=950" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div>

!!! Panel
    ![img](img/screen/trimsheet/trimsheet_panel.png)

## Trim sheet data storage in blend file
Trim sheet can be stored either in a scene or in an image data-block of blend file

| ![](img/screen/trimsheet/storage_modes.png) |
|---|
| Data storage modes|

| | |
|---|---|
| **Scene** | Trim sheet is stored in a scene data-block |
| **Image** | Trim sheet is stored in an image data-block |

### Active Trim Sheet
There is exactly one active trim sheet at any time in certain Blender editor (UV Image Editor, 3D Viewport).

- **Scene Mode**: never changes for the same scene
- **Image Mode**: depends on the current editor type
    - **UV Image Editor**: <BR>
    trim sheet data is taken from the active Image Editor image
    ![](img/screen/trimsheet/uv_active_image.png)

    - **3D Viewport**: <BR>
    Trim sheet data is taken either from property trimsheet image of the active material or from the texture connected to the base color

        - Active Material Trimsheet Image
        ![](img/screen/trimsheet/active_material_image.png)

        - Active Material Base Color Image
        ![](img/screen/trimsheet/base_color_image.png)

## Trim Sheet Creation
Use ZenUV tool to create trims in UV Editor

| ![](img/screen/trimsheet/trimsheet_tool_create.png) |
|---|
| |

### Draw Trim in UV Editor
There is an option to draw a trim using mouse:

1. Activate ZenUV tool
2. Select tool category "Trims"
3. Select tool mode "Create"

| ![](img/screen/trimsheet/create_trims.gif) |
|---|
| |

### Trims Snapping for Creation and Resizing
Snapping lets you easily align trims. It can be toggled by clicking the magnet icon in the ZenUV tool header

| ![](img/screen/trimsheet/trims_snapping.png) |
|---|
| |

| Snap Mode | Description |
|---|---|
| Pixels | Trim is snapped to image pixels if image is active in UV Editor |
| Grid | Trim is snapped to UV Grid |
| Trims | Trim is snapped to other trim borders |

| ![](img/screen/trimsheet/trims_snapping.gif) |
|---|
| |

### Trims List
This control is useful to manage lists of trims. In the center of its area you can select, deselect, rename trims. On the right of the list view are additional buttons and button to call the additional popup menu.

![](img/screen/trimsheet/trimlist.png)

### Active Trim
There is exactly one active trim in the curent trim sheet. It is highlighted in trim sheet UI list and surrounded with handles in trim editor

![](img/screen/trimsheet/active_trim.png)

#### Select Active Trim with Preview Panel
You can select active trim with preview panel.

1. You need to press `Preview` button and after
![](img/screen/trimsheet/trim_preview_panel.png)

2. Select a corresponding trim
![](img/screen/trimsheet/trim_preview_select.png)

### Selected Trims
Selected trims are indicated with tickmarks in trim sheet UI list and have a blue shape border in trim editor

![](img/screen/trimsheet/selected_trims.png)

#### Select Trim in UI List
To select an item in trim sheet UI list, `LMB` on it.

#### Select Trim in the Viewport
It is also possible to select trim by `LMB` in the viewport by activating selection mode

![](img/screen/trimsheet/trim_select_mode.png)

#### Rename
By double-clicking on an item, you can edit its name via a text field. This can also be achieved by pressing `Ctrl-LMB` over it.
#### Resize
The list view can be resized to show more or fewer items. Hover the mouse over the handle `(==)` then click and drag the handle to expand or shrink the list.
#### Filter
Click the Show filtering options button (+) to toggle filter option buttons.

- **Search**: <BR>
Type part of a list item’s name in the filter text field to filter items by part of their name.
- **Filter Include**: <BR>
When the magnifying glass icon has a + sign then only items that match the text will be displayed.
- **Filter Exclude**: <BR>
When the magnifying glass icon has a - sign then only items that do not match text will be displayed.
- **Sort**: <BR>
Sort list items.
    - Alphabetical: <BR>
This button switches between alphabetical and non-alphabetical ordering.
    - Inverse: <BR>
Sort objects in ascending or descending order. This also applies to alphabetical sorting, if selected.

### Add
Adds a new item.

### Remove
Removes the selected item.

### Duplicate
Duplicates active or selected trim

| Option | Descripton |
|---|---|
| Ignore Color | Does not duplicate trim color settings |
| Clear Selection | Clear selection from source trims after duplicating |

### Menu
A menu with operators e.g. copy paste, or operations on all items.

!!! Menu
    ![](img/screen/trimsheet/trim_menu.png)

#### Copy Trims to Clipboard
Copy [active](#active-trim), [selected](#selected-trims) or [all trims](#trims-list) to clipboard

#### Paste Trims from Clipboard
| Mode | Description |
|---|---|
| Clear | Clear all trims before paste operation |
| Add | Add trims to the end of trim sheet |
| Replace | Add new trims and replace trims with the same name |

#### Batch Rename
Can rename many trims at once. This uses a pop-up dialog with operations and their options to change the name. These actions are applied in order, from first to last in a trim sheet.

![](img/screen/trimsheet/trim_batch_rename.png)

#### Add Trim Grid
Create grid of trims inside active, selected trims, from zero coordinates or 2D cursor position

#### Add Trim UDIM
Creates trims in positions and with UDIM tile sizes

#### Set Trim World Size
Set trim 'World Size' property based on texture size. Works on selected trims

#### Frame Trim
Moves view to active or selected trims center in UV editor

#### Clear Trimshet Preview Folder
Clear folder where trimsheet preview temporary icons are stored

### Move (up/down arrow icon)
Moves the selected item up/down one position.

### Delete All
Deletes all trims in the trim sheet

## Trim Sheet Presets
!!! Presets
    ![](img/screen/trimsheet/trim_presets.png)

### Preset Selector
A list of available presets. A selection will override the included properties.

### Add
New presets can be added based on a predefined set of properties, which will be saved for later reuse. A pop-up opens where you can set a name after which you can select it from the list and in some cases additional settings.

### Remove
Deletes the selected preset.

### Open Presets Folder
You can override the default presets folder with your own path

## Trim Settings
Trim settings property inspector shows settings of the active trim

!!! Dimensions
    ![](img/screen/trimsheet/trim_axis.png)

### Trim Units
By default trim units are in UV points based on values from 0 to 1, but it is possible to switch to image pixels depending on image size

![](img/screen/trimsheet/trim_pixels.gif)

### X
Trim left point

### Y
Trim bottom point

### W
Trim width

### H
Trim height

### Fit Axis

| | |
|---|---|
| **U** | U axis |
| **V** | V axis |
| **Min** | The minimum length axis is automatically determined |
| **Max** | The maximum length axis is automatically determined |
| **Automatic** | Automatically detected axis for full dimensional compliance |

### Inset
Trim inset

### Keep Proportion
Keep trim proportions while transforming

### Match Rotation
Match trim rotation

### Align To
Align to remembered directions in Fit, Align operations

### World Size
Width and height of trim in [UV world size calculation units](#units)

### Units
UV world size calculation units

### Tags
Trim tags

### How to apply same settings to multiple trims?
| ![](img/screen/trimsheet/trim_group_settings.png) |
|---|
| Group Apply Button-Indicator |

1. Select 2 or more trims
2. Press Apply button

#### Check the equality of properties in selected trims

| | |
|---|---|
| ![](img/screen/trimsheet/trim_prop_not_active.png) | Properties are not equal |
| ![](img/screen/trimsheet/trim_prop_active.png) | Properties are equal |

## Display Trims
Trims can be displayed in viewport with special gizmo layer

### Trims Display Overlay in UV Image Editor
| ![](img/screen/trimsheet/trim_display.png) |
|---|
| |

### Trims Display Polygon Overlay in 3D Viewport
!!! Note
    Trims display in 3D Viewport is enabled only if Zen UV Tool is active and active object has active polygon

| ![](img/screen/trimsheet/trim_display_3D.png) |
|---|
| |

### Trims Display Overlay Widget in 3D Viewport
Trims can be displayed in overlay widget. To activate it you need to press gizmo button in the right side of 3D viewport

| ![](img/screen/trimsheet/trim_display_widget.png) |
|---|
| |

#### Overlay Widget Locking Options
Trims display overlay widget can be moved by `Shift + Middle Mouse Button` and scaled by `Mouse Wheel Up|Down`. And its position can be locked in the settings

| ![](img/screen/trimsheet/trim_display_widget_locked.png) |
|---|
| |

## Transform Trims
| ![](img/screen/trimsheet/trim_transform.png) |
|---|
| |

### Align Trims
Determines how selected trims will be aligned.

Use Align to align selected trims to the top, bottom, left, or right of an active trim or each other, or UV area bounds.

| ![](img/screen/trimsheet/tr_align.png) |
|---|
| |

### Crop Trims
Use Crop to crop selected trims or all trims by UV area bounds

| ![](img/screen/trimsheet/tr_crop.png) |
|---|
| |

### Adjust Trims
Set the same width or height of the selected trim. You can select to use minimum or maximum value.

| ![](img/screen/trimsheet/tr_adjust.png) |
|---|
| |

### Distribute Trims
Use Distribute to distribute selected trims at equal distances between each other, starting distribution as is or from active trim, or from UV area bounds

| ![](img/screen/trimsheet/tr_distribute.png) |
|---|
| |
