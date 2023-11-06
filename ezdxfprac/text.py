import ezdxf
from ezdxf.enums import TextEntityAlignment

# The TEXT entity is a DXF primitive and is supported in all DXF versions.
# The argument setup=True creates standard linetypes and text styles in the
# new DXF document.
doc = ezdxf.new("R12", setup=True)
msp = doc.modelspace()

# Use method set_placement() to define the TEXT alignment, because the
# relations between the DXF attributes 'halign', 'valign', 'insert' and
# 'align_point' are tricky.
msp.add_text("A Simple Text").set_placement(
    (2, 3),
    align=TextEntityAlignment.MIDDLE_RIGHT
)

# Using a predefined text style:
msp.add_text(
    "Text Style w来啦啦啦啦啦了e: Liberation Serif",
    height=0.35,
    dxfattribs={"style": "LiberationSerif"}
).set_placement((2, 6), align=TextEntityAlignment.LEFT)

doc.saveas("simple_text.dxf")