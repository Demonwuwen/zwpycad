import ezdxf
import math
import drawtool.drawSquare as ds
import drawtool.draw_device as dd
from ezdxf.enums import TextEntityAlignment

def draw_net_eclipse(msp,point,net_name):

    # 画网元
    msp.add_ellipse((220+point[0], 260+point[1]), major_axis=(46, 0), ratio=11/45)
    msp.add_text(net_name, dxfattribs={'style': 'OpenSans', 'height': 3, 'width': 0.7} ).set_placement((220+point[0], 260+point[1]),align =TextEntityAlignment.MIDDLE_CENTER)

def draw_link_eclipse(msp, point, net_name):
    # 画链路
    msp.add_ellipse(center=(220+point[0], 180+point[1]), major_axis=(0, 46), ratio=16/35, start_param=math.pi/6, end_param=-math.pi/6)
    msp.add_text(net_name, dxfattribs={'style': 'OpenSans', 'height': 3, 'width': 0.7} ).set_placement((220+point[0], 180+point[1]),align =TextEntityAlignment.MIDDLE_CENTER)


def main():
    doc, msp = ds.create_document()
    point = [0, 0]
    ds.create_drawing(doc, msp, point)
    dd.create_device_block(doc, "device")
    dd.draw_devices_legend(msp, point)

    draw_net_eclipse(msp, point,"成都-5G-100GE-HR31")
    draw_link_eclipse(msp,point,"GXN-5G-10GE-JR067")
    doc.saveas("draw_net_unit.dxf")


if __name__ == "__main__":
    main()
