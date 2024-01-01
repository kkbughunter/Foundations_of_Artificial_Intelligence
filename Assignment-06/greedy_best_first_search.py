import heapq

def heuristic_cost_estimate(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_neighbors(matrix, node):
    neighbors = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
            neighbors.append((x, y))
    return neighbors

def greedy_best_first_search(matrix, start, goal):
    frontier = [(heuristic_cost_estimate(start, goal), start)]
    heapq.heapify(frontier)
    came_from = {start: None}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for next_node in get_neighbors(matrix, current):
            if next_node not in came_from:
                heapq.heappush(frontier, (heuristic_cost_estimate(next_node, goal), next_node))
                came_from[next_node] = current

    return None

# Your matrix and nodes
matrix = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
]
start_node = (0, 0)
goal_node = (2, 2)

# Finding the path using Greedy Best-First Search
path = greedy_best_first_search(matrix, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found")
