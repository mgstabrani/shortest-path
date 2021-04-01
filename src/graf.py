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