#Input file
fileName = input("Masukkan file: ")
fileName = open(fileName, 'r')
numOfNode = int(fileName.readline())

#Graf Variables
nodes = []
adjacentNode = []
nodeCoordinate = []

#Mendapatkan koordinat dan node
for i in range(numOfNode):

    #Mendapatkan koordinat
    content = fileName.readline()
    j = 1
    x = ''
    y = ''
    node = ''
    while(content[j] != ','):
        x += content[j]
        j += 1
    j += 1
    while(content[j] != ')'):
        y += content[j]
        j += 1
    nodeCoordinate.append((int(x),int(y)))
    j += 1

    #Mendapatkan node
    while(content[j] != '\n'):
        node += content[j]
        j += 1
    nodes.append(node)

#Inisialisasi adjacent
for i in range(numOfNode):
    adjacentNode.append([])

#Mendapatkan adjacent node
while(True):
    adjacent = fileName.readline()
    if(adjacent == ""):
        break
    adjacent = list(map(str, adjacent.split(',')))
    if(adjacent[1][-1] == "\n"):
        adjacent[1] = adjacent[1][:-1]

    #Mencatat adjacent node sebelah kanan
    for i in range(len(nodes)):
        if(adjacent[0] == nodes[i]):
            adjacentNode[i].append(adjacent[1])

    #Mencatat adjacent node sebelah kiri
    for i in range(len(nodes)):
        if(adjacent[1] == nodes[i]):
            adjacentNode[i].append(adjacent[0])