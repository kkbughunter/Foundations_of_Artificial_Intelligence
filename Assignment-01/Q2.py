def dfs(graph, start,visited): 
    
    visited[start] = 1
    print(start, " => ", end="")

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph,i,visited)

graph = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
visited = [0] * len(graph)
print("Starting State ",end="")
dfs(graph, 0,visited)
print("Goal Reached")
