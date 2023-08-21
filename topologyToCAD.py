import networkx as nx
import ezdxf

# 创建示例拓扑结构图
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6)])

# 创建DXF图
doc = ezdxf.new()
msp = doc.modelspace()

# 绘制拓扑结构图
node_positions = nx.spring_layout(G)  # 选择一种布局算法
scale_factor = 1.0  # 不进行缩放
for node, pos in node_positions.items():
    msp.add_circle(center=(pos[0], pos[1]), radius=0.05, dxfattribs={'layer': 'Nodes'})
    for neighbor in G.neighbors(node):
        neighbor_pos = node_positions[neighbor]
        msp.add_line(start=(pos[0], pos[1]), end=(neighbor_pos[0], neighbor_pos[1]), dxfattribs={'layer': 'Edges'})

# 手动设置绘图范围以适应A4纸张大小（210mm x 297mm）
layout = doc.layout()

viewport = layout.add_viewport(center=(105, 148.5), width=210, height=297)
viewport.dxf.view_target = (105, 148.5, 0)  # 设置视点
viewport.dxf.view_height = 297  # 设置视口高度

# 保存DXF文件
doc.saveas("topology_a4.dxf")
