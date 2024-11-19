bl_info = {
    "name": "Tower Generator",
    "blender": (4, 2, 0),
    "category": "Object",
    "version": (1, 0, 0),
    "author": "RIX Kft.",
    "description": "A Blender script to procedurally generate 3D towers",
}

from . import tower_generator


def register():
    tower_generator.register()


def unregister():
    tower_generator.unregister()


if __name__ == "__main__":
    register()
