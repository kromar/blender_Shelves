import bpy
shelf = bpy.context.scene.shelf_list

shelf.clear()
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'suzanne'
item_sub_1.button_operator = 'mesh.primitive_monkey_add'
item_sub_1.button_icon = 'MONKEY'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'cube'
item_sub_1.button_operator = 'mesh.primitive_cube_add'
item_sub_1.button_icon = 'MESH_CUBE'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'sphere'
item_sub_1.button_operator = 'mesh.primitive_ico_sphere_add'
item_sub_1.button_icon = 'MESH_ICOSPHERE'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Import FBX'
item_sub_1.button_operator = 'import_scene.fbx'
item_sub_1.button_icon = 'IMPORT'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Export FBX'
item_sub_1.button_operator = 'export_scene.fbx'
item_sub_1.button_icon = 'EXPORT'
item_sub_1.show_button_name = False
