import heapq

# Calculate Manhattan distance heuristic
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# A* algorithm
def astar(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    pq = [(0, start)]
    heapq.heapify(pq)
    came_from = {}
    cost_so_far = {start: 0}

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            new_row, new_col = current_node[0] + dx, current_node[1] + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] != -1:
                new_node = (new_row, new_col)
                new_cost = cost_so_far[current_node] + matrix[new_row][new_col]

                if new_node not in cost_so_far or new_cost < cost_so_far[new_node]:
                    cost_so_far[new_node] = new_cost
                    priority = new_cost + heuristic(new_node, goal)
                    heapq.heappush(pq, (priority, new_node))
                    came_from[new_node] = current_node

    return None

# Example usage:
matrix = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
]

start_node = (0, 0)
goal_node = (2, 2)

path = astar(matrix, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found")
