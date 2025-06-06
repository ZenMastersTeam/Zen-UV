# Favourites

## Prerequisites
Zen UV has a lot of different operators and tools that are located in different panels. And we decided to make Favorites to collect frequently used operators in one place. Also there is an option to build in Blender native panels: such as [UV Maps](https://docs.blender.org/manual/en/4.2/modeling/meshes/uv/uv_texture_spaces.html#uv-maps) or [Attributes](https://docs.blender.org/manual/en/4.2/modeling/meshes/properties/object_data.html#attributes).

!!! tip
    Watch the video explaining how to organize **Favourites**.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/W-m9hAitLQU?start=17&end=150" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div>

## Favourites Interface Panel
All favourties items are displayed in interface panel which could be placed depending on [display modes](#display-modes)

!!! Panel
    | ![](img/screen/favourites/panel_uv.png) | ![](img/screen/favourites/panel_view3d.png) |
    |---|---|
    | UV Editor | View 3D |

### Display Modes
You can choose a combination of one or several display favourites panel options.

| ![](img/screen/favourites/modes.png) |
|---|
| Favourites Display Modes |

#### Top Display Mode
Favourites will be placed at the top of N-Panel.

| ![](img/screen/favourites/top_mode.png) |
|---|
| Top display mode |

##### Show Header
If **Show Header** option in top mode is unset than favourites header is not showing

| ![](img/screen/favourites/show_top_header.png) |
|---|
| Show header in top mode |

#### Tab Display Mode
Favourites will be represented as the tab page of N-Panel.

| ![](img/screen/favourites/tab_mode.png) |
|---|
| Tab display mode |

#### Float Display Mode
Favourites will be represented as the separate floating panel.

| ![](img/screen/favourites/float_mode.png) |
|---|
| Float display mode |

## Favourite Items List View
This control is used for managing lists of favourite [items](#favourite-item). In addition to the main list, there is a Filtering panel on the bottom (hidden by default) and modification buttons on the right.

| ![](img/screen/favourites/list_view.png) |
|---|
| List View |

### Select
To select an [item](#favourite-item), click `LMB` on it.

### Rename
By double-clicking on an [item](#favourite-item), you can edit its name via a text field. This can also be achieved by clicking it with `Ctrl-LMB`.

### Resize
The list view can be resized to show more or fewer [items](#favourite-item). Hover the mouse over the handle `::::`, then click and drag to expand or shrink the list.

### Filter
Detailed information about filter is written in [general list view description](https://docs.blender.org/manual/en/dev/interface/controls/templates/list_view.html#ui-list-view)

### Add +
Adds a new [item](#favourite-item).

### Remove -
Removes the selected [item](#favourite-item).

### Move (up/down arrow icon)
Moves the selected [item](#favourite-item) up/down one position.

### Delete All
Deletes all [items](#favourite-item)ms in the [list](#favourite-items-list-view)

### Duplicate
Duplicates [item](#favourite-item) with copying all its properties.

## Favourite Item
Is used to define UI element in favourites panel.

| ![](img/screen/favourites/fav_item.png) |
|---|
| Favourite item and the corresponding UI element |

### Name
Is used to display text in UI and is an identifier in the [list](#favourite-items-list-view).

#### Display Name Option
You can disable name by unchecking tickmark at the right corner in the name property field.

| ![](img/screen/favourites/name_display_setting.png) | ![](img/screen/favourites/name_display_setting_not.png) |
|---|---|
| ![](img/screen/favourites/name_display.png) | ![](img/screen/favourites/name_display_not.png) |
| Display name enabled | Display name disabled |

### Category
If you want to group items in collapsible panel, you can mark them with the same category and they automatically will be groupped.

| ![](img/screen/favourites/fav_category.png) |
|---|
| Category example |

### Command and Mode
These two options depends on each other and are the main instrument to draw favourite item in the UI.

#### Mode
##### Operator
Displays an [operator button](https://docs.blender.org/manual/en/4.2/interface/controls/buttons/buttons.html#operator-buttons) in UI

| ![](img/screen/favourites/fav_operator_preview.png) |
|---|
| Example of embedded **Zen Unwrap** operator |

!!! Command
    | ![](img/screen/favourites/fav_operator_command.png) |
    |---|
    | Command interface in **Operator** mode |

    **Python Command** - is a text field where operator identifier or operator identifier with properties (optionally) should be set
    
    | Command Example | Description |
    |---|---|
    | uv.unwrap | UV Unwrap with last context properties |
    | uv.unwrap(fill_holes=True) | UV Unwrap with enable always 'Fill Holes' property |
    
**Operator Properties** - is a popup window to edit operator properties without necesserity to write them manually

| ![](img/screen/favourites/fav_operator_prop_edit.png) |
|---|
| Operator properties editor |

- **Operator Selector** - wizzard to define operator identifier in different ways
    - **Select Operator** - Select operator which will be added to the favourites

    | ![](img/screen/favourites/fav_operator_list.png) |
    |---|
    | Select operator from list of available operators |

    - **Select Text Block** - Select user text datablock which will be loaded and executed when operator button will be clicked

    | ![](img/screen/favourites/fav_text_block.png) |
    |---|
    | Example of executing Text data-block |

    - **Select Script** - Select user script which will be loaded and executed when operator button will be clicked. **It works in the same way as Select Text procedure with the only difference that code will be loaded from script.**

##### Panel
Displays a [panel](https://docs.blender.org/manual/en/4.2/interface/window_system/tabs_panels.html#panels) in UI

| ![](img/screen/favourites/fav_command_panel.png) |
|---|
| Example of Blender **UV Maps** panel embedded |

!!! Command
    **Python Command** - must be a valid python [panel](https://docs.blender.org/manual/en/4.2/interface/window_system/tabs_panels.html#panels) or [menu](https://docs.blender.org/manual/en/4.2/interface/controls/buttons/menus.html#popup-menus) identifier

    | Command Example | Description |
    |---|---|
    | DATA_PT_uv_texture | UV Maps Panel |
    | VIEW3D_MT_uv_map | UV Mapping Menu |

- **Command Menu** - popup menu where a panel or menu could be selected from the list

| ![](img/screen/favourites/fav_select_panel_menu.png) |
|---|
| Command Menu in 3D Viewport context |    

#### Property
Displays a [property field](https://docs.blender.org/manual/en/4.2/interface/controls/buttons/fields.html#fields) in UI

| ![](img/screen/favourites/fav_property_preview.png) |
|---|
| Example of **UV Sync Selection** and **Auto Texture Space** properties embedded |    

!!! Command
    **Python Command** - must be a valid [context variable](https://docs.blender.org/api/current/bpy.context.html) that is available through [Python API](https://docs.blender.org/api/current/index.html)

    | Command Example | Description | Preview |
    |---|---|---|
    | scene.tool_settings.use_uv_select_sync | UV Sync Selection | ![](img/screen/favourites/fav_uv_sync_selection.png) |
    | active_object.data.use_auto_texspace | Auto Texture Space | ![](img/screen/favourites/fav_auto_texture_space.png) |

#### Label
Displays a text string, icon or one of them in UI.

| ![](img/screen/favourites/fav_label_preview.png) |
|---|
| Label with icon |  

!!! Command
    Is not used in this mode.

#### Script
Displays a UI block defined as python script. This mode is necessary when you would like to display difficult UI elements that are avilable through addon [Python API](https://docs.blender.org/api/current/index.html) functions


| Embedded Texel Density Ranges | Native Texel Density Ranges  |
|---|---|
| ![](img/screen/favourites/fav_script_preview.png) | ![](img/screen/favourites/fav_script_preview_original.png) |

!!! Command
    **Python Command** - must be a valid [Python API](https://docs.blender.org/api/current/index.html) script line that can draw UI element in the current [UILayout](https://docs.blender.org/api/current/bpy.types.UILayout.html).

    | Example | Zen UV Texel Density Ranges |
    |---|---|
    | Command | `from ZenUV.ops.texel_density.td_ui import draw_td_ranges;  draw_td_ranges(context, op_row)` |
    | Preview | ![](img/screen/favourites/fav_td_ranges.png) |

##### Context variables
The context members available depend on the area of Blender which is currently being accessed.

!!! Warning
    All context values are **read-only**. Do not change them! Just use for UI display purposes.

- [**context**](https://docs.blender.org/api/current/bpy.types.Context.html) - current windowmanager and data context
    
    **TYPE:** `bpy.types.Context`

- [**layout**](https://docs.blender.org/api/current/bpy.types.UILayout.html) - current [Favourites Panel](#favourites-interface-panel) UI layout

    **TYPE:** `bpy.types.UILayout`

- [**op_row**](https://docs.blender.org/api/current/bpy.types.UILayout.html) - current [Favoutite Item](#favourite-item) UI layout

    **TYPE:** `bpy.types.UILayout`

- [**p_item**](#favourite-item) - current [Favoutite Item](#favourite-item) preferences ([mode](#mode), [name](#name), etc.)

    **TYPE:** `ZUV_FavItem`

- [**addon_prefs**](preferences.md) - Zen UV [preferences](preferences.md) class

    **TYPE:** `ZUV_AddonPreferences`

!!! Note
    We understand that this may look very difficult so feel free to contact with us in our [**Discord channel**](https://discord.gg/wGpFeME). We will be very glad to help you!

### Layout
Defines how [favourite UI items](#favourite-item) will be placed in the [favourite UI panel](#favourites-interface-panel) organizing items in sub-layouts.

- **Row** - starts a sub-layout where items are placed next to each other in a row.

    | ![](img/screen/favourites/fav_layout_row.png) |
    |---|
    | Projection operators placed in a row |

- **Column** - starts a sub-layout where items are placed under each other in a column.

    | ![](img/screen/favourites/fav_layout_col.png) |
    |---|
    | Projection operators placed in a column |

- **Flow Grid** - starts a sub-layout where items are placed in a flow grid depending on [panel](#favourites-interface-panel) width.

    | ![](img/screen/favourites/fav_layout_flow_grid.png) |
    |---|
    | Projection operators placed in a flow grid |

- **Auto** - follows the previously created sub-layout. If sub-layout was not previously defined than **Flow Grid** is set by default.

!!! Note
    Every sub-layout type except **Auto** inserts a separator before. If you want to skip separators creation group items with Layout Group property.

### Layout Group
Option to skip creation of separators betweeen sub-layouts.

| ![](img/screen/favourites/fav_layout_group.png) | ![](img/screen/favourites/fav_layout_group_open.png) |
|---|---|
| None | Open |

- **None** - Does not change anything in current [sub-layout](#layout).
- **Open** - Opens active [sub-layout](#layout), where all elements will be placed without separators.
- **Close** - Closes [sub-layout](#layout) without separators.

### Icon
Adds an icon to the current favourtie item element in UI.

| ![](img/screen/favourites/fav_layout_icon.png) |
|---|
| Standard Blender Icon |

### Icon Type
Defines type of an [icon](#icon) that will be placed in UI.

- **Standard** - Standard Blender icon.

    | ![](img/screen/favourites/fav_icon_select_standard.png) |
    |---|
    | Standard Blender Icon Selector |

- **Custom** - On of the ZenUV icons that are shipped with the addon.

    | ![](img/screen/favourites/fav_icon_select_custom.png) |
    |---|
    | Custom Zen UV Icon Selector |

### Icon Only
If option is set then only [icon](#icon) will be shown in [favourite item](#favourite-item) UI element.

| ![](img/screen/favourites/fav_icon_only.png) |
|---|
| UV Projection Operators |
