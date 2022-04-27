from astar import *
from input import *
from mapVisualization import *
from grafVisualization import *
import sys

#Membuat graf dari file eksternal
g = Graf(nodes, adjacentNode, nodeCoordinate)

while(True):
    #Input node awal dan node akhir
    print(50*"=")
    for i in range(g.getNumOfNode()):
        print(str(i+1) + ". " + nodes[i])
    nodeFromInt = int(input("Masukkan lokasi awal (angka sesuai yang di atas): "))
    nodeToInt = int(input("Masukkan lokasi tujuan (angka yang sesuai di atas): "))
    nodeFrom = nodes[nodeFromInt-1]
    nodeTo = nodes[nodeToInt-1]
    #Mencari apakah nodeFrom dan nodeTo memiliki jalur
    hasil = []
    dikunjungi = []
    for i in range(g.getNumOfNode()):
        dikunjungi.append(0)
    found = dfsExploreNode(g, nodeFrom, nodeTo, dikunjungi, hasil)

    answer = []
    choosenEdges = []

    print(50*"=")
    #Jika ada jalur
    if(found):
        #Mencari jarak dan rute terpendek
        answer = astar(g,nodeFrom, nodeTo)
        print("Jarak terdekat: " + str(answer[1]*100) + " km")
        print("Rute yang ditempuh: ", end=" ")
        for i in range(len(answer[0])-1):
            print(answer[0][i], end=" -> ")
        print(answer[0][len(answer[0])-1])

        #Set edge yang diwarnai berbeda
        for i in range(len(answer[0]) - 1):
            choosenEdges.append([answer[0][i],answer[0][i+1]])

    #Jika tidak ada jalur
    else:
        print(nodeFrom, "ke", nodeTo, "tidak memiliki jalur.")

    #Menu pilih visualisasi
    print(50*"=")
    print("Visualisasi:")
    print("1. Graf")
    print("2. Map")
    visualize = int(input("Masukkan pilihan: "))

    if(visualize == 1):
        grafVisualization(g, nodes, edges, found, answer, choosenEdges, nodeFrom, nodeTo)
    elif(visualize == 2):
        mapVisualization(g,nodeFrom,nodeTo,nodes,answer, found, choosenEdges)

    #Menu lanjut program
    print(50*"=")
    print("Lanjut?")
    print("1. Ya")
    print("2. Tidak")
    pilihan = int(input("Masukkan pilihan: "))

    if(pilihan == 1):
        continue
    if(pilihan == 2):
        sys.exit()
