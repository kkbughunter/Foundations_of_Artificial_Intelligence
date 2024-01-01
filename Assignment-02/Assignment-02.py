from queue import PriorityQueue

# Function to perform Greedy Best-First Search
def greedy_best_first_search(matrix, start, goal):
    rows = len(matrix)
    cols = len(matrix[0])

    # Helper function to calculate heuristic distance
    def heuristic_distance(curr, goal):
        return abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])

    # Priority queue to store nodes to be explored
    pq = PriorityQueue()
    pq.put((0, start))  # (priority, node)

    visited = set()
    visited.add(start)
    print(start, end=" ")
    # Possible movements: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while not pq.empty():
        # Get the current node with the lowest heuristic distance
        cost, current = pq.get()

        if current == goal:
            print("Goal found!")
            return True  # Goal reached

        # Explore all possible moves
        for move in moves:
            new_row = current[0] + move[0]
            new_col = current[1] + move[1]
            new_pos = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and new_pos not in visited:
                visited.add(new_pos)
                print(new_pos, end=" ")
                priority = heuristic_distance(new_pos, goal)
                pq.put((priority, new_pos))

    print("Goal not reachable.")
    return False  # Goal not reachable

# Example matrix
matrix = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

greedy_best_first_search(matrix, start, goal)
