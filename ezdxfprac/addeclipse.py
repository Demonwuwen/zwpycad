import ezdxf
import math
from ezdxf.enums import TextEntityAlignment
# 创建新的DXF文档
doc = ezdxf.new()

# 添加新的图纸和模型空间
msp = doc.modelspace()

# 添加椭圆
center = (5, 5)  # 椭圆的中心坐标
major_axis = (3, 0)  # 长轴的向量
ratio = 0.5  # 长轴和短轴的比例
ellipse = msp.add_ellipse(center, major_axis, ratio)

# 将椭圆等分成5份
num_divisions = 5
for i in range(num_divisions):
    angle = math.radians(i * 360 / num_divisions)  # 将角度转换为弧度
    x = center[0] + major_axis[0] * math.cos(angle)
    y = center[1] + major_axis[1] * math.sin(angle)

    # 添加小方块
    size = 0.2  # 小方块的大小
    square = msp.add_lwpolyline([
        (x + size, y + size),
        (x + size, y - size),
        (x - size, y - size),
        (x - size, y + size),
        (x + size, y + size)
    ])

    # 标注方块名字
    text_location = (x + size, y + 1.5)
    msp.add_text(f"Square {i + 1}", dxfattribs={'height': 0.2}).set_placement(text_location, align=TextEntityAlignment.MIDDLE_RIGHT)

# 保存DXF文件
doc.saveas('ellipse_with_squares.dxf')
