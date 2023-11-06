import ezdxf
import drawtool.drawSquare as ds
from ezdxf.enums import TextEntityAlignment

def create_device_block(doc, name):
    block = doc.blocks.new(name)

    block.add_lwpolyline([
        (0, 0),
        (0, 5.2),
        (5.2, 5.2),
        (5.2, 0),
        (0, 0)
    ])

    block.add_circle((2.6, 2.6), 2.25)
    return block


devices = ["1900", "990", "970", "960", "950", "910", "3900", "6900-8", "6900-16"]
status = ["原有", "新增", "扩容"]

offset_x = 37
offset_y = 13
device_name = "Optix PTN"
def draw_devices_legend(msp, point):

    x = 0
    for j in status:

        y = 0
        for i in devices:

            if j == "原有":
                msp.add_blockref("device", (point[0] + offset_x+x, point[1] + offset_y+y), dxfattribs={
                    'layer': 'origin_device'
                })
                msp.add_text(j+device_name + i + "设备", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((point[0] + offset_x+x+7.2, point[1] + offset_y+y+1), align =TextEntityAlignment.LEFT)
                msp.add_text(i, dxfattribs={'style': 'OpenSans', 'height': 1.6, 'width': 0.4}).set_placement((point[0] + offset_x+x+2.6, point[1] + offset_y+y+2.6),align =TextEntityAlignment.MIDDLE_CENTER)
                y += 9.4
            if j == "新增":
                msp.add_blockref("device", (point[0] + offset_x+x, point[1] + offset_y+y), dxfattribs={
                    'layer': 'new_device'
                })
                msp.add_text(j+device_name + i + "设备", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((point[0] + offset_x+x+7.2, point[1] + offset_y+y+1), align=TextEntityAlignment.LEFT)
                msp.add_text(i, dxfattribs={'style': 'OpenSans', 'height': 1.6, 'width': 0.4}).set_placement((point[0] + offset_x+x+2.6, point[1] + offset_y+y+2.6),align =TextEntityAlignment.MIDDLE_CENTER)

                y += 9.4
            if j == "扩容":
                msp.add_blockref("device", (point[0] + offset_x+x, point[1] + offset_y+y), dxfattribs={
                    'layer': 'extension_device'
                })
                msp.add_text(j+device_name + i + "设备", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((point[0] + offset_x+x+7.2, point[1] + offset_y+y+1), align=TextEntityAlignment.LEFT)
                msp.add_text(i, dxfattribs={'style': 'OpenSans', 'height': 1.6, 'width': 0.4}).set_placement((point[0] + offset_x+x+2.6, point[1] + offset_y+y+2.6),align =TextEntityAlignment.MIDDLE_CENTER)
                y += 9.4
        x += 56.5


def main():
    doc, msp = ds.create_document()
    point = [0, 0]
    ds.create_drawing(doc, msp, point)
    create_device_block(doc, "device")
    draw_devices_legend(msp, point)

    doc.saveas("draw_devices.dxf")


if __name__ == "__main__":
    main()
