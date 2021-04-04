from astar import *
from input import *
import networkx as nx
import matplotlib.pyplot as plt

g = Graf(nodes, adjacentNode, nodeCoordinate)

#Input node awal dan node akhir
nodeFrom = input("Masukkan lokasi awal: ")
nodeTo = input("Masukkan lokasi tujuan: ")

#Mencari jarak dan rute terpendek
answer = astar(g,nodeFrom, nodeTo)
print("Jarak terdekat: " + str(answer[1]) + " km")
print("Rute yang ditempuh: ", end=" ")
for i in range(len(answer[0])-1):
    print(answer[0][i], end=" -> ")
print(answer[0][len(answer[0])-1])

#Visulisasi Graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
nx.draw_networkx(G)
plt.show()