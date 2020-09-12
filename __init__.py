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
from bl_operators.presets import AddPresetBase
from bpy.types import AddonPreferences, Menu, PropertyGroup, UIList, Operator, Panel 
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        IntProperty,
                        EnumProperty,
                        CollectionProperty,
                        )

bl_info = {
    "name": "Custom Header Buttons",
    "description": "Customize operators to use via header buttons",
    "author": "Daniel Grauer",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "TopBar",
    "category": "System",
    "wiki_url": ""
}


def draw_button(self, context):
    pref = bpy.context.preferences.addons[__package__.split(".")[0]].preferences 
    scene = context.scene 
    if scene.chb_list:
        item = scene.chb_list[scene.chb_list_index] 
        if context.region.alignment == 'RIGHT':
            layout = self.layout
            row = layout.row(align=True)
            for i in range(0, len(scene.chb_list)):
                if scene.chb_list[i].show_button_text:
                    row.operator(operator=scene.chb_list[i].button_operator, 
                                text=scene.chb_list[i].button_name, 
                                icon=scene.chb_list[i].button_icon)
                                
                else:
                    row.operator(operator=scene.chb_list[i].button_operator, 
                                text="", 
                                icon=scene.chb_list[i].button_icon)
        return{'FINISHED'}


class CHB_ListItem(PropertyGroup): 
    """Group of properties representing an item in the list.""" 
    
    button_name: StringProperty(
        name="Name", 
        description="button_name", 
        default="name") 

    button_operator: StringProperty(
        name="Operator", 
        description="button_operator", 
        default="screen.userpref_show") 

    button_icon: StringProperty(
        name="", 
        description="buton_icon", 
        default="FUND")  

    show_button_text: BoolProperty(
        name="",
        description="show_button_text",
        default=False) 
        

class CHB_UL_List(UIList): 
    """Demo UIList.""" 
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index): 
        
        layout.label(text="", icon = item.button_icon) 
        layout.prop(item, "button_icon") 
        layout.prop(item, "button_name") 
        layout.prop(item, "show_button_text")
        layout.prop(item, "button_operator") 
            
            
class CHB_LIST_OT_NewItem(Operator): 
    """Add a new item to the list.""" 
    bl_idname = "chb_list.new_item" 
    bl_label = "Add a new item" 
    def execute(self, context): 
        context.scene.chb_list.add() 
        draw_button(self, context)
        return{'FINISHED'} 
        
        
class CHB_LIST_OT_DeleteItem(Operator): 
    """Delete the selected item from the list.""" 
    bl_idname = "chb_list.delete_item" 
    bl_label = "Deletes an item" 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.chb_list 
        
    def execute(self, context): 
        chb_list = context.scene.chb_list 
        index = context.scene.chb_list_index 
        chb_list.remove(index) 
        context.scene.chb_list_index = min(max(0, index - 1), len(chb_list) - 1) 
        draw_button(self, context)
        return{'FINISHED'} 
        
        
class CHB_LIST_OT_MoveItem(Operator): 
    """Move an item in the list.""" 
    bl_idname = "chb_list.move_item" 
    bl_label = "Move an item in the list" 
    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),)) 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.chb_list 
        
    def move_index(self): 
        """ Move index of an item render queue while clamping it. """ 
        index = bpy.context.scene.chb_list_index 
        list_length = len(bpy.context.scene.chb_list) - 1 
        # (index starts at 0) 
        new_index = index + (-1 if self.direction == 'UP' else 1) 
        bpy.context.scene.chb_list_index = max(0, min(new_index, list_length)) 
        
    def execute(self, context): 
        chb_list = context.scene.chb_list 
        index = context.scene.chb_list_index 
        neighbor = index + (-1 if self.direction == 'UP' else 1) 
        chb_list.move(neighbor, index) 
        self.move_index() 
        draw_button(self, context)
        return{'FINISHED'} 
        

classes = (
    preferences.CHB_Preferences,

    CHB_ListItem,
    CHB_UL_List,
    CHB_LIST_OT_NewItem,
    CHB_LIST_OT_DeleteItem,
    CHB_LIST_OT_MoveItem,
    )            

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)

    bpy.types.Scene.chb_list = CollectionProperty(type = CHB_ListItem) 
    bpy.types.Scene.chb_list_index = IntProperty(name = "Index for custom header button list", default = 0) 
    

def unregister():
    del bpy.types.Scene.chb_list 
    del bpy.types.Scene.chb_list_index 
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)
    [bpy.utils.unregister_class(c) for c in classes]


if __name__ == "__main__":
    register()
