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


def IDS(root, max_depth):
	result = []
	res = BFS(tree)

	for i in range(max_depth):
		temp =[]
		for j in range((2**(i+1))-1):
			temp.append(res[j])
		result.append(temp)
	return result

	
depth = 3
root_val = 3 
tree = generateTree(root_val, depth)

ids_val = IDS(tree, depth)
print("IDS : ", ids_val)