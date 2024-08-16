# Emergency Light
![](../img/tutorial/emergency_light/preview.jpg)

The example is maked as step-by-step guide to cover the basics of Zen UV

## Download Example
1. Використовуючи [examples panel](../help.md#examples) виберіть та скачайте приклад що звется Emergency Light Tutorial натиснувши на кнопку Download справа від назви
2. Коли сцена скачається, натисніть кнопку Open що з`явилася на місці кнопки Download
3. Виберіть об'єкт з назвою Emergency Light та перейдіть в режим редагування

    ![](../img/tutorial/emergency_light/open_and_edit_mode.gif)

## Reset UV Maps and Unmark All
1. По замовчуванню Zen UV використовує [систему глобального маркування](../unwrap.md#mark-by-angle). Зробимо налаштування так, щоб Seam та Sharp маркувалися одночасно. Перейдіть на вкладку [Unwrap](../unwrap.md). Налаштування знаходяться в меню на кнопці з шестернею справа від кнопки Mark by Angle. Відкрийте меню та активуйте опцію Mark Sharp Edges
2. Для того щоб стерти всі наявні Seams та Sharp, у вкладці [Unwrap](../unwrap.md) натисніть кнопку [Unmark all](../unwrap.md#unmark-all)
3. Перевіримо чи немає островів що теговані як Finished. Система Finished служить для візуального контролю за станом островів (закінчені/не закінчені) та не дозволяє оператору Zen Unwrap розгортати острови якщо вони теговані як Finished.
Виділіть всі полігони у моделі. У вкладці [Unwrap](../unwrap.md) розгорніть панель з назвою Finished та натисніть кнопку Tag Uninished.
4. Щоб стерти можливі наявні UV координати, перейдіть у вкладку [Advanced UV Maps](../adv_uv-maps.md), виділіть всі можливі наявні UV Maps, та натисніть кнопку "-". Нема необхідності створювати нову UV Map. Zen UV працює з UV координатами а от же слідкує за тим, щоб були наявні UV Maps. Якщо таких немає, то вони будуть створені автоматично.

    ![](../img/tutorial/emergency_light/reset_uvs.gif)

## Initial Unwrap
1. Зараз, коли все підготовлено, ми можемо починати робити розгортку. Етап перший це розділення моделі на UV острови. На цьому етапі не має значення наскільки ці острови коректно розгорнуті. Ми тільки розділяємо. Зробимо розмітку швів в залежності від гостори edge. Більш гострі edges будуть помічені як шви і тим самим зададуть місця де модель буде розділена. То ж у вкладці [Unwrap](../unwrap.md) натисніть кнопку Mark By Angle.
2. Ми створили шви в залежності від гостроти edge але ще не розділили модель на острови. Для розділення використаємо оператор [Zen Unwrap](../unwrap.md#zen-unwrap-zen-unwrap) який працює в залежності від того, що виділено. То ж на даному етапі переконайтеся що нічого не виділено. В режимі коли нічого не виділено [Zen Unwrap](../unwrap.md#zen-unwrap-zen-unwrap) просто розділяє модель на UV острови по існуючим seams. Якщо щось виділено, результат буде інакшим. Якщо все вірно, натисніть [Zen Unwrap](../unwrap.md#zen-unwrap-zen-unwrap) з панелі [Unwrap](../unwrap.md). Інші режими робти [Zen Unwrap](../unwrap.md#zen-unwrap-zen-unwrap) ми розглянемо в продовж цього туторіалу.

    ![](../img/tutorial/emergency_light/initial_unwrap.gif)


## Switch on Checker Texture
1. На цьому етапі ми маємо базове розділення моделі на острови але цього не достатньо. Потрібно візуально перевірити модель, створити додаткові острови, та в процесі розправити вже існуючі острови якщо це необхідно. На цьому етапі важливо покращити сприйняття атрефактів для того щоб виконати роботу якнайшвидше. Одним з самих дієвих методів є призначення спеціальної текстури що складається з квадратів. Якщо ви бачите на моделі не квадрат а щось інше, значить в цьому місці є проблеми з розглажуванням острову. Накладемо цю спеціальну текстуру використовуючи [Zen UV Checkr](../checker.md) на панелі [UV Checker](../checker.md) натисніть кнопку Checker Texture.
2. Кольорові текстури створені також і для визначення місця положення острову на текстурі. Але для нашого випадку це не має значення. То ж перемкнем текстуру на монохромну. Це зменшить кількість інформації для сприйтяття а отже зменшить втому від роботи. Відкрийте drop-down меню нижче кнопки "Checker Texture" та виберіть текстуру з назвою ['zen-mono-2048x2048' texture image](../checker.md#checker-textures-selector)
3. Наступний крок не важливий для цієї моделі, але може знадобиться в майбутньому. Вимкнемо відображення всіх типів edges крім seam. Це копії нативної системи відображення але тепер вони в близькому доступі на панелі UV Checker. Пам'ятаємо про втому від збитку інформації.[Set only Seams to be displayed in the viewport](../checker.md#blender-draw-system)
4. Майже всі операції в Zen UV можуть бути виконані у 3D View але нема більш комфортного способу взємодіяти з UV Maps ніж використати UV Editor. Для того щоб швидко відкрити UV Editor, натисніть на кнопку розміщену зліва по центру 3D View viewport з літерою "T". У випадку якщо UV Editor уже відкритий, після натискання на цю кнопку він закриється. [Open UV Editor area](../sticky_uv_editor.md#sticky-uv-editor)

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
