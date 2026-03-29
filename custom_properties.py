# type: ignore

import bpy

class StripProperties(bpy.types.PropertyGroup): 
    action: bpy.props.PointerProperty(
        type=bpy.types.Action, 
        name="Action"
    )  

    blend_in: bpy.props.FloatProperty(
        name="Blend In",
        default=0.0,
        description="Set blend in value",
        options=set()
    )  

    blend_out: bpy.props.FloatProperty(
        name="Blend Out",
        default=0.0,
        description="Set blend out value",
        options=set()
    )  
    
    blend_type : bpy.props.EnumProperty(
        items=[("REPLACE", "Replace", "Set blend type to"),
               ("COMBINE", "Combine", "Set blend type to"),
               ("ADD", "Add", "Set blend type to"),
               ("SUBTRACT", "Subtract", "Set blend type to"),
               ("MULTIPLY", "Multiply", "Set blend type to")],
        name="Blend Type",
        options=set()
    ) 

    extrapolation : bpy.props.EnumProperty(
        items=[("HOLD", "Hold", "Set extrapolation to"),
               ("HOLD_FORWARD", "Hold Forward", "Set extrapolation to"),
               ("NOTHING", "Nothing", "Set extrapolation to")],
        name="Extrapolation",
        options=set()
    ) 

    frame_end: bpy.props.IntProperty(
        name="End Frame",
        default=0,
        description="Set frame end value",
        options=set()
    )  

    frame_start: bpy.props.IntProperty(
        name="Start Frame",
        default=0,
        description="Set frame start value",
        options=set()
    )  

    influence: bpy.props.FloatProperty(
        name="Influence",
        default=0.0,
        description="Set animated influence value",
        options=set()
    )  

    mute: bpy.props.BoolProperty(
        name="Mute",
        default=False,
        description="Set mute type",
        options=set()
    )  

    name: bpy.props.StringProperty(
        name="Name",
        default="**STRIP_NAME**",
        description="Edit track name. Tip: **STRIP_NAME** will be substituted with the name of the original track",
        options=set()
    )  

    repeat: bpy.props.IntProperty(
        name="Repeat",
        default=0,
        description="Set repeat value",
        options=set()
    )  

    scale: bpy.props.FloatProperty(
        name="Scale",
        default=0.0,
        description="Set scale value",
        options=set()
    )  

    strip_time: bpy.props.FloatProperty(
        name="Strip Time",
        default=0.0,
        description="Set animated strip time value",
        options=set()
    )  

    # type: bpy.props.StringProperty(
    #     name="Type",
    #     default="",
    #     description="Include type attribute to edit",
    #     options=set()
    # )  

    use_animated_influence: bpy.props.BoolProperty(
        name="Animated Influence",
        default=False,
        description="Toggle animated influence",
        options=set()
    )  

    use_animated_time: bpy.props.BoolProperty(
        name="Animated Time",
        default=False,
        description="Toggle animated time",
        options=set()
    )  

    use_animated_time_cyclic: bpy.props.BoolProperty(
        name="Animated Time Cyclic",
        default=False,
        description="Toggle animated time cyclic",
        options=set()
    )  

    use_auto_blend: bpy.props.BoolProperty(
        name="Auto Blend In/Out",
        default=False,
        description="Toggle auto blend",
        options=set()
    )  

    use_reverse: bpy.props.BoolProperty(
        name="Reverse",
        default=False,
        description="Toggle reverse",
        options=set()
    )  

    use_sync_length: bpy.props.BoolProperty(
        name="Sync Length",
        default=False,
        description="Toggle sync length",
        options=set()
    )  
    
    is_search_includes : bpy.props.BoolProperty( ## WARNING: Not a blender porperty
        name="Name Contains Keyword",
        default=True,
        description="When enabled, the search key will inclusively match any part of the target names. Disable for exact matching only.",
        options=set()
    ) 

class StripPropertyToggles(bpy.types.PropertyGroup):
    action : bpy.props.BoolProperty(
        name="Action",
        default=False,
        description="Include action to edit",
        options=set()
    )  

    # action_frame_end : bpy.props.BoolProperty(
    #     name="Action Frame End",
    #     default=False,
    #     description="Include action frame end to edit",
    #     options=set()
    # )  

    # action_frame_start : bpy.props.BoolProperty(
    #     name="Action Frame Start",
    #     default=False,
    #     description="Include action frame start to edit",
    #     options=set()
    # )  

    blend_in : bpy.props.BoolProperty(
        name="Blend In",
        default=False,
        description="Include blend in amount to edit",
        options=set()
    )  

    blend_out : bpy.props.BoolProperty(
        name="Blend Out",
        default=False,
        description="Include blend out amount to edit",
        options=set()
    )  

    blend_type : bpy.props.BoolProperty(
        name="Blend Type",
        default=False,
        description="Include blend type to edit",
        options=set()
    )  

    extrapolation : bpy.props.BoolProperty(
        name="Extrapolation",
        default=False,
        description="Include extrapolation type to edit",
        options=set()
    )  

    fcurves : bpy.props.BoolProperty(
        name="Fcurves",
        default=False,
        description="Include fcurves to edit",
        options=set()
    )  

    frame_end : bpy.props.BoolProperty(
        name="End Frame",
        default=False,
        description="Include end frame value to edit",
        options=set()
    )  

    frame_start : bpy.props.BoolProperty(
        name="Start Frame",
        default=False,
        description="Include start frame value to edit",
        options=set()
    )  

    modifiers : bpy.props.BoolProperty(
        name="Modifiers",
        default=False,
        description="Include modifiers to edit",
        options=set()
    )  

    name : bpy.props.BoolProperty(
        name="Name",
        default=False,
        description="Include name attribute to edit",
        options=set()
    )  

    repeat : bpy.props.BoolProperty(
        name="Repeat",
        default=False,
        description="Include repeat amount to edit",
        options=set()
    )  

    scale : bpy.props.BoolProperty(
        name="Scale",
        default=False,
        description="Include scale amount to edit",
        options=set()
    )  

    strips : bpy.props.BoolProperty(
        name="Strips",
        default=False,
        description="Include strips attribute to edit",
        options=set()
    )  

    # type : bpy.props.BoolProperty(
    #     name="Type",
    #     default=False,
    #     description="Include type attribute to edit",
    #     options=set()
    # )  

    use_animated_influence : bpy.props.BoolProperty(
        name="Animated Influence",
        default=False,
        description="Include animated influence to edit",
        options=set()
    )  

    influence : bpy.props.BoolProperty(
        name="Influence",
        default=False,
        description="Include influence amount to edit",
        options=set()
    )  

    use_animated_time : bpy.props.BoolProperty(
        name="Animated Time",
        default=False,
        description="Include animated time to edit",
        options=set()
    )  

    strip_time : bpy.props.BoolProperty(
        name="Strip Time",
        default=False,
        description="Include strip time attribute to edit",
        options=set()
    )  

    use_animated_time_cyclic : bpy.props.BoolProperty(
        name="Animated Time Cyclic",
        default=False,
        description="Include animated time cyclic to edit",
        options=set()
    )  

    use_auto_blend : bpy.props.BoolProperty(
        name="Auto Blend In/Out",
        default=False,
        description="Include auto blend attribute to edit",
        options=set()
    )  

    mute : bpy.props.BoolProperty(
        name="Mute",
        default=False,
        description="Include mute attribute to edit",
        options=set()
    )  

    use_reverse : bpy.props.BoolProperty(
        name="Reverse",
        default=False,
        description="Include reverse attribute to edit",
        options=set()
    )  

    use_sync_length : bpy.props.BoolProperty(
        name="Sync Length",
        default=False,
        description="Include sync length to edit",
        options=set()
    )  

class PushdownProperties(bpy.types.PropertyGroup):
    frame_start : bpy.props.IntProperty(
        name="Frame Start",
        default=1,
        description="Frame starts at",
        options=set()
    ) 

    start_min : bpy.props.IntProperty(
        name="Start Min",
        default=2,
        description="Assigns start frame min",
        options=set()
    ) 

    start_max : bpy.props.IntProperty(
        name="Start Max",
        default=5,
        description="Assigns start frame max",
        options=set()
    ) 

    random_start : bpy.props.BoolProperty(
        name="Randomize",
        default=False,
        description="Assigns random starts for each strip",
        options=set()
    ) 

    track_name : bpy.props.StringProperty(
        name="New Track Name",
        default="Animation_**OBJECT_NAME**",
        description="Sets name for new tracks. Tip: **OBJECT_NAME** will be substituted with the name of the associated object."
    ) 

    strip_name : bpy.props.StringProperty(
        name="New Strip Name",
        default="AnimationStrip_**OBJECT_NAME**",
        description="Sets name for new strips. Tip, **OBJECT_NAME** will be replaced by its object name."
    ) 

    distinct_strip_name : bpy.props.BoolProperty(
        name="Distinct Strip Names",
        default=False,
        description="Sets strip names different than tracks",
        options=set()
    ) 

    set_mute_new_track : bpy.props.BoolProperty(
        name="Mute New Tracks",
        default=False,
        description="Sets mute for new tracks",
        options=set()
    ) 

    keep_actions : bpy.props.BoolProperty(
        name="Keep actions",
        default=False,
        description="Keeps actions in Action Editor",
        options=set()
    ) 

    # change_action_name : bpy.props.BoolProperty(
    #     name="Change Action Name",
    #     default=False,
    #     description="Change action names (Number prefixes will be added as blender default)",
    #     options=set()
    # ) 

class DublicateOpsProperties(bpy.types.PropertyGroup):
    dublicate_name: bpy.props.StringProperty(
        name="Track Name",
        default="Dublicate_**TRACK_NAME**",
        description="Set name for copy tracks. Tip: **TRACK_NAME** will be substituted with the name of the original track",
        options=set()
    ) #type: ignore

    is_copy_linked : bpy.props.BoolProperty(
        name="Linked Copy",
        default=True,
        description="When disabled, actions of strips will also be dublicated",
        options=set()
    ) 

class ModifySelectionProperties(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Name",
        default="",
        description="Search by name",
        options=set()
    )

    selection_option : bpy.props.EnumProperty(
        items=[("ADD", "Add", "Add to current selection"),
               ("SUBTRACT", "Subtract", "Subtract from current selection"),
               ("INTERSECT", "Intersect", "Intersect with current selection"),
               ],
        name="Selection Option",
        options=set()
    ) 
    
    selection_type : bpy.props.EnumProperty(
        items=[("TRACK", "Track", "Modify track selection"),
               ("STRIP", "Strip", "Modify strip selection")],
        name="Selection by",
        options=set()
    ) 
    
    include_tracks : bpy.props.EnumProperty(
        items=[("BOTH", "Both", "Include both muted and locked tracks"),
               ("MUTE", "Mute", "Include only muted tracks"),
               ("LOCK", "Lock", "Include only locked tracks"),
               ("NONE", "None", "Muted and locked tracks are excluded"),],
        name="Include Tracks",
        options=set()
    ) 
    
    filter_method : bpy.props.EnumProperty(
        items=[("name", "Name", "Filter by name"),
               ("frame_start", "Start Frame", "Filter by start frame value"),
               ("frame_end", "End Frame", "Filter by end frame value"),
               ("extrapolation", "Extrapolation Type", "Filter by extrapolation type"),
               ("blend_type", "Blend Type", "Filter by blend type"),
               ("use_auto_blend", "Auto Blend State", "Filter by auto blend state"),
               ("blend_in", "Blend In Amount", "Filter by blend in amount"),
               ("blend_out", "Blend Out Amount", "Filter by blend out amount"),
               ("use_reverse", "Reverse State", "Filter by reverse state"),
               ("use_animated_influence", "Animated Influence State", "Filter by animated influence state"),
               ("influence", "Influence Amount", "Filter by influence amount"),
               ("scale", "Scale", "Filter by scale"),
               ("repeat", "Repeat", "Filter by repeat")],
        name="Filter by",
        options=set()
    ) 

class EditTrackProperties(bpy.types.PropertyGroup):
    name_input : bpy.props.StringProperty(
        name="Name",
        default="**TRACK_NAME**",
        description="Edit track name. Tip: **TRACK_NAME** will be substituted with the name of the original track",
        options=set()
    ) 

    edit_mode : bpy.props.EnumProperty(
        items=[("TOGGLE", "Toggle", "Toggle mute or lock properties"),
               ("SET", "Set", "Set mute or lock properties"),
               ],
        name="Edit Mode",
        options=set()
    ) 

    mute_input : bpy.props.BoolProperty(
        name="Mute",
        default=False,
        description="Mute",
        options=set()
    ) 

    lock_input : bpy.props.BoolProperty(
        name="Lock",
        default=False,
        description="Lock",
        options=set()
    ) 

class NbeProperties(bpy.types.PropertyGroup):
    strip_props: bpy.props.PointerProperty(type=StripProperties) 
    strip_toggles: bpy.props.PointerProperty(type=StripPropertyToggles)
    pushdown_props: bpy.props.PointerProperty(type=PushdownProperties)
    dublicate_ops_props: bpy.props.PointerProperty(type=DublicateOpsProperties)
    modify_selection_props: bpy.props.PointerProperty(type=ModifySelectionProperties)
    edit_track_props: bpy.props.PointerProperty(type=EditTrackProperties)

classes = (
    ModifySelectionProperties,
    StripProperties,
    PushdownProperties,
    DublicateOpsProperties,
    EditTrackProperties,
    StripPropertyToggles,
    NbeProperties,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.NBE_properties = bpy.props.PointerProperty(type=NbeProperties)
    # bpy.types.Scene.NBE_modify_selection_properties = bpy.props.PointerProperty(type=ModifySelectionProperties)
    # bpy.types.Scene.NBE_strip_properties = bpy.props.PointerProperty(type=StripProperties)
    # bpy.types.Scene.NBE_pushdown_properties = bpy.props.PointerProperty(type=PushdownProperties)
    # bpy.types.Scene.NBE_dublicate_op_properties = bpy.props.PointerProperty(type=DublicateOpsProperties)
    # bpy.types.Scene.NBE_edit_track_op_properties = bpy.props.PointerProperty(type=EditTrackProperties)
    # bpy.types.Scene.NBE_strip_property_toggles = bpy.props.PointerProperty(type=StripPropertyToggles)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.NBE_properties
    # del bpy.types.Scene.NBE_modify_selection_properties
    # del bpy.types.Scene.NBE_strip_properties
    # del bpy.types.Scene.NBE_pushdown_properties
    # del bpy.types.Scene.NBE_dublicate_op_properties
    # del bpy.types.Scene.NBE_edit_track_op_properties
    # del bpy.types.Scene.NBE_strip_property_toggles