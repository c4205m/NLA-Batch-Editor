import bpy

class op(bpy.types.Operator):
    """Switches selection between NLA tracks and their strips."""
    bl_idname = "anim.transfer_selection"
    bl_label = "Transfer Selection"
    bl_options = {"REGISTER", "UNDO"} # WARNING: This may be external to the search, why not

    transfer_type: bpy.props.EnumProperty(
        items=[
            ("STOT", "Strips to tracks", "Transfer strip selection to tracks"),
            ("TTOS", "Tracks to strips", "Transfer track selection to strips",)
        ],
        default="STOT",
        name="Transfer Type",
        options=set()
    ) #type: ignore

    @classmethod
    def poll(self, context):
        return context.area.type == "NLA_EDITOR"
    
    def execute(self, context):
        selected = 0
        is_stot = self.transfer_type == "STOT"

        for obj in context.view_layer.objects: # WARNING: Blender has no selected tracks context
            if not obj.animation_data or not obj.animation_data.nla_tracks:
                continue
            
            for track in obj.animation_data.nla_tracks:
                if not is_stot:
                    if track.select:
                        track.select = False
                        selected +=1
                        
                        for strip in track.strips:
                            strip.select = True

                    continue

                for strip in track.strips:
                    if strip.select:
                        strip.select = False

                        if not track.select:
                            track.select = True
                            selected += 1

        if selected > 0:
            self.report({"INFO"}, f"{selected} new {'track(s)' if is_stot else 'strip(s)'} selected")
        else:
            self.report({"WARNING"}, f"No new {'track(s)' if is_stot else 'strip(s)'} were selected")

        return {"FINISHED"}