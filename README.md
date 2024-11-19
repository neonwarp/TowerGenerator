# Tower Generator Addon for Blender

This Blender addon allows users to procedurally generate towers in the middle of the viewport. The towers come with various attributes and can be either cubic or cylindrical in shape. Random attributes, such as damage, range, cost, and attack speed, are assigned to each tower. Additionally, the towers are adorned with modifiers to resemble windows or bricks.

## Installation

- Open Blender and go to `Edit > Preferences > Add-ons`.
- Click `Install from Disk`, navigate to where you saved the zip, and select it.
- Enable the addon by clicking the checkbox next to its name in the addon list.

## Usage

Press Shift + A to open the "Add" menu in the 3D Viewport.

Navigate to the "Mesh" section and select "Generate Tower".

A randomly generated tower will be placed in the center of the viewport.

### Build and verify

```sh
blender --command extension build
```

```sh
blender --command extension validate .\tower_generator-1.0.0.zip
```