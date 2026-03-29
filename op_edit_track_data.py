import bpy

class op(bpy.types.Operator):
    """Edit select tracks"""
    bl_idname = "anim.edit_track_data"
    bl_label = "Edit Tracks"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    @classmethod
    def poll(self, context):
        return context.area.type == "NLA_EDITOR"
    
    def execute(op, context):
        op = context.scene.NBE_properties.edit_track_props
        TRACK_NAME_PLACEHOLDER = "TRACK_NAME"
        
        for obj in context.view_layer.objects:
            if not obj.animation_data or not obj.animation_data.nla_tracks:
                continue

            for track in obj.animation_data.nla_tracks:
                if track.select:
                    track.name = op.name_input.replace(f"**{TRACK_NAME_PLACEHOLDER}**", track.name)
                    
                    if op.edit_mode == "SET":
                        track.mute = not op.mute_input
                        track.lock = op.lock_input
                    else:
                        track.mute = not track.mute if op.mute_input else track.mute
                        track.lock = not track.lock if op.lock_input else track.lock

        return {"FINISHED"}