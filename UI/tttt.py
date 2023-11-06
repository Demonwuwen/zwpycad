import os
import ezdxf

# 创建示例数据
data = {
    "源网元": ["Node1", "Node2", "Node3"],
    "宿网元": ["Node2", "Node3", "Node1"]
}

# 创建DXF图
doc = ezdxf.new()
msp = doc.modelspace()

# 添加节点和边
for node1, node2 in zip(data["源网元"], data["宿网元"]):
    # 获取节点位置（这里假设节点的位置已经有了）
    node1_position = (0, 0)  # 你需要替换为实际的节点位置
    node2_position = (1, 1)  # 你需要替换为实际的节点位置

    # 添加节点名称文本
    msp.add_text("testnodestr")
    # msp.add_text(node1, dxfattribs={'layer': 'Nodes'}).set_location(node1_position)
    # msp.add_text(node2, dxfattribs={'layer': 'Nodes'}).set_location(node2_position)

    # 添加边
    msp.add_line(start=node1_position, end=node2_position, dxfattribs={'layer': 'Edges'})

# 保存DXF文件
doc.saveas("topology_with_labels.dxf")
