import os
import ezdxf
import pandas as pd
import drawtool.drawSquare as ds
import drawtool.draw_device as dd
from ezdxf.enums import TextEntityAlignment
from draw_net_unit import draw_link_eclipse, draw_net_eclipse

file_path = "C:\\Users\\demon\\Desktop\\work\\资料\\资料"


def handle_data(file_path, net_name, store_path):
    network_element_files = [filename for filename in os.listdir(file_path) if "网元报表" in filename]

    df = pd.read_excel(os.path.join(file_path, network_element_files[0]), skiprows=3)
    print("read excel done")
    if net_name == "":
        net_name = "GXX-5G-50GE-JR046"
        # net_name = "GXN-5G-10GE-JR067"

    filtered_df = df[df["所属子网"].str.contains(net_name)]

    selected_column_values = filtered_df["网元名称"].tolist()

    print("selected_column_values = ", selected_column_values)

    net_element_type = filtered_df["网元类型（主控类型）"]
    print("net_element_type = ", net_element_type.tolist())

    type_dic = {}
    print("len(selected_column_values)= ", len(selected_column_values))
    for i, j in zip(selected_column_values, net_element_type):
        type_dic[i] = j

    print("type_dic = ", type_dic)

    # 从链路报表中查找数据
    link_road_files = [filename for filename in os.listdir(file_path) if "链路报表" in filename]
    # link_road_files
    link_road_df = pd.read_excel(os.path.join(file_path, link_road_files[0]), skiprows=3)
    # link_road_df

    # net_unit = link_road_df[link_road_df["链路名称"].isin(selected_column_values)]
    net_unit = link_road_df[link_road_df["链路名称"].apply(lambda x: any(item in x for item in selected_column_values))]
    # print("net_unit = ",net_unit)

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

    print("data = ", data)
    df = pd.DataFrame(data)

    print("创建无向图")
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
    print("创建DXF图")

    from draw_net_unit import draw_link_eclipse
    # doc = ezdxf.new()
    # msp = doc.modelspace()
    doc, msp = ds.create_document()
    point = [0, 0]
    ds.create_drawing(doc, msp, point)
    dd.create_device_block(doc, "device")
    dd.draw_devices_legend(msp, point)
    draw_net_eclipse(msp, point, net_name)
    draw_link_eclipse(msp, point, net_name)

    # 将节点和边添加到DXF图中
    node_positions = nx.spring_layout(G)  # 选择一种布局算法

    from draw_device import create_device_block

    # create small block
    # block = doc.blocks.new("small_device_block")
    # block.add_lwpolyline([
    #     (0, 0),
    #     (0, 5.2/150),
    #     (5.2/150, 5.2/150),
    #     (5.2/150, 0),
    #     (0, 0)
    # ])
    #
    # block.add_circle((2.6/150, 2.6/150), 2.25/150)
    # block.add_text("name",(2.6,2.6), dxfattribs={'style': 'OpenSans', 'height': 1.6, 'width': 0.4},align =TextEntityAlignment.MIDDLE_CENTER)

    '''
        for node, pos in node_positions.items():
        msp.add_circle(center=(pos[0], pos[1]), radius=0.04, dxfattribs={'layer': 'Nodes'})

        # create block
        msp.add_text(str(node), dxfattribs={'style': 'OpenSans', 'height': 0.01, 'width': 0.7}).set_placement((pos[0], pos[1]), align= TextEntityAlignment.LEFT)
        for neighbor in G.neighbors(node):
            neighbor_pos = node_positions[neighbor]
            msp.add_line(start=(pos[0], pos[1]), end=(neighbor_pos[0], neighbor_pos[1]), dxfattribs={'layer': 'Edges'})
    '''

    block = doc.blocks.new("topology")
    for node, pos in node_positions.items():
        msp.add_circle(center=(pos[0], pos[1]), radius=0.04, dxfattribs={'layer': 'Nodes'})
        block.add_lwpolyline([
            (pos[0] + 0, pos[1] + 0),
            (pos[0] + 0, pos[1] + 5.2 / 150),
            (pos[0] + 5.2 / 150, pos[1] + 5.2 / 150),
            (pos[0] + 5.2 / 150, pos[1] + 0),
            (pos[0] + 0, pos[1] + 0)
        ])
        block.add_circle((pos[0]+2.6 / 150, pos[1]+2.6 / 150), 2.25 / 150)
        # create block
        block.add_text(str(node), dxfattribs={'style': 'OpenSans', 'height': 1.6/150, 'width': 0.7}).set_placement(
            (pos[0], pos[1]), align=TextEntityAlignment.LEFT)
        for neighbor in G.neighbors(node):
            neighbor_pos = node_positions[neighbor]
            block.add_line(start=(pos[0], pos[1]), end=(neighbor_pos[0], neighbor_pos[1]), dxfattribs={'layer': 'Edges'})

    msp.add_blockref("topology", (point[0]+300 , point[1]+100 ), dxfattribs={
        'layer': 'origin_device',
        'xscale': 150,
        'yscale': 150
    })
    print("ready save file")
    # 保存DXF文件
    doc.saveas(store_path + "net_element_topology.dxf")


def draw(store_path):
    net_name = "GXX-5G-50GE-JR046"
    handle_data(file_path, net_name, store_path)


def main():
    store_path = ""
    draw(store_path)


if __name__ == '__main__':
    main()
