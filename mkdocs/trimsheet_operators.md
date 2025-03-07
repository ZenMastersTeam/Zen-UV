# Trim Sheet Operators

!!! Panel
    ![](img/screen/trimsheet/trim_operators.png)

## Mesh Selection Mode
The mode defines the behaviour what part of mesh will be transformed

### Islands
Islands that has selected mesh elements are transformed in the mode

| ![](img/screen/trimsheet/mode_selection_islands.gif) |
|---|
| |

## Processing Order
### One By One
Islands are processed with separate pivots

| ![](img/screen/trimsheet/trim_one_by_one.gif) |
|---|
| |

### Overall
All islands are processed with the same pivot

| ![](img/screen/trimsheet/trim_overall.gif) |
|---|
| |

### Selection
Only selected mesh elements are transformed in the mode

| ![](img/screen/trimsheet/mode_selection.gif) |
|---|
| |

## Move In Trim
Move islands inside active trim. Islands outside active trim will be ignored if **Lock in Trim** option is set

## Rotate In Trim
Rotate islands inside active trim

## Flip In Trim
Flip islands relative to the center of active trim

| ![](img/screen/trimsheet/flip_in_trim.gif) |
|---|
| |

## Fit To Trim
Fit islands into active trim

| ![](img/screen/trimsheet/fit_to_trim.gif) |
|---|
| |

## Align To Trim
Align islands to active trim

| ![](img/screen/trimsheet/align_to_trim.gif) |
|---|
| |

## Scale In Trim
Scale in active trim. Islands outside active trim will be ignored if **Lock in Trim** option is set

| ![](img/screen/trimsheet/scale_in_trim.gif) |
|---|
| |

## Hotspot Mapping
Hotspot Mapping is a UV mapping method that compares the parameters of Islands and Trims and makes automatic mapping based on the given settings.

[**Follow the link**](trimsheet_hotspot.md) to find more information about Hotspot Mapping.

## Select Trim By Face
Select and activate trim by selected face

## Select Islands By Trim
Select islands inside active trim

---
## Directional Hotspot Mapping

![Directional hotspot panel](img/screen/trimsheet/directional_hotspot_panel.png)

### Directional Hotspot Operator

Hotspot mapping using island normal vector.

!!! Properties
    ![Directional Hotspot Operator](img/screen/trimsheet/directional_hotspot_op_prop.png)

    - **Mode** – Defines which trims will be used for mapping.  
        - *All Trims* – Uses all available trims.  
        - *Selected Trims* – Uses only the selected trims.  
    - **Orient** – Determines island rotation before mapping.  
        - *As Is* – No rotation applied.  
        - *Orient to World* – Aligns the island to the world axis.  
        - *Orient to Axis* – Auto-orients the island to the nearest axis.  
    - **Threshold** – Defines how precisely the island's normal must match the trim's normal for mapping.  
    - **Keep Proportion** – Prevents stretching or squashing by maintaining the original aspect ratio of the UV islands.  
    - **Allow Location Variation** – If enabled, islands may be placed in different trims that have similar size and orientation parameters. If disabled, islands are strictly mapped to their assigned trims.  
    - **Allow Scaling** – Automatically scales UV islands to fit the target trim while preserving proportions (unless 'Keep Proportion' is disabled).  
    - **Select Processed** – After applying the mapping, this option highlights the UV islands that were successfully adjusted to trims.  
    - **Seed** – Sets a seed value for the randomization algorithm, ensuring consistent placement variations of islands in similar trims.  


    - **Orient** - Perform some Island rotation before Hotspotting

---
### **Normals To Trim**

Retrieve the normal vector from the selected face and apply it to the active trim.

!!! Properties  
    ![Normals To Trim](img/screen/trimsheet/normals_to_trim_op_prop.png)  

- **Average Normal Value** – If enabled, calculates the average normal when multiple faces are selected.  
  If disabled, only the normal of the active face will be applied to the trim.  
