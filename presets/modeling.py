import bpy
items = bpy.context.scene.custom_buttons_list

items.clear()
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'suzanne'
item_sub_1.button_operator = 'mesh.primitive_monkey_add'
item_sub_1.button_icon = 'MONKEY'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'cube'
item_sub_1.button_operator = 'mesh.primitive_cube_add'
item_sub_1.button_icon = 'MESH_CUBE'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'sphere'
item_sub_1.button_operator = 'mesh.primitive_ico_sphere_add'
item_sub_1.button_icon = 'MESH_ICOSPHERE'
item_sub_1.show_button_name = False
