# Select

!!! Panel
    | 3D Viewport | UV Editor| 
    |---|---|  
    | ![](img/screen/select/select_main_panel.png) |![](img/screen/select/select_main_panel_uv.png)| 

!!! Tip 
    Select **Seam** and **Sharp** are absent on the panel in **UV Editor**.
    To use these operators you need to switch to **3D Viewport** context. 

---
### Islands ![](img/icons/select.png)
Select Islands by selected edge/face of the Islands.

![Select_Islands](img/gifs/select_operators/Select_Islands.gif)

### Int. Loop
Inter seam loop. Select Edge Loop with respect to Seams. 

![Select_Int_Loop](img/gifs/select_operators/Select_Int_Loop.gif)

### Overlapped
Select Overlapped Islands.

![Select_Overlapped](img/gifs/select_operators/Select_Overlapped.gif)

### Flipped
Select Flipped Islands.

![Select_Flipped](img/gifs/select_operators/Select_Flipped.gif)

### Seam
Select Edges Marked as Seams.

![Select_Seam](img/gifs/select_operators/Select_Seam.gif)

### Sharp
Select Edges Marked as Sharp.

![Select_Sharp](img/gifs/select_operators/Select_Sharp.gif)

### Select UV Borders
Select existing UV Borders.

![Select_UV_Borders](img/gifs/select_operators/Select_UV_Borders.gif)

### Similar
Select Islands similar to those selected.

![Select_Similar](img/gifs/select_operators/Select_Similar.gif)

### Select in Tile
Select Islands in bounding box of active UDIM Tile or UV Area.

![](img/screen/adv_uv_map/adv_uv_map_udim_select_active.gif) 

### Select Half
Select part of the model according to its location relative to the coordinate axis.

![Select_Half](img/screen/select/select_half.gif)

![Select_Half](img/screen/select/select_half_zero.gif)

### Select Edges By Direction
Select edges by direction along U or V axis.

![Select_Edges_by_Direction](img/gifs/select_operators/Select_Edges_by_Direction.gif)

### Select by UV Area
The operator consists of two buttons. Where the first is the main operator and the second is an auxiliary operator. You can use it to get the area of the selection.

![Select_By_UV_Area](img/screen/select/sel_by_uv_area_buttons.png)



---
#### Operator Select by UV Area:

![](img/screen/select/select_by_uv_area_op_prop.png)

  - **Mode** - What should be selected? Islands or faces.
  - **Clear selection** - Clear the previous selection.
  - **Condition** - The conditions under which the selection will be made.
    - **Zero Area** - Elements with zero area value.
    - **Within range** - Elements, the area of which is within a specified range.
    - **More than** - Elements with an area greater than the specified value.
    - **Equal to** - Elements, the area of which is equal to a specified value.
    - **Less than** - Elements with an area smaller than the specified value.
  - **With Threshold** - Calculation threshold.

#### Operator Get Selected Area:
After you run this operator, the Multiplied Area value goes into the Select by UV Area operator.

![](img/screen/select/get_selected_area_op_prop.png)

  - **Mode** - The area of what should be obtained? Islands or faces.
  - **Average** - Averaging.
  - **Real Area** - The area within the UV Editor is very small. This value shows the real area.
  - **Real UV Area** - Same value as Real Area, but in full size.
  - **Multiplied Area** - The same value as the Real Area, but multiplied for easier use.

### Isolate Islands (Toggle)
Isolate Islands (Toggle).

![Isolate_Islands](img/gifs/select_operators/Isolate_Islands.gif)
