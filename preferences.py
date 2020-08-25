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
from bpy.types import AddonPreferences
from bpy.props import ( StringProperty, 
                        BoolProperty, 
                        FloatProperty,
                        IntProperty,
                        PointerProperty,
                        EnumProperty)


class CHBPreferences(AddonPreferences):
    bl_idname = __package__
    
    button_count: IntProperty(
        name="button_count",
        description="button_count",
        default=5,
        min=0,
        soft_max=20,
        step=1,
        subtype='FACTOR')

    button_name: StringProperty(
        name="button_name", 
        description="button_name", 
        default="name") 
    button_operator: StringProperty(
        name="button_operator", 
        description="button_operator", 
        default="screen.userpref_show") 
    button_icon: StringProperty(
        name="button_icon", 
        description="button_icon", 
        default="FUND")  
    button_text: StringProperty(
        name="button_text", 
        description="button_text", 
        default="text")
    show_button_text: BoolProperty(
        name="show_button_text",
        description="show_button_text",
        default=False) 


    def draw(self, context):        
        layout = self.layout
        #layout.use_property_split = True
        col = layout.column(align=True)
        col.prop(self, 'button_count')
        col.prop(self, 'button_name')
        col.prop(self, 'button_operator') 
        col.prop(self, 'button_icon')
        col.prop(self, 'button_text')        
        col.prop(self, 'show_button_text')
 
