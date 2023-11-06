import ezdxf
from ezdxf.enums import TextEntityAlignment


def create_frame_block(doc, name, width, height):
    block = doc.blocks.new(name)
    block.add_lwpolyline([
        (0, 0),
        (width, 0),
        (width, height),
        (0, height),
        (0, 0)
    ])
    return block


def create_title(doc):
    block = doc.blocks.new('title')
    block.add_lwpolyline([
        (0, 0),
        (0, 30),
        (180, 30),
        (180, 0),
        (0, 0)
    ])
    block.add_lwpolyline([
        (20, 0),
        (20, 30)
    ])
    block.add_text("专业设计人", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((4, 2),
                                                                                                              align=TextEntityAlignment.LEFT)
    block.add_text("校 审 人", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((5, 9.5),
                                                                                                            align=TextEntityAlignment.LEFT)
    block.add_text("设 计 人", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((5, 17),
                                                                                                            align=TextEntityAlignment.LEFT)
    block.add_text("项目总负责人", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement(
        (3, 24.5), align=TextEntityAlignment.LEFT)

    block.add_text("出图日期", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((44, 2),
                                                                                                            align=TextEntityAlignment.LEFT)
    block.add_text("比   例", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((45, 9.5),
                                                                                                           align=TextEntityAlignment.LEFT)
    block.add_text("单   位", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((45, 17),
                                                                                                           align=TextEntityAlignment.LEFT)
    block.add_text("专业负责人", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement(
        (43, 24.5), align=TextEntityAlignment.LEFT)

    block.add_text("图 号", dxfattribs={'style': 'OpenSans', 'height': 2.5, 'width': 0.7}).set_placement((83, 2),  align=TextEntityAlignment.LEFT)
    block.add_text("中国移动通信集团设计院有限公司",dxfattribs={'style': 'OpenSans', 'height': 5, 'width': 0.7}).set_placement((92, 20.5),align=TextEntityAlignment.LEFT)
    block.add_lwpolyline([
        (40, 0),
        (40, 30)
    ])
    block.add_lwpolyline([
        (60, 0),
        (60, 30)
    ])
    block.add_lwpolyline([
        (80, 0),
        (80, 30)
    ])
    block.add_lwpolyline([
        (90, 0),
        (90, 7.5)
    ])

    block.add_lwpolyline([
        (0, 7.5),
        (180, 7.5)
    ])
    block.add_lwpolyline([
        (0, 15),
        (80, 15)
    ])
    block.add_lwpolyline([
        (0, 22.5),
        (80, 22.5),
        (80, 18.5),
        (180, 18.5)
    ])
    block.add_lwpolyline([
        (0, 30),
        (180, 30)
    ])
    return block


def create_document():
    # 创建新的DXF文档
    doc = ezdxf.new(setup=True)
    # 创建层
    # 添加新的图纸和模型空间
    msp = doc.modelspace()
    # 'RED'、'YELLOW'、'GREEN'、'CYAN'、'BLUE'、'MAGENTA'
    doc.layers.add(name="outline_border", color=5, linetype="CONTINUOUS")
    doc.layers.add(name="border", linetype="CONTINUOUS", dxfattribs={'lineweight': 0.5})
    doc.layers.add(name="origin_device", linetype="CONTINUOUS")
    doc.layers.add(name="new_device", color=1, linetype="CONTINUOUS")
    doc.layers.add(name="extension_device", color=6, linetype="CONTINUOUS")
    # 返回模型空间对象
    return doc, msp


def create_drawing(doc, msp, point):
    # 创建矩形块
    o_name = "outline_border"
    o_width = 425
    o_height = 297
    create_frame_block(doc, o_name, o_width, o_height)
    msp.add_blockref('outline_border', point, dxfattribs={
        'layer': 'outline_border',
        'xscale': 1,
        'yscale': 1,
        'rotation': 0})

    i_point = [point[0]+25, point[1]+10]
    i_width = 390
    i_height = 277
    i_name = "border"
    create_frame_block(doc, i_name, i_width, i_height)
    msp.add_blockref('border', i_point, dxfattribs={
        'layer': 'border'
    })

    create_title(doc)
    t_point = [235, 10]
    msp.add_blockref('title', t_point, dxfattribs={
        'layer': 'border'
    })


def main():
    doc, msp = create_document()
    point = [0, 0]
    create_drawing(doc, msp, point)
    doc.saveas("draw_border.dxf")


if __name__ == "__main__":
    main()
