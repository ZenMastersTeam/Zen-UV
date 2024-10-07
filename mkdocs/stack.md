# Stack

This panel contains tools for grouping similar islands into stacks.

!!! Panel
    ![Stack](img/screen/stack/stack_main_panel.png)

!!! tip
    Watch the video explaining how **Stack** works.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/Yj2SecY-c1Y?start=142&end=313" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div>

## Stack operator

!!! Properties
    ![Stack](img/screen/stack/stack_options.png)

- **Move Only** - Don't fit Islands. Just move to the same position.
- **Stack Offset** - The offset value. Can be used for preventing auto merging the UV vertices.
- **Unstack Direction** - The Direction where the island will be shifted.

## Unstack operator

Shift Islands from Stacks in a given direction.

!!! Properties
    ![unstack properties](img/screen/stack/unstack_properties.png)

- **Mode** - Mode to Unstack Islands
    - *Global* - Unstack all Similar Islands
    - *Stacked* - Unstack Stacked Islands
    - *Overlapped* - Unstack Overlapped Islands
    - *Selected* - Unstack Selected Islands
- **Only UV Area** - Unstack islands located in the UV Area only
- **Iterative Unstack** - Unstack Islands iteratively with moving in given direction
- **Use Seams** - Use seams as an island separator to prevent stacked islands from self-welding
- **Direction** - The unstack direction
- **Break Stacks** - Shift Islands from Stacks by given increment until all of them will be individually placed
- **Unstack Increment** -  Is a value that gradually separates stacked elements in incremental steps.

## Stack Mode

!!! Panel
    ![](img/screen/stack/stack_modes.png)

- **Global Mode** - Collect all Similar Islands on Stacks.
- **Selected Mode** - Collect selected Similar Islands on Stacks.
- **Simple Mode** - Collect selected islands in the stack, with no respect for their topology.

## Stacks 

There are 3 different types of Stacked Islands. You can select all of them in this panel.

![](img/screen/stack/stack_types.png)

### Primaries
Primaries this is islands which detected as a better instance. The position and the topology from Primaries will be translated to the Replicas. The island is defined as Primary if its position is closer to the center of coordinates, and the distortion of topology is less compared to other similar islands.

### Replicas

Replicas are islands that have the same topology but were not chosen as Primary. The position and topology of the Replicas will be changed in the process of Stacking.

### Singles

Singles this is islands that have no similar islands.

## Stacks Display

![](img/screen/stack/stack_display.png)

### Similar

Display all Similar Islands.

### Similar of Selection

Display and Select Similar Islands from Selected Islands.

### Stacked

Display and Select Stacked Islands.


!!! Options

    **Options for Stacked Islands**

    ![Display Stacked](img/screen/stack/stack_display_stacked_options.png)

- **Overlay Sync** - Draw is sincronized with Overlay On/Off mode.
- **Stacked Color** - Color for displaying Stacked Islands.
- **Only UV Area** - Display Stacks only in the UV area.

---

### UV Island Counter

Count UV islands in selected objects and display the result. With this operator, you can easily find out how many islands are in the stack.

Here you will find [full information](checker.md#uv-islands-counter) about this operator.

---

## Copy / Paste System

 - **Copy** - Copy parameters of selected Islands/Faces and save them.

 - **Paste** - Paste the parameters saved earlier to selected Islands/Faces.

[Here is full information](operators/stack_copy_paste.md) about Copy / Paste System.

---

## Manual Stack

!!! Panel
    ![Panel](img/screen/stack/stack_manual_stack.png)


### Area Matching ![Area Matching](img/icons/a.png)

Set strict requirements for Islands Area Matching when Stacking. Disable this option if the Islands have a slightly different Area.


### Move Only ![Move Only](img/icons/m.png)

Don't fit Islands. Just move to the same position.

### Add ![Add](img/icons/plus.png)

Add new Stack.

### Delete ![Delete](img/icons/minus.png)

Delete selected Stack.

### Add Islands ![Add Islands](img/icons/download.png)

Append selected Islands to the active Stack.

### Select Islands ![Add Islands](img/icons/select_bl_ico.png)

Select Islands in the Stack

### Analyze Stack ![Analyse Stack](img/icons/analyse.png)

Analyze Islands Similarities in the Stack. You can find details in the Zen UV Manual Stack Analyze document in the Text Editor.

### Remove All ![Remove All](img/icons/trash.png)

Remove all Manual Stacks from selected Objects.

### Stack

Collect Islands on Manual Stacks.

### Unstack

Shift Islands from Manual Stacks in a given direction.

### Stack Mode

- **Global Mode**. Collect all Similar Islands on Stacks.
- **Selected Mode**. Collect selected Similar Islands on Stacks.

### Display Manual Stacks

Display Manual Stacks (Static)
