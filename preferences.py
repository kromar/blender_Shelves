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


class CB_Preferences(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        scene = context.scene 
        layout = self.layout      

        row = layout.row(align=True)  
        preset_label = bpy.types.CB_MT_Presets.bl_label
        row.menu('CB_MT_Presets', text=preset_label)
        row.operator('custom_buttons_preset.add_preset', text='', icon='ADD')
        row.operator('custom_buttons_preset.add_preset', text='', icon='REMOVE').remove_active = True
       
        row = layout.row(align=True)  
        row.label(text="Icon")
        row.label(text="Name (Show/Hide)")
        row.label(text="Operator")

        row = layout.row(align=True)
        col = row.column(align=True)
        col.template_list("CB_UL_ButtonsList", 
                            "Custom Header Buttons List ", 
                            scene, 
                            "custom_buttons_list", 
                            scene, 
                            "custom_buttons_list_index",                            
                            type='DEFAULT',
                            columns=1,
                        ) 
                        
        col = row.column(align=True)
        col.operator('custom_buttons_list.new_item', text='', icon='ADD') 
        col.operator('custom_buttons_list.delete_item', text='', icon='REMOVE')  
        col.operator('custom_buttons_list.move_item', text='', icon='TRIA_UP').direction = 'UP'   
        col.operator('custom_buttons_list.move_item', text='', icon='TRIA_DOWN').direction = 'DOWN' 