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

def DFS(root,result=[]):
	if root is not None:
		result.append(root.data)
		DFS(root.left)
		DFS(root.right)
	return result

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

Inorder(tree)

bfs_val = BFS(tree)
print("Breadth First Search: ", bfs_val)

dfs_val = DFS(tree)
print("Deapth First Search: ", dfs_val)

depth_limit = 1
result = DLS(tree, depth_limit)
print("DLS: ",result)

ids_val = IDS(tree, depth)
print("IDS : ", ids_val)