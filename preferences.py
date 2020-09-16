# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import bpy
from bpy.types import AddonPreferences, PropertyGroup, UIList
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        IntProperty,
                        EnumProperty,
                        )


class SHELVES_Preferences(AddonPreferences):
    bl_idname = __package__

    default_shelf: StringProperty(
        name="default_shelf", 
        description="default_shelf", 
        default="Default") 


    def draw(self, context):
        scene = context.scene 
        layout = self.layout      

        row = layout.row(align=True)  
        preset_label = bpy.types.SHELVES_MT_Presets.bl_label
        row.menu('SHELVES_MT_Presets', text=self.default_shelf)
        row.operator('shelves.save_preset', text='', icon='ADD')
        row.operator('shelves.save_preset', text='', icon='REMOVE').remove_active = True
        
        
        row = layout.row(align=True)  
        #row.operator('self.default_shelf', text="set as default",  icon='ADD')
        row.prop(self, 'default_shelf')
        self.default_shelf = preset_label
        #row.label(text=self.default_shelf)

        row = layout.row(align=True)
        col = row.column(align=True)
        col.template_list("SHELVES_UL_ButtonsList", 
                            "Custom Shelf List ", 
                            scene, 
                            "shelf_list", 
                            scene, 
                            "shelf_list_index",                            
                            type='DEFAULT',
                            columns=1,
                        ) 
                        
        col = row.column(align=True)
        col.operator('shelf_list.new_button', text='', icon='ADD') 
        col.operator('shelf_list.delete_button', text='', icon='REMOVE') 
         
        col.operator('shelf_list.move_button', text='', icon='TRIA_UP').direction = 'UP'   
        col.operator('shelf_list.move_button', text='', icon='TRIA_DOWN').direction = 'DOWN' 