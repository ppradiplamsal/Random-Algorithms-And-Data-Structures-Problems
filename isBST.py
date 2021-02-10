##class TreeNode:
##
##    def __init__(self, data):
##        self.data = data
##        self.left = None
##        self.right = None
##
##    def getValue(self): return self.data
##    def getLeft(self): return self.left
##    def setLeft(self, left): self.left = left
##    def getRight(self): return self.right
##    def setRight(self, right): self.right = right
##
##n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
##
##n2.setLeft(n1)
##n2.setRight(n3)
##
##n6.setLeft(n5)
##n6.setRight(n7)
##
###n7.setRight(n8)
###n8.setRight(n9)
##
##
##n4.setLeft(n2)
##n4.setRight(n6)




#print(isBST(n4, TreeNode(float('-inf'))))


# Data structure to store a Binary Search Tree node
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Recursive function to insert a key into BST
def insert(root, key):

	# if the root is None, create a node and return it
	if root is None:
		return Node(key)

	# if given key is less than the root node, recur for left subtree
	if key < root.data:
		root.left = insert(root.left, key)

	# if given key is more than the root node, recur for right subtree
	else:
		root.right = insert(root.right, key)

	return root


# Function to perform inorder traversal of the given binary tree and
# check if it is a BST or not . Here prev is previous processed node
def isBST(root, prev):
 
    # base case: empty tree is a BST
    if root is None:
        return True
 
    # check if left subtree is BST or not
    
 
    # value of current node should be more than that of previous node
    if root.data <= prev.data:
        return False
 
    # update previous node data and check if right subtree is BST or not
   # prev.data = root.data
    return isBST(root.left, prev) and isBST(root.right, root)


# Function to determine if given Binary Tree is a BST or not
def checkForBST(node):

    # pointer to store previous processed node in inorder traversal
    prev = Node(float('-inf'))

    # check if nodes are nodes are processed in sorted order
    if isBST(node, prev):
            print("This is a BST!")
    else:
            print("This is NOT a BST!")


def swap(root):

	left = root.left
	root.left = root.right
	root.right = left


if __name__ == '__main__':

	root = None
	keys = [15, 10, 20, 8, 12, 16, 25]

	for key in keys:
		root = insert(root, key)

	# swap nodes
	swap(root)
	checkForBST(root)
