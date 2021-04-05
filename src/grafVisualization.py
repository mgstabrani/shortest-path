import networkx as nx
import matplotlib.pyplot as plt

def grafVisualization(g, nodes, edges, found, answer, choosenEdges):
    #Set posisi node
    pos = {}
    for i in range(g.getNumOfNode()):
        pos[nodes[i]] = g.getNodeCoordinate(nodes[i])

    #Visulisasi Graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.draw_networkx(G, pos, node_color="blue", font_size=8, edge_color="blue")
    if(found):
        nx.draw_networkx(G, pos, nodelist=answer[0], node_color="red", font_size=8, edgelist=choosenEdges, edge_color="red")
    plt.show()