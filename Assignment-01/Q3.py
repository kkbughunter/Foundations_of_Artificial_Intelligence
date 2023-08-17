def bfs(graph, start):
    visited = [False]*len(graph)
    visited[start] = True
    queue = [start]
    print(start,"-> ",end="")
    while queue:
        curr_node = queue.pop(0)
        for node in range(len(graph)):
            if graph[curr_node][node]>-1 and not visited[node]:
                print(node,"-> ",end="")
                visited[node] = True
                queue.append(node)

graph = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print("Starting State ",end="")
bfs(graph, 0) 
print("Goal Reached")
