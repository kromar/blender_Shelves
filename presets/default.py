import bpy
shelf = bpy.context.scene.shelf_list

shelf.clear()
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
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Search'
item_sub_1.button_operator = 'wm.search_menu'
item_sub_1.button_icon = 'VIEWZOOM'
item_sub_1.show_button_name = False
