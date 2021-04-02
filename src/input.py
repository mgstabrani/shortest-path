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
    nodeCoordinate.append((float(x),float(y)))
    j += 1

    #Mendapatkan node
    while(content[j] != '\n'):
        node += content[j]
        j += 1
    nodes.append(node)

#Mendapatkan adjacent node
for i in range(numOfNode):
    #Inisialisasi adjacent
    adjacentNode.append([])

    #Menentukan adjacent node
    adjacent = fileName.readline()
    adjacent = list(map(str, adjacent.split(' ')))
    if(adjacent[len(adjacent)-1][-1] == '\n'):
        adjacent[len(adjacent)-1] = adjacent[len(adjacent)-1][:-1]

    #Memasukkan adjacent node
    for j in range(numOfNode):
        if(adjacent[j] == '1'):
            adjacentNode[i].append(nodes[j])