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

def DLS(root, max_depth):
    if root is None:
        return []

    result = []
    queue = [(root, 0)]  # Store node and current depth

    while queue:
        current, depth = queue.pop(0)
        if depth > max_depth:
            continue  # Skip nodes beyond the depth limit

        result.append(current.data)

        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    return result

	
depth = 3
root_val = 3 
tree = generateTree(root_val, depth)

depth_limit = 1
result = DLS(tree, depth_limit)
print("DLS: ",result)
