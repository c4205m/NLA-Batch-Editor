import bpy
import random

class op(bpy.types.Operator):
    """Pushdown actions to nla tracks"""
    bl_idname = "anim.batch_pushdown"
    bl_label = "Pushdown Actions"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
        
    def execute(self, context):
        OBJECT_NAME_PLACEHOLDER = "OBJECT_NAME"

        op_props = context.scene.NBE_properties.pushdown_props
        pushdowns = 0

        for object in context.selected_objects:
            if object.animation_data and object.animation_data.action:
                frame_start = random.randint(op_props.start_min, op_props.start_max) if op_props.random_start else op_props.frame_start
                nla_tracks = object.animation_data.nla_tracks

                new_track = nla_tracks.new(prev=None)
                new_track.name = op_props.track_name.replace(f"**{OBJECT_NAME_PLACEHOLDER}**", object.name)
                new_track.mute = op_props.set_mute_new_track

                new_strip = new_track.strips.new(object.animation_data.action.name, frame_start, object.animation_data.action)
                new_strip.name = op_props.strip_name.replace(f"**{OBJECT_NAME_PLACEHOLDER}**", object.name) if op_props.distinct_strip_name else new_track.name

                object.animation_data.action = object.animation_data.action if op_props.keep_actions else None

                pushdowns += 1
            else:
                self.report({"WARNING"}, f"{object.name} has no action to pushdown")
        
        self.report({"INFO"}, f"{pushdowns} action(s) pushed down to nla tracks")
        return {'FINISHED'}