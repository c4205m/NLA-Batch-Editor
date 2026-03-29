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
        source = context.active_nla_strip
        toggle_props = context.scene.NBE_properties.strip_toggles

        if not source:
            self.report({"WARNING"}, "No active strip")
            return {"CANCELLED"}

        STRIP_NAME_PLACEHOLDER = "STRIP_NAME"

        for strip in context.selected_nla_strips:
            if strip == source:
                continue

            for item in toggle_props.__annotations__.keys():
                is_editable = getattr(toggle_props, item)

                if hasattr(source, item) and is_editable:
                    value = source.name.replace(f"**{STRIP_NAME_PLACEHOLDER}**", strip.name) if item == "name" else getattr(source, item)
                    setattr(strip, item, value)

        return {"FINISHED"}