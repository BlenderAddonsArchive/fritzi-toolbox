import bpy


def draw_op(self, context):
    layout = self.layout
    if len(bpy.context.selected_nla_strips) <= 1:
        layout.operator("nla.ftb_prepare_strip")
    else:
        layout.operator_context = 'INVOKE_DEFAULT'
        layout.operator("nla.ftb_batch_prepare_strips")
    layout.operator_context = 'INVOKE_DEFAULT'
    layout.operator("nla.ftb_clean_bake_strips")


def register():
    bpy.types.NLA_MT_context_menu.append(draw_op)
    bpy.types.NLA_MT_strips.append(draw_op)


def unregister():
    bpy.types.NLA_MT_strips.remove(draw_op)
    bpy.types.NLA_MT_context_menu.remove(draw_op)
