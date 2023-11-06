import ezdxf
from ezdxf.enums import TextEntityAlignment

def Draw_device(filename, square_size, circle_radius, text):
    # 创建新的DXF文档
    doc = ezdxf.new()
    msp = doc.modelspace()

    # 计算正方形的顶点坐标
    square_vertices = [
        (0, 0),
        (square_size, 0),
        (square_size, square_size),
        (0, square_size)
    ]

    # 添加正方形
    square = msp.add_lwpolyline(square_vertices, close=True)

    # 计算圆的中心
    circle_center = (square_size / 2, square_size / 2)

    # 添加圆
    msp.add_circle(circle_center, circle_radius)

    # 计算文本的插入点
    text_insert_point = (circle_center[0] - circle_radius / 2, circle_center[1] - circle_radius / 2+1.4)

    # 添加文本
    msp.add_text(text, dxfattribs={"style": "LiberationSerif",'height': 1.6,'width': 0.4}).set_placement(text_insert_point, align=TextEntityAlignment.LEFT)

    # 保存DXF文件
    doc.saveas(filename)

    # 使用示例：


Draw_device('square_with_circle.dxf', square_size=5.2, circle_radius=4.5, text='7900-12')