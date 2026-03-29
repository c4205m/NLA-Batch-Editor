import bpy
from . import utils_attributes

class op(bpy.types.Operator):
    """Creates new tracks with copy of selected tracks"""
    bl_idname = "anim.dub_track_data"
    bl_label = "Dublicate Tracks"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        TRACK_NAME_PLACEHOLDER = "TRACK_NAME"

        selected = 0
        op_props = context.scene.NBE_properties.dublicate_ops_props

        bpy.ops.nla_batch_editor.transfer_selection(transfer_type="STOT")

        for obj in context.view_layer.objects:
            if not obj.animation_data or not obj.animation_data.nla_tracks:
                continue

            tracks = obj.animation_data.nla_tracks.values()

            for track in tracks:
                if track.select:
                    new_track = obj.animation_data.nla_tracks.new(prev=None)
                    new_track.name = op_props.dublicate_name.replace(f"**{TRACK_NAME_PLACEHOLDER}**", track.name)
                    new_track.mute = track.mute
                    new_track.lock = track.lock

                    new_track.select = True
                    track.select = False

                    for strip in track.strips:
                        new_action = strip.action if op_props.is_copy_linked else strip.action.copy()

                        new_strip = new_track.strips.new(strip.action.name, int(strip.frame_start), strip.action)
                        utils_attributes.copy_attr(strip, new_strip)
                        new_strip.action = new_action # WARNING: Not quite happy with this but moving on

                        new_strip.select = True
                        strip.select = False

                    selected += 1

        if selected > 0:
            self.report({"INFO"}, f"{selected} track(s) copied")
        else:
            self.report({"WARNING"}, f"No track(s) were selected")

        return {'FINISHED'}