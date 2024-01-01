from aima import search

# Define the problem
problem = aima.EightPuzzle((2, 8, 3, 1, 4, 6, 0, 7, 5))

# Define the heuristic
heuristic = aima.manhattan_distance

# Solve the problem
result = search.astar_search(problem, heuristic)

# Print the solution
print(result.actions)
