
import os

import ezdxf

print(os.listdir(os.getcwd()))


filePath = "C:\\Users\\demon\\Desktop\\work\\资料\\资料"
# print(os.listdir(filePath))
network_element_files = [filename for filename in os.listdir(filePath) if "网元报表" in filename]
import pandas as pd

startrow=2
skiprows=startrow
df = pd.read_excel(os.path.join(filePath,  network_element_files[0]),skiprows=3)

keyword = "GXN-5G-10GE-JR067"
filtered_df = df[df["所属子网"].str.contains(keyword)]

selected_column_values = filtered_df["网元名称"].tolist()
# print(selected_column_values)

link_road_files = [filename for filename in os.listdir(filePath) if "链路报表" in filename]
# link_road_files
link_road_df = pd.read_excel(os.path.join(filePath,  link_road_files[0]),skiprows=3)
# link_road_df

# net_unit = link_road_df[link_road_df["链路名称"].isin(selected_column_values)]
net_unit = link_road_df[link_road_df["链路名称"].apply(lambda x: any(item in x for item in selected_column_values))]
# print(net_unit)

source_net = net_unit["源网元"].tolist()
# source_net

dest_net = net_unit["宿网元"].tolist()

import networkx as nx
import matplotlib.pyplot as plt

# 创建示例数据
data = {
    "源网元": source_net,
    "宿网元": dest_net
}

df = pd.DataFrame(data)

# 创建无向图a
G = nx.Graph()

# 添加节点和边
for _, row in df.iterrows():
    G.add_edge(row["源网元"], row["宿网元"])

# 绘制网络图
pos = nx.spring_layout(G)  # 选择一种布局算法
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_color="black")
# plt.title("拓扑结构")
# plt.savefig('拓扑.jpg')
# plt.show()

# 创建DXF图
doc = ezdxf.new()
msp = doc.modelspace()

# 将节点和边添加到DXF图中
node_positions = nx.spring_layout(G)  # 选择一种布局算法
for node, pos in node_positions.items():
    msp.add_circle(center=(pos[0], pos[1]), radius=0.05, dxfattribs={'layer': 'Nodes'})
    for neighbor in G.neighbors(node):
        neighbor_pos = node_positions[neighbor]
        msp.add_line(start=(pos[0], pos[1]), end=(neighbor_pos[0], neighbor_pos[1]), dxfattribs={'layer': 'Edges'})

# 保存DXF文件
doc.saveas("topology1.dxf")