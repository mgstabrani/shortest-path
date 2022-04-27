class Graf:
    def __init__(self, nodes, adjacentNode, nodeCoordinate):
        self.nodes = nodes
        self.adjacentNode = adjacentNode
        self.nodeCoordinate = nodeCoordinate

    def getNumOfNode(self):
        return len(self.nodes)

    def getIdxNode(self, node):
        for i in range(len(self.nodes)):
            if(node == self.nodes[i]):
                return i

    def getNodeCoordinate(self, node):
        return self.nodeCoordinate[self.getIdxNode(node)]

    def getNodeAdjacent(self, node):
        return self.adjacentNode[self.getIdxNode(node)]

    def getAbsis(self, node):
        coordinate = self.getNodeCoordinate(node)
        return coordinate[0]

    def getOrdinat(self, node):
        coordinate = self.getNodeCoordinate(node)
        return coordinate[1]

    def getDistant(self, nodeFrom, nodeTo):
        return ((self.getAbsis(nodeFrom) - self.getAbsis(nodeTo))**2 + (self.getOrdinat(nodeFrom) - self.getOrdinat(nodeTo))**2)**(1/2)
