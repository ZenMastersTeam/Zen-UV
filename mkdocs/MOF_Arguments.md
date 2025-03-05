# Ministry OF Flat UnWrapConsole3.exe Documentation for version 3.7.2

It only takes .obj files, but most tools can import and export obj-files, so it should work for most usages.

## UI Version

To change the camera, press the right mouse button. Right + Left dollys, and Right + Middle pans. Multi-touch camera controls also work (two fingers to tumble/zoom and three to pan), as well as standard Maya camera controls by pressing **Alt + mouse buttons**.

Click in empty space to switch between 3D and UV view.

## Contact and Feedback

If you encounter any issues, please mail me, and if possible, send me the mesh you have problems with. If you can't send the mesh, a screenshot will also do. If you are having problems, you can turn on the **"validate"** option in the settings. This will run a bunch of validation steps and output any errors it finds in the `betray_stdout.txt` file. It only gets better if I know what’s wrong with it!

UV mapping is subjective, so if you have opinions, please let me know. If you think it sucks, **LET ME KNOW** and tell me why.  

> **Note:** I am more focused on hand-made meshes with good topology than on scanned meshes, so that will remain my focus for now.

Follow me on Twitter at **[@quelsolaar](https://twitter.com/quelsolaar)**. I will post when I release new versions and when issues are fixed.

If you are interested in **Licensing the full version**, contact **license@ministryofflat.com**.

---

# Settings

## Texture Resolution
- **Description:** Resolution of texture, to give the right amount of island gaps to prevent bleeds.
- **Command-line usage:** `-RESOLUTION <VALUE>`
- **Default value:** `1024`

## Separate Hard Edges
- **Description:** Guarantees that all hard edges are separated. Useful for lightmapping and normal mapping.
- **Command-line usage:** `-SEPARATE <TRUE/FALSE>`
- **Default value:** `FALSE`

## Aspect
- **Description:** Aspect ratio of pixels. For non-square textures.
- **Command-line usage:** `-ASPECT <VALUE>`
- **Default value:** `1.000000`

## Use Normal
- **Description:** Use the model’s normals to help classify polygons.
- **Command-line usage:** `-NORMALS <TRUE/FALSE>`
- **Default value:** `FALSE`

## UDIMs
- **Description:** Split the model into multiple UDIMs.
- **Command-line usage:** `-UDIMS <VALUE>`
- **Default value:** `1`

## Overlap Identical Parts
- **Description:** Overlap identical parts to take up the same texture space.
- **Command-line usage:** `-OVERLAP <TRUE/FALSE>`
- **Default value:** `FALSE`

## Overlap Mirrored Parts
- **Description:** Overlap mirrored parts to take up the same texture space.
- **Command-line usage:** `-MIRROR <TRUE/FALSE>`
- **Default value:** `FALSE`

## Scale UV Space to Worldspace
- **Description:** Scales the UVs to match their real-world scale, going beyond the zero-to-one range.
- **Command-line usage:** `-WORLDSCALE <TRUE/FALSE>`
- **Default value:** `FALSE`

## Texture Density
- **Description:** If worldspace is enabled, this value sets the number of pixels per unit.
- **Command-line usage:** `-DENSITY <VALUE>`
- **Default value:** `1024`

## Seam Direction
- **Description:** Sets a point in space that seams are directed toward. By default, it's the center of the model.
- **Command-line usage:** `-CENTER <X VALUE> <Y VALUE> <Z VALUE>`
- **Default value:** `0.000000 0.000000 0.000000`

---

## Debugging Settings

> **Warning:**  
> All following settings are for debugging purposes only.  
> Making any change to these settings is likely to result in worse UV mapping and/or longer processing time.

### Suppress Validation Errors
- **Description:** Faulty geometry errors will not be printed to standard output.
- **Command-line usage:** `-SUPRESS <TRUE/FALSE>`
- **Default value:** `FALSE`

### Quads
- **Description:** Searches the model for triangle pairs that make good quads. Improves the use of patches.
- **Command-line usage:** `-QUAD <TRUE/FALSE>`
- **Default value:** `TRUE`

### Vertex Weld
- **Description:** Merges duplicate vertices. Does not affect the output polygon or vertex data.
- **Command-line usage:** `-WELD <TRUE/FALSE>`
- **Default value:** `TRUE`

### Flat Soft Surface
- **Description:** Detects flat areas of soft surfaces in order to minimize distortion.
- **Command-line usage:** `-FLAT <TRUE/FALSE>`
- **Default value:** `TRUE`

### Cones
- **Description:** Searches the model for sharp cones.
- **Command-line usage:** `-CONE <TRUE/FALSE>`
- **Default value:** `TRUE`

### Cone Ratio
- **Description:** The minimum ratio of a triangle used in a cone.
- **Command-line usage:** `-CONERATIO <VALUE>`
- **Default value:** `0.500000`

### Grids
- **Description:** Searches the model for grids of quads.
- **Command-line usage:** `-GRIDS <TRUE/FALSE>`
- **Default value:** `TRUE`

### Strips
- **Description:** Searches the model for strips of quads.
- **Command-line usage:** `-STRIP <TRUE/FALSE>`
- **Default value:** `TRUE`

### Tubes
- **Description:** Finds tube-shaped geometry and unwraps it using cylindrical projection.
- **Command-line usage:** `-TUBES <TRUE/FALSE>`
- **Default value:** `TRUE`

### Packing
- **Description:** Packs islands into a rectangle.
- **Command-line usage:** `-PACKING <TRUE/FALSE>`
- **Default value:** `TRUE`

### Packing Iterations
- **Description:** How many times the packer will pack the islands to find the optimal spacing.
- **Command-line usage:** `-PACKING_ITERATIONS <VALUE>`
- **Default value:** `4`

### Validate
- **Description:** Validates geometry after each stage and prints out any issues found (**for debugging only**).
- **Command-line usage:** `-VALIDATE <TRUE/FALSE>`
- **Default value:** `FALSE`
