from enum import Enum

class Status(Enum):
    VISITED = "VISITED"
    UNVISITED = "UNVISITED"
    VISITING = "VISITING"
    

class Node:
    def __init__(self,name,neighbors=[],status=Status.UNVISITED):
        self.name = name
#        self.neighbors = neighbors
        self.status = status
        

class Graph:
    def __init__(self,adjList,list_nodes):
        self.adjList = adjList
        self.list_nodes = list_nodes

a, b, c, d, e = Node("a"), Node("b"), Node("c"), Node("d"), Node("e")
list_nodes = [a,b,c,d,e]
adjList = {"a": [b, c],
        "b": [a, e],
        "c": [a, d],
        "d": [c, e],
        "e": [b, d]
        }
graph = Graph(adjList,list_nodes)


##def bfss(startNode):
##    if startNode==None or startNode.status != Status.UNVISITED: return
##    queue = []
##    cache = []
###    print("pp")
##    queue.append(startNode)
##    startNode.status = Status.VISITING
##    cache.append(startNode)
##    while (len(queue)>0):
##        node = queue[0]
##        queue = queue[1:]
##        node.status = Status.VISITED
##        for element in cache:
##            print(element.name)        
##        for neighbor in adjList[node.name]:
##            if neighbor.status==Status.UNVISITED:
##                queue.append(neighbor)
##                neighbor.status = Status.VISITING


def bfs(startNode, visited):

    if startNode==None: return
    queue = []
    queue.append(startNode)
    while (len(queue)>0):
        node = queue.pop(0)
        print(node.name)
        for neighbor in adjList[node.name]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(node)


def level_order_traversal(graph):
    visited = set()
    for node in graph.list_nodes:
        if node not in visited:
            bfs(node, visited)
        

level_order_traversal(graph)   
    
    


