# Select

!!! Panel
    | 3D Viewport | UV Editor| 
    |---|---|  
    | ![](img/screen/select/select_main_panel.png) |![](img/screen/select/select_main_panel_uv.png)| 


| Operator | Operator | Operator | Operator |
|   :---:  |   :---:  |  :---:   |  :---:   |
| [Islands](#islands)    | [Int. Loop](#int-loop) | [Cylinder Edges (Splits)](#select-cylinder-edges-splits) | [Edges To Loops](#select-edges-to-loops) |
| [Overlapped](#overlapped) | [Flipped](#flipped)   | [Edges by Condition](#select-edges-by-condition) | [Loop to Face](#convert-loops-to-face) |
| [Seam](#seam) | [Sharp](#sharp) | [Edges by Direction](#select-edges-by-direction) | [Loop to Edge](#convert-loop-to-edge) |
| [Borders](#select-uv-borders) | [Open Edges](#open-edges) | [Island by Direction](#select-islands-by-direction) | [Select Linked Loops](#select-linked-loops) |
| [Similar](#similar) | [Select in Tile](#select-in-tile) | [Select by UV Area](#select-by-uv-area) | [Isolate Islands (Toggle)](#isolate-islands-toggle)|
| [Half](#select-half) | [Quaded Islands](#select-quaded-islands) | [Face To Loops](#select-face-to-loops) ||


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

---
### Select Sharp
Select Edges Marked as Sharp.

| ![Select_Sharp](img/gifs/select_operators/Select_Sharp.gif) |
| --- |
| Select sharp |

---
### Select UV Borders
Select existing UV Borders.

| ![Select_UV_Borders](img/gifs/select_operators/Select_UV_Borders.gif) |
| --- |
| Select UV Borders |

---
### Select Open Edges
Select open edges the way that looks in the 3D viewport. Including the open edges that appeared after the faces were hidden.
| ![Select_Open_Edges](img\gifs\select_operators\Select_Open_Edges.gif) |
| --- |
| Select open edges |

---
### Select Similar
Select Islands similar to those selected.

| ![Select_Similar](img/gifs/select_operators/Select_Similar.gif) |
| --- |
| Select similar |

---
### Select in Tile
Select Islands in bounding box of active UDIM Tile or UV Area.

| ![](img/screen/adv_uv_map/adv_uv_map_udim_select_active.gif) |
| --- |
| Select in tile |

---
### Select Half
Select part of the model according to its location relative to the coordinate axis.

| ![Select_Half](img/screen/select/select_half.gif) |
| --- |
| Select half |

| ![Select_Half](img/screen/select/select_half_zero.gif) |
| --- |
| Select half. Include Zero option|

---
### Select Quaded Islands
Select islands that consist only of quads.

| ![Select_Quaded_Islands](img\gifs\select_operators\Select_Quaded_Islands.gif) |
| --- |
| Select quaded islands |

### Select Cylinder Edges (Splits)
|![Cylinder Edges](img\gifs\select_operators\Select_Splits.gif)|
| --- |
| Select splits |

### Select Edges by Condition
|![Edges by Condition](img\gifs\select_operators\Select_Edges_by_Condition.gif))|
| --- |
| Select edges by condition |

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

### Select by UV Area
The operator consists of two buttons. Where the first is the main operator and the second is an auxiliary operator. You can use it to get the area of the selection.

| ![Select_By_UV_Area](img/screen/select/sel_by_uv_area_buttons.png) |
| --- |
| Select by UV area |

---
#### Select by UV Area:

![](img/screen/select/select_by_uv_area_op_prop.png) |
| --- |
| Operator settings |

  - **Mode** - What should be selected? Islands or faces.
  - **Clear selection** - Clear the previous selection.
  - **Condition** - The conditions under which the selection will be made.
    - **Zero Area** - Elements with zero area value.
    - **Within range** - Elements, the area of which is within a specified range.
    - **More than** - Elements with an area greater than the specified value.
    - **Equal to** - Elements, the area of which is equal to a specified value.
    - **Less than** - Elements with an area smaller than the specified value.
  - **With Threshold** - Calculation threshold.

---
#### Get Selected Area:
After you run this operator, the Multiplied Area value goes into the Select by UV Area operator.

| ![](img/screen/select/get_selected_area_op_prop.png) |
| --- |
| Operator settings |

  - **Mode** - The area of what should be obtained? Islands or faces.
  - **Average** - Averaging.
  - **Real Area** - The area within the UV Editor is very small. This value shows the real area.
  - **Real UV Area** - Same value as Real Area, but in full size.
  - **Multiplied Area** - The same value as the Real Area, but multiplied for easier use.

---
### Select Face to Loops
Convert selected mesh faces to UV loops.
| ![Select Face to Loops](img/gifs/select_operators/Select_Face_to_Loops.gif) |
| --- |
| Select Face to Loops |

---
### Select Edges to Loops
Convert selected mesh edges to UV loops.
| ![Select Edges to Loops](img/gifs/select_operators/Select_Edges_to_Loops.gif) |
| --- |
| Select Edges to Loops |

---
### Convert Loops to Face
Only for UV Sync Selection - off. Convert selected UV loops to mesh face selection.
| ![Convert Loops to Face](img/gifs/select_operators/Select_Loops_to_Face.gif) |
| --- |
| Convert Loops to Face |

---
### Convert Loop to Edge
Only for UV Sync Selection - off. Convert selected UV loop to mesh edge selection.
| ![Convert Loop to Edge](img/gifs/select_operators/Select_Loop_to_Edge.gif) |
| --- |
| Convert Loop to Edge |

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

---
