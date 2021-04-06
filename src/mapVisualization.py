import folium

def mapVisualization(g,nodeFrom,nodeTo,nodes,answer,found, choosenEdges):
    m = folium.Map(location=[g.getOrdinat(nodeTo), g.getAbsis(nodeTo)], zoom_start=20)

    #Mewarnai seluruh node dan edge
    for i in range(g.getNumOfNode()):
        folium.Marker([g.getOrdinat(nodes[i]), g.getAbsis(nodes[i])],popup=nodes[i], icon=folium.Icon(color='blue', icon='leaf')).add_to(m)
        for j in range(g.getNumOfNode()):
            adjacentNode = g.getNodeAdjacent(nodes[j])
            for k in range(len(g.getNodeAdjacent(nodes[j]))):
                folium.PolyLine([[g.getOrdinat(nodes[j]),g.getAbsis(nodes[j])],[g.getOrdinat(adjacentNode[k]),g.getAbsis(adjacentNode[k])]], color="blue").add_to(m)
    folium.Marker([g.getOrdinat(nodeFrom), g.getAbsis(nodeFrom)],popup=nodeFrom, icon=folium.Icon(color='red', icon='leaf')).add_to(m)
    folium.Marker([g.getOrdinat(nodeTo), g.getAbsis(nodeTo)],popup=nodeTo, icon=folium.Icon(color='green', icon='leaf')).add_to(m)
    
    #Mewarnai rute

    #Jika jalur ketemu
    if(found):
        for i in range(len(answer[0])):
            folium.Marker([g.getOrdinat(answer[0][i]), g.getAbsis(answer[0][i])],popup=answer[0][i], icon=folium.Icon(color='red', icon='leaf')).add_to(m)
        folium.Marker([g.getOrdinat(answer[0][-1]), g.getAbsis(answer[0][i])],popup=answer[0][-1], icon=folium.Icon(color='green', icon='leaf')).add_to(m)
        for i in range(len(choosenEdges)):
            text = "Jarak terdekat dari " + nodeFrom + " ke " + nodeTo + " adalah " + str(answer[1]*100) + " km"
            folium.PolyLine([[g.getOrdinat(choosenEdges[i][0]),g.getAbsis(choosenEdges[i][0])],[g.getOrdinat(choosenEdges[i][1]),g.getAbsis(choosenEdges[i][1])]], color="red", tooltip=text).add_to(m)
    
    #Jika jalur tidak ada
    else:
        text = nodeFrom + " ke " + nodeTo + " tidak memiliki jalur"
        for j in range(g.getNumOfNode()):
            adjacentNode = g.getNodeAdjacent(nodes[j])
            for k in range(len(g.getNodeAdjacent(nodes[j]))):
                folium.PolyLine([[g.getOrdinat(nodes[j]),g.getAbsis(nodes[j])],[g.getOrdinat(adjacentNode[k]),g.getAbsis(adjacentNode[k])]], color="blue", tooltip=text).add_to(m)

    #Menyimpan map
    m.save('map.html')