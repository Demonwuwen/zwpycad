import ezdxf


doc = ezdxf.new()
# Getting the modelspace of a DXF document:
msp = doc.modelspace()

# Getting a paperspace layout by the name as shown in the tab of a CAD application:
psp = doc.paperspace()

# Getting a block layout by the block name:
blk = doc.blocks.get("NAME")

# Get all lines of layer "MyLayer"
