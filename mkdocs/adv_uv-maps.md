# Advanced UV Maps
Advanced UV Maps section created to have quick access to Object Data Properties — UV Maps.
It allows to select the active, add, remove, and rename UV Maps from the list.

If more than one object is selected, you can synchronously work with UV maps of the selected objects.

!!! Panel
    ![Advanced UV Map](img/screen/adv_uv_map/adv_uv_map.png)

!!! tip
    Watch the video explaining how **Advanced UV Maps** works.

    <div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%;">
    <iframe src="https://www.youtube.com/embed/Y7dG2i-FASs?start=541&end=619" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" allowfullscreen="" seamless="" frameborder="0"></iframe>
    </div>

---
## Clean UV Maps
Remove inactive UV Map.

!!! tip
    Hold [Zen Modifier Key](addon_prefs.md/#zen-modifier-key) (default 'Alt') to apply on all selected objects.

---
## Rename UV Maps
Rename UV Map using pattern. The pattern can be defined in the operator popup.

![](img/screen/adv_uv_map/rename_uv_maps_popup.png)

   - **Name** - The pattern.
   - **Use Default Name** - Use the native name defined in Blender.
   - **Use Numbering** - Add numbers to the end of the name.
   - **Active Only** - Rename Active UV Maps only.

!!! tip
    Hold [Zen Modifier Key](addon_prefs.md/#zen-modifier-key) (default 'Alt') to apply on all selected objects.

---
## Duplicate active UV Map ![Add Button](img/icons/plus.png)
Duplicate the active UV Map or create a new one depending on the operator's properties.
![](img/screen/adv_uv_map/duplicate_active_map.png)

!!! tip
    Hold [Zen Modifier Key](addon_prefs.md/#zen-modifier-key) (default 'Alt') to apply on all selected objects.

---
## Remove active UV Map ![Remove Button](img/icons/minus.png)
Remove active UV Map.

!!! tip
    Hold [Zen Modifier Key](addon_prefs.md/#zen-modifier-key) (default 'Alt') to apply on all selected objects.

---
## Sync UV Maps IDs ![Sync Button](img/icons/adv_uv_sync.png)
Set the same active UV Map index for all selected objects.
Alt + Click - activates automatic synchronization mode.

In automatic synchronization mode:

   ![True Sync Button](img/icons/adv_uv_sync_true.png) If the background of the button is blue, the UVs are synchronized.

   ![False Sync Button](img/icons/adv_uv_sync_false.png) If the background of the button is purple, the UVs are out of sync.

---

## Copy UV / Paste UV

Allows transferring the UV coordinates between UV Maps.

![](img/screen/adv_uv_map/uv_copy_paste.png)

**Copy UV** - Copy the UV coordinates of the selection.

**Paste UV** - Paste the UV coordinates.