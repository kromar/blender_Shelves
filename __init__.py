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
from bpy.props import StringProperty, IntProperty, CollectionProperty 
from bpy.types import AddonPreferences, PropertyGroup, UIList, Operator, Panel 


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


icons = ['PREFERENCES',
        'IMPORT',
        'FILE_BACKUP',
        'FILE_SCRIPT',
]



def draw_button(self, context):
    pref = bpy.context.preferences.addons[__package__.split(".")[0]].preferences 
    if context.region.alignment == 'RIGHT':
        layout = self.layout
        row = layout.row(align=True)
        for i in range(1, context.scene.list_index):
            if pref.show_button_text:
                row.operator(operator=pref.button_operator, 
                        text=pref.button_text, 
                        icon=pref.button_icon)
            else:                
                row.operator(operator=pref.button_operator, 
                        text="", 
                        icon=pref.button_icon)
            

class ListItem(PropertyGroup): 
    """Group of properties representing an item in the list.""" 
    name: StringProperty( 
        name="Name", 
        description="A name for this item", 
        default="Untitled") 
        
    random_prop: StringProperty( 
        name="Any other property you want", 
        description="", 
        default="") 
        

class MY_UL_List(UIList): 
    """Demo UIList.""" 
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index): 
        # We could write some code to decide which icon to use here... 
        custom_icon = 'OBJECT_DATAMODE' 
        # # Make sure your code supports all 3 layout types 
        if self.layout_type in {'DEFAULT', 'COMPACT'}: 
            layout.label(text=item.name, icon = custom_icon) 
        elif self.layout_type in {'GRID'}: 
            layout.alignment = 'CENTER' 
            layout.label(text="", icon = custom_icon) 
            
            
class LIST_OT_NewItem(Operator): 
    """Add a new item to the list.""" 
    bl_idname = "my_list.new_item" 
    bl_label = "Add a new item" 
    def execute(self, context): 
        context.scene.my_list.add() 
        return{'FINISHED'} 
        
        
class LIST_OT_DeleteItem(Operator): 
    """Delete the selected item from the list.""" 
    bl_idname = "my_list.delete_item" 
    bl_label = "Deletes an item" 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.my_list 
        
    def execute(self, context): 
        my_list = context.scene.my_list 
        index = context.scene.list_index 
        my_list.remove(index) 
        context.scene.list_index = min(max(0, index - 1), len(my_list) - 1) 
        return{'FINISHED'} 
        
        
class LIST_OT_MoveItem(Operator): 
    """Move an item in the list.""" 
    bl_idname = "my_list.move_item" 
    bl_label = "Move an item in the list" 
    direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""), ('DOWN', 'Down', ""),)) 
    
    @classmethod 
    def poll(cls, context): 
        return context.scene.my_list 
        
    def move_index(self): 
        """ Move index of an item render queue while clamping it. """ 
        index = bpy.context.scene.list_index 
        list_length = len(bpy.context.scene.my_list) - 1 
        # (index starts at 0) 
        new_index = index + (-1 if self.direction == 'UP' else 1) 
        bpy.context.scene.list_index = max(0, min(new_index, list_length)) 
        
    def execute(self, context): 
        my_list = context.scene.my_list 
        index = context.scene.list_index 
        neighbor = index + (-1 if self.direction == 'UP' else 1) 
        my_list.move(neighbor, index) 
        self.move_index() 
        return{'FINISHED'} 
        


classes = (
    preferences.CHB_Preferences,
    ListItem,
    MY_UL_List,
    LIST_OT_NewItem,
    LIST_OT_DeleteItem,
    LIST_OT_MoveItem,
    )            

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)

    bpy.types.Scene.my_list = CollectionProperty(type = ListItem) 
    bpy.types.Scene.list_index = IntProperty(name = "Index for my_list", default = 0) 
    

def unregister():
    del bpy.types.Scene.my_list 
    del bpy.types.Scene.list_index 
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)
    [bpy.utils.unregister_class(c) for c in classes]


if __name__ == "__main__":
    register()
