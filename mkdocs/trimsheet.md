# Trim Sheets

## What is a trim sheet?
Trim sheets are a common technique to increase your texture quality on 3D assets while at the same time reducing the number of materials/textures on them. Trim sheets are a way to texture many assets with just a single set of textures, allowing for very efficient use of texture memory.

The Trim Sheet process is basically creating a texture that allows you to apply different details (from the same texture) to a model. This texture can be used on multiple objects, or even just one large one, with fantastic quality results. 
Most AAA games use this technique a lot on environment assets in order to have fantastic quality, save time on development, keep assets together with a set theme, and many other reasons.

| ![img](img/screen/trimsheet/intro.png) |
|---|

## Why would you use a trim sheet?
The main thing which make trim sheets valuable is their reusability. If you have a scene with lots
of recurring elements those are ideal candidates for a trim sheet.

| ![img](img/screen/trimsheet/coridor_elements.png) |
|---|

## [Creating your trim sheet with Zen UV](trimsheet_creation.md)
Zen UV addon provides all necessary tools to create your trim sections

!!! Preview
    ![](img/screen/trimsheet/trimsheet_editor.png)