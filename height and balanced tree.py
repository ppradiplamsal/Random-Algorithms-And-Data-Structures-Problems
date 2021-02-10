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


def height(node):
    if node == None: return -1
    return max(height(node.left), height(node.right)) + 1

#print(height(n4))

def isBalanced(root):
    if root == None: return None
    def height(node):
        if node == None:
            return -1
        hLeft = height(node.left)
        hRight = height(node.right)
        return max(hLeft, hRight)+1
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if (((leftHeight - rightHeight)) ** 2) > 1:
        return False
    else:
        return True

#print(isBalanced(n4))
print(abs(-5))
    


    
