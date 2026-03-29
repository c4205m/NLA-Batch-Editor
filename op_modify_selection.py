import bpy
from . import utils_attributes

class op(bpy.types.Operator):
    """Modify your selection with a search key"""
    bl_idname = "anim.modify_selection"
    bl_label = " Make Selection"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}
    
    @classmethod
    def poll(self, context):
        return context.area.type == 'NLA_EDITOR'
    
    def execute(self, context):
        class props:
            op = context.scene.NBE_properties.modify_selection_props
            strip = context.scene.NBE_properties.strip_props

        class selection:
            is_track = props.op.selection_type == "TRACK"
            has_mute = props.op.include_tracks == 'BOTH' or props.op.include_tracks == 'MUTE'
            has_locked = props.op.include_tracks == 'BOTH' or props.op.include_tracks == 'LOCK'

        search_source = props.op if props.op.filter_method == "name" else props.strip
        search_value = getattr(search_source, props.op.filter_method) 

        selectable_stacks = set()
        selected_stacks = set()

        new_selection_count = 0

        for object in context.view_layer.objects:
            if not object.animation_data or not object.animation_data.nla_tracks:
                continue

            nla_tracks = {track for track in object.animation_data.nla_tracks}
            mute_discard = {track for track in nla_tracks if track.mute} if not selection.has_mute else set()
            lock_discard = {track for track in nla_tracks if track.lock} if not selection.has_locked else set()
            nla_tracks -= lock_discard | mute_discard

            target_stacks = nla_tracks if selection.is_track else (strip for track in nla_tracks for strip in track.strips)

            for item in target_stacks:
                if (utils_attributes.compare_attribute(props.op.filter_method, 
                                        item, search_value, 
                                        props.strip.is_search_includes)):
                    selectable_stacks.add(item)

                if item.select:
                    item.select = False
                    selected_stacks.add(item)
                    new_selection_count -= 1

        final_selection = combine_selection(props.op.selection_option, selected_stacks, selectable_stacks)

        for stack in final_selection:
            stack.select = True
            new_selection_count += 1

        if new_selection_count > 0:
            self.report({"INFO"}, f"{new_selection_count} {'track(s)' if selection.is_track else 'strip(s)'} added to your selection")
        elif new_selection_count < 0:
            self.report({"INFO"}, f"{-new_selection_count} {'track(s)' if selection.is_track else 'strip(s)'} discarded from your selection")
        else:
            self.report({"WARNING"}, f"No new {'tracks' if selection.is_track else 'strips'} were selected")

        return {"FINISHED"}

def combine_selection(combination_type, current_items, new_items):
    match combination_type:
        case 'INTERSECT':
            return current_items & new_items
        case 'ADD':
            return current_items | new_items
        case 'SUBTRACT':
            return current_items - new_items