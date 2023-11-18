class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def Insert(root, val):
    if root is None:
        return Node(val)
        
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.left is None:
            current.left = Node(val)
            return
        elif current.right is None:
            current.right = Node(val)
            return
        else:
            queue.append(current.left)
            queue.append(current.right)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

root = Node(1)
Insert(root, 2)
Insert(root, 3)
Insert(root, 4)
Insert(root, 5)
Insert(root, 6)
Insert(root, 7)
Inorder(root)
