import ezdxf

# doc = ezdxf.new("R2000")
# msp = doc.modelspace()
#
# points = [(0, 0), (3, 0), (6, 3), (6, 6)]
# msp.add_lwpolyline(points)
#
# doc.saveas("lwpolyline1.dxf")

doc = ezdxf.readfile("lwpolyline1.dxf")
msp = doc.modelspace()

line = msp.query("LWPOLYLINE").first
if line is not None:
    line.append_points([(8, 7), (10, 7)])

doc.saveas("lwpolyline2.dxf")

doc = ezdxf.readfile("lwpolyline2.dxf")
msp = doc.modelspace()

line = msp.query("LWPOLYLINE").first

with line.points("xyseb") as points:
    # points is a standard Python list
    # existing points are 5-tuples, but new points can be
    # set as (x, y, [start_width, [end_width, [bulge]]]) tuple
    # set start_width, end_width to 0 to be ignored (x, y, 0, 0, bulge).

    # delete last 2 points
    del points[-2:]
    # adding two points
    points.extend([(4, 7), (0, 7)])

doc.saveas("lwpolyline3.dxf")

doc = ezdxf.new("R2000")
msp = doc.modelspace()

# point format = (x, y, [start_width, [end_width, [bulge]]])
# set start_width, end_width to 0 to be ignored (x, y, 0, 0, bulge).

points = [(0, 0, .1, .15), (3, 0, .2, .25), (6, 3, .3, .35), (6, 6)]
msp.add_lwpolyline(points)

doc.saveas("lwpolyline4.dxf")


doc = ezdxf.new("R2000")
msp = doc.modelspace()

# point format = (x, y, [start_width, [end_width, [bulge]]])
# set start_width, end_width to 0 to be ignored (x, y, 0, 0, bulge).

points = [(0, 0, 0, .05), (3, 0, .1, .2, -.5), (6, 0, .1, .05), (9, 0)]
msp.add_lwpolyline(points)

doc.saveas("lwpolyline5.dxf")