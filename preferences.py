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

    
"""Addon preferences"""
import bpy
from bpy.types import AddonPreferences, PropertyGroup, UIList
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        IntProperty,
                        EnumProperty,
                        )


class CHB_Preferences(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        scene = context.scene 

        layout = self.layout
        #layout.use_property_split = True         
         
        row = layout.row()
        row.template_list("CHB_UL_List", 
                            "Custom Header Buttons List ", 
                            scene, 
                            "chb_list", 
                            scene, 
                            "chb_list_index",                            
                            type='DEFAULT',
                            columns=1,
                        ) 
                        
        row = layout.row() 
        row.operator('chb_list.new_item', text='New') 
        row.operator('chb_list.delete_item', text='Delete') 
        row.operator('chb_list.move_item', text='Up').direction = 'UP' 
        row.operator('chb_list.move_item', text='Down').direction = 'DOWN' 
    
        #template_list(listtype_name, 
        #               list_id, 
        #               dataptr, 
        #               propname, 
        #               active_dataptr, 
        #               active_propname, 
        #               item_dyntip_propname='', 
        #               rows=5, 
        #               maxrows=5, 
        #               type='DEFAULT', 
        #               columns=9, 
        #               sort_reverse=False, 
        #               sort_lock=False)