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
        for i in range(1,pref.button_count):
            if pref.show_button_text:
                row.operator(operator=pref.button_operator, 
                        text=pref.button_text, 
                        icon=pref.button_icon)
            else:                
                row.operator(operator=pref.button_operator, 
                        text="", 
                        icon=pref.button_icon)
            
 

classes = (
    preferences.CHBPreferences,
    )            

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.TOPBAR_HT_upper_bar.prepend(draw_button)


def unregister():
    bpy.types.TOPBAR_HT_upper_bar.remove(draw_button)
    [bpy.utils.unregister_class(c) for c in classes]


if __name__ == "__main__":
    register()
