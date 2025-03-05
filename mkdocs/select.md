# Select

!!! Panel
    | 3D Viewport | UV Editor| 
    |---|---|  
    | ![](img/screen/select/select_main_panel.png) |![](img/screen/select/select_main_panel_uv.png)| 


<table>
<thead>
<tr>
<th colspan="4" style="text-align: center;">Table of contents</th>
</tr>
</thead>
<tbody>

<!-- Islands -->
<tr>
<th colspan="4" style="text-align: center;">Islands</th>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-islands">Islands</a></td>
<td style="text-align: center;"><a href="#select-overlapped">Overlapped</a></td>
<td style="text-align: center;"><a href="#select-flipped">Flipped</a></td>
<td style="text-align: center;"><a href="#select-quaded-islands">Quaded Islands</a></td>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-holed-islands">Holed Islands</a></td>
<td style="text-align: center;"><a href="#select-similar">Similar</a></td>
<td style="text-align: center;"><a href="#select-in-tile">Select in Tile</a></td>
<td style="text-align: center;"><a href="#select-islands-by-direction">Island by Direction</a></td>
</tr>
<tr>
<td style="text-align: center;"><a href="#filter-islands-by-property">Filter Islands by Property</a></td>
<td colspan="3"></td>
</tr>

<!-- Faces -->
<tr>
<th colspan="4" style="text-align: center;">Faces</th>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-stretched-faces">Stretched Faces</a></td>
<td style="text-align: center;"><a href="#select-self-intersecting-faces">Self-Intersecting Faces</a></td>
<td style="text-align: center;"><a href="#select-by-uv-area">Select by UV Area</a></td>
<td style="text-align: center;"><a href="#select-zero-area-faces">Zero Area Faces</a></td>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-faces-less-than-one-pixel">Faces Less than Pixel</a></td>
<td style="text-align: center;"><a href="#select-faces-by-normal">Faces by Normal</a></td>
<td colspan="2"></td>
</tr>

<!-- Edges -->
<tr>
<th colspan="4" style="text-align: center;">Edges</th>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-seam">Seam</a></td>
<td style="text-align: center;"><a href="#select-sharp">Sharp</a></td>
<td style="text-align: center;"><a href="#select-uv-borders">Borders</a></td>
<td style="text-align: center;"><a href="#select-open-edges">Open Edges</a></td>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-cylinder-edges-splits">Cylinder Edges (Splits)</a></td>
<td style="text-align: center;"><a href="#select-edges-by-condition">Edges by Condition</a></td>
<td style="text-align: center;"><a href="#select-edges-by-direction">Edges by Direction</a></td>
<td colspan="1"></td>
</tr>

<!-- Loops -->
<tr>
<th colspan="4" style="text-align: center;">Loops</th>
</tr>
<tr>
<td style="text-align: center;"><a href="#zen-sync">Zen Sync</a></td>
<td style="text-align: center;"><a href="#select-linked-loops">Select Linked Loops</a></td>
<td colspan="2"></td>
</tr>

<!-- Misc -->
<tr>
<th colspan="4" style="text-align: center;">Misc</th>
</tr>
<tr>
<td style="text-align: center;"><a href="#select-int-loop">Int. Loop</a></td>
<td style="text-align: center;"><a href="#select-half">Half</a></td>
<td style="text-align: center;"><a href="#isolate-islands-toggle">Isolate Islands (Toggle)</a></td>
<td style="text-align: center;"><a href="#isolate-part-toggle">Isolate Part (Toggle)</a></td>
</tr>

</tbody>
</table>

---
### Select Islands
Select Islands by selected edge/face of the Islands. ![Islands](img/icons/select.png)

| ![Select_Islands](img/gifs/select_operators/Select_Islands.gif) |
| --- |
| Select islands |

---
### Select Int. Loop
Inter seam loop. Select Edge Loop with respect to Seams. 

| ![Select_Int_Loop](img/gifs/select_operators/Select_Int_Loop.gif) |
| --- |
| Select inter seam loop |

---
### Select Overlapped
Select Overlapped Islands.

| ![Select_Overlapped](img/gifs/select_operators/Select_Overlapped.gif) |
| --- |
| Select overlapped |

---
### Select Flipped
Select Flipped Islands.

| ![Select_Flipped](img/gifs/select_operators/Select_Flipped.gif) |
| --- |
| Select flipped |

---
### Select Seam
Select Edges Marked as Seams.

| ![Select_Seam](img/gifs/select_operators/Select_Seam.gif) |
| --- |
| Select Seam |

!!! Properties
      ![Select Seam Props](img/screen/select/SelectSeamProps.png)

 - **Clear Selection** - Clear initial selection
 - **Mode** - Selection type
    - *Select* - Select edges
    - *Deselect* - Deselect edges

---
### Select Sharp
Select Edges Marked as Sharp.

| ![Select_Sharp](img/gifs/select_operators/Select_Sharp.gif) |
| --- |
| Select sharp |

!!! Properties
      ![Select Sharp Props](img/screen/select/SelectSharpProps.png)

 - **Clear Selection** - Clear initial selection
 - **Mode** - Selection type
    - *Select* - Select edges
    - *Deselect* - Deselect edges

---
### Select UV Borders
Select existing UV Borders.

| ![Select_UV_Borders](img/gifs/select_operators/Select_UV_Borders.gif) |
| --- |
| Select UV Borders |

!!! Properties
      ![Select Sharp Props](img/screen/select/SelectUVBordersProperties.png)


- **Clear Selection** - Clear initial selection
- **Mode** - Selection type
    - *All borders* - All UV border edges
    - *By Island* - By selected island
    - *By Faces* - By selected faces

---
### Select Open Edges
Select open edges the way that looks in the 3D viewport. Including the open edges that appeared after the faces were hidden.

| ![Select_Open_Edges](img\gifs\select_operators\Select_Open_Edges.gif) |
| --- |
| Select open edges |

!!! Properties
      ![Select Open Edges Props Props](img/screen/select/SelectOpenEdgesProperties.png)

 - **Clear Selection** - Clear initial selection
 - **Mode** - Selection type
    - *Select* - Select edges
    - *Deselect* - Deselect edges

---
### Select Similar
Select Islands similar to those selected.

| ![Select_Similar](img/gifs/select_operators/Select_Similar.gif) |
| --- |
| Select similar |

!!! Properties
      ![Select Similar Islands](img/screen/select/SelectSimilarIslandsProperties.png)

- **Area Matching** - Set strict requirements to Islands Area Matching when Stacking. Disable this option if the Islands have a slightly different Area
- **Select Primary** - Select Primary Island
- **Select Similar** - Select Similar Islands

---
### Select in Tile
Select Islands in bounding box of active UDIM Tile or UV Area.

| ![Select_In_Tile](img/screen/adv_uv_map/adv_uv_map_udim_select_active.gif) |
| --- |
| Select in tile |

!!! Properties
      ![Select In Tile](img/screen/select/SelectInTileProperties.png)

- **Clear Selection** - Clear initial selection
- **Base** - What to select relative to:
    - *UV Area* - UV Area square
    - *UDIM tile number* - UDIM tile number
    - *Active UDIM* - Active UDIM tile
    - *Any UDIM* - Any UDIM tile
- **Location**
    - *Inside* - Inside of UV Area
    - *Outside* - Outside of UV Area
    - *Cross* - Crossing of UV Area borders
    - *Check Margin* - Select islands where the margin between islands within the defined area and the area itself are less than the specified value.
- **Tile Number** - Number of UDIM tile

---
### Select Half
Select part of the model according to its location relative to the coordinate axis.

| ![Select_Half](img/screen/select/select_half.gif) |
| --- |
| Select half |

| ![Select_Half](img/screen/select/select_half_zero.gif) |
| --- |
| Select half. Include Zero option|

!!! Properties
      ![Select Half](img/screen/select/SelectHalfProperties.png)

- **Clear Selection** - Clear initial selection
- **Axis Direction** - Axis direction
    - *"+"* - Positive
    - *"-"* - Negative
- **Mesh Axis** - The axis along which the selection is made
    - *X* - X Axis
    - *Y* - Y Axis
    - *Z* - Z Axis
- **Include Zero** - Including zero coordinates

---
### Select Quaded Islands
Select islands that consist only of quads.

| ![Select_Quaded_Islands](img\gifs\select_operators\Select_Quaded_Islands.gif) |
| --- |
| Select quaded islands |

!!! Properties
      ![Select Sharp Props](img/screen/select/SelectQuadedIslandsProperties.png)

 - **Clear Selection** - Clear initial selection
 - **Mode** - Selection type
    - *Select* - Select edges
    - *Deselect* - Deselect edges

---
### Select Holed Islands
Selects islands that have holes within their geometry.

| ![Select_Holed_Islands](img\gifs\select_operators\Select_Holed_Islands.gif) |
| --- |
| Select holed islands |

!!! Properties
      ![Select Holed Islands Props](img/screen/select/select_holed_islands_op_prop.png)

- **Clear Selection** - Clear initial selection

!!! Tip
    In most cases, this operator is convenient for identifying islands that can be processed with the Quadrify operator.

---

### Select Cylinder Edges (Splits)
Select island edges that belong to the same mesh edge and split the island by itself.

| ![Cylinder Edges](img\gifs\select_operators\Select_Splits.gif) |
| --- |
| Select splits |

!!! Properties
      ![Select Splits Poperties](img/screen/select/SelectSplitsProperties.png)

 - **Clear Selection** - Clear initial selection
 - **Mode** - Selection type
    - *Select* - Select edges
    - *Deselect* - Deselect edges

### Select Edges by Condition
Select edges based on various conditions and logic operations with NOT support.

| ![Edges by Condition](img\gifs\select_operators\Select_Edges_by_Condition.gif) |
| --- |
| Select edges by condition |

!!! Properties
      ![Select Edges by Condition](img/screen/select/SelectEdgesByConditionProperties.png)

- **Clear Selection** - Clear initial selection
- **Edge Is** - Select first condition
    - *Sharp* - Select edges that are markerd sharp
    - *Seam* - Select edges that are markerd seam
    - *Splits* - Selects edges that belong to the same mesh edge and split the island by itself
    - *Borders* - Select edges that are UV borders
    - *Open* - Select edges that are open. Including those adjacent to hidden faces
- **Second Condition** - Apply second condition (Entering this parameter is optional)
- **Boolean Operation** - boolean logic operator
    - *And*
    - *Or*
    - *Xor*
    - *Nor*
- **Apply Not** - Append logical "Not"
- **Edge Is** - Select second condition
    - *Sharp* - Select edges that are markerd sharp
    - *Seam* - Select edges that are markerd seam
    - *Splits* - Selects edges that belong to the same mesh edge and split the island by itself
    - *Borders* - Select edges that are UV borders
    - *Open* - Select edges that are open. Including those adjacent to hidden faces


---
### Select Edges By Direction
Select edges by direction along U or V axis.

| ![Select_Edges_by_Direction](img/gifs/select_operators/Select_Edges_by_Direction.gif) |
| --- |
| Select edges by direction |

---
### Select Islands By Direction
Select island by direction.

| ![Select Island by Direction](img/gifs/select_operators/Select_Island_by_Direction.gif) |
| --- |
| Select island by direction |

!!! Properties
    ![select Island by Direction](img/screen/select/SelectIslandByDirection.png)

- **Clear Selection** - Clear initial selection
- **Type** - What type of islands will be selected
    - *Horizontal* - Horizontally oriented islands
    - *Vertical* - Vertically oriented islands
    - *Radial* - Islands that are shaped like a circle
    - *Not Aligned* - Islands that are not aligned with the axes

---

### Filter Islands by Property
Filters islands based on specific properties.

| ![Filter Islands by Property Example](img/screen/select/FilterIslands.gif) |
| --- |
| Filter Islands by Property |

!!! Properties
    ![Filter Islands by Property](img/screen/select/filter_islands_by_props_op_prop.png)

    - **Group Method** - Method of defining groups.
        - *Even Split* - Uniform division.
        - *Split by Gaps* - Automatic splitting by gaps.
        - *Auto Split by Gaps* - Automatically determines the number of groups.
    - **Property** - The property by which islands will be grouped.
        - *Island Height* - Grouping based on island height.
        - *Island Width* - Grouping based on island width.
        - *Island Aspect Ratio* - Grouping based on island aspect ratio.
    - **Number of Groups** - Defines how many groups the islands will be divided into.
    - **Group Index** - Specifies which group’s islands should be selected.
    - **Threshold** - Threshold for detecting large gaps (used in **Auto Split by Gaps** mode).


!!! Tip
    This operator is useful when you need to divide a large number of islands into a limited number of zones (e.g., trims).

---

### Select Faces By Normal

Select polygons by reference normal

![Select Faces By Normal Example](img/screen/select/select_faces_by_normal_example.png)

This way, you can select polygons that are "not visible" from the position of the reference normal. If the reference normals are arranged in a cylindrical shape, as shown in the screenshot, you will get a correct selection around the reference normals.

!!! Properties
    ![Select Faces By Normal](img/screen/select/select_faces_by_normal_op_prop.png)

    - **Clear Initial Selection** - Clears the initial selection before applying the operation.
    - **Mode** - Defines how faces are selected based on the reference normal.
        - *Front* - Selects polygons facing the reference normal.
        - *Back* - Selects polygons oriented away from the reference normal.
        - *All* - Selects all polygons that match the reference normal.
    - **Reverse Ref. Normal** - Reverses the reference normal direction.
    - **Threshold** - Controls the accuracy of normal alignment (acts as an angular tolerance).

---

### Select Stretched Faces

Selects faces with stretched UV coordinates

Checks each polygon angle and compares it with the corresponding angle in UV space.  
If the angle exceeds the specified threshold, the polygon will be selected.

![Select Stretched Faces Example](img/screen/select/select_stretched_faces_example.png)

!!! Tip  
    This operator works using the **Overlay → UV Stretch → Angle** algorithm.  
    This means you can easily select what you see or what you might have missed.  
    ![Select Stretched Faces Display](img/screen/select/select_stretched_faces_display.png)

!!! Properties
    ![Select Stretched Faces](img/screen/select/select_stretched_faces_op_prop.png)

- **Influence** - Defines the selection target.
    - *Face* - Selects individual stretched faces.
    - *Island* - Selects entire islands containing stretched faces.
- **Clear Selection** - Clears the initial selection before applying the operation.
- **Threshold** - Defines the minimum stretch factor required for a face to be selected.
- **N-gons Only** - Selects only n-gons (faces with more than four edges).

---

### Select by UV Area
Select faces by their UV area.
The operator consists of two buttons. Where the first is the main operator and the second is an auxiliary operator. You can use it to get the area of the selection.

!!! Panel
    ![Select_By_UV_Area](img/screen/select/sel_by_uv_area_buttons.png)

!!! Properties
    ![](img/screen/select/select_by_uv_area_op_prop.png)

  - **Mode** - What should be selected? Islands or faces.
    - *Island* - Island selection mode
    - *Faces* - Faces selection mode
  - **Clear selection** - Clear the previous selection.
  - **Condition** - The conditions under which the selection will be made.
    - *Zero Area* - Elements with zero area value.
    - *Within range* - Elements, the area of which is within a specified range.
    - *More than* - Elements with an area greater than the specified value.
    - *Equal to* - Elements, the area of which is equal to a specified value.
    - *Less than* - Elements with an area smaller than the specified value.
  - **With Threshold** - Calculation threshold.

---
#### Get Selected Area
After you run this operator, the Multiplied Area value goes into the Select by UV Area operator.

!!! Properties
    ![](img/screen/select/get_selected_area_op_prop.png)


  - **Mode** - The area of what should be obtained? Islands or faces.
    - *Island* - Island selection mode.
    - *Faces* - Faces selection mode.
  - **Average** - Averaging.
  - **Real Area** - The area within the UV Editor is very small. This value shows the real area.
  - **Real UV Area** - Same value as Real Area, but in full size.
  - **Multiplied Area** - The same value as the Real Area, but multiplied for easier use.

---
### Select Zero Area Faces
Selects islands with zero area.

This is the [Select by UV Area](#select-by-uv-area) operator with **Condition - Zero Area** and **Threshold - 0.0 (zero)** activated. You can adjust its settings after execution through the operator properties.

| ![Select Zero Area Faces](img/screen/select/sel_by_uv_area_zero_preset.png) |
| --- |
| Activated preset "select zero area faces" with zero threshold. |

---
### Select Faces Less than Pixel
Selects faces with an area less than the specified number of pixels.

!!! Properties
    ![Select Zero Area Faces](img/screen/select/sel_faces_less_than_pixel_op_prop.png)

- **Clear Selection** - Clear initial selection.
- **Pixel Count** - Number of pixels for the calculation.
- **Area Threshold** - Tolerance level for face area selection.

!!! Warning
    This operator works only in the UV Editor context and requires an active texture in the UV Editor.

---
### Select Self-Intersecting Faces

Select faces that have intersecting uv edges.

When working with **n-gons** or using third-party unwrapping software, situations may arise where polygons overlap themselves.  
This operator allows you to select problematic polygons for further correction.

![Select Self-Intersecting Faces](img/screen/select/self_intersect_example.png)

---
### Select Linked Loops
Only for UV Sync Selection - off. Selects all loops belonging to the mesh vertex based on any already selected loop.

| ![Select Linked Loops](img/gifs/select_operators/Select_Linked_Loops.gif) |
| --- |
| Select Linked Loops |

### Isolate Islands (Toggle)
Isolate Islands (Toggle).

| ![Isolate_Islands](img/gifs/select_operators/Isolate_Islands.gif) |
| --- |
| Isolate islands |

### Isolate Part (Toggle)
Isolate Part (Toggle).

| ![Isolate Part](img/gifs/select_operators/Isolate_Part.gif) |
| --- |
| Isolate mesh part |

---
