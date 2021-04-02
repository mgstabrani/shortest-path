from astar import *
from input import *

g = Graf(nodes, adjacentNode, nodeCoordinate)
print(astar(g,"Palembang", "Empat Lawang"))