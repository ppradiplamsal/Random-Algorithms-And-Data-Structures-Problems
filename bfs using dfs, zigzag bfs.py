class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self): return self.value
    def getLeft(self): return self.left
    def setLeft(self, left): self.left = left
    def getRight(self): return self.right
    def setRight(self, right): self.right = right

n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)

n2.setLeft(n1)
n2.setRight(n3)

n6.setLeft(n5)
n6.setRight(n7)

#n7.setRight(n8)
#n8.setRight(n9)

n4.setLeft(n2)
n4.setRight(n6)


def bfs(root):
    result = [[],[],[]]
    
    def dfs(root, level):
        if not root: return
        result[level].append(root.value)
        dfs(root.left, level+1)
        dfs(root.right, level+1)

    dfs(root, 0)
    return result

print(bfs(n4))


from collections import deque

def zigzagBfs(root):
    if not root: raise Exception("Illegal input")
    result = []
    queue = []
    dequeue = deque()
    level = 0
    queue.append(root)
    queue.append(TreeNode(None))

    while (len(queue) > 0):
        node = queue.pop(0)
        if node.value == None:
            level += 1
            queue.append(TreeNode(None))
            print(dequeue)
            dequeue = deque()
            continue
        if level % 2 == 0:
            dequeue.append(node.value)
        else:
            dequeue.appendleft(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

print(zigzagBfs(n4))
        
        
        
             
            
            
        
        
































    


    
