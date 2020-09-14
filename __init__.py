# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
if "bpy" in locals():
    import importlib
    importlib.reload(preferences)
else:
    from . import preferences

import bpy
import os
import shutil
from bl_operators.presets import AddPresetBase
from bl_ui.utils import PresetPanel

from bpy.types import AddonPreferences, Menu, PropertyGroup, UIList, Operator, Panel 
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        IntProperty,
                        EnumProperty,
                        CollectionProperty,
                        )

bl_info = {
    "name": "Custom Buttons",
    "description": "Creat your costom buttons in the Header",
    "author": "Daniel Grauer",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "Header",
    "category": "System",
    "wiki_url": ""
}


def draw_button(self, context):
    scene = context.scene 
    #if scene.custom_buttons_list:
    if context.region.alignment == 'RIGHT':
        layout = self.layout


        row = layout.row(align=True)
        for i in range(0, len(scene.custom_buttons_list)):
            if scene.custom_buttons_list[i].show_button_name:
                row.operator(operator=scene.custom_buttons_list[i].button_operator, 
                            text=scene.custom_buttons_list[i].button_name, 
                            icon=scene.custom_buttons_list[i].button_icon)                                
            else:
                row.operator(operator=scene.custom_buttons_list[i].button_operator, 
                            text="", 
                            icon=scene.custom_buttons_list[i].button_icon)
        
        row = layout.row()
        preset_label = bpy.types.CB_MT_Presets.bl_label
        row.menu('CB_MT_Presets', text=preset_label, icon='PRESET')

        return{'FINISHED'}


class CB_MT_Presets(Menu):  
    bl_label = "Shelfes"
    preset_subdir = 'custom_buttons' 
    preset_operator = 'script.execute_preset' 
    draw = Menu.draw_preset


class CB_OT_SavePreset(AddPresetBase, Operator): 
    """ Save Preset """
    bl_idname = 'custom_buttons_preset.save_preset' 
    bl_label = 'Save Shelf' 
    preset_menu = 'CB_MT_Presets' 
    preset_subdir = 'custom_buttons'
    
    # Common variable used for all preset values     
    preset_defines = [
        'items = bpy.context.scene.custom_buttons_list'
        ] 
    # Properties to store in the preset 
    preset_values = [
        'items'
        ] 


class CB_ButtonsList(PropertyGroup): 
    """Group of properties representing an item in the list."""
    button_name: StringProperty(
        name="", 
        description="button_name", 
        default="Name") 

    button_operator: StringProperty(
        name="", 
        description="button_operator", 
        default="screen.userpref_show") 

    button_icon: StringProperty(
        name="", 
        description="buton_icon", 
        default="FUND")  

    show_button_name: BoolProperty(
        name="",
        description="Show Button Name",
        default=False) 
        

class CB_UL_ButtonsList(UIList): 
    """Custom Buttons List."""    
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index): 
        layout.label(text='', icon='TRIA_RIGHT')
        layout.prop(item, "button_icon", icon = item.button_icon) 
        layout.prop(item, "button_name") 
        layout.prop(item, "show_button_name")
        layout.prop(item, "button_operator") 
                    
            
class CB_LIST_OT_NewItem(Operator): 
    """Add a new item to the list.""" 
    bl_idname = "custom_buttons_list.new_item" 
    bl_label = "Add a new item" 
    def execute(self, context): 
        context.scene.custom_buttons_list.add() 
        return{'FINISHED'} 
        
        
class CB_LIST_OT_DeleteItem(Operator): 
    """Delete the selected item from the list.""" 
    bl_idname = "custom_buttons_list.delete_item" 
    bl_label = "Deletes an item" 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.custom_buttons_list 
        
    def execute(self, context): 
        custom_buttons_list = context.scene.custom_buttons_list 
        index = context.scene.custom_buttons_list_index 
        custom_buttons_list.remove(index) 
        context.scene.custom_buttons_list_index = min(max(0, index - 1), len(custom_buttons_list) - 1) 
        return{'FINISHED'} 
        
        
class CB_LIST_OT_MoveItem(Operator): 
    """Move an item in the list.""" 
    bl_idname = "custom_buttons_list.move_item" 
    bl_label = "Move an item in the list" 
    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),)) 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.custom_buttons_list 
        
    def move_index(self): 
        """ Move index of an item render queue while clamping it. """ 
        index = bpy.context.scene.custom_buttons_list_index 
        list_length = len(bpy.context.scene.custom_buttons_list) - 1 
        # (index starts at 0) 
        new_index = index + (-1 if self.direction == 'UP' else 1) 
        bpy.context.scene.custom_buttons_list_index = max(0, min(new_index, list_length)) 
        
    def execute(self, context): 
        custom_buttons_list = context.scene.custom_buttons_list 
        index = context.scene.custom_buttons_list_index 
        neighbor = index + (-1 if self.direction == 'UP' else 1) 
        custom_buttons_list.move(neighbor, index) 
        self.move_index() 
        return{'FINISHED'} 
        

classes = (
    preferences.CB_Preferences,

    CB_MT_Presets,
    CB_OT_SavePreset,

    CB_ButtonsList,
    CB_UL_ButtonsList,
    CB_LIST_OT_NewItem,
    CB_LIST_OT_DeleteItem,
    CB_LIST_OT_MoveItem,
    )            


def register():
    for c in classes:
        bpy.utils.register_class(c)    
    
    #install default preset
    presets_target_folder = bpy.utils.user_resource('SCRIPTS', "presets/custom_buttons/", create=True)
    bundled_presets =  os.path.abspath(os.path.dirname(__file__) + '/presets/')
    preset_files = os.listdir(bundled_presets) 
    for p in preset_files:
        if not os.path.isfile(presets_target_folder + p): 
            print("installing preset: ", p)
            shutil.copy2(os.path.join(bundled_presets, p), presets_target_folder)            

    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)

    bpy.types.Scene.custom_buttons_list = CollectionProperty(type = CB_ButtonsList) 
    bpy.types.Scene.custom_buttons_list_index = IntProperty(default = 0) 
    

def unregister():
    del bpy.types.Scene.custom_buttons_list 
    del bpy.types.Scene.custom_buttons_list_index 
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)
    [bpy.utils.unregister_class(c) for c in classes]


if __name__ == "__main__":
    register()
