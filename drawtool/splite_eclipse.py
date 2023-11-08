

import ezdxf
import math

def draw_equally_spaced_blocks_on_ellipse_arc(center, major_axis, ratio, start_angle, end_angle, num_divisions):
    doc = ezdxf.new()
    msp = doc.modelspace()

    for i in range(num_divisions):
        angle = start_angle + (i * (end_angle - start_angle) / num_divisions)
        x = center[0] + major_axis[0] * ratio * math.cos(math.radians(angle))
        y = center[1] + major_axis[1] * ratio * math.sin(math.radians(angle))

        # 计算方块的四个角坐标
        square_size = 0.1  # 方块的大小
        points = [(x - square_size / 2, y - square_size / 2),
                  (x + square_size / 2, y - square_size / 2),
                  (x + square_size / 2, y + square_size / 2),
                  (x - square_size / 2, y + square_size / 2)]

        # 绘制方块
        msp.add_lwpolyline(points)

    doc.saveas('ellipse_arc_with_blocks.dxf')

# 椭圆弧参数
center = (2, 2)
major_axis = (3, 0)
ratio = 0.5
start_angle = 30  # 起始角度
end_angle = 150  # 结束角度

num_divisions = 5  # 等分数

draw_equally_spaced_blocks_on_ellipse_arc(center, major_axis, ratio, start_angle, end_angle, num_divisions)
