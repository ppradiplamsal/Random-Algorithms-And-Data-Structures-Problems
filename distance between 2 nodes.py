def distance(root, node1, node2):
    if not root or not node1 or not node2: raise Exception("Illegal Arguments")

    lcaOfNodes = findLCA(root, node1, node2)

    return findDistance(lcaOfNodes, node1, 0) + findDistance(lcaOfNodes, node2, 0)

def findLCA(root, node1, node2):
    if not root: return None

    if root == node1 or root == node2: return root

    foundOnLeft = findLCA(root.left, node1, node2)

    foundOnRight = findLCA(root.right, node1, node2)

    if foundOnLeft and foundOnRight: return root

    if foundOnLeft: return foundOnLeft
    else return foundOnRight

def findDistance(root, node, distance):
    if not root: return

    if root == node: return distance

    distanceLeft = findDistance(root.left, node, distance+1)
    distanceRight = findDistance(root.right, node, distance+1)    

    return distanceLeft if distanceLeft != 0 else distanceRight

def findDepth(root, node, depth):
    if not root: return 0
    depth[0] += 1
    findDepth(root.left, node, depth)
    depth[0] -= 1
    findDepth(root.right, node, depth)
