import bpy
scene = bpy.context.scene
item = scene.chb_list[scene.chb_list_index]

item.button_icon = 'FUND'
item.button_name = 'name'
item.show_button_text = False
item.button_operator = 'screen.userpref_show'
