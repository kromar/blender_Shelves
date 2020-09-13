import bpy
items = bpy.context.scene.custom_buttons_list

items.clear()
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Preferences'
item_sub_1.button_operator = 'screen.userpref_show'
item_sub_1.button_icon = 'PREFERENCES'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Save Preferences'
item_sub_1.button_operator = 'wm.save_userpref'
item_sub_1.button_icon = 'IMPORT'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Save Startup File'
item_sub_1.button_operator = 'wm.save_homefile'
item_sub_1.button_icon = 'FILE_BACKUP'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Relaod Scripts'
item_sub_1.button_operator = 'script.reload'
item_sub_1.button_icon = 'FILE_SCRIPT'
item_sub_1.show_button_name = False
item_sub_1 = items.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Export FBX'
item_sub_1.button_operator = 'export_scene.fbx'
item_sub_1.button_icon = 'EXPORT'
item_sub_1.show_button_name = False
