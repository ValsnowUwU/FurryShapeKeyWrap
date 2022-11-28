import bpy
from . import skw_panel
from . import skw_operators
from . import skw_props


bl_info = {
    'name' : 'ShapeKeyWrap',
    'author' : 'Mykyta Petrenko (Squeezy Weasel)',
    'description' : 'Blender addon for transfering shapekeys from on mesh to another one using surface deform modifier.',
    'blender' : (3, 00, 0),
    'version' : (0, 2, 2),
    'location' : 'View3D > Object Mode > N-Panel > Tools > Shape Key Wrap',
    'warning' : '',
    'doc_url': 'https://github.com/MykytaPetrenko/ShapeKeyWrap',
    'category': 'Mesh'
}

MODULES = [skw_panel, skw_operators, skw_props]


def register():
    for module in MODULES:
        module.register()


def unregister():
    for module in MODULES:
        module.unregister()


if __name__ == "__main__":
    register()
