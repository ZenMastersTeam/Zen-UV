# Advanced UV Maps
Advanced UV Maps section created to have quick access to Object Data Properties — UV Maps.
It allows to select the active, add, remove, and rename UV Maps from the list.

If more than one object is selected, you can synchronously work with UV maps of the selected objects.

!!! Panel
     | Edit Mode | Object Mode| 
     |---|---|  
     | ![](img/screen/adv_uv_map/adv_uv_map.png) |![](img/screen/adv_uv_map/adv_uv_map__obj.png)|  

<!-- !!! tip
    Watch the video explaining how **Advanced UV Maps** works.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/Y7dG2i-FASs?start=541&end=619" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div> -->

## Advanced UV Maps List
The list can work in two modes:
- Multi object mode
- Single object mode

| List Description |
|---|
| ![](img/screen/adv_uv_map/multi_preview.png) |

| List Color | Individual for every column |
|---|---|
| Default color | All selectected objects has the same active UV Map, render, same position in the list |
| Red color | At least one object differs with one of the UV Map parameters |

| 1. Active UV Map status | |
|---|---|
| ![](img/screen/adv_uv_map/uvmaps_active.png) | UV Map is active |
| ![](img/screen/adv_uv_map/uvmaps_inactive.png) | UV Map is not active |

| 2. UV Map name | |
|---|---|
| Name is highlighted | All selected objects have UV Map with the name |
| Name is grayed out | At least one object from selection does not have UV Map with the name |

| 3. UV Map count and position status | |
|---|---|
| First or single digit | Number of objects that have UV Map with the selected name |
| Second digit | Selected objects count |

| 4. Active Render UV Map status | |
|---|---|
| ![](img/screen/adv_uv_map/uvmap_active_render.png) | UV Map is active for render |
| ![](img/screen/adv_uv_map/uvmaps_render_not_active.png) | UV Map is not active for render |

### UV Maps Status Detection
Advanced Maps system detects synchronization status of all UV Maps in the selected objects. It is possible to disable some parameters which are not neccessary for you to detect.

| ![](img/screen/adv_uv_map/uvmaps_status_detection.png) |
|---|
| |

---
## Duplicate active UV Map ![Add Button](img/icons/plus.png)
Duplicate the active UV Map or create a new one depending on the operator's properties.

![](img/screen/adv_uv_map/duplicate_active_map.png)

## Remove active UV Map ![Remove Button](img/icons/minus.png)
![](img/screen/adv_uv_map/uvmaps_remove.gif)

---
## Rename UV Maps
![](img/screen/adv_uv_map/rename_bake.gif)

| Rename Settings |
|---|
| ![](img/screen/adv_uv_map/uvmaps_rename_preview.png) |

| UV Maps source | |
|---|---|
| Selected | Operates on the currently selected UV Map items in the list |
| All | Operates on all UV Map items in the list |

| Options | |
|---|---|
| Find | The text to search for in names |
| | _1) if text is empty then all name will be renamed_ |
| | _2) if 'Use Regex' is set then text must be a valid regular expression_ |
| Replace | The text to replace for in matching names found from the 'Find' text |
| Match Case | Search results must exactly match the case of the 'Find' text |
| Use Regex | Replace by regular expression in the 'Find' text |

### Generate UV Map names from template
If you have naming convension for UV Maps in your projects, you can create template preset and quickly rename all UV Maps in one click

| UV Map naming preset |
|---|
| ![](img/screen/adv_uv_map/rename_template.gif) |

## Sync UV Maps ![Sync Button](img/icons/adv_uv_sync.png)
If your model requires UV Maps to have the same postion, name, active or render status you can synchronize them

![](img/screen/adv_uv_map/uvmaps_sync.png)

---

## Copy UV / Paste UV

Allows transferring the UV coordinates between UV Maps.

!!! note
    Available in Edit Mesh mode if geometry of selected objects is the same.

| ![](img/screen/adv_uv_map/copy_paste_UV.gif) |
|---|

#### Copy UV 

Copy the UV coordinates of the selection.

#### Paste UV 

Paste the UV coordinates.

---

## Adv UV Maps Tools

#### Clean UV Maps

Remove all inactive UV Maps.

![](img/screen/adv_uv_map/adv_uv_map_clean_inactive.gif)

#### Set UV Map Name by Index

Set UV Map name by its Index in the list.

![](img/screen/adv_uv_map/adv_uv_map_rename_by_index.gif)

---

## Transfer UV
| ![](img/screen/adv_uv_map/transfer_uv_maps.png) |
|---|

![](img/screen/adv_uv_map/transfer_uv_maps.gif)

| Transfer Modes | |
|---|---|
| Matching geometry | Objects must be of type mesh and must have a matching topology |
| Advanced | Transfer UV maps by generating an interpolated mapping between source and target mesh elements |
| Layout | Transfer layout of UV maps from active to selected meshes |

---

## UDIM tools

[**UDIM workflow**](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/workflows/udims.html) is a special workflow that allow to spread UV islands across several different textures of the model.

!!! note
    Available only in UV Editor context in Edit Mode.
    The image Source must be set to 'UDIM Tiles'.

![](img/screen/adv_uv_map/adv_uv_map_udim.png)


#### Fill Tile

Fill the current tile with a generated texture.

#### Add Missed

Create the missing UDIM Tile at the Island location. 

![](img/screen/adv_uv_map/adv_uv_map_udim_add_missed.png)


| Options | |
|---|---|
| By Selection | Use selection to determine where where UDIM tile will be created|
| In order | Create all the missing tiles in order until it reaches the last missed tile with the selection |
| Fill | Fill tile with settings below |


#### Set Active 

Set the active UDIM Tile based on the selection. 

![](img/screen/adv_uv_map/adv_uv_map_udim_set_active.gif)  

#### Remove Active

Remove the active UDIM Tile. 

![](img/screen/adv_uv_map/adv_uv_map_udim_remove_active.gif) 

#### Select in Active 

Select Islands in bounding box of active UDIM Tile or UV Area.

![](img/screen/adv_uv_map/adv_uv_map_udim_select_active.gif) 

#### Move to active

Move Islands to active or selected by number UDIM Tile. 

![](img/screen/adv_uv_map/adv_uv_map_udim_move_active.gif) 

#### Set Active

Set active UDIM Tile by eyedropper.

![](img/screen/adv_uv_map/adv_uv_map_udim_set_active_eyedropper.gif)
