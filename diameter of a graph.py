class Node:
    def __init__(self, name):
        self.name = name
        self.minSemesters = 0
        self.neighbors = []
        self.parent = None

    def addNeighbors(self, neighbors):
        self.neighbors = neighbors


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


def customizedDfs(node, visitedNodes, sortedStack):
    visitedNodes.add(node)
    
    for neighbor in node.neighbors:
        if neighbor not in visitedNodes:
            customizedDfs(neighbor, visitedNodes, sortedStack)

    sortedStack.append(node)  


def topologicalSort(graph):
    visitedNodes = set()
    sortedStack = []
    
    for node in graph.nodes:
        if node not in visitedNodes:
            customizedDfs(node, visitedNodes, sortedStack)
            
    sortedStack.reverse()
    
    return sortedStack


def diameter(graph):
    diameter = 0
    lastNode = None
    
    for node in topologicalSort(graph):
        for neighbor in node.neighbors:
            if node.minSemesters + 1 > neighbor.minSemesters:
                neighbor.minSemesters = node.minSemesters + 1
                neighbor.parent = node
            if neighbor.minSemesters > diameter:
                diameter = neighbor.minSemesters
                lastNode = neighbor

    return (diameter, lastNode)


nA, nB, nC, nD, nE, nF, nG, nH, nI = Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('g'), Node('h'), Node('i')

nA.addNeighbors([nB, nD])
nB.addNeighbors([nC, nF])
nD.addNeighbors([nE])
nE.addNeighbors([nI])
nF.addNeighbors([nG, nH])
nH.addNeighbors([nI])


graph = Graph([nA, nB, nC, nD, nE, nF, nG, nH, nI])

print(diameter(graph)[0])

node = diameter(graph)[1]
while(node.parent!=None):
    print(node.name)
    node = node.parent
print(node.name)
    
