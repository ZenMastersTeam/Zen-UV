# Emergency Light
![](../img/tutorial/emergency_light/preview.jpg)

The example is maked as step-by-step guide to cover the basics of Zen UV

## Download Example
1. Download example using [examples panel](../help.md#examples)
2. Open it
3. Switch to edit mode

    ![](../img/tutorial/emergency_light/open_and_edit_mode.gif)

## Reset UV Maps and Unmark All
1. [Unmark all](../unwrap.md#unmark-all) (remove all seams and sharp edges from mesh)
2. Check that all islands are tagged as unfinished
3. Delete all UV maps

    ![](../img/tutorial/emergency_light/reset_uvs.gif)

## Initial Unwrap
1. Deselect all
2. Call [Zen Unwrap](../unwrap.md#zen-unwrap-zen-unwrap)
3. Set 'Mark by angle & Unwrap'

    ![](../img/tutorial/emergency_light/initial_unwrap.gif)

!!! NOTE
    If you didn't see 'Mark by Angle' menu then it was probably something selected in the mesh or mesh was not unmarked properly

## Switch on Checker Texture
1. [Switch on checker texture](../checker.md#checker-texture)
2. [Select 'zen-mono-2048x2048' texture image](../checker.md#checker-textures-selector)
3. [Set only Seams to be displayed in the viewport](../checker.md#blender-draw-system)
4. [Open UV Editor area](../sticky_uv_editor.md#sticky-uv-editor)

    ![](../img/tutorial/emergency_light/switch_on_checker.gif)

## Adjust Viewport For Mapping
1. Close all areas except View3D and UV Editor
2. Unlink checker image in UV Editor for better view of islands

    ![](../img/tutorial/emergency_light/adjust_viewport.gif)

## Unwrap Internal Cylindrical Part
1. Select and isolate cylindrical part of the mesh

    ![](../img/tutorial/emergency_light/isolate_cylinder.gif)

2. Unwrap cap 1 by selected polygons

    ![](../img/tutorial/emergency_light/unwrap_cap_1.gif)

3. Unwrap tube by selected edge

    ![](../img/tutorial/emergency_light/unwrap_tube.gif)

4. Unwrap cap 2 by selected polygons

    ![](../img/tutorial/emergency_light/unwrap_cap2.gif)

5. Merge islands by re-unwrap

    ![](../img/tutorial/emergency_light/merge_islands.gif)

6. [Quadrify rectangular-shaped islands](../transform.md#quadrify-islands)

    ![](../img/tutorial/emergency_light/quadrify_1.gif)

7. [Pack islands](../pack.md#pack-islands)
8. [Tag as finished](../unwrap.md#tag-finished)

    ![](../img/tutorial/emergency_light/pack_tag_finished.gif)

## Unwrap External Cover
1. [Isolate](../select.md#isolate-islands-toggle) external cover mesh part

    ![](../img/tutorial/emergency_light/isolate_external_cover.gif)

2. Re-unwrap mesh to separate rectangular-shaped island

    ![](../img/tutorial/emergency_light/external_cover_unwrap_1.gif)

3. Quadrify created island

    ![](../img/tutorial/emergency_light/external_cover_quadrify.gif)

4. Unwrap by side cuts

    ![](../img/tutorial/emergency_light/unwrap_by_side_cuts.gif)

5. Unwrap by creating project from view

    ![](../img/tutorial/emergency_light/project_from_view.gif)

6. Pack islands and tag as finished

    ![](../img/tutorial/emergency_light/external_cover_tag_as_finished.gif)

## Unwrap Small Parts
1. Isolate small mesh parts

    ![](../img/tutorial/emergency_light/small_parts_isolate.gif)

2. Unwrap by cuts

    ![](../img/tutorial/emergency_light/small_parts_unwrap_cuts.gif)

3. Unwrap part by selected polygons

    ![](../img/tutorial/emergency_light/small_parts_unwrap_by_polygons.gif)

4. Unwrap by cut to get rectangular shape

    ![](../img/tutorial/emergency_light/small_parts_unwrap_to_get_quad.gif)

5. Quadrify rectangular-shaped islands

    ![](../img/tutorial/emergency_light/small_parts_quadrify.gif)

6. Pack islands and tag as finished

    ![](../img/tutorial/emergency_light/small_parts_pack_and_finished.gif

## Unwrap Wires
1. Select and isolate islands

    ![](../img/tutorial/emergency_light/wires_isolate.gif)

2. Unwrap by selected polygons

    ![](../img/tutorial/emergency_light/wires_unwrap.gif)

3. Quadrify
4. Tag as finished

    ![](../img/tutorial/emergency_light/wires_quadrify.gif)

## Unwrap Handle
1. Select and isolate islands

    ![](../img/tutorial/emergency_light/handle_isolate.gif)

2. Unwrap to create one island

    ![](../img/tutorial/emergency_light/handle_create_one_island.gif)

3. Create cuts and unwrap

    ![](../img/tutorial/emergency_light/handle_create_cuts.gif)

4. [Relax](../transform.md#relax) island

    ![](../img/tutorial/emergency_light/handle_relax.gif)

5. [Orient by selected](../transform.md#rotate)

    ![](../img/tutorial/emergency_light/handle_orient_by_selected.gif)

6. Make rectangular-shaped island:
    - align and distribute surrounded vertices
    
        ![](../img/tutorial/emergency_light/handle_align_and_distribute.gif)

    - unwrap with 'Unfold Vertices' mode

        ![](../img/tutorial/emergency_light/handle_unwrap_unfold_vertices.gif)

7. Tag as finished

    ![](../img/tutorial/emergency_light/handle_tag_finished.gif)

## Final Pack
1. Unhide all
2. Select all
3. Pack

    ![](../img/tutorial/emergency_light/pack_tag_finished.gif)

## Reduce UV Space With Stacks
1. Select islands that can be identified as [replicas](../stack.md#replicas)

    ![](../img/tutorial/emergency_light/stack_select_replicas.gif)

2. Hide replicas
3. Set texture size for packing
4. Set corresponding margin for packing
5. Pack islands

    ![](../img/tutorial/emergency_light/stack_pack_islands.gif)

6. [Stack](../stack.md#stack) selected replicas

    ![](../img/tutorial/emergency_light/stack_do_stack.gif)

## Set Sharp Edges
1. Set [sharp by UV borders](../unwrap.md#sharp-by-uv-borders)
2. Mark
3. Enable option 'Unmark sharp'
4. [Smooth by sharp](../unwrap.md#smooth-by-sharp-toggle)

    ![](../img/tutorial/emergency_light/sharp_by_uv_borders.gif)
