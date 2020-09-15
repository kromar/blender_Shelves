import bpy
buttons = bpy.context.scene.shelf_list

buttons.clear()
buttons_sub_1 = buttons.add()
buttons_sub_1.name = ''
buttons_sub_1.button_name = 'suzanne'
buttons_sub_1.button_operator = 'mesh.primitive_monkey_add'
buttons_sub_1.button_icon = 'MONKEY'
buttons_sub_1.show_button_name = False
buttons_sub_1 = buttons.add()
buttons_sub_1.name = ''
buttons_sub_1.button_name = 'cube'
buttons_sub_1.button_operator = 'mesh.primitive_cube_add'
buttons_sub_1.button_icon = 'MESH_CUBE'
buttons_sub_1.show_button_name = False
buttons_sub_1 = buttons.add()
buttons_sub_1.name = ''
buttons_sub_1.button_name = 'sphere'
buttons_sub_1.button_operator = 'mesh.primitive_ico_sphere_add'
buttons_sub_1.button_icon = 'MESH_ICOSPHERE'
buttons_sub_1.show_button_name = False
