import bpy
shelf = bpy.context.scene.shelf_list

shelf.clear()
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Preferences'
item_sub_1.button_operator = 'screen.userpref_show'
item_sub_1.button_icon = 'PREFERENCES'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Save Preferences'
item_sub_1.button_operator = 'wm.save_userpref'
item_sub_1.button_icon = 'IMPORT'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Save Startup File'
item_sub_1.button_operator = 'wm.save_homefile'
item_sub_1.button_icon = 'FILE_BACKUP'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Reload Scripts'
item_sub_1.button_operator = 'script.reload'
item_sub_1.button_icon = 'FILE_SCRIPT'
item_sub_1.show_button_name = False
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Search'
item_sub_1.button_operator = 'wm.search_menu'
item_sub_1.button_icon = 'VIEWZOOM'
item_sub_1.show_button_name = False
