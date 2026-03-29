bl_info = {
    "name": "NLA Batch Editor",
    "version": (1, 0, 0),
    "author": "c4205M",
    "blender": (4, 5, 2),
    "description": "Batch editing for NLA Editor",
    "category": "NLA",
    "doc_url": "https://github.com/c42m05/NLA-Batch-Editor",
}

if "bpy" in locals():
    from importlib import reload

    reload(custom_properties)
    reload(op_batch_pushdown)
    reload(op_modify_selection)
    reload(op_dublicate)
    reload(op_edit_strip_data)
    reload(op_edit_track_data)
    reload(op_transfer_selection)
else:
    from . import custom_properties
    from . import op_batch_pushdown
    from . import op_modify_selection
    from . import op_dublicate
    from . import op_edit_strip_data
    from . import op_edit_track_data
    from . import op_transfer_selection

import bpy

# WARNING: To always see tabs on sidebar, two seperate category is created
class NLA_PT_pushdown(bpy.types.Panel):
    bl_label = "Batch Pushdown"
    bl_idname = "NLA_PT_pushdown_settings"
    bl_space_type = "NLA_EDITOR"
    bl_region_type = "UI"
    bl_category = "NBE | Batch Pushdown"
    bl_options = {"HIDE_HEADER"}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        props = context.scene.NBE_properties.pushdown_props
        is_any_selected = len(context.selected_objects) > 0

        # Name options layout
        segment = layout.column()

        row = segment.row()
        row.prop(props,
                'track_name',
                text="Track Name" if props.distinct_strip_name else "New Stack Name"
                )

        if props.distinct_strip_name:
            row = segment.row()
            row.prop(props, 'strip_name', text="Strip Name")

        row = segment.row()
        row.prop(props, 'distinct_strip_name')
        
        # Start frame options layout
        segment = layout.column()
        segment.separator(type="SPACE")

        if props.random_start:
            row = segment.row()
            row.prop(props, 'start_min')
            
            row = segment.row()
            row.prop(props, 'start_max')
        else:
            row = segment.row()
            row.prop(props, 'frame_start')

        row = segment.row()
        row.prop(props, 'random_start')

        # Other options
        segment = layout.column()
        segment.separator(type="SPACE")

        row = segment.row()
        row.prop(props, 'set_mute_new_track')
        row = segment.row()
        row.prop(props, 'keep_actions')

        # Main button
        main_button = layout.column()
        main_button.separator(type="SPACE")
        main_button = main_button.row()
        main_button.scale_y = 4.0
        main_button.split(factor=1)
        main_button.operator(
            op_batch_pushdown.op.bl_idname,
            # icon="EVENT_DOWN_ARROW",
            )
        main_button.split(factor=1)
        main_button.enabled = is_any_selected

class NLA_PT_modify_selection(bpy.types.Panel):
    bl_label = "Selection"
    bl_idname = "NLA_PT_modify_selection"
    bl_space_type = "NLA_EDITOR"
    bl_region_type = "UI"
    bl_category = "NBE | Batch Edit"

    def draw(self, context):
        op_props = context.scene.NBE_properties.modify_selection_props
        strip_props = context.scene.NBE_properties.strip_props

        layout = self.layout
        layout.use_property_split = True

        col = layout.column()
        col.scale_y = 2.0
        col.operator(op_transfer_selection.op.bl_idname)

        col.separator(type="SPACE")
        col.separator(type="LINE")
        col.separator(type="SPACE")

        segment = layout.box()
        segment.prop(op_props, 'selection_option')
        segment.prop(op_props, 'include_tracks')
        segment.prop(op_props, 'selection_type')
        segment.separator(type="SPACE")

        if op_props.selection_type == 'STRIP':
            segment.prop(op_props, 'filter_method')
            if op_props.filter_method == 'name':
                segment.prop(op_props, op_props.filter_method)
                segment.prop(strip_props, 'is_search_includes')
            else:
                segment.prop(strip_props, op_props.filter_method)

        else:
            segment.prop(op_props, 'name')
            segment.prop(strip_props, 'is_search_includes')
       
        segment.separator(type="SPACE")
        
        row = segment.row()
        row.scale_y = 2.0
        row.split(factor=1)
        row.operator(op_modify_selection.op.bl_idname)
        row.split(factor=1)
        segment.separator(type="SPACE")

class NLA_PT_track_edit(bpy.types.Panel):
    bl_label = "Track Edit"
    bl_idname = "NLA_PT_track_edit"
    bl_space_type = "NLA_EDITOR"
    bl_region_type = "UI"
    bl_category = "NBE | Batch Edit"

    def draw(self, context):
        dub_op_props = context.scene.NBE_properties.dublicate_ops_props
        edit_track_op_props = context.scene.NBE_properties.edit_track_props

        layout = self.layout
        layout.use_property_split = True
        layout = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)

        col = layout.column()

        ## Track Edit Op
        edit_track_op = col.box()
        edit_track_op.label(text="Edit Tracks")
        edit_track_op.prop(edit_track_op_props, "name_input")
        edit_track_op.prop(edit_track_op_props, "edit_mode")

        is_toggle_edit = edit_track_op_props.edit_mode == "TOGGLE"

        edit_track_op.prop(edit_track_op_props, "mute_input", text = "Toggle Mute" if is_toggle_edit else "Set Mute")
        edit_track_op.prop(edit_track_op_props, "lock_input", text = "Toggle Lock" if is_toggle_edit else "Set Lock")

        row = edit_track_op.row()
        row.scale_y = 2.0
        row.split(factor=1)
        row.operator(op_edit_track_data.op.bl_idname)
        row.split(factor=1)
        edit_track_op.separator(type="SPACE")

        ## Dublicate Track Op
        dub_op = col.box()
        dub_op.label(text="Dublicate Tracks")
        dub_op.prop(dub_op_props, "dublicate_name")
        dub_op.prop(dub_op_props, "is_copy_linked")

        row = dub_op.row()
        row.scale_y = 2.0
        row.split(factor=1)
        row.operator(op_dublicate.op.bl_idname)
        row.split(factor=1)
        dub_op.separator(type="SPACE")

class NLA_PT_strip_edit(bpy.types.Panel):
    bl_label = "Strip Edit"
    bl_idname = "NLA_PT_strip_edit"
    bl_space_type = "NLA_EDITOR"
    bl_region_type = "UI"
    bl_category = "NBE | Batch Edit"

    def draw(self, context):
        edit_strip_op_props = context.scene.NBE_properties.strip_toggles
        strip_properties = context.scene.NBE_properties.strip_props

        layout = self.layout
        layout.use_property_split = True
        layout = layout.grid_flow(row_major=True, columns=0, even_columns=True, even_rows=False, align=False)

        edit_strip_op = layout.column()
        
        is_any_enabled = False
        for prop in edit_strip_op_props.__annotations__.keys():
            if hasattr(strip_properties, prop):
                prop_name = edit_strip_op_props.bl_rna.properties[prop].name
                toggle_value = getattr(edit_strip_op_props, prop)
                label_stat = "RESTRICT_SELECT_OFF" if toggle_value else "RESTRICT_SELECT_ON"

                if toggle_value:
                    is_any_enabled = True

                row = edit_strip_op.row()
                row.label()
                row.label()
                row = row.row()
                row.prop(edit_strip_op_props, prop, icon=label_stat, icon_only=True)
                subrow = row.row()
                subrow.active = getattr(edit_strip_op_props, prop)
                subrow.prop(strip_properties, prop, text=prop_name)
                row.label()
                row.label()

        edit_strip_op.separator(type="SPACE")
        main_button = edit_strip_op.row()
        main_button.scale_y = 2.0
        main_button.split(factor=1)
        main_button.operator(op_edit_strip_data.op.bl_idname)
        main_button.split(factor=1)
        main_button.enabled = is_any_enabled
        edit_strip_op.separator(type="SPACE")

 

classes = (
    op_modify_selection.op,
    op_batch_pushdown.op,
    op_dublicate.op,
    op_edit_strip_data.op,
    op_edit_track_data.op,
    op_transfer_selection.op,

    NLA_PT_pushdown,
    NLA_PT_modify_selection,
    NLA_PT_track_edit,
    NLA_PT_strip_edit,
)

def register():
    custom_properties.register()

    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    custom_properties.unregister()

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
	register()