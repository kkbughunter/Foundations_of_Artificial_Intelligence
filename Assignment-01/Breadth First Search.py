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

def BFS(root):
	if root is None:
		return []

	result = []
	queue = [root]

	while queue:
		current = queue.pop(0)
		result.append(current.data)

		if current.left:
			queue.append(current.left)
		if current.right:
			queue.append(current.right)
	return result

	
depth = 3
root_val = 3 
tree = generateTree(root_val, depth)

bfs_val = BFS(tree)
print("Breadth First Search: ", bfs_val)
