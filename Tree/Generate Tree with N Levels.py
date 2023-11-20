class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_state_space_tree(root_value, depth):
    if depth == 0:
        return None
    root = Node(root_value)
    root.left = generate_state_space_tree((2 * root_value) + 2, depth - 1)
    root.right = generate_state_space_tree((2 * root_value) + 3, depth - 1)
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L -- ")
        print_tree(root.right, level + 1, "R -- ")

# Generating and printing a state space tree with root value 3 and depth 3
depth = 3
root_value = 3
state_space_tree = generate_state_space_tree(root_value, depth)
print_tree(state_space_tree)

