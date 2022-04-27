import networkx as nx
import matplotlib.pyplot as plt

def grafVisualization(g, nodes, edges, found, answer, choosenEdges, nodeFrom, nodeTo):
    #Set posisi node
    pos = {}
    for i in range(g.getNumOfNode()):
        pos[nodes[i]] = g.getNodeCoordinate(nodes[i])

    #Visulisasi Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.draw_networkx(G, pos, node_color="blue", font_size=8, edge_color="blue")

    #Jika jalur ketemu
    if found:
        nx.draw_networkx(G, pos, nodelist=answer[0], node_color="red", font_size=8, edgelist=choosenEdges, edge_color="red")
        nx.draw_networkx(G, pos, nodelist=[answer[0][-1]], node_color="green", font_size=8, edgelist=choosenEdges, edge_color="red")
        plt.xlabel("Jarak terdekat dari " + nodeFrom + " ke " + nodeTo + " adalah " + str(answer[1]*100) + " km")

    #Jika tidak punya jalur
    else:
        nx.draw_networkx(G, pos, nodelist=[nodeFrom], node_color="red", font_size=8, edge_color="blue")
        nx.draw_networkx(G, pos, nodelist=[nodeTo], node_color="green", font_size=8, edge_color="blue")
        plt.xlabel(nodeFrom + " ke " + nodeTo + " tidak memiliki jalur")

    #Menampilkan graf
    plt.show()
