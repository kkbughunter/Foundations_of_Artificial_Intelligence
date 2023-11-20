class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_tree_with_n_nodes(n):
    if n <= 0:
        return None
    root = Node(3)  
    nodes = [root]
    count = 1

    while count < n:
        current = nodes.pop(0)
        current.left = Node(2 * current.value)
        nodes.append(current.left)
        count += 1

        if count == n:
            break

        current.right = Node(2 * current.value + 1)
        nodes.append(current.right)
        count += 1

    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L -- ")
        print_tree(root.right, level + 1, "R -- ")

n = 10
tree_with_n_nodes = generate_tree_with_n_nodes(n)
print_tree(tree_with_n_nodes)
