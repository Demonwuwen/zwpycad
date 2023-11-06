import ezdxf

doc = ezdxf.new("R2010",setup=True)

msp = doc.modelspace()
msp.add_line((0, 0), (10, 0), dxfattribs={"linetype": "DASHED"})

doc.saveas("ezdxfprac.dxf")