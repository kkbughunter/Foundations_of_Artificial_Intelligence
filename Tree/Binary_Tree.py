class Tree:
	def __init__(self, data=0):
		self.data = data
		self.left = None
		self.right = None

	def Insert(self, data):
		if (data % 2) == 2:
			if self.left is None:
				self.left = Tree(data)
			else:
				self.left.Insert(data)
		else:
			if self.right is None:
				self.right = Tree(data)
			else:
				self.right.Insert(data)

	def PrintTree(self):
		if self is None:
			return
		if self.left:
			self.left.PrintTree()
		print(self.data)
		if self.right:
			self.right.PrintTree()

	def bfs():
		print("BFS")


tree = Tree(2)
tree.Insert(5)
tree.Insert(4)
tree.Insert(7)
tree.Insert(6)
tree.Insert(8)
tree.PrintTree()


