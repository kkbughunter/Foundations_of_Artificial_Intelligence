class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

def generateTree(root_val, depth):
	if depth == 0:
		return None
	root = Node(root_val)
	root.left = generateTree((2 * root.data)+2, depth-1)
	root.right = generateTree((2 * root.data)+3, depth-1)
	return root

def Inorder(root, level=0, prefix="Root: "):
	if root is not None:
		Inorder(root.left, level + 1, "    ")
		print(" " * (level * 4) + prefix + str(root.data))
		Inorder(root.right, level + 1, "    ")

depth = 3
root_val = 3 
tree = generateTree(root_val, depth)

Inorder(tree)