# Blender Character Generation Script

## Question 1: Could you create a script, advanced script in Blender, let's suppose, that would be like a modeler?

Sure! I can guide you through creating an advanced Blender script that acts as a modeler. Blender uses Python as its scripting language, so the script will generate some 3D geometry based on user input. Let's create a script that allows the user to define some basic parameters (like radius, height, subdivisions, etc.) and then generates a 3D shape like a parametric cylinder or some more advanced geometry.

Here’s a basic idea of what the script could do:

1. **Define User Inputs:** Radius, height, number of subdivisions (complexity), and other customizable options.
2. **Generate Geometry:** Use Blender’s `bpy` module to create and manipulate mesh objects.
3. **Apply Modifiers:** Add modifiers like subdivision surface, boolean, or bevel for advanced modeling.
4. **Add Custom Shape Logic:** For example, the user could create different shapes based on conditions (like switching between different primitive types).

Here’s an example of such a script in Blender that could generate a customizable parametric shape (a kind of cylinder) with user-defined parameters:

```python
import bpy
import math

# Function to create a parametric shape (a customized cylinder)
def create_parametric_cylinder(radius=1, height=2, subdivisions=32, taper=1):
    # Create a new mesh and object
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=height, vertices=subdivisions)
    obj = bpy.context.object
    mesh = obj.data

    # Access the vertices of the mesh
    for vert in mesh.vertices:
        # Taper the cylinder using the taper parameter
        factor = (1 - (vert.co.z / height)) * taper
        vert.co.x *= factor
        vert.co.y *= factor

    return obj

# Function to apply a modifier to the object
def add_modifier(obj, modifier_type, properties={}):
    # Add a modifier of the specified type
    mod = obj.modifiers.new(name=modifier_type, type=modifier_type)

    # Apply properties to the modifier
    for prop, value in properties.items():
        setattr(mod, prop, value)

    # Apply the
```

## Question 2: I was thinking rather about full character generation

Creating a full character generation script in Blender is a more complex task, but it can be an exciting project! This script will focus on creating a basic humanoid character with customizable parameters like height, body proportions, and features (e.g., head shape, limb length).

Below, I'll provide a Python script that you can run in Blender's scripting environment. The script will create a basic humanoid character by generating simple geometric shapes for the body parts (head, torso, arms, legs) and allowing you to customize some parameters.

### Blender Character Generation Script

```python
import bpy
import bmesh
import random

def create_sphere(name, location, radius):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location)
    obj = bpy.context.object
    obj.name = name
    return obj

def create_cylinder(name, location, radius, depth):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=location)
    obj = bpy.context.object
    obj.name = name
    return obj

def create_humanoid_character(height=2.0, head_radius=0.25, torso_height=0.8, limb_radius=0.1):
    # Calculate positions based on height
    head_location = (0, 0, height - head_radius)
    torso_location = (0, 0, height - head_radius - torso_height / 2)
    arm_location_left = (-0.5, 0, height - head_radius - torso_height / 2)
    arm_location_right = (0.5, 0, height - head_radius - torso_height / 2)
    leg_location_left = (-0.25, 0, (height - torso_height) - 1)
    leg_location_right = (0.25, 0, (height - torso_height) - 1)

    # Create head, torso, arms, and legs
    head = create_sphere("Head", head_location, head_radius)
    torso = create_cylinder("Torso", torso_location, 0.3, torso_height)
    arm_left = create_cylinder("Arm_Left", arm_location_left, limb_radius, 0.6)
    arm_right = create_cylinder("Arm_Right", arm_location_right, limb_radius, 0.6)
    leg_left = create_cylinder("Leg_Left", leg_location_left, limb_radius, 1.0)
    leg_right = create_cylinder("Leg_Right", leg_location_right, limb_radius, 1.0)

    # Set origin to geometry for better positioning
    for obj in [head, torso, arm_left, arm_right, leg_left, leg_right]:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

    # Parent all parts to the torso
    for obj in [head, arm_left, arm_right, leg_left, leg_right]:
        obj.parent = torso

    return torso

# Generate a humanoid character with specified parameters
create_humanoid_character(height=2.0, head_radius=0.25, torso_height=0.8, limb_radius=0.1)

# Optional: Apply basic materials
def apply_material(obj, name, color):
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = (*color, 1)  # RGB + Alpha
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

# Apply materials to each body part
apply_material(bpy.data.objects['Head'], "Skin_Material", (0.8, 0.6, 0.4))
apply_material(bpy.data.objects['Torso'], "Torso_Material", (0.1, 0.5, 0.8))
apply_material(bpy.data.objects['Arm_Left'], "Limb_Material", (0.1, 0.5, 0.8))
apply_material(bpy.data.objects['Arm_Right'], "Limb_Material", (0.1, 0.5, 0.8))
apply_material(bpy.data.objects['Leg_Left'], "Limb_Material", (0.1, 0.5, 0.8))
apply_material(bpy.data.objects['Leg_Right'], "Limb_Material", (0.1, 0.5, 0.8))
```

### How to Use the Script

1. **Open Blender:**
   Launch Blender and switch to the Scripting workspace.

2. **Create a New Script:**
   Create a new text file in the text editor and copy-paste the above script.

3. **Run the Script:**
   Click on the "Run Script" button. This will generate a basic humanoid character model in the 3D view.

### Customization Options

You can modify the parameters in the `create_humanoid_character` function call:

- `height`: Change the height of the character.
- `head_radius`: Adjust the size of the head.
- `torso_height`: Modify the height of the torso.
- `limb_radius`: Change the radius of the limbs.

### Further Development Ideas

1. **Advanced Features:**

   - Add facial features using sculpting or more complex geometry.
   - Incorporate a rig for animation.

2. **Customization Options:**

   - Allow for randomization of features like hair, clothing, or colors.
   - Create a user interface (UI) in Blender for easier adjustments.

3. **Exporting:**
   - Implement functionality to export the character to a game engine or other formats.

This script is a basic starting point for generating humanoid characters in Blender. You can expand upon it based on your specific needs and preferences!
