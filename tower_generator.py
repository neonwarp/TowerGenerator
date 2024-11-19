import bpy
import random


class Tower:
    def __init__(self, name, damage, range, cost, attack_speed, location):
        self.name = name
        self.damage = damage
        self.range = range
        self.cost = cost
        self.attack_speed = attack_speed
        self.location = location

    def create_blender_object(self):
        tower_type = random.choice(["cube", "cylinder"])
        if tower_type == "cube":
            bpy.ops.mesh.primitive_cube_add(size=2, location=self.location)
        elif tower_type == "cylinder":
            bpy.ops.mesh.primitive_cylinder_add(
                radius=1, depth=4, location=self.location
            )

        obj = bpy.context.object
        obj.name = self.name
        obj["damage"] = self.damage
        obj["range"] = self.range
        obj["cost"] = self.cost
        obj["attack_speed"] = self.attack_speed

        modifier = obj.modifiers.new(name="Bevel", type="BEVEL")
        modifier.width = 0.1
        modifier.segments = 3

    def __str__(self):
        return (
            f"Tower: {self.name}\n"
            f"  Damage: {self.damage}\n"
            f"  Range: {self.range}\n"
            f"  Cost: {self.cost}\n"
            f"  Attack Speed: {self.attack_speed}\n"
        )


def generate_tower(location):
    tower_names = [
        "Archer Tower",
        "Cannon Tower",
        "Magic Tower",
        "Laser Tower",
        "Poison Tower",
    ]
    name = random.choice(tower_names)

    damage = random.randint(10, 100)
    range = random.randint(50, 200)
    cost = random.randint(50, 300)
    attack_speed = round(random.uniform(0.5, 2.0), 2)

    return Tower(name, damage, range, cost, attack_speed, location)


def generate_tower_operator():
    location = (0, 0, 0)
    tower = generate_tower(location)
    tower.create_blender_object()
    return tower


class OBJECT_OT_generate_tower(bpy.types.Operator):
    bl_idname = "object.generate_tower"
    bl_label = "Generate Tower"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        generate_tower()
        return {"FINISHED"}


def menu_func(self, _):
    self.layout.operator(OBJECT_OT_generate_tower.bl_idname, icon="MESH_CYLINDER")


def register():
    bpy.utils.register_class(OBJECT_OT_generate_tower)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_generate_tower)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
