
#Algoritma A*
def astar(graf, nodeFrom, nodeTo):
    nodeFrom = nodeFrom
    result = [[nodeFrom]]
    currentState = [nodeFrom]
    cost = [0]
    currentCost = 0
    while(nodeFrom != nodeTo):
        nodeAdjacent = graf.getNodeAdjacent(nodeFrom)
        for i in range(len(result)):
            if(result[i] == currentState):
                result.pop(i)
                cost.pop(i)
                break

        for i in range(len(nodeAdjacent)):
            temp = [[] for i in range(len(currentState))]
            for j in range(len(temp)):
                temp[j] = currentState[j]
            temp.append(nodeAdjacent[i])
            result.append(temp)
            cost.append(currentCost + graf.getDistant(nodeFrom,nodeAdjacent[i]) + graf.getDistant(nodeAdjacent[i], nodeTo))

        for i in range(len(result)):
            if(cost[i] == min(cost)):
                currentState = result[i]
                currentCost = cost[i] - graf.getDistant(result[i][-1], nodeTo)
                nodeFrom = result[i][len(result[i])-1]
                break

    fixResult = []
    fixCost = 0
    for i in range(len(result)):
        if(cost[i] == min(cost) and result[i][-1] == nodeTo):
            fixResult = result[i]
            fixCost = cost[i] - graf.getDistant(result[i][-1], nodeTo)
            break

    return (fixResult,fixCost)

#Pencarian node menggunakan algoritma DFS
def dfsExploreNode(graf, nodeFrom, nodeTo, dikunjungi, hasil):
    if(dikunjungi[graf.getIdxNode(nodeFrom)] == 0):
        dikunjungi[graf.getIdxNode(nodeFrom)] = 1
        hasil.append(nodeFrom)
    if(nodeFrom == nodeTo):
        return True
    if(len(graf.getNodeAdjacent(nodeFrom)) == 0):
        return False
    isExist = False
    connectNodes = []
    adjacent = graf.getNodeAdjacent(nodeFrom)
    for i in range(len(graf.getNodeAdjacent(nodeFrom))):
        connectNodes.append(adjacent[i])
    connectNodes.sort()
    for i in range(len(graf.getNodeAdjacent(nodeFrom))):
        if(dikunjungi[graf.getIdxNode(connectNodes[i])] == 0):
            isExist = True
            break
    if(not isExist):
        hasil.pop(len(hasil) - 1)
        if(len(hasil) == 0):
            return False
        return dfsExploreNode(graf, hasil[len(hasil) - 1], nodeTo, dikunjungi, hasil)
    else:
        return dfsExploreNode(graf, connectNodes[i], nodeTo, dikunjungi, hasil)
