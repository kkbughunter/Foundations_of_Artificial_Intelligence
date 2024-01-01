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

def AOstar(matrix, start, goal):
    frontier = [(0, start)]
    heapq.heapify(frontier)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for next_node in get_neighbors(matrix, current):
            new_cost = cost_so_far[current] + matrix[next_node[0]][next_node[1]]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic_cost_estimate(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
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

# Finding the path
path = AOstar(matrix, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found")
