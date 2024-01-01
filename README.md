# Foundations_of_Artificial_Intelligence
Foundations of Artificial Intelligence 


## ASSIGNMENT
1. Assignment-01 [Uniformed Search Strategies](https://github.com/KKBUGHUNTER/Foundations_of_Artificial_Intelligence/tree/main/Assignment-01)


## TEST



| Algorithm | Category | Toy Examples | Real-Time Examples | Completeness | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| Depth-First Search (DFS) | Uninformed | Solving mazes, finding paths in graphs | Web crawling, file system traversal | Not complete for infinite-depth graphs | O(b^d), where b is branching factor and d is depth | O(d) |
| Breadth-First Search (BFS) | Uninformed | Finding shortest paths in unweighted graphs | Social network analysis, mapping networks | Complete for finite graphs | O(b^d) | O(b^d) |
| Depth-Limited Search (DLS) | Uninformed | Solving puzzles with limited moves | Game AI, pathfinding with constraints | Not complete for deep solutions | O(b^l), where l is depth limit | O(bl) |
| Iterative Deepening Search (IDS) | Uninformed | Solving 8-puzzle, pathfinding with unknown depth | Routing in networks, task scheduling | Complete | O(b^d) | O(d) |
| Greedy Best-First Search | Informed | 8-puzzle, traveling salesman problem | Navigation systems, resource allocation | Not complete | Depends on heuristic | O(b^d) |
| A* Search | Informed | Pathfinding in games, route planning | GPS navigation, logistics optimization | Complete for admissible heuristics | O(b^(d*h)), where h is heuristic accuracy | O(b^d) |
| Hill Climbing | Local Search | Optimizing function parameters, solving puzzles | Machine learning, image processing | Not complete, can get stuck in local optima | Depends on problem and neighborhood structure | Usually low |
| Simulated Annealing | Local Search | Traveling salesman problem, circuit design | VLSI design, protein folding | Complete (with infinite time) | Depends on cooling schedule | Usually low |
| Min-Max Search | Adversarial | Games like tic-tac-toe, checkers | Game AI, decision-making in uncertain environments | Complete for finite games | O(b^m), where m is game depth | O(bm) |
| Alpha-Beta Pruning | Adversarial | Chess, Go, other complex games | AI for strategy games, automated theorem proving | Complete for finite games | O(b^(m/2)), best-case | O(bm) |
