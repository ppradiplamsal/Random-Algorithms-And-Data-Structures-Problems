def findGoodNodes(root, target):
    if not root: raise Exception("Illegal Argument")

    def fGNHelper(root, target, count):

        if not root: return [0]
        if not root.left and not root.right: return [1]

        goodNodesLeft = fGNHelper(root.left, target, count)
        goodNodesRight = fGNHelper(root.right, target, count)

        for valueL in goodNodesLeft:
            for valueR in goodNodesRight:
                if valueL + valueR <= target:
                    count[0] += 1

        goodNodes = []
        appendGoodNodes(goodNodes, target, goodNodesLeft)
        appendGoodNodes(goodNodes, target, goodNodesRight)

        return goodNodes


    def appendGoodNodes(goodNodes, target, goodNodesLeftOrRight):
        for value in goodNodesLeftOrRight:
            if value+1 <= target:
                goodNodes.append(value)
 
