import networkx as nx
import matplotlib.pyplot as plt
 
def describe():
    G = nx.read_edgelist('./output/save1.txt', nodetype=str)
    #図の作成。figsizeは図の大きさ
    plt.figure(figsize=(10, 8))
 
    #図のレイアウトを決める。kの値が小さい程図が密集する
    pos = nx.spring_layout(G, k=0.8)
 
    #ノードとエッジの描画
    # _color: 色の指定
    # alpha: 透明度の指定
    nx.draw_networkx_edges(G, pos, edge_color='y')

    nodes = G.nodes()

    color = [ choose_color(n) for n in nodes]

    nx.draw_networkx_nodes(G, pos, node_color=color, alpha=0.5)
 
    #ノード名を付加
    nx.draw_networkx_labels(G, pos, font_size=10)
 
    #X軸Y軸を表示しない設定
    plt.axis('off')
 
    #図を描画
    plt.show()

def choose_color(node):
    if node[1] == "1":
        return "r"
    elif node[1] == "2":
        return "g"
    elif node[1] == "3":
        return "b"
    


describe()
