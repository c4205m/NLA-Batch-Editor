import bpy

class op(bpy.types.Operator):
    """Edit strips"""
    bl_idname = "anim.edit_strip_data"
    bl_label = "Edit Strips"
    bl_options = {"REGISTER", "INTERNAL", "UNDO"}

    @classmethod
    def poll(self, context):
        return context.area.type == "NLA_EDITOR"
    
    def execute(self, context):
        strip_props = context.scene.NBE_properties.strip_props
        toggle_props = context.scene.NBE_properties.strip_toggles

        print(context.selected_nla_strips)

        STRIP_NAME_PLACEHOLDER = "STRIP_NAME"

        for strip in context.selected_nla_strips:
            for item in toggle_props.__annotations__.keys():
                is_editable = getattr(toggle_props, item)

                if hasattr(strip_props, item):
                    user_input = getattr(strip_props, item)
                    if item is "name":
                        user_input = strip_props.name.replace(f"**{STRIP_NAME_PLACEHOLDER}**", strip.name)

                    if is_editable:
                        setattr(strip, item, user_input)

        return {"FINISHED"}