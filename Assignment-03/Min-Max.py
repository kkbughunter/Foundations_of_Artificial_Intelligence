def generate_state_space_tree(node, level, current_level=0):
    if current_level == level:
        return
    else:
        node.left = Node(2 * node.value + 1)
        node.right = Node(2 * node.value + 2)
        generate_state_space_tree(node.left, level, current_level + 1)
        generate_state_space_tree(node.right, level, current_level + 1)

def print_tree(node, depth=0, prefix="Root: "):
    if node is not None:
        print(" " * (depth * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, depth + 1, "L--- ")
            print_tree(node.right, depth + 1, "R--- ")

def print_tree_with_values(node, depth=0, prefix="Root: "):
    if node is not None:
        print(" " * (depth * 4) + prefix + f"{node.value} (Minimax: {node.minimax_value})")
        if node.left is not None or node.right is not None:
            print_tree_with_values(node.left, depth + 1, "L--- ")
            print_tree_with_values(node.right, depth + 1, "R--- ")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.minimax_value = None  # Store Minimax values

def minimax(node, depth, max_player):
    if depth == 0:
        node.minimax_value = node.value
        return node.value  # Evaluation function for terminal nodes

    if max_player:
        best_value = float('-inf')
        for child in [node.left, node.right]:
            if child is not None:
                value = minimax(child, depth - 1, False)
                best_value = max(best_value, value)
                node.minimax_value = best_value
        return best_value
    else:
        best_value = float('inf')
        for child in [node.left, node.right]:
            if child is not None:
                value = minimax(child, depth - 1, True)
                best_value = min(best_value, value)
                node.minimax_value = best_value
        return best_value

# Input for the desired level of the state space tree
init_node_value = int(input("\nEnter initial node value: "))
level = int(input("\nEnter the level of the state space tree (first level is 0): "))

# Create the state space tree
root = Node(init_node_value)
generate_state_space_tree(root, level)

# Print the tree
print("Printing the tree:")
print_tree(root)

# Calculate the optimal value for the root node (max player's turn)
print("\n\t\t-------------------")
print("\t\t| Max Player Turn |")
print("\t\t-------------------\n")
optimal_value_maxplayer = minimax(root, level, True)
# Print the tree structure with Minimax values
print("Selection Process:")
print_tree_with_values(root)
print("\nOptimal value for the root node (Max player's turn) is:", optimal_value_maxplayer)

# Calculate the optimal value for the root node (min player's turn)
print("\n\t\t-------------------")
print("\t\t| Min Player Turn |")
print("\t\t-------------------\n")
optimal_value_minplayer = minimax(root, level, False)
# Print the tree structure with Minimax values
print("Selection Process:")
print_tree_with_values(root)
print("\nOptimal value for the root node (Min player's turn) is:", optimal_value_minplayer)
print("\n")
